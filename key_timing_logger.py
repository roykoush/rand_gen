from pynput import keyboard
import time
import threading
import os



l_f = "key_timings.log"
l_t = None
lock = threading.Lock()

def on_press(key):
    global l_t
    now = time.time()
    with lock:
        if l_t is not None:
            d = now - l_t
            with open(l_f, "a") as f:
                f.write(f"{d:.6f}\n")
        l_t = now

with keyboard.Listener(on_press=on_press) as listener:
    print("ok.")
    print(f"Log size: {os.path.getsize('key_timings.log') / 1024:.2f} KB")
    listener.join()
