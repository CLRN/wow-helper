from memory.memory import Memory
import logging

mem = Memory()


class Process:
    def __init__(self, name):
        self.pid = mem.GetProcessIDByName(name)
        self.handle = mem.GetProcessHandle(name, 1)
        self.cache = dict()

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

    def invalidate_cache(self):
        self.cache = dict()

    def int(self, address):
        key = 'int', address
        if key in self.cache:
            return self.cache[key]
        res = mem.read_integer(self.handle, address)
        self.cache[key] = res
        return res

    def float(self, address):
        key = 'float', address
        if key in self.cache:
            return self.cache[key]
        res = mem.read_float(self.handle, address)
        self.cache[key] = res
        return res

    def byte(self, address):
        key = 'byte', address
        if key in self.cache:
            return self.cache[key]
        res = mem.read_byte(self.handle, address)
        self.cache[key] = res
        return res

    def ptr(self, address):
        key = 'ptr', address
        if key in self.cache:
            return self.cache[key]
        res = mem.read_long(self.handle, address)
        self.cache[key] = res
        return res

    def str(self, address, size):
        key = 'str', address, size
        if key in self.cache:
            return self.cache[key]
        res = mem.read_bytes(self.handle, address, size).decode("utf-8")
        self.cache[key] = res
        return res
