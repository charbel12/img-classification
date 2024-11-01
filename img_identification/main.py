import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    results = model(frame)

    annotated_frame = results[0].plot()  

    cv2.imshow('Cable Detection - YOLOv8', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
