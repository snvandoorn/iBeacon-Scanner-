# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
from datetime import datetime

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

filterbeacon = None
if __name__=="__main__":
  if (len(sys.argv) >1):
    filterbeacon = sys.argv[1]
  while True:
	returnedList = blescan.parse_events(sock, 10,filterbeacon)
	print "----------"+ str(datetime.now())
	for beacon in returnedList:
		print beacon

