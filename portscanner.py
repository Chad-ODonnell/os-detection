import socket
import subprocess
import sys
from datetime import datetime

# Credit for this file goes towards: Python for Beginners,
# I couldn't have done it without them helping me out.
# This helps us infer which OS the user has, comparing ports to listed chart below.

# Clear the screen
subprocess.call('clear', shell=True)

# Asking for input
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Graphic representing where scan will take place
print ("-" * 60)
print ("Please wait, scanning remote host (this may take awhile)", remoteServerIP)
print ("-" * 60)

# Check what time the scan started, used for finding scan time-stamps
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 65535)
# TCP WINDOW SIZE CHART ->
# LINUX:            5840
# GOOGLE'S lINUX:   5720
# FreeBSD:          65535
# WINDOWS XP/10:    65535
# WINDWOS 7/2008:   8192
# Depending on open ports, you can infer OS.

# We also put in some error handling for catching errors
try:
    for port in range(1,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        # If port isn't used, share that port is open
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()

# Just in case this doesn't go as expected
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)
