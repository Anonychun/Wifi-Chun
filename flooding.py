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

os.system("iwconfig")
wlan = input("[+] Select an interface? : ")
os.system("clear")

print("[+] Process of creating WiFi / SSID . . .\n")

# making an adapter type monitor
os.system("sudo iw {} interface add mon0 type monitor".format(wlan))
# flooding WiFi
os.system("sudo mdk3 mon0 b -f ssid.txt")
os.system("clear")
