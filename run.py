#!virtual/bin/python3.6

from app import app
import signal
import sys


def sig_term_handler(signal, frame):
    print("ta for now!")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_term_handler)

app.run(debug=True, threaded=True)
