import paramiko

# final variables
server = 'raspberrypi'
username = 'pi'
password = '27052002'

# define scan command
scan_cmd = 'scanimage --format jpeg --mode col --resolution 150dpi -p > scan/' +

# setup ssh client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=username, password=password)

# and sftp client
# transport = paramiko.Transport((hostname, Port))
# transport.connect(
#     hostkey,
#     username,
#     password,
#     gss_host=socket.getfqdn(hostname),
#     gss_auth=UseGSSAPI,
#     gss_kex=DoGSSAPIKeyExchange,
# )
# sftp = paramiko.SFTPClient.from_transport(transport)

# perform scan
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(scan_cmd)


# close
ssh.close()
# sftp.close()