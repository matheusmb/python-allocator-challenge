from .base_allocator import Allocator


class NonSilentAllocator(Allocator):
    def __ini__(self):
        super().__init__()

    def allocate(self, host_type):
        allocated_intance = super().allocate(host_type)
        if allocated_intance:
            return allocated_intance
        return "Invalid Name"

    def deallocate(self, host_name):
        try:
            return super().deallocate(host_name)
        except ValueError as e:
            return e.message
