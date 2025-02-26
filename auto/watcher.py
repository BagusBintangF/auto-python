import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = self.start_script()

    def start_script(self):
        return subprocess.Popen([sys.executable, self.script])
    
    def restart_script(self):
        print(f"[auto]{self.script} changed, restarting...")
        self.process.terminate()
        self.process = self.start_script()

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            self.restart_script()

def watch(script):
    print(f"[auto] watching {script} for changes...")
    event_handler = ReloadHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        event_handler.process.terminate()
    observer.join() 
    

