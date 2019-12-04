# auto login for putty session
import subprocess
import getpass

usr = input('usr: ')
pw = getpass.getpass(prompt='pw: ')
pid = subprocess.Popen(f"putty.exe {usr}@ibm251 -pw {pw}").pid
