from crypt import methods
from ctypes import resize
from email.mime import image
from flask import Flask,render_template,request
import cv2
import random
app = Flask(__name__,static_url_path='/static')

class YoloV4:
    def __init__(self):
        self.net = cv2.dnn.readNetFromDarknet("model/yolov4.cfg","model/yolov4.weights")
        self.model = cv2.dnn_DetectionModel(self.net)
        self.classes = {
            0 : "Sau ve bua",
            1 : "Phan trang",
            2 : "Nam ri sat",
            3 : "Dom rong"
        }
        self.color = {
            1 : (255,255,255),
            2 : (255,255,255),
            3 : (255,255,255)
        }
    def load_model(self):
        self.model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    def predict(self,path):
        img = cv2.imread(path)
        h = img.shape[0]
        w = img.shape[1]
        # img = cv2.resize(img,(416,416))
        classIds, scores, boxes = self.model.detect(img, confThreshold=0.25, nmsThreshold=0.4)
        print(classIds)
        for (classId, score, box) in zip(classIds, scores, boxes):
            index = random.randint(1,3)
            cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                    color=self.color[index], thickness=2)
    
            text = '%s: %.2f' % (self.classes[classIds[0]], score)
            if box[1] < 100:
                cv2.putText(img, text, (box[0], box[1] + box[3]+ 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=self.color[index], thickness=2)
            else:
                cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=self.color[index], thickness=2)
        name = path.split(".jpg")
        imgDetected = "{}.jpg".format(name[0]+"_detected")
        img = cv2.resize(img,(w,h))
        cv2.imwrite(imgDetected,img)
        return imgDetected
m = YoloV4()
m.load_model()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect",methods=['POST','GET'])
def detect():
    if request.method == "POST":
        imgFile = request.files['file'];
        # imgFile = request.args.get("img")
        imgPath =   "./static/images/" + imgFile.filename
        imgFile.save(imgPath)
        path = m.predict(imgPath)
        return path
        # return "<img src='"+path+"'/>"
        
if __name__ == "__main__":
    app.run(debug=False)