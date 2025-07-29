import subprocess
import threading
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run_face_lock():
    subprocess.run(["python", "system_lock/background_face_lock.py"])

def run_secure_access():
    subprocess.run(["python", "secure_folder/secure_access.py"])

if __name__ == "__main__":
    t1 = threading.Thread(target=run_face_lock)
    t1.start()

    while True:
        cmd = input("\nType 'unlock' to open secure folder or 'exit' to quit:\n> ")
        if cmd.lower() == "unlock":
        elif cmd.lower() == "exit": #type: ignore
            break
