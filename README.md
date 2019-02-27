# WiFi - Chun

Library to penetration testing on WiFi. This library only tested on Linux

## Features
- Update and upgrade repository synaptic package `apt`
- Installing `MDK3` and `Aircrack-ng` from synaptic pakcage repository.
- Deauthentication / Disassociation Amok Mode.
- Kicks everybody found from `AP` (acces point)
- Beacon `Flood Mode`
- Sends beacon frames to show `fake APs` at clients.
- restart the network with systemctl.

## Installing
```bash
git clone git@github.com:Anonychun/Wifi-Chun.git
cd wifichun
make
sudo make install
```

## Uninstalling
```bash
sudo make uninstall
```

## Running
```bash
sudo wifichun
```

## Authors
* **Achmad Chun-Chun Winata Adi** - *Initial Works* - [Facebook](https://facebook.com/Anonychun) [Instagram](https://instagram.com/Anonychun) [Telegram](https://t.me/Anonychun) [GitHub](https://github.com/Anonychun)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
