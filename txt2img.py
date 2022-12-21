import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import argparse
import socket
import os
import time

def msg_to_bytes(msg):
    return msg.encode('utf-8')

path = 'sd_images'

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
parser.add_argument("-prompt")
parser.add_argument("-cfg")
parser.add_argument("-steps")
parser.add_argument("-width")
parser.add_argument("-height")
parser.add_argument("-seed")
parser.add_argument("-negative")

# Read arguments from command line
args = parser.parse_args()

# Generate
try:
	url = "http://127.0.0.1:7860"
	checkAPI = requests.get('http://127.0.0.1:7860/sdapi/v1/hypernetworks')
	if checkAPI.status_code == 200:
		payload = {
			"prompt": args.prompt,
			"cfg_scale": args.cfg,
			"steps": args.steps,
			"negative_prompt": args.negative,
			"width": args.width,
			"height": args.height,
			"seed": args.seed
		}

		payload_json = json.dumps(payload)
		response = requests.post(url=f'{url}/sdapi/v1/txt2img', data=payload_json).json()

		for i in response['images']:
			image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
			pnginfo = PngImagePlugin.PngInfo()
			pnginfo.add_text("parameters", str(response['info']))
			image.save('sd_images/' + str(int(time.time())) + '.png', pnginfo=pnginfo)
			ending_msg = "image ready"
			sock.sendto(msg_to_bytes(ending_msg), (upd_ip, udp_port))
	else:
		ending_msg = "API not running"
		sock.sendto(msg_to_bytes(ending_msg), (upd_ip, udp_port))

except:
	ending_msg = "error on opening API"
	sock.sendto(msg_to_bytes(ending_msg), (upd_ip, udp_port))
