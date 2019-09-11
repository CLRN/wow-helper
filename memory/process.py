from memory.memory import Memory
import logging

mem = Memory()


class Process:
    def __init__(self, name):
        self.pid = mem.GetProcessIDByName(name)
        self.handle = mem.GetProcessHandle(name, 1)

        if not self.pid or not self.handle:
            raise Exception(f"Can't find process by name {name}")

        self.base_address = 0
        for mod_name, base_addr in mem.EnumModules(self.pid):
            if mod_name == name:
                self.base_address = base_addr
                break
        if not self.base_address:
            raise Exception("No base address found")

        logging.info(f"Base for {name} is {self.base_address}")

        global current
        current = self

    def int(self, address):
        return mem.read_integer(self.handle, address)

    def float(self, address):
        return mem.read_float(self.handle, address)

    def byte(self, address):
        return mem.read_byte(self.handle, address)

    def ptr(self, address):
        return mem.read_long(self.handle, address)

    def str(self, address, size):
        return mem.read_bytes(self.handle, address, size).decode("utf-8")


