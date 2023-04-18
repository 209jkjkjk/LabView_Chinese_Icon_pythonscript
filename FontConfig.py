class FontConfig:
    def __int__(self):
        self.multixy = (0, 0)
        self.multispacing = 0
        self.textxy = (0, 0)
        self.fontSource = ""
        self.fontSize = 10

# 丁卯点阵Demo像素字体
DinkieDemoConfig = FontConfig()
DinkieDemoConfig.multixy = (1, -1)
DinkieDemoConfig.multispacing = 0
DinkieDemoConfig.textxy = (32, 30)
DinkieDemoConfig.fontSource = "./fonts/DinkieBitmap-9pxDemo.ttf"
DinkieDemoConfig.fontSize = 10

# 正体点阵
ZfullConfig = FontConfig()
ZfullConfig.multixy = (1, 0)
ZfullConfig.multispacing = -1
ZfullConfig.textxy = (31, 30)
ZfullConfig.fontSource = "./fonts/Zfull-GB.ttf"
ZfullConfig.fontSize = 10

# 丁卯点阵像素字体
DinkieConfig = FontConfig()
DinkieConfig.multixy = (1, -1)
DinkieConfig.multispacing = 0
DinkieConfig.textxy = (32, 30)
DinkieConfig.fontSource = "./fonts/DinkieBitmap-9px.ttf"
DinkieConfig.fontSize = 10