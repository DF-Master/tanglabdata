# Default Code https://www.gy-printer.com/index.php?id=test-sample
test_code = bytes([0x12, 0x54])

ini_code = bytes([0x1B, 0x40])  # 1B 40 （初始化）

pageIni_code = bytes([0x1A, 0x5B, 0x01])  # 1A 5B 01（页开始）
defaultPos_code = bytes([0x00, 0x00, 0x00, 0x00])  #  00 00 00 00 （初始位置）
defaultWidth_code = bytes([0x80, 0x01])  # 80 01（页宽384个点即48MM）
defaultHeight_code = bytes([0x40, 0x01])  #  40 01（页高320个点即40MM）
defaultDegree_code = bytes([0x00])  # 00（页旋转方向“00”默认不旋转）
defaultStartCode = ini_code + pageIni_code + defaultPos_code + defaultWidth_code + defaultHeight_code + defaultDegree_code

oneDPrint_code = bytes([0x1A, 0x30, 0x00])  # 1A 30 00（打印条码）
oneDX_code = bytes([0x18, 0x00])  # 18 00（X横向坐标3MM位置即3*8=24个点）
oneDY_code = bytes([0x10, 0x00])  # 6C 00（Y纵向坐标2MM位置即2*8=16个点）
oneDType_code = bytes([0x08])  # 08（条码类型CODE128）
oneDHeight_code = bytes([0x4B])  # 4B（条码高度）
oneDWeight_code = bytes([0x02])  # 02（条码宽度）
oneDDegree_code = bytes([0x00])  # 00（旋转角度）
defaultOneDCode = oneDPrint_code + oneDX_code + oneDY_code + oneDType_code + oneDHeight_code + oneDWeight_code + oneDDegree_code
oneDDefaultCode = "e038ba45c47d".encode(
    "utf-8")  # （条码内容“c33ca4a3-fa26-440e-8c34-e038ba45c47d”）
end_code = bytes([0x00])  # 00（结束）


def printWord(name, y=108, size=0):
    return (bytes([0x1A, 0x54, 0x01]) + bytes([0x18, 0x00]) +
            bytes.fromhex(hex(y)[2:].zfill(4)[2:]) +
            bytes.fromhex(hex(y)[2:].zfill(4)[:2]) + bytes([0x18, 0x00]) +
            bytes([0x00]) + bytes.fromhex(hex(size)[2:].zfill(2)) +
            name.encode("gbk") + bytes([0x00]))


pageEnd_code = bytes([0x1A, 0x5D, 0x00])  # 1A 5D 00（页结束）
pagePrint_code = bytes([0x1A, 0x4F, 0x00])  # 1A 4F 00（页打印）
defaultEndCode = pageEnd_code + pagePrint_code

# Server
host_url = "http://tanglabdata.top:7860/catalog/data/"