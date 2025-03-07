import os
import numpy as np
import cv2
from PIL import Image
from tqdm import tqdm
from skimage.metrics import structural_similarity as ssim
import shutil

def image_to_array(image_path):
    try:
        image = Image.open(image_path).convert('L')  # Convert to grayscale
        image = image.resize((100, 100))  # Resize for uniformity
        return np.array(image)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def find_redundant_images(image_folder, similarity_threshold=0.89):
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    image_data = {}
    redundant_images = set()
    
    print(f"Found {len(image_files)} images for comparison.")
    
    for img in tqdm(image_files, desc="Processing Images"):
        img_path = os.path.join(image_folder, img)
        img_array = image_to_array(img_path)
        if img_array is not None:
            image_data[img] = img_array
    
    img_names = list(image_data.keys())
    
    for i in range(len(img_names)):
        for j in range(i + 1, len(img_names)):
            img1, img2 = img_names[i], img_names[j]
            ssim_score = ssim(image_data[img1], image_data[img2])
            print(f"Comparing {img1} and {img2} - SSIM: {ssim_score:.4f}")
            if ssim_score > similarity_threshold:
                redundant_images.add(img2)
                print(f"Marked {img2} as redundant (SSIM: {ssim_score:.4f})")
    
    print(f"Identified {len(redundant_images)} redundant images.")
    return redundant_images

def remove_images(image_folder, redundant_images, move_to_folder=None):
    if not redundant_images:
        print("No redundant images found. Exiting.")
        return
    
    for img in redundant_images:
        img_path = os.path.join(image_folder, img)
        if move_to_folder:
            shutil.move(img_path, os.path.join(move_to_folder, img))
            print(f"Moved {img} to {move_to_folder}")
        else:
            os.remove(img_path)
            print(f"Removed: {img}")
    
    print("Duplicate removal process completed!")

if __name__ == "__main__":
    image_folder = "images/"  # Change this to your folder
    move_to_folder = "duplicates"  # Optional: Folder to move duplicates instead of deleting
    os.makedirs(move_to_folder, exist_ok=True)
    
    redundant_images = find_redundant_images(image_folder)
    remove_images(image_folder, redundant_images, move_to_folder=move_to_folder)
