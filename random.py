import os
import sys
import platform
import subprocess

# Author: Chad O'Donnell
# Purpose: To detect OS type from any remote device.
# IMPORTANT: Look at 'portscanner.py' for working portscanner!

# This is an example of calling the OS data straight from the terminal of a local computer
print(os.name)
print(sys.platform)
print(platform.platform())
print(platform.system())

# Testing an online example from GeeksforGeeks to see if it would actually work. It does not.
# I'm keeping it here to figure out why and try fixing it. 
# Look at my 'portscanner.py' file for a working port scanner in Python 3.

import socket 
from datetime import datetime 

# Defining a targetIP in the form of array command line arguments.
if len(sys.argv) == 2: 
	
	# Translating hostname into targetIPV4 or targetIPV6, e.g. socket.gethostbyname;
	targetIP = (socket.getaddrinfo(sys.argv[1])) 
else: 
	print("Invalid ammount of Argument") 

# Graphical representation banner for user.
print("-" * 50) 
print("Scanning targetIP: " + targetIP) 
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 

try: 
	
	# Scans ports between 1 and 65,535. 
	for port in range(1,65535): 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		socket.setdefaulttimeout(1) 
		
		# returns an error indicator 
		result = s.connect_ex((targetIP,port)) 
		# If port is open (0), then print out open port.
		if result ==0: 
			print("Port {} is open".format(port)) 
		s.close() 
		
except KeyboardInterrupt: 
		print("\n Exitting Program !!!!") 
		sys.exit() 
except socket.gaierror: 
		print("\n Hostname Could Not Be Resolved !!!!") 
		sys.exit() 
except socket.error: 
		print("\ Server not responding !!!!") 
		sys.exit() 
