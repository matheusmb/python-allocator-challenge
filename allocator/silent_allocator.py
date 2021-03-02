from .base_allocator import Allocator

class SilentAllocator(Allocator):
    def __init__(self):
        super().__init__()

    def allocate(self, host_type):
        allocated_intance = super().allocate(host_type)
        if allocated_intance:
            return allocated_intance

    def deallocate(self, host_name):
        try:
            super().deallocate(host_name)
        except:
            pass
