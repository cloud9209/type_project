import os, sys
sys.path.insert(0, "C:\\Program Files (x86)\\Google\\google_appengine")
from application import manager

manager.run()

""" Recover Path """
sys.path.pop(0)