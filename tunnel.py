# auto login for putty session
import subprocess
import getpass

host = input('host: ')
usr = input('usr: ')
pw = getpass.getpass(prompt='pw: ')
pid = subprocess.Popen(f"putty.exe {usr}@{host} -pw {pw}").pid
