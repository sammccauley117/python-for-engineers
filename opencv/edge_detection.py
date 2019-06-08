import cv2

'''
Uses Canny edge detection to find the edges of various objects
'''

path = 'objects.jpg' # Path to the desired image
title = 'Objects' # Title of the image

# Load and show an image
img = cv2.imread(path) # Read the jpg file
cv2.namedWindow(title, cv2.WINDOW_NORMAL) # Create a named window
cv2.imshow(title, img) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image

# Show the Canny edge detection
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert image to grayscale
cv2.imshow(title, img) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image
img = cv2.GaussianBlur(img, (7,7), 0) # Blur the image (gray+blur makes edge detection easier)
cv2.imshow(title, img) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image
canny = cv2.Canny(img, 50, 150) # Compute the Canny edge detection with pixel threshold (50-150)
cv2.imshow(title, canny) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image
