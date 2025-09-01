class WMITransport:
    name = "wmi"
    def connect(self): return True
    def write(self, data: bytes): return len(data)
    def read(self, n: int): return b"\x00" * n
