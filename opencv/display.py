import cv2

'''
Loads an image and shows it in full color, grayscale, and blurred grayscale
'''

path = 'the_gang.jpg' # Path to the desired image
title = 'The Gang' # Title of the image

# Load and show an image
img = cv2.imread(path) # Read the jpg file
cv2.namedWindow(title, cv2.WINDOW_NORMAL) # Create a named window
cv2.resizeWindow(title, 600, 800) # Size the window to 600x800
cv2.imshow(title, img) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image

# Show the same image in grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow(title, img) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image

# Show a gaussian blur of the image
img = cv2.GaussianBlur(img, (5,5), 0) # Gaussian blur of 5x5 (LxW) pixels
cv2.imshow(title, img) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image
