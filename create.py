"""
This file creates the update.py and run.py files
It is ran by the installer and does not need to be ran manually 
Credits for this code: Dylanb92010
"""

import os
import time

FOLDER = os.path.dirname(__file__)
PATHADD = FOLDER.__add__(r"\ETS2-ATS-Lane-Assist-Mockup")
os.chdir(PATHADD)

print("Creating update.py...")
with open("update.py", "w") as upd:
    time.sleep(2)
    upd.write('import os\n')
    upd.write('FOLDER = os.path.dirname(__file__)\n')
    upd.write('os.chdir(FOLDER)\n')
    upd.write('if os.path.exists("app"):\n')
    upd.write('  print("Please delete the app folder before updating")\n')
    upd.write('  print("Press enter to exit...")\n')
    upd.write('  input()\n')
    upd.write('  quit()\n')
    upd.write('os.system("git clone https://github.com/dylanb92010/ETS2-ATS-Lane-Assist-Mockup")\n')
    upd.write('print("Program has been updated")\n')
    upd.write('print("Press enter to exit...")\n')
    upd.write('input()\n')
    upd.write('quit()\n')
    upd.close()

print("Creating run.py...")
with open("run.py", "w") as run:
    time.sleep(2)
    run.write('import os \n')
    run.write('PATH = (os.path.dirname(__file__))\n')
    run.write('PATHADD = PATH.__add__(r"\app")\n')
    run.write('os.chdir(PATHADD)\n')
    run.write('os.startfile("lane_assist.py") \n')
    run.write('exit()\n')
    run.close()

print("Update.py and Run.py succsessfully created")
print("App has been downloaded")
print("Use run.py to open the Lane Assist app")
print("Use update.py to update the app when a new release is out")
print("Press Enter to exit...")
input()
quit()