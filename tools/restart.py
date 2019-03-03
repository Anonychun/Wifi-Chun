import os


os.system("sudo ifconfig mon0 down")
os.system("sudo iw mon0 del")
os.system("sudo systemctl stop network-manager")
os.system("sudo systemctl restart network-manager")
os.system("sudo systemctl start network-manager")
print("[+] Restart Network successfully\n")