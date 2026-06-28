import cv2

# Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)
print(cap.isOpened())

colormap = None

filters = {
    '0': None,
    '1': cv2.COLORMAP_AUTUMN,
    '2': cv2.COLORMAP_BONE,
    '3': cv2.COLORMAP_JET,
    '4': cv2.COLORMAP_WINTER,
    '5': cv2.COLORMAP_RAINBOW,
    '6': cv2.COLORMAP_OCEAN,
    '7': cv2.COLORMAP_SUMMER,
    '8': cv2.COLORMAP_PINK,
    '9': cv2.COLORMAP_HOT
}

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not accessible")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )

    # face detection
    for (x,y,w,h) in faces:

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            "Face Detected",
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )


    # Instructions
    cv2.putText(
        frame,
        "Press 0-9 to Change Filters",
        (20,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        "Press Q to Quit",
        (20,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )


    # Apply filter
    if colormap is None:
        display_frame = frame
    else:
        display_frame = cv2.applyColorMap(frame, colormap)


    # Face count
    cv2.putText(
        display_frame,
        "Faces: "+str(len(faces)),
        (20,100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,0,0),
        2
    )


    cv2.imshow("Selfie Camera", display_frame)


    key = cv2.waitKey(1) & 0xFF


    if key == ord('q'):
        break


    elif chr(key) in filters:
        colormap = filters[chr(key)]


    elif key == ord('s'):
        cv2.imwrite("myimage.png", display_frame)


cap.release()
cv2.destroyAllWindows()