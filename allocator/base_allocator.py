from .name_validator import NameValidator


class InvalidHostName(ValueError):
    def __init__(self, msg):
        super().__init__()
        self.message = msg


class Allocator:
    def __init__(self):
        self.allocated_hosts = dict()
        self.deallocated_pool = dict()

    def allocate(self, host_type):
        if not NameValidator.hasValidHostType(host_type):
            return False

        from_pool = self.getHostFromPool(host_type)
        if from_pool:
            return from_pool

        new_instance_num = self.allocated_hosts.get(host_type, 1)

        self.allocated_hosts[host_type] = new_instance_num + 1
        return f"{host_type}{new_instance_num}"

    def getHostFromPool(self, host_type):
        host_pool = self.deallocated_pool.get(host_type, None)
        if host_pool:
            return host_pool.pop(0)

    def deallocate(self, host_name):
        if not NameValidator.hasValidHostName(host_name):
            raise InvalidHostName("Invalid host name")

        host_type, host_id = NameValidator.parseTypeIdFrom(host_name)

        total_allocations = self.allocated_hosts.get(host_type, 0)

        if host_id <= total_allocations:
            pool = self.deallocated_pool.get(host_type, list())
            pool.append(host_name)
            self.deallocated_pool[host_type] = pool
            return True
        return False
