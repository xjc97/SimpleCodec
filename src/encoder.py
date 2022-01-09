import struct
import aec
import enc


class PIC_INFO:
    'store the input pic file info'
    y_org = []
    u_org = []
    v_org = []
    org_path = ""
    pic_width = 176
    pic_height = 144
    frame = 1
    luma_size = pic_width * pic_height
    chroma_size = int(pic_width * pic_height * 1 / 4)

    def __init__(self, width, height, path) -> None:
        self.pic_width = width
        self.pic_height = height
        self.org_path = path
        self.luma_size = width * height
        self.chroma_size = int(width * height * 1 / 4)

    def read_yuv(self):

        yuv = open(self.org_path, "rb")
        y = yuv.read(self.luma_size)
        u = yuv.read(self.chroma_size)
        v = yuv.read(self.chroma_size)

        pix_num_luma = str(self.luma_size) + "B"
        pix_num_chroma = str(self.chroma_size) + "B"

        self.y_org = struct.unpack(pix_num_luma, y)
        self.u_org = struct.unpack(pix_num_chroma, u)
        self.v_org = struct.unpack(pix_num_chroma, v)

        yuv.close()


def enc_start(pic_info, aec_info):
    'start encoder'
    # read yuv and split to luma and chroma
    pic_info.read_yuv()

    # write pic_head info, max pic size is 1920x1080
    aec_info.bs_write(pic_info.pic_width, 2)
    aec_info.bs_write(pic_info.pic_height, 2)
    aec_info.bs_write(pic_info.frame, 2)


def enc_core(enc_info, pic_info, aec_info):
    'start encode'
    enc_info.enc_one_frame(aec_info, pic_info)


def enc_end(aec_info, pic_info):
    'encoder finish, output recon and bitstream'
    aec_info.output_bs("yuv.bin")
    del pic_info
    del aec_info


def encoder():
    # encoder top
    pic_info = PIC_INFO(176, 144, "G:\SimpleCodec\oneframe.yuv")
    aec_info = aec.AEC()
    enc_info = enc.ENC_CORE()

    enc_start(pic_info, aec_info)
    enc_core(enc_info, pic_info, aec_info)
    enc_end(aec_info, pic_info)


encoder()
