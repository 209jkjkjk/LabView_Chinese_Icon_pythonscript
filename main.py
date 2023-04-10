from PIL import Image, ImageDraw, ImageFont
from TextConfig import *
from TextStyle import *
import os


def watermark(iconTemplateSource, deviceName, funcText, config: TextConfig, style: TextStyle):
    # 打开图片
    img = Image.open(iconTemplateSource)

    # 处理换行
    deviceText = ""
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
    draw.multiline_text(config.multixy, text=deviceText, font=font, stroke_width=0, spacing=config.multispacing, fill=style.deviceColor)
    draw.text(config.textxy, anchor="rs", text=funcText, align="right", font=font, stroke_width=0, fill=style.funcColor)

    # 获取后缀名并保存
    name, ext = os.path.splitext(iconTemplateSource)
    img.save(f"test{ext}")
    # img.save(f"./output/{deviceName}_{funcText}{ext}")


if __name__ == '__main__':
    watermark("./模板.png", "可调电源", "写额V", ZfullConfig, powerStyle)


