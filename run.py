from paktmonitor import paktmonitor

import sys

if __name__ == "__main__":
    try:
        paktmonitor.run("127.0.0.1", sys.argv[1])
    except IndexError: # there should be a neater way to do this
        paktmonitor.run("127.0.0.1", 5000)
    
