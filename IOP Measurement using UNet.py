!pip install tensorflow opencv-python scikit-learn matplotlib

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

def calculate_applanation_area(image):
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)
            return area
        return None

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image_path = "/content/cornea.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 2)


contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contour = max(contours, key=cv2.contourArea)

area_pixels = cv2.contourArea(largest_contour)

pixel_to_mm2_conversion = 0.2646
area_mm2 = area_pixels * pixel_to_mm2_conversion

force_N = 40
pressure_Pa = force_N / (area_mm2 + 1e-6)
pressure_mmHg = pressure_Pa * 7500.6168

processed_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(processed_image, [largest_contour], -1, (0, 255, 0), 2)

cv2_imshow(processed_image)

print(f"Force: {force_N} N")
print(f"Applanation Area: {area_mm2:.2f} mm²")
print(f"Intraocular Pressure: {pressure_mmHg:.2f} mmHg")
