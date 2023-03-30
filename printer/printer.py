import settings as set
import Serialcontrol as sc

if __name__ == '__main__':
    printer = sc.Communication(
        com="COM5",
        bps=115200,
    )
    print(set.printWord("e038ba45c47d"))
    # printer.Send_data(set.defaultStartCode + set.defaultOneDCode +
    #                   set.oneDDefault_code + set.end_code +
    #                   set.printWord("ID: e038ba45c47d", y=96) +
    #                   set.printWord("Name: 甘氨酸", y=126) +
    #                   set.printWord("date: 2023-03-30", y=156) +
    #                   set.printWord("Manager: Yida Jiang", y=186) +
    #                   set.printWord("Location: B213", y=216) +
    #                   set.printWord("Note: ", y=246) + set.defaultEndCode)
