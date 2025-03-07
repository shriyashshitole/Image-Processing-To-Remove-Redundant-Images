# 🖼️Image-Processing-To-Remove-Redundant-Images

A Python script to identify and remove redundant (**highly similar**) images in a folder using **Structural Similarity Index (SSIM)**.

## 📌Features

- Detects duplicate or highly similar images based on SSIM.  
- Converts images to grayscale and resizes them for uniformity before comparison.  
- Provides an option to either delete redundant images or move them to a separate folder.  
- Uses `tqdm` for progress tracking.
  

## 📃Requirements

Install dependencies using:

bash:
pip install numpy opencv-python pillow tqdm scikit-image  


## 🚀Usage

#### 1. Place all images in a folder (default: images/).

#### 2. Run the script:

  bash:
  python Remove\ Redundant.py

#### 3. Redundant images will be either:

  Deleted (default behavior)
  Moved to a folder named duplicates/ (can be changed in the script).  
  

## 🤖Customization
Change image_folder in the script to specify your image directory.
Modify move_to_folder to define where redundant images should be moved.
Adjust similarity_threshold (default: 0.89) to control how strictly images are considered duplicates.  


## 🗳️Example Output

bash:  
Found 100 images for comparison.  
Comparing img1.jpg and img2.jpg - SSIM: 0.9203  
Marked img2.jpg as redundant (SSIM: 0.9203)  
...
Identified 10 redundant images.  
Moved img2.jpg to duplicates/  


## 🤝 Contributing
Feel free to submit issues or pull requests!  


## 📜License
This project is licensed under the MIT License.
