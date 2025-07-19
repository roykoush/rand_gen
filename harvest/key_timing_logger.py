from pynput import keyboard
import time
import threading
import os

log_file = "key_timings.log"
last_time = None
lock = threading.Lock()


with open(log_file, "a") as f:
    pass

def on_press(key):
    global last_time
    now = time.time()
    with lock:
        if last_time is not None:
            dt = now - last_time
            with open(log_file, "a") as f:
                f.write(f"{dt:.6f}\n")
        last_time = now

print("Logger started.")
print(f"Logging to: {log_file}")
print(f"Current size: {os.path.getsize(log_file) / 1024:.2f} KB")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
er.join()
