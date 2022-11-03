import sys, os

def set() -> None:
    libdir = '\\'.join(__file__.split('\\')[:-2])
    sys.path.insert(0, os.path.abspath(libdir))