from deepface import DeepFace
import cv2

cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    DeepFace.stream(db_path = 'Resources/')
    cv2.imshow("Live Stream", frame)
    cv2.waitKey(1)

# verification = DeepFace.verify(img1_path = "Resources/Tony_New.jpg", img2_path = "Resources/Manikandan.jpg")
# recognition = DeepFace.find(img_path = "img.jpg", db_path = “C:/facial_db")
# analysis = DeepFace.analyze(img_path = "Resources/Bharat.jpg", actions = ["age", "gender", "emotion", "race"])
# DeepFace.stream(db_path = “C:/facial_db”)
# print(analysis)


# models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]
# face verification
# verification1 = DeepFace.verify("Resources/Tony_New.jpg", "Resources/Tony_Old.jpg", model_name = models[0])
# verification2 = DeepFace.verify("Resources/Tony_New.jpg", "Resources/Tony_Old.jpg", model_name = models[1])
# verification3 = DeepFace.verify("Resources/Tony_New.jpg", "Resources/Tony_Old.jpg", model_name = models[2])
# verification4 = DeepFace.verify("Resources/Tony_New.jpg", "Resources/Tony_Old.jpg", model_name = models[3])
# verification5 = DeepFace.verify("Resources/Tony_New.jpg", "Resources/Tony_Old.jpg", model_name = models[4]) # Error
# verification6 = DeepFace.verify("Resources/Tony_New.jpg", "Resources/Tony_Old.jpg", model_name = models[5]) # Error
# verification7 = DeepFace.verify("Resources/Tony_New.jpg", "Resources/Tony_Old.jpg", model_name = models[6])
# print("verification1", verification1)
# print("verification2", verification2)
# print("verification3", verification3)
# print("verification4", verification4)
# print("verification5", verification5) # Error
# print("verification6", verification6) # Error
# print("verification7", verification7)


# face recognition
# recognition = DeepFace.find(img_path = "img.jpg", db_path = “C:/facial_db", model_name = models[1])
