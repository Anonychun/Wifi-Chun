CC=g++

wifichun: wifichun.o
	$(CC) -o wifichun wifichun.o

install:
	# membuat direktori app di opt
	mkdir /opt/wifichun
	# mengcopy file ke direktori
	cp wifichun /opt/wifichun
	cp disconnect.py /opt/wifichun
	cp flooding.py /opt/wifichun
	cp restart.py /opt/wifichun
	cp ssid.txt /opt/wifichun
	cp whitelist.txt /opt/wifichun
	# memberikan akses app
	chmod +x wifichun
	# membuat konfigurasi file ke bin/bash
	echo "#!/bin/bash" >> /usr/bin/wifichun
	echo "cd /opt/wifichun/" >> /usr/bin/wifichun
	echo "./wifichun" >> /usr/bin/wifichun
	# memberikan akses app
	chmod +x /usr/bin/wifichun
	clear

uninstall:
	# menghapus file di direktori
	rm /opt/wifichun/wifichun
	rm /opt/wifichun/disconnect.py
	rm /opt/wifichun/flooding.py
	rm /opt/wifichun/restart.py
	rm /opt/wifichun/ssid.txt
	rm /opt/wifichun/whitelist.txt
	# menghapus folder direktori
	rmdir /opt/wifichun
	# menghapus konfigurasi file bin/bash
	rm /usr/bin/wifichun
	clear