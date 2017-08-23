# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/E2m3u2bouquet/log.py
import sys
from cStringIO import StringIO
import threading
logfile = StringIO()
mutex = threading.Lock()

def write(data):
    mutex.acquire()
    try:
        if logfile.tell() > 2000:
            logfile.reset()
        logfile.write(data)
    finally:
        mutex.release()

    sys.stdout.write(data)


def getvalue():
    mutex.acquire()
    try:
        pos = logfile.tell()
        head = logfile.read()
        logfile.reset()
        tail = logfile.read(pos)
    finally:
        mutex.release()

    return head + tail