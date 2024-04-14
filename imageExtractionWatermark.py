from blind_watermark import WaterMark

def extract_watermark(input_path, len_wm_path):
    """
    从给定的图片中提取水印。

    :param input_path: 带水印图片的路径。
    :param len_wm_path: 保存水印长度的文本文件路径。
    :return: 提取的水印文本。
    """
    # 首先读取水印长度
    with open(len_wm_path, 'r') as f:
        len_wm = int(f.read())

    # 创建WaterMark对象
    bwm1 = WaterMark(password_img=1, password_wm=1)

    # 提取水印
    wm_extract = bwm1.extract(input_path, wm_shape=len_wm, mode='str')
    return wm_extract
# 封装提取水印的功能到一个函数
# def extract_watermark_from_image(input_image_path, wm_shape):
#     # 创建 WaterMark 实例
#     bwm1 = WaterMark(password_img=1, password_wm=1)
#     # 提取水印
#     wm_extract = bwm1.extract(input_image_path, wm_shape=wm_shape, mode='str')
#
#     return wm_extract


# 如果直接运行此脚本，可以用作测试
# if __name__ == "__main__":
#     extracted_watermark = extract_watermark_from_image('output/wm_9311.jpg_wh300.jpg', 100)  # 假设水印长度为100
#     #print('Extracted Watermark:', extracted_watermark#@#)
