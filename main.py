from PIL import Image, ImageDraw, ImageFont
from FontConfig import *
from ImgStyle import *
import os


def func(deviceName, funcText, config: FontConfig, style: ImgStyle):
    # 打开图片
    img = Image.open(style.template)

    # 处理换行
    if '_' in deviceName:   # 有_则按照_换行
        deviceText = deviceName.replace("_", "\n")
    else:
        deviceLen = len(deviceName)
        if deviceLen <= 3:
            deviceText = deviceName
        elif deviceLen == 4:
            deviceText = deviceName[0:2] + '\n' + deviceName[2:4]
        elif deviceLen == 5:
            deviceText = deviceName[0:3] + '\n' + deviceName[3:5]
        elif deviceLen == 6:
            deviceText = deviceName[0:3] + '\n' + deviceName[3:6]
        else:
            deviceText = "名字很\n长很长"

    # 添加文字
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font=config.fontSource, size=config.fontSize)
    draw.multiline_text(config.multixy, text=deviceText, font=font, stroke_width=0, spacing=config.multispacing,
                        fill=style.mainColor)
    draw.text(config.textxy, anchor="rs", text=funcText, align="right", font=font, stroke_width=0, fill=style.subColor)

    # 获取后缀名并保存
    name, ext = os.path.splitext(style.template)
    img.save(f"test{ext}")
    img.save(f"./output/{deviceName}_{funcText}{ext}")


if __name__ == '__main__':
    func("工具函数", f"位判断", DinkieConfig, toolStyle)
