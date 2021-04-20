import subprocess

cmd_line = "sudo ssh -R 0:localhost:3389 serveo.net"
p = subprocess.Popen(cmd_line, shell=True)
out = p.communicate()[0]
print(out)
