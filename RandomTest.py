from Board import *

import json

import subprocess

theBoard = Board()

command = ["py", "python_arcade_test_file.py"]

subprocess.run(command)

choice = input("Command me")

while choice != "quit":
    subprocess.run(command)

    choice = input("Command me")

