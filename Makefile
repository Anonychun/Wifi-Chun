CC=g++

wifichun: wifichun.o
	$(CC) -o wifichun wifichun.o

install:
	# make the app directory on opt
	mkdir /opt/wifichun
	# copy files to directory
	cp -rf files /opt/wifichun
	cp -rf tools /opt/wifichun
	cp wifichun /opt/wifichun
	# configure the files to bin/bash
	echo "#!/bin/bash" >> /usr/bin/wifichun
	echo "cd /opt/wifichun/" >> /usr/bin/wifichun
	echo "./wifichun" >> /usr/bin/wifichun
	# provide app access
	chmod +x /usr/bin/wifichun
	clear

uninstall:
	# remove files in directory
	rm -rf /opt/wifichun/files
	rm -rf /opt/wifichun/tools
	rm /opt/wifichun/wifichun
	# remove directory
	rmdir /opt/wifichun
	# remove configure on bin/bash
	rm /usr/bin/wifichun
	clear