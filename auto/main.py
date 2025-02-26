import sys
from .watcher import watch

def main():
    if len(sys.argv) < 2 :
        print("Usage : autoreload <script.py>")
        sys.exit(1)

    script = sys.argv[1]
    watch(script)

