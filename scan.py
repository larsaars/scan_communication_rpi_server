"""
scan a single file as jpg on rpi server and send it after finishing via sftp to the folder pre
"""

import paramiko
import utils
import time
from PIL import Image
import os
import math

# final variables
server = 'raspberrypi'
username = 'pi'
password: str

# read password from file
with open('password.txt', 'r') as file:
    password = file.readline().strip()

# define scan command and host file
host_filename = utils.stamp() + '.jpg'
host_path = 'scan/' + host_filename
remote_path = 'pre/' + host_filename
scan_cmd = 'scanimage --format jpeg --mode col --resolution 150dpi -p > ' + host_path

print('initializing')

# setup ssh client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=username, password=password)

# and sftp client
sftp: paramiko.SFTPClient = ssh.open_sftp()

# perform scan
print('performing scan')
stdin, stdout, stderr = ssh.exec_command(scan_cmd)
# sleep
time.sleep(5)
# wait for finish
stdout.readlines()

# transfer file via sftp
print('transferring file')
with sftp.open(host_path) as host_file:
    with open(remote_path, 'wb') as remote_file:
        remote_file.write(host_file.read())

# delete at host
sftp.remove(host_path)

# close
ssh.close()
sftp.close()

# crop jpg to a4 format
print('cropping file')
image = Image.open(remote_path)
# set sides with a4 format (top 1, side sqrt 2)
a4side = image.width - 48
a4top = math.sqrt(2) * a4side
# crop with pillow
image.crop((0, 0, a4side, a4top)).save(remote_path)

# inform user
print('saved at ' + os.path.abspath(remote_path))
