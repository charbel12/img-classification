from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')
model.train(data='dataset/data.yaml', epochs=50, imgsz=640)

metrics = model.val()
print(metrics)

results = model.predict('C:\Users\DEV 15\Desktop\AI\dataset\images\train\cable_image_12.jpg')
print(results)
