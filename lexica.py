import os
import requests
import socket
import argparse

def msg_to_bytes(msg):
    return msg.encode('utf-8')

path = 'lexica_image'

# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(path)



# Callback
upd_ip = "127.0.0.1"
udp_port = 7001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-img")
# Read arguments from command line
args = parser.parse_args()

s = args.img
l = s.split()

# Message

for i in range (len(l)):
	imgReq = requests.get(l[i])
	if imgReq.status_code == 200:
		with open("lexica_image/" + str(i) + ".jpg", 'wb') as f:
			f.write(imgReq.content)
		msg = "downloading image: " + str(i+1)
		sock.sendto(msg_to_bytes(msg), (upd_ip, udp_port))

#Message
ending_msg = "all images downloaded"
sock.sendto(msg_to_bytes(ending_msg), (upd_ip, udp_port))
