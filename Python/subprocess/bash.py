import subprocess
script = 'sudo apt-get install idle'
action = subprocess.Popen(script, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=None, executable="/bin/sh").stdout.read()
print action
