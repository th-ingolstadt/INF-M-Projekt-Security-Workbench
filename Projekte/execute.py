import subprocess
import sys
import os

i=2
command=str(sys.argv[1])
while (i<len(sys.argv)):
	command = command + " " + str(sys.argv[i])
	i+=1

os.system(command)
response = raw_input("Press enter to close window: ")

