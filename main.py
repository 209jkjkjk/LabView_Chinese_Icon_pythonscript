from PIL import Image, ImageDraw, ImageFont
import os

class TextConfig:
    def __int__(self):
        self.multixy = (0, 0)
        self.multispacing = 0
        self.textxy = (0, 0)
        self.fontSource = ""
        self.fontSize = 10

# 丁卯点阵像素字体
DinkieConfig = TextConfig()
DinkieConfig.multixy = (1, -1)
DinkieConfig.multispacing = 0
DinkieConfig.textxy = (32, 30)
DinkieConfig.fontSource = "./fonts/DinkieBitmap-9pxDemo.ttf"
DinkieConfig.fontSize = 10

# 正体点阵
ZfullConfig = TextConfig()
ZfullConfig.multixy = (1, 0)
ZfullConfig.multispacing = -1
ZfullConfig.textxy = (31, 30)
ZfullConfig.fontSource = "./fonts/Zfull-GB.ttf"
ZfullConfig.fontSize = 10




def watermark(iconTemplateSource, deviceName, funcText, config: TextConfig):
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
    draw.multiline_text(config.multixy, text=deviceText, font=font, stroke_width=0, spacing=config.multispacing, fill=(239, 175, 74))
    draw.text(config.textxy, anchor="rs", text=funcText, align="right", font=font, stroke_width=0, fill=(236, 82, 35))

    # 获取后缀名并保存
    name, ext = os.path.splitext(iconTemplateSource)
    img.save(f"test{ext}")
    # img.save(f"{deviceName}_{funcText}{ext}")


if __name__ == '__main__':
    watermark("./模板.png", "可调电源", "读额V", DinkieConfig)


