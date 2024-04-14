from blind_watermark import bw_notes  # 导入bw_notes
# 关闭启动信息
bw_notes.close()
from blind_watermark import WaterMark

def embed_watermark(input_path, output_path, watermark_text='felix is the best!'):
    bwm1 = WaterMark(password_img=1, password_wm=1)
    bwm1.read_img(input_path)
    bwm1.read_wm(watermark_text, mode='str')
    bwm1.embed(output_path)
    len_wm = len(bwm1.wm_bit)
    return len_wm  # 返回水印长度
# def embed_watermark(input_path, output_path, watermark_text='felix is the best'):
#     """
#     将水印嵌入给定的图片中，并保存到指定的输出路径。
#
#     :param input_path: 输入图片的路径。
#     :param output_path: 输出图片的路径，水印嵌入后的图片将保存在此。
#     :param watermark_text: 要嵌入的水印文本，默认为'felix is the best'。
#     """
#     bwm1 = WaterMark(password_img=1, password_wm=1)
#     bwm1.read_img(input_path)
#     bwm1.read_wm(watermark_text, mode='str')
#     bwm1.embed(output_path)
#     print('Watermark embedded successfully. Output file:', output_path)


# 如果这个脚本被直接运行，下面的代码块不会执行。
# 这确保了当从另一个脚本（如 app.py）导入函数时，不会执行下面的测试代码。
if __name__ == "__main__":
    # 这里可以添加一些测试代码，例如：
    embed_watermark('src/uploads/2590.jpg_wh300.jpg', 'src/output/wm_7588.jpg_wh300.png')
    pass

# import os
#
# from blind_watermark import WaterMark
#
#
# # 注意：这里假设关闭启动信息的 bw_notes.close() 是有效的
# # 如果在您的环境中 blind_watermark 库不包含这个功能，请注释掉下面这行代码
# # from blind_watermark import bw_notes
# # bw_notes.close()
#
# def embed_watermark(input_path, watermark_text='felix is the best'):
#     """
#     将水印嵌入给定的图片中，并保存到指定的输出路径。
#
#     :param input_path: 输入图片的路径。
#     :param watermark_text: 要嵌入的水印文本，默认为'felix is the best'。
#     :return: 嵌入水印后图片的路径和水印长度。
#     """
#     # 创建 WaterMark 实例
#     bwm1 = WaterMark(password_img=1, password_wm=1)
#
#     # 读取图像文件
#     bwm1.read_img(input_path)
#
#     # 读取水印文本
#     bwm1.read_wm(watermark_text, mode='str')
#
#     # 创建输出文件路径，将文件扩展名更改为 .png
#     output_path = os.path.splitext(input_path)[0] + "_wm.png"
#
#     # 嵌入水印
#     bwm1.embed(output_path)
#
#     # 获取水印长度
#     len_wm = len(bwm1.wm_bit)
#
#     print('Watermark embedded successfully. Output file:', output_path)
#
#     # 返回输出路径和水印长度
#     return output_path, len_wm
#
#
# # 如果这个脚本被直接运行，下面的代码块不会执行。
# # 这确保了当从另一个脚本（如 app.py）导入函数时，不会执行下面的测试代码。
# if __name__ == "__main__":
#     # 这里可以添加一些测试代码，例如：
#     output_path, len_wm = embed_watermark('uploads/9311.jpg_wh300.jpg', 'Watermark content')
#     print('Output path:', output_path)
#     print('Length of watermark:', len_wm)
#
