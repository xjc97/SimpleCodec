import struct
import os


class AEC:
    'class of aec'
    bs = []

# encoder func
    def bs_write(self, elemt, byte_size):
        'binary sytex'
        dic = {1: 'B', 2: 'H', 4: 'I'}
        fmt = dic[byte_size]
        self.bs.append(struct.pack(fmt, elemt))

    def output_bs(self, bs_path):
        'output bitstream'
        if os.path.exists(bs_path):
            os.remove(bs_path)
        f_out = open(bs_path, "ab")
        for bit in self.bs:
            f_out.write(bit)
        f_out.close

    def aec_top(self, pic_info):
        'write mode decide info to bitstream'
        for bit in pic_info.y_org:
            self.bs_write(bit, 1)
        for bit in pic_info.u_org:
            self.bs_write(bit, 1)
        for bit in pic_info.v_org:
            self.bs_write(bit, 1)

# decoder func
    def translate_bin(self, bin, byte_size):
        'trans bin to elemt'
        dic = {1: 'B', 2: 'H', 4: 'I'}
        fmt = dic[byte_size]
        elemt = struct.unpack(fmt, bin)
        return elemt[0]
