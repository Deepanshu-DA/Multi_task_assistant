import cv2
from services.speech import speak

class CameraService:
    def take_picture(self):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            filename = "camera_capture.jpg"
            cv2.imwrite(filename, frame)
            speak("Picture taken and saved.")
        else:
            speak("Failed to take picture.")
        cam.release()
        cv2.destroyAllWindows()
