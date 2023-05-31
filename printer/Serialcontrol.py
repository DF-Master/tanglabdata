import serial
import serial.tools.list_ports

# 定义默认系统变量

# 打开串口


class Communication():
    #初始化

    def __init__(self, com='/dev/ttyACM0', bps=9600, timeout=1):
        global Ret
        try:
            self.main_engine_ser = serial.Serial(port=com,
                                                 baudrate=bps,
                                                 timeout=timeout)
            if (self.main_engine_ser.is_open):
                Ret = True
            self.main_engine_ser.stopbits = serial.STOPBITS_ONE
            self.main_engine_ser.bytesize = 8
            self.main_engine_ser.parity = serial.PARITY_NONE
            self.main_engine_ser.rtscts = 0
            print('### InitSerial ALREADY ###')
        except Exception as e:
            print('\033[1;33;44m### InitSerial Failed! ###\033[0m', e)

    # 打印设备基本信息

    def Print_Name(self):
        print("Name:", self.main_engine_ser.name)  #设备名字
        print("Port:", self.main_engine_ser.port)  #读或者写端口
        print("Baudrate:", self.main_engine_ser.baudrate)  #波特率
        print("Bytesize:", self.main_engine_ser.bytesize)  #字节大小
        print("Parity:", self.main_engine_ser.parity)  #校验位
        print("stopbits:", self.main_engine_ser.stopbits)  #停止位
        print("Timeout:", self.main_engine_ser.timeout)  #读超时设置
        print("WriteTimeout:", self.main_engine_ser.writeTimeout)  #写超时
        print("Xonxoff:", self.main_engine_ser.xonxoff)  #软件流控
        print("Rtscts:", self.main_engine_ser.rtscts)  #软件流控
        print("Dsrdtr:", self.main_engine_ser.dsrdtr)  #硬件流控
        print("InterCharTimeout:",
              self.main_engine_ser.interCharTimeout)  #字符间隔超时

    # 打印可用串口列表
    @staticmethod
    def Print_Used_Com():
        port_list = list(serial.tools.list_ports.comports())
        print("Available Ports:", port_list)

    # 计算Ascii码的异或和校验
    @staticmethod
    def Cal_Xor(str_order, key="$", append_order=False, hex_swtich=False):
        r = ord(key)
        for i in list(str_order):
            r = r ^ ord(i)
        if append_order == False:

            if hex_swtich == False:
                return r
            else:
                return hex(r)[2:].zfill(2)
        else:
            return ("$" + str(str_order) + str(hex(r)[2:].zfill(2)))

    #打开串口
    def Open(self):
        self.main_engine_ser.open()
        print("COM STATUS:", self.main_engine_ser.is_open)  # 检验串口是否打开

    #关闭串口
    def Close(self):
        self.main_engine_ser.close()
        print("COM STATUS:", self.main_engine_ser.is_open)  # 检验串口是否打开

    #检查串口
    def Check(self):
        print("COM STATUS:", self.main_engine_ser.is_open)  # 检验串口是否打开

    #接收指定大小的数据
    #从串口读size个字节。如果指定超时，则可能在超时后返回较少的字节；如果没有指定超时，则会一直等到收完指定的字节数。
    def Read_Size(self, size):
        return self.main_engine_ser.read(size=size)

    #接收一行数据
    # 使用readline()时应该注意：打开串口时应该指定超时，否则如果串口没有收到新行，则会一直等待。
    # 如果没有超时，readline会报异常。
    def Read_Line(self):
        return self.main_engine_ser.readline()

    #发数据
    def Send_data(self, data):
        self.main_engine_ser.write(data)

    #更多示例
    # self.main_engine_ser.write(chr(0x06).encode("utf-8")) # 十六制发送一个数据
    # print(self.main_engine_ser.read().hex()) # # 十六进制的读取读一个字节
    # print(self.main_engine_ser.read())#读一个字节
    # print(self.main_engine_ser.read(10).decode("gbk"))#读十个字节
    # print(self.main_engine_ser.readline().decode("gbk"))#读一行
    # print(self.main_engine_ser.readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
    # print(self.main_engine_ser.in_waiting)#获取输入缓冲区的剩余字节数
    # print(self.main_engine_ser.out_waiting)#获取输出缓冲区的字节数
    # print(self.main_engine_ser.readall())#读取全部字符。

    #接收数据
    #一个整型数据占两个字节
    #一个字符占一个字节

    def Recive_data(self, way):
        # 循环接收数据，此为死循环，可用线程实现
        print("### Start Recive_data ###：")
        while True:
            try:
                # 一个字节一个字节的接收
                if self.main_engine_ser.in_waiting:
                    if (way == 0):
                        for i in range(self.main_engine_ser.in_waiting):
                            print("Recive Ascii Data：" +
                                  str(self.Read_Size(1)))
                            data1 = self.Read_Size(1).hex()  #转为十六进制
                            data2 = int(data1, 16)  #转为十进制
                            if (data2 == "exit"):  # 退出标志
                                break
                            else:
                                print("收到数据十六进制：" + data1 + " 收到数据十进制：" +
                                      str(data2))
                    if (way == 1):
                        #整体接收
                        # data = self.main_engine_ser.read(self.main_engine_ser.in_waiting).decode("utf-8")#方式一
                        data = self.main_engine_ser.read_all()  #方式二
                        if (data == "exit"):  # 退出标志
                            break
                        else:
                            print("Recive Ascii Data：", data)
            except Exception as e:
                print("异常报错：", e)


if __name__ == '__main__':
    Communication.Print_Used_Com()
    channel_1 = Communication(
        com="/dev/ttyACM0",
        bps=115200,
    )
    channel_1.Print_Name()
    channel_1.Check()
    # # channel_1.Send_data(b"$3100016")
