import subprocess
import threading
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run_face_lock():
    subprocess.run(["python", "system_lock/background_face_lock.py"])

if __name__ == "__main__":
    t1 = threading.Thread(target=run_face_lock)
    t1.start()