class ECTransport:
    name = "ec"
    def acquire(self): return True
    def poke(self, addr: int, val: int): return (addr, val)
