class NVMeTransport:
    name = "nvme"
    def send_vendor_cmd(self, opcode: int, payload: bytes): return {"opcode": opcode, "len": len(payload)}
