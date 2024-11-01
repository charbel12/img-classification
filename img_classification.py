import os
from ultralytics import YOLO

# Set dataset paths
dataset_path = r'C:\Users\DEV 15\Desktop\AI\datasets\imagenet'
train_path = os.path.join(dataset_path, 'train')
test_path = os.path.join(dataset_path, 'test')

# Check if train dataset exists
if not os.path.exists(train_path):
    print(f"Training dataset not found at {train_path}. Please ensure the dataset is downloaded and structured correctly.")
else:
    model = YOLO('yolov8n-cls.pt')
    
    # Validate the model
    metrics = model.val()
    print(metrics)

    # Define the image path
    image_path = r'C:\Users\DEV 15\Desktop\AI\dataset\images\train\cable_image_2.jpg'

    # Predict on the image
    results = model.predict(image_path)
    print(results)
