import win32api, win32process, win32con
from ctypes import *
from ctypes.wintypes import *
import struct

PROCESS_ALL_ACCESS = 0x1F0FFF
SIZE_DOUBLE = 8
SIZE_LONGLONG = 8
SIZE_FLOAT = 4
SIZE_LONG = 4
SIZE_INT = 4
SIZE_SHORT = 2
SIZE_CHAR = 1

# Create w32api references
__rPM__ = WinDLL('kernel32', use_last_error=True).ReadProcessMemory
__rPM__.argtypes = [HANDLE, LPCVOID, LPVOID, c_size_t, POINTER(c_size_t)]
__rPM__.restype = BOOL

__wPM__ = WinDLL('kernel32', use_last_error=True).WriteProcessMemory
__wPM__.argtypes = [HANDLE, LPVOID, LPCVOID, c_size_t, POINTER(c_size_t)]
__wPM__.restype = BOOL


class PROCESSENTRY32(Structure):
    _fields_ = [('dwSize', DWORD),
                ('cntUsage', DWORD),
                ('th32ProcessID', DWORD),
                ('th32DefaultHeapID', POINTER(ULONG)),
                ('th32ModuleID', DWORD),
                ('cntThreads', DWORD),
                ('th32ParentProcessID', DWORD),
                ('pcPriClassBase', LONG),
                ('dwFlags', DWORD),
                ('szExeFile', c_char * 260)]


class Memory(object):

    def __init__(self):
        self.CreateToolhelp32Snapshot = CDLL("kernel32.dll").CreateToolhelp32Snapshot
        self.Process32First = CDLL("kernel32.dll").Process32First
        self.Process32Next = CDLL("kernel32.dll").Process32Next
        self.GetLastError = CDLL("kernel32.dll").GetLastError
        self.CloseHandle = CDLL("kernel32.dll").CloseHandle
        self.OpenProcess = CDLL("kernel32.dll").OpenProcess
        self.VirtualProtectEx = CDLL("kernel32.dll").VirtualProtectEx
        self.EnumProcessModulesEx = CDLL("Psapi.dll").EnumProcessModulesEx
        self.TH32CS_SNAPPROCESS = 0x00000002
        self.TH32CS_SNAPMODULE = 0x00000008
        self.ALL_ACCESS = 0x1f0fff

    def EnumModules(self, pid):
        INVALID_HANDLE_VALUE = (-1)

        class MODULEENTRY32(Structure):
            _fields_ = [('dwSize', DWORD),
                        ('th32ModuleID', DWORD),
                        ('th32ProcessID', DWORD),
                        ('GlblcntUsage', DWORD),
                        ('ProccntUsage', DWORD),
                        ('modBaseAddr', c_void_p),
                        ('modBaseSize', DWORD),
                        ('hModule', HMODULE),
                        ('szModule', c_char * 256),
                        ('szExePath', c_char * 260)]

        mod32 = MODULEENTRY32()
        mod32.dwSize = sizeof(MODULEENTRY32)

        ret = []

        kernel32 = windll.kernel32  # Link to kernel32 Library
        hSnapshot = kernel32.CreateToolhelp32Snapshot(self.TH32CS_SNAPMODULE, pid)

        if hSnapshot == INVALID_HANDLE_VALUE:
            raise Exception(f'CreateToolhelp32Snapshot cannot create snapshot, err: {self.GetLastError()}')

        status = kernel32.Module32First(hSnapshot, pointer(mod32))
        if not status:
            kernel32.CloseHandle(hSnapshot)
            raise Exception(f'Module32FirstW call error, err: {self.GetLastError()}')

        while status:
            ret.append((mod32.szModule.decode("utf-8"), int(mod32.modBaseAddr)))
            status = kernel32.Module32NextW(hSnapshot, byref(mod32))

        kernel32.CloseHandle(hSnapshot)
        return ret

    def GetProcessIDByName(self, pname):
        pname = bytes(pname, encoding="utf8")
        hSnapshot = HANDLE
        hSnapshot = self.CreateToolhelp32Snapshot(self.TH32CS_SNAPPROCESS, 0)

        if (hSnapshot):
            pe32 = PROCESSENTRY32()
            pe32.dwSize = sizeof(PROCESSENTRY32);
            process = self.Process32First(hSnapshot, byref(pe32))
            while True:
                process = self.Process32Next(hSnapshot, byref(pe32))
                if process:
                    if pe32.szExeFile.lower() == pname.lower():
                        return pe32.th32ProcessID
                else:
                    print("Process not found!")
                    return False
        else:
            print("Snapshot failed!")
            return False

    def GetProcessHandle(self, pname, hType):
        pid = self.GetProcessIDByName(pname)
        if pid and type(1) == type(pid):
            if hType == 0:
                phandle = HANDLE(self.OpenProcess(DWORD(self.ALL_ACCESS), False, DWORD(pid)))
            elif hType == 1:
                phandle = self.OpenProcess(DWORD(self.ALL_ACCESS), False, DWORD(pid))

            if phandle:
                return phandle
            else:
                return self.GetLastError()
        else:
            print("Couldn't get the process ID!")
            return False

    def read_integer(self, process_handle, address):
        """Reads an int at a specified address from a process
        Returns an int which is the value at [address]
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to read from
        """
        buffer = create_string_buffer(SIZE_INT)
        bytes_read = c_size_t()
        if not __rPM__(process_handle, address, buffer, SIZE_INT, byref(bytes_read)):
            raise Exception(f"Failed to read {get_last_error()}")
        return struct.unpack("I", buffer[0:SIZE_INT])[0]

    def read_long(self, process_handle, address):
        """Reads an lon int at a specified address from a process
        Returns an int which is the value at [address]
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to read from
        """
        buffer = create_string_buffer(SIZE_LONGLONG)
        bytes_read = c_size_t()
        if not __rPM__(process_handle, address, buffer, SIZE_LONGLONG, byref(bytes_read)):
            raise Exception(f"Failed to read {get_last_error()}")
        return struct.unpack("q", buffer[0:SIZE_LONGLONG])[0]

    def read_short(self, process_handle, address):
        """Reads an short at a specified address from a process
        Returns an short which is the value at [address]
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to read from
        """
        buffer = create_string_buffer(SIZE_SHORT)
        bytes_read = c_size_t()
        if not __rPM__(process_handle, address, buffer, SIZE_SHORT, byref(bytes_read)):
            raise Exception(f"Failed to read {get_last_error()}")
        return struct.unpack("H", buffer[0:SIZE_SHORT])[0]

    def read_byte(self, process_handle, address):
        """Reads a single byte at a specified address from a process
        Returns an byte which is the value at [address]
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to read from
        """
        buffer = create_string_buffer(SIZE_CHAR)
        bytes_read = c_size_t()
        if not __rPM__(process_handle, address, buffer, SIZE_CHAR, byref(bytes_read)):
            raise Exception(f"Failed to read {get_last_error()}")
        return struct.unpack("B", buffer[0:SIZE_CHAR])[0]

    def read_bytes(self, process_handle, address, length):
        """Reads an array of bytes at a specified address from a process
        Returns a list which is values at [address], with a length of [length]
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to read from
        length -- number of bytes to read
        """
        buffer = create_string_buffer(length)
        bytes_read = c_size_t()
        if not __rPM__(process_handle, address, buffer, length, byref(bytes_read)):
            raise Exception(f"Failed to read {get_last_error()}")
        return buffer.value

    def read_float(self, process_handle, address):
        """Reads a single float at a specified address from a process
        Returns an float which is the value at [address]
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to read from
        """
        buffer = create_string_buffer(SIZE_FLOAT)
        bytes_read = c_size_t()
        if not __rPM__(process_handle, address, buffer, SIZE_FLOAT, byref(bytes_read)):
            raise Exception(f"Failed to read {get_last_error()}")
        return struct.unpack("f", buffer[0:SIZE_FLOAT])[0]

    def read_double(self, process_handle, address):
        """Reads a single double at a specified address from a process
        Returns an double which is the value at [address]
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to read from
        """
        buffer = create_string_buffer(SIZE_DOUBLE)
        bytes_read = c_size_t()
        if not __rPM__(process_handle, address, buffer, SIZE_DOUBLE, byref(bytes_read)):
            raise Exception(f"Failed to read {get_last_error()}")
        return struct.unpack("d", buffer[0:SIZE_DOUBLE])[0]

    def write_integer(self, process_handle, address, value):
        """Writes a single int at a specified address in a process
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to write to
        value -- value to write at [address]
        """
        c_data = c_char_p(struct.pack("I", value))
        c_data_ = cast(c_data, POINTER(c_char))
        __wPM__(process_handle, address, c_data_, SIZE_INT, None)
        err = get_last_error()
        if err:
            set_last_error(0)
            # print(ERR_CODE.get(err, err))

    def write_short(self, process_handle, address, value):
        """Writes a single short at a specified address in a process
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to write to
        value -- value to write at [address]
        """
        c_data = c_char_p(struct.pack("H", value))
        c_data_ = cast(c_data, POINTER(c_char))
        __wPM__(process_handle, address, c_data_, SIZE_SHORT, None)
        err = get_last_error()
        if err:
            set_last_error(0)
            # print(ERR_CODE.get(err, err))

    def write_float(self, process_handle, address, value):
        """Writes a single float at a specified address in a process
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to write to
        value -- value to write at [address]
        """
        c_data = c_char_p(struct.pack("f", value))
        c_data_ = cast(c_data, POINTER(c_char))
        __wPM__(process_handle, address, c_data_, SIZE_FLOAT, None)
        err = get_last_error()
        if err:
            set_last_error(0)
            # print(ERR_CODE.get(err, err))

    def write_double(self, process_handle, address, value):
        """Writes a single double at a specified address in a process
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to write to
        value -- value to write at [address]
        """
        c_data = c_char_p(struct.pack("d", value))
        c_data_ = cast(c_data, POINTER(c_char))
        __wPM__(process_handle, address, c_data_, SIZE_DOUBLE, None)
        err = get_last_error()
        if err:
            set_last_error(0)
            # print(ERR_CODE.get(err, err))

    def write_byte(self, process_handle, address, value):
        """Writes a single byte at a specified address in a process
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to write to
        value -- value to write at [address]
        """
        c_data = c_char_p(struct.pack("B", value))
        c_data_ = cast(c_data, POINTER(c_char))
        __wPM__(process_handle, address, c_data_, SIZE_CHAR, None)
        err = get_last_error()
        if err:
            set_last_error(0)
            # print(ERR_CODE.get(err, err))

    def write_bytes(self, process_handle, address, buffer):
        """Writes a buffer (number of bytes) to a specified address in a process
        Keyword arguments:
        process_handle -- handle to process
        address -- address in process to write to
        buffer -- a bytearray or bytes object to write at [address]
        """
        c_data = c_char_p(bytes(buffer))
        c_data_ = cast(c_data, POINTER(c_char))
        __wPM__(process_handle, address, c_data_, len(buffer), None)
        err = get_last_error()
        if err:
            set_last_error(0)
            # print(ERR_CODE.get(err, err))

    def resolve_multi_pointer(self, process_handle, base_address, offset_list):
        """Resolves a multi-level pointer to an address.
        Returns an address as (int)
        Keyword arguments:
        process_handle -- handle to process
        base_address -- base address of pointer
        offset_list -- a list of offsets (ints)
        """
        resolved_ptr = base_address
        for i in offset_list:
            resolved_ptr = self.read_integer(process_handle, resolved_ptr) + i
        return resolved_ptr

    def resolve_pointer(self, process_handle, base_address, offset):
        """Resolves a single level pointer to an address.
        Returns an address as (int)
        Keyword arguments:
        process_handle -- handle to process
        base_address -- base address of pointer
        offset -- pointer offset
        """
        return self.read_integer(process_handle, base_address) + offset