import os, sys

if len(sys.argv) != 3:
	sys.exit('Usage: sudo python flashburner.py <iso> <device>')

isofile = sys.argv[1]
device = sys.argv[2]
tempiso = "fburn-temp.iso"

if not os.path.exists(isofile):
	sys.exit('ERROR: ISO file %s was not found!' % isofile)

if not os.path.exists(device):
	sys.exit('ERROR: Device on %s was not found!' % device)

print 'Installing additional packages...'
print

os.system('sudo apt-get install pv')
os.system('clear')

print
print 'Flashburner for GNU/Linux (version 1.0)'
print 'Developed and tested by 0x00101'
print

list = os.popen('sudo fdisk -l %s' % device)
print list.read()
print

correctdevice = raw_input("This is correct flash drive? [y/n]: ")
if correctdevice != 'y':
	sys.exit('Yep? Okay..')

print('Unmounting device %s..' % device)
os.system('sudo umount -f %s' % device)

copyiso = raw_input("Copy ISO before burning? (recommended but it's maybe very long) [y/n]: ")
if copyiso != 'y':
	print('Copying %s to %s' % (isofile, tempiso))
	os.system('pv %s > %s' % (isofile, tempiso))

hybridd = raw_input("Convert ISO file to hybrid? (not-recommended) [y/n]: ")
if hybridd != 'n':
	print('Trying to hybrid %s..' % isofile)
	os.system("isohybrid %s" % isofile)
print

continueburn = raw_input("You really wanna continue and burn your flash drive? (WARNING: It's full reformating! ALL DATA WILL BE LOST!) [y/n]: ")
if continueburn != 'y':
	print('Mounting back %s on /mnt/flash/' % device)
	os.system('sudo mkdir /mnt/flash')
	os.system("sudo mount -o rw,force %s /mnt/flash" % device)
	sys.exit('Terminating...')

print('Burning on %s..' % device)
os.system("sudo dd if=%s of=%s status=progress" % (isofile, device))

msboot = raw_input("Would you like install MS MBR boot record? (ms-sys package needed) [y/n]: ")

if msboot != 'n':
	print('Trying to setup Microsoft MBR bootsector in %s' % device)
	os.system('ms-sys -w %s' % device)

print 'Done!'
sys.exit()

#os.system("sudo dd if=")
#os.system('hdiutil convert -format UDRW -o bootable.img %s' % sys.argv[1])
#os.system('mv bootable.img.dmg bootable.img')
#os.system('sudo diskutil unmount /dev/%s' % diskid)
#print 'It is not stuck, just wait until it finishes.'
#print 'Creating bootable usb...'
#os.system('sudo dd bs=1m if=bootable.img of=/dev/r%s' % diskid)
#os.system('rm -f bootable.img')
#print 'Done!'
