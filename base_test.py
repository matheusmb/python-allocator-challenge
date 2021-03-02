import pytest

from allocator import Allocator, SilentAllocator, NonSilentAllocator


@pytest.fixture
def allocator():
    return Allocator()


@pytest.fixture
def silent_allocator():
    return SilentAllocator()


@pytest.fixture
def non_silent_allocator():
    return NonSilentAllocator()


def test_should_not_allocate_bad_name(allocator):
    assert allocator.allocate("invalid_name") is False


def test_should_allocate_good_name(allocator):
    assert allocator.allocate("api") == "api1"

def test_should_allocate_two_times(allocator):
    assert allocator.allocate("api") == "api1"
    assert allocator.allocate("api") == "api2"


def test_should_allocate_different_hosts(allocator):
    assert allocator.allocate("api") == "api1"
    assert allocator.allocate("db") == "db1"
    assert allocator.allocate("api") == "api2"
    assert allocator.allocate("db") == "db2"


def test_should_return_error_on_bad_name_deallocate(allocator):
    assert allocator.allocate("api") == "api1"
    with pytest.raises(ValueError):
        assert allocator.deallocate("invalid_name") is False


def test_should_allocate_deallocate(allocator):
    assert allocator.allocate("api") == "api1"
    assert allocator.deallocate("api1") is True


def test_should_not_deallocate_on_not_allocated(allocator):
    assert allocator.deallocate("db1") is False
    assert allocator.allocate("api") == "api1"
    assert allocator.deallocate("api1") is True


def test_should_use_previous_deallocated_type(allocator):
    assert allocator.allocate("api") == "api1"
    assert allocator.deallocate("api1") is True
    assert allocator.allocate("api") == "api1"


def test_should_allocate_and_deallocate_sequentially(allocator):
    assert allocator.allocate("api") == "api1"
    assert allocator.allocate("api") == "api2"
    assert allocator.allocate("api") == "api3"

    assert allocator.allocate("db") == "db1"
    assert allocator.allocate("api") == "api4"
    assert allocator.allocate("db") == "db2"

    assert allocator.deallocate("db1") == True
    assert allocator.deallocate("api2") == True
    assert allocator.deallocate("api1") == True

    assert allocator.allocate("api") == "api2"
    assert allocator.allocate("db") == "db1"
    assert allocator.allocate("api") == "api1"
    assert allocator.allocate("api") == "api5"


def test_silent_allocator(silent_allocator):
    assert silent_allocator.allocate("api") == "api1"
    assert silent_allocator.allocate("invalid_name") is None
    assert silent_allocator.deallocate("invalid_name") is None
    assert silent_allocator.deallocate("api1") is None


def test_non_silent_allocator(non_silent_allocator):
    assert non_silent_allocator.allocate("api") == "api1"
    assert non_silent_allocator.allocate("invalid_name") == "Invalid Name"
    assert non_silent_allocator.deallocate("invalid_name") == "Invalid host name"
    assert non_silent_allocator.deallocate("api1") is True
