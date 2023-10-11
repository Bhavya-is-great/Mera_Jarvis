# Importing the required module
# Find more projects at codewithcurious.com
import pywhatkit as kit
import cv2

# Converting text into handwritting image
kit.text_to_handwriting("Hey theere! curious programmer here.", save_to="others\\writing.jpg")

# Saving the Generated Image
img = cv2.imread("others\\writing.jpg")

# Showing the Generated image
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()