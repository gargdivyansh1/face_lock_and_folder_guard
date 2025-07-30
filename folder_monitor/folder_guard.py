import os
import time
import subprocess
import ctypes
import cv2
from face_verification.verify_face import verify_face

# for showing the working of the model .. 
# we could also select multiple paths and could implement a frontend which could give us the choice for selecting the paths of the folders and files 
GUARDED_FOLDER = r'C:\Users\divya\SecretFiles'
CHECK_INTERVAL = 0.2 

def get_active_window_title():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    length = user32.GetWindowTextLengthW(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, buff, length + 1)
    return buff.value

def is_folder_open():
    active_window = get_active_window_title()
    return os.path.basename(GUARDED_FOLDER).lower() in active_window.lower()

def start_monitoring():
    print(f"[MONITORING] Guarding folder: {GUARDED_FOLDER}")
    folder_checked = False

    while True:
        if is_folder_open():
            if not folder_checked:
                print("[DETECTED] Folder is being accessed. Verifying user...")

                capture = cv2.VideoCapture(0)
                verified = verify_face(capture)
                capture.release()  

                if not verified:
                    print("[ALERT] Unauthorized! Closing folder window...")
                    subprocess.call('taskkill /f /im explorer.exe', shell=True)
                    time.sleep(2)
                    subprocess.Popen('explorer')
                else:
                    print("[ACCESS GRANTED] Facial verification successful.")

                folder_checked = True  
        else:
            folder_checked = False 

        time.sleep(CHECK_INTERVAL)
