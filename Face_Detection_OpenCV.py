import cv2

# Create a CascadeClassifier object and load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the default camera (camera index 0)
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()

    # Convert the frame to grayscale for face detection
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow("video_live", video_data)

    # Check for the 'a' key to exit the loop
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture object and close the OpenCV window
video_cap.release()
cv2.destroyAllWindows()
