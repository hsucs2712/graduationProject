import tkinter
import serial
import time
import threading

COM_PORT = 'COM4'           #ardiuno 連接序
BAUD_RATES = 9600
COM_PORT2 = 'COM3'           #ardiuno 連接序
BAUD_RATES2 = 115200

try:
    ser = serial.Serial(COM_PORT, BAUD_RATES)
except:
    print('連接失敗 Arduino 1')


try:
    ser2 = serial.Serial(COM_PORT2, BAUD_RATES2)
except:
    print('連接失敗 Arduino 2')


def get():
    while True:
        mcu_feedback = ser2.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)
        ser.write(b'stop\n')


def general():
    ser.write(b'general\n')  # 訊息必須是位元組類型 傳送訊息到arduino
    ser2.write(b'run\n')     # 傳送飼料雞移動訊息
    time.sleep(5)
    while ser2.in_waiting:
        mcu_feedback = ser2.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)
        ser.write(b'stop\n')


def feather():
    ser.write(b'feather\n')  # 訊息必須是位元組類型 傳送訊息到arduino
    ser2.write(b'run\n')    # 傳送飼料雞移動訊息
    time.sleep(5)
    while ser2.in_waiting:
        mcu_feedback = ser2.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)
        ser.write(b'stop\n')




def UI():
    root = tkinter.Tk()
    root.title('飼料機控制')
    root.geometry("960x480")
    root.title('飼料機')
    root.resizable(False, False)

    # label
    label = tkinter.Label(root, text="飼料機控制器", font=("微軟正黑體", 24))
    label.place(x=400, y=50)

    # 模式按鈕
    label2 = tkinter.Label(root, text="模式選擇", font=("微軟正黑體", 24))
    label2.place(x=50, y=125)
    model1 = tkinter.Button(root, text='一般模式', font=('微軟正黑體', 16), bg="green", command=general)
    model1.place(x=50, y=200)
    model2 = tkinter.Button(root, text='退羽模式', font=('微軟正黑體', 16), bg="yellow", command=feather)
    model2.place(x=200, y=200)

    root.mainloop()


t1 = threading.Thread(target=UI, args=())
c1 = threading.Thread(target=get, args=())
t1.start()
c1.start()
