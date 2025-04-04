    import cv2
import sqlite3
import time
import requests
import schedule

with open('opencv_haarcascade_data/obj.names', 'rt') as f:
    names = f.read().rstrip('\n').split('\n')
net = cv2.dnn_DetectionModel('opencv_haarcascade_data/yolo-obj-2.cfg', 'opencv_haarcascade_data/yolo-obj-2_best.weights')
net.setInputSize(608, 608)
net.setInputScale(1.0 / 255)
net.setInputSwapRB(True)

localtime = time.localtime()
result = time.strftime("%Y-%m-%d %H:%M:%S", localtime)


def time():
    print("it's running")
    schedule.every(10).seconds.do(detection)
    while True:
        schedule.run_pending()


def detection():
    try:
        frame = cv2.imread('D://python/Django_VideoStream/image/out.jpg')
        print("test")
        # print(names)
        classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.4)
        # print(classes, confidences)
        if len(classes) == 0:
            return

        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            if (names[classId] == 'death') & (confidence > 0.7):
                lineNotifyMessage(result)
                insertdata()
    except:
        pass


def lineNotifyMessage(result):

    # 修改為你要傳送的訊息內容
    message = result + '偵測到死雞'
    token = 'dUoXUlqYrB3UeX2O2u5AKuDj7OWQGeyogUXWPkXeaHB'
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': message}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

def insertdata():
    conn = sqlite3.connect('d:\python\Django_VideoStream\db.sqlite3')
    c = conn.cursor()
    c.execute("INSERT INTO streamapp_data(locals,creatTime) VALUES('a',datetime(CURRENT_TIMESTAMP,'localtime'))")
    conn.commit()
    conn.close()

# def dataopen():
#     conn = sqlite3.connect('C:\Django_VideoStream\db.sqlite3')
#     c = conn.cursor()
#     cursor = c.execute("SELECT * FROM streamapp_data")
#     for row in cursor:
#         print("ID = ", row[0])
#         print("locals = ", row[1])
#         print("creatTime = ", row[2])
#
#     print("数据操作成功")
#     conn.close()
if __name__=='__main__':
    time()
# detection()
# dataopen()
