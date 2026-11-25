import os
import cv2
import matplotlib.pyplot as plt
def RotateToPerfection(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rotation_matrix, (width, height))
def BrightenPhotoToGiveVibrantLook(image, factor):
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)
def CropToHighlightMainSection(image, start_row, end_row, start_col, end_col):
    return image[start_row:end_row, start_col:end_col]
def PerformFunction(function, image, *args):
    return function(image, *args)
def Show(image, title="Edited Image"):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "color.jpeg")
Image = cv2.imread(image_path)
if Image is None:
    raise FileNotFoundError(f"Could not find image at: {image_path}")
brightened = PerformFunction(BrightenPhotoToGiveVibrantLook, Image, 1.5)
cropped = PerformFunction(CropToHighlightMainSection, brightened, 100, 300, 200, 400)
rotated = PerformFunction(RotateToPerfection, cropped, 45)
Show(Image, "Original Image")
Show(brightened, "Brightened")
Show(cropped, "Brightened & Cropped")
Show(rotated, "Brightened, Cropped & Rotated")