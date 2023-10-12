from fontTools.ttLib import TTFont
import binascii

base_font = [
    {"name": "&#xa895;", "value": "4", "hex": "ec9467393c47041e0fafff7f4a2852a8"},
    {"name": "&#xb341;", "value": "9", "hex": "4119e3dc64f73251d40cf1fc0323e20f"},
    {"name": "&#xb643;", "value": "6", "hex": "af603543300bfc5f0e35e941d4208759"},
    {"name": "&#xb917;", "value": "2", "hex": "9bb92485b3e2ba4bd8a93ebbd3a0fa4e"},
    {"name": "&#xc216;", "value": "0", "hex": "0aef9a3385d96e7bdd1f3003669a940c"},
    {"name": "&#xc387;", "value": "3", "hex": "b024173b00a3c901b6e696ba12812124"},
    {"name": "&#xc637;", "value": "7", "hex": "3dcfec8e26ef48730f25363da55da77a"},
    {"name": "&#xe678;", "value": "1", "hex": "2c0ec07331fa25dc226f1ca83561cb46"},
    {"name": "&#xf427;", "value": "5", "hex": "9ebca885e21990cee127d23d03acb3ac"},
    {"name": "&#xf836;", "value": "8", "hex": "f9d12372b7002b9a1522dd3dd142cf70"},
]

# TTFont打开字体文件
font = TTFont("q7/font.woff")
# 将字体文件保存为可读的xml文件
font.saveXML("q7/font.xml")
# 找字体的映射关系，字体的映射关系在cmap中体现
font_map = font.getBestCmap()
font_order = font.getGlyphOrder()
for name, glyph in font["glyf"].glyphs.items():
    flag = bytes(glyph.flags)
    print(name, flag.hex())

