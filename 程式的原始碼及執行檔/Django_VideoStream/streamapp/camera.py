import cv2, os, time
from django.conf import settings

Conf_threshold = 0.4
NMS_threshold = 0.4
COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# 讀取物件名稱
with open(os.path.join(settings.BASE_DIR, 'opencv_haarcascade_data/obj.names'), 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.frame_counter = 0
        self.starting_time = time.time()

        # 初始化 YOLO 模型
        net = cv2.dnn.readNet(os.path.join(settings.BASE_DIR, 'opencv_haarcascade_data/yolo-obj-2_best.weights'),
                              os.path.join(settings.BASE_DIR, 'opencv_haarcascade_data/yolo-obj-2.cfg'))
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if not success:
            return None

        self.frame_counter += 1

        # 計算 FPS
        elapsed_time = time.time() - self.starting_time
        fps = self.frame_counter / elapsed_time if elapsed_time > 0 else 0
        cv2.putText(image, f'FPS: {fps:.2f}', (20, 50),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

        # 每 30 幀儲存一次圖片，避免頻繁寫入影響性能
        if self.frame_counter % 30 == 0:
            cv2.imwrite('D:/Python/Django_VideoStream/image/out.jpg', image)

        # 轉換成 JPEG 格式輸出
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
