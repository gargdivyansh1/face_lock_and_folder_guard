import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

import cv2
import time
import platform
import ctypes
from face_verification.verify_face import verify_face

def lock_system():
    os_type = platform.system()
    if os_type == "Windows":
        ctypes.windll.user32.LockWorkStation()
    elif os_type == "Linux":
        os.system("gnome-screensaver-command --lock")
    elif os_type == "Darwin":
        os.system("osascript -e 'tell application \"System Events\" to start current screen saver'")

def run_face_lock():
    print("[SYSTEM] Face lock started. Will verify every 5 seconds.")

    while True:
        print("[INFO] Verifying face...")

        capture = cv2.VideoCapture(0)
        if not capture.isOpened():
            print("[ERROR] Could not open webcam.")
            time.sleep(5)
            continue

        result = verify_face(capture)
        capture.release()  
        cv2.destroyAllWindows()

        if not result:
            print("[ALERT] Unauthorized face detected! Locking system...")
            lock_system()
            time.sleep(10)  
        else:
            print("[INFO] Authorized user.")

        time.sleep(5)  

if __name__ == '__main__':
    run_face_lock()
