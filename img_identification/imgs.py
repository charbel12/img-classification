import os

def create_labels(image_directory, label_directory, class_index, bbox):
    # Ensure the label directory exists
    os.makedirs(label_directory, exist_ok=True)

    # Get the list of files in the specified directory
    files = os.listdir(image_directory)

    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # Adjust for your image types
            # Create the corresponding label filename
            label_filename = os.path.splitext(filename)[0] + '.txt'
            label_path = os.path.join(label_directory, label_filename)

            # Create the label file with the specified bounding box
            with open(label_path, 'w') as label_file:
                label_file.write(f"{class_index} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n")
            print(f"Created label: {label_path}")

def main():
    # Define directories for train and validation images
    base_directory = os.path.dirname(os.path.abspath(__file__))
    train_directory = os.path.join(base_directory, 'dataset', 'images', 'train')
    val_directory = os.path.join(base_directory, 'dataset', 'images', 'val')
    
    # Define output directories for labels
    train_label_directory = os.path.join(base_directory, 'dataset', 'labels', 'train')
    val_label_directory = os.path.join(base_directory, 'dataset', 'labels', 'val')

    # Define the class index and bounding box values
    class_index = 0
    bbox = [0.5, 0.5, 0.3, 0.2]  # Example bounding box values

    # Create labels for training and validation images
    create_labels(train_directory, train_label_directory, class_index, bbox)
    create_labels(val_directory, val_label_directory, class_index, bbox)

if __name__ == "__main__":
    main()
