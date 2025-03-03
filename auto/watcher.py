import subprocess
import sys
import time
import signal
import keyboard
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = self.start_script()

    def start_script(self):
        return subprocess.Popen([sys.executable,"-i", self.script])
    
    def restart_script(self):
        print(f"[auto] {self.script} changed, restarting...")
        self.process.terminate()
        self.process = self.start_script()

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            self.restart_script()

def watch(script):
    print(f"[auto] Watching {script} for changes...")
    print(f"[auto] Press ALT + Q to quit the auto....")
    event_handler = ReloadHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    signal.signal(signal.SIGINT, lambda signum, frame:print("[auto] Ignoring Keybaoard Interupt...."))

    try:
        while True:
            time.sleep(0.5)

            if keyboard.is_pressed("alt+q"):
                print(f"[auto] ALT + Q pressed.... ")
                break

    # except KeyboardInterrupt:
    #     print(f"Keyboard Interupt")
    finally:
        observer.stop()
        event_handler.process.terminate()
        print(f"[auto] Shutdown the observer and close {script} .....")
        sys.exit(0)
    observer.join() 
    

