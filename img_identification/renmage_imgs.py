import os

def rename_images(directory, prefix):
    # Get the list of files in the specified directory
    files = os.listdir(directory)
    
    # Filter out non-JPEG files and keep track of the index
    index = 1
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # You can add more extensions if needed
            # Define the new filename
            new_filename = f"{prefix}_{index}.jpg"  # Change to .jpeg or .png if necessary
            # Create the full old and new file paths
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")
            
            # Increment the index for the next file
            index += 1

def main():
    # Define the directories for train and validation images
    # Use absolute paths based on the current working directory
    base_directory = os.path.dirname(os.path.abspath(__file__))
    train_directory = os.path.join(base_directory, 'dataset', 'images', 'train')
    val_directory = os.path.join(base_directory, 'dataset', 'images', 'val')
    
    # Rename images in the training set
    rename_images(train_directory, 'cable_image')
    
    # Rename images in the validation set
    rename_images(val_directory, 'cable_val_image')

if __name__ == "__main__":
    main()
