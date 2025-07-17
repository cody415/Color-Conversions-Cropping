import cv2
import matplotlib.pyplot as plt 

image=cv2.imread("ant.jpg")
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()

cropped=image[100:300,200:400]
image_rgb=cv2.cvtColor(cropped,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("cropped rgb image")
plt.show()