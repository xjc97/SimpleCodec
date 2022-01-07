import struct

class PIC_INFO:
    'store the input pic file info'
    y_org = []
    u_org = []
    v_org = []
    org_path = ""
    pic_width = 176
    pic_height = 144
    def __init__(self, width, height, path) -> None:
        self.pic_width = width
        self.pic_height = height
        self.org_path = path

    def read_yuv(self):
        luma_size = self.pic_width * self.pic_height
        chroma_size = int(self.pic_width * self.pic_height * 1 / 4)

        yuv = open(self.org_path, "rb")
        y = yuv.read(luma_size)
        u = yuv.read(chroma_size)
        v = yuv.read(chroma_size)

        pix_num_luma = "<" + str(luma_size) + "B"
        pix_num_chroma = "<" + str(chroma_size) + "B"

        self.y_org = struct.unpack(pix_num_luma, y)
        self.u_org = struct.unpack(pix_num_chroma, u)
        self.v_org = struct.unpack(pix_num_chroma, v)

        yuv.close()


def enc_core():
    # encoder core
    print("encoder core")

def enc_end():
    # write bitstream and recon out
    print("write bitstream and recon out")

def encoder():
    # encoder top
    pic = PIC_INFO(176, 144, "C:\work\SimpleCodec\oneframe.yuv")
    pic.read_yuv()
    enc_core()
    enc_end()

    
    del pic





encoder()
