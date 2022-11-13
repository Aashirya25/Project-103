import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/HP/Downloads"

class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path + "has been created")

    def on_deleted(self, event):
        print(f"Uh oh {event.src_path} has been deleted! :( ")

    def on_moved(self, event):
        print(f"Its looks like {event.src_path} has been moved!")

    def on_modified(self, event):
        print(f"Seems like {event.src_path} has been modified!")



event_handler = EventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("Program Running...")
except KeyboardInterrupt:
    print("Attention! Error occured! Observing stopped")
    observer.stop()