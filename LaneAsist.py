import os
path = os.path.dirname(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
os.chdir("{path}\app")
print(os.path.dirname(os.path.realpath(__file__)))
