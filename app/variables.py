#DISCLAIMER This is not my file, the file was orginally from Tumppi066's ETS2 Lane Assist
#All credits to Tumppi066
#Small edits were made to account for my lack of software

'''
Stores all main variables for the program.
'''
import os


PATH = os.path.dirname(__file__).replace("src", "")
ENABLELOOP = False
UPDATEPLUGINS = False
RELOAD = False

def ToggleEnable():
    global ENABLELOOP
    ENABLELOOP = not ENABLELOOP

def UpdatePlugins():
    global UPDATEPLUGINS
    UPDATEPLUGINS = True