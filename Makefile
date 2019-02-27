CC=g++

wifichun: wifichun.o
	$(CC) -o wifichun wifichun.o

install:
	# make the app directory on opt
	mkdir /opt/wifichun
	# copy files to directory
	cp wifichun /opt/wifichun
	cp disconnect.py /opt/wifichun
	cp flooding.py /opt/wifichun
	cp restart.py /opt/wifichun
	cp ssid.txt /opt/wifichun
	cp whitelist.txt /opt/wifichun
	cp logo.txt /opt/wifichun
	# provide app access
	chmod +x wifichun
	# configure the files to bin/bash
	echo "#!/bin/bash" >> /usr/bin/wifichun
	echo "cd /opt/wifichun/" >> /usr/bin/wifichun
	echo "./wifichun" >> /usr/bin/wifichun
	# provide app access
	chmod +x /usr/bin/wifichun
	clear

uninstall:
	# remove files in directory
	rm /opt/wifichun/wifichun
	rm /opt/wifichun/disconnect.py
	rm /opt/wifichun/flooding.py
	rm /opt/wifichun/restart.py
	rm /opt/wifichun/ssid.txt
	rm /opt/wifichun/whitelist.txt
	rm /opt/wifichun/logo.txt
	# remove directory
	rmdir /opt/wifichun
	# remove configure on bin/bash
	rm /usr/bin/wifichun
	clear
