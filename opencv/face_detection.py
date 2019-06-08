import cv2

'''
Uses Canny edge detection to find the edges of various objects
'''

path = 'the_gang.jpg' # Path to the desired image
title = 'The Gang' # Title of the image
cascPath = 'haarcascade_frontalface_default.xml' # Path to cascade algorithm for detection

# Initialize Haar cascade algorithm
face_cascade = cv2.CascadeClassifier(cascPath)

# Read the image
img = cv2.imread(path) # Load the desired image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert image to grayscale for easier detection

# # Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray, # Pass image
    scaleFactor = 1.2, # Compensates for face sizes
    minNeighbors = 5, # How many objects are detected before considered found
    minSize = (150,150) # Minimum size of each window
)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 10)

# Show the detected faces
cv2.namedWindow(title, cv2.WINDOW_NORMAL) # Create a named window
cv2.resizeWindow(title, 600, 800) # Size the window to 600x800
cv2.imshow(title, img) # Fit the image to the window
cv2.waitKey(0) # Wait for a key press before closing the image
