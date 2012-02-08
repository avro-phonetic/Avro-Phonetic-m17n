VERSION=1.1
TEMP_DIR=./avro-phonetic-m17n-$(VERSION)
deb:
	mkdir -p $(TEMP_DIR)/usr/share/m17n/icons
	cp bn-avro-phonetic.mim $(TEMP_DIR)/usr/share/m17n
	cp bn-avro-phonetic.png $(TEMP_DIR)/usr/share/m17n/icons
	
	mkdir $(TEMP_DIR)/DEBIAN
	cp COPYRIGHT $(TEMP_DIR)/DEBIAN
	sed 's/VERSION_HERE/$(VERSION)/g' debian_control > $(TEMP_DIR)/DEBIAN/control
	dpkg-deb --build $(TEMP_DIR)
	rm -rf $(TEMP_DIR)
