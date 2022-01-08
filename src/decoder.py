import aec


def decoder():
    'test demo'
    aec_info = aec.AEC()
    bs_path = 'G:\SimpleCodec\yuv.bin'
    bs = open(bs_path, "rb")

    yuv = []
    # read pic_head info
    pic_width = aec_info.translate_bin(bs.read(2), 2)
    pic_height = aec_info.translate_bin(bs.read(2), 2)
    pic_frame = aec_info.translate_bin(bs.read(2), 2)
    print(pic_width, pic_height, pic_frame)

    luma_size = pic_width * pic_height
    chroma_size = int(pic_width * pic_height * 1 / 4)
    for i in range(0, luma_size):
        yuv.append(aec_info.translate_bin(bs.read(1), 1))

    for i in range(0, chroma_size):
        yuv.append(aec_info.translate_bin(bs.read(1), 1))

    for i in range(0, chroma_size):
        yuv.append(aec_info.translate_bin(bs.read(1), 1))

    for pix in yuv:
        aec_info.bs_write(pix, 1)

    aec_info.output_bs("dec.yuv")
    
    bs.close

decoder()