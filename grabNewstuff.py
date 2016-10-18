/bin/bash
import watchdog
import paramiko, base64
import os

key = paramiko.RSAKey(data=base64.decodestring('D6YV3EVlAiWZB&nm'))
client = paramiko.SSHClient()
client.get_host_keys().add('dragoncave8.ddns.net', 'ssh-rsa', key)
client.connect('dragoncave8.ddns.net',username='stpaddock', password='D6YV3EVlAiWZB&nm')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    if line == os.
