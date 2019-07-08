import os, sys

if len(sys.argv) != 3:
	sys.exit('Usage: sudo %s iso-file burn-device' % sys.argv[0])

isofile = sys.argv[1]
device = sys.argv[2]

if not os.path.exists(isofile):
	sys.exit('ERROR: ISO file %s was not found!' % isofile)

if not os.path.exists(device):
	sys.exit('ERROR: Device on %s was not found!' % device)

print 'Starting ISO Flashburner...'
print ''

f = os.popen('sudo fdisk -l %s' % device)
print f.read()

thisdriveornot = raw_input("This is really your burning drive? [y/n]: ")

if thisdriveornot != 'y':
	sys.exit('Okay. Terminating flashburner..')

hybridornot = raw_input("Convert ISO file to hybrid? (Try if simple burn don't working) [y/n]: ")

if hybridornot != 'n':
	copyornot = raw_input("Copy ISO before converting? (recommended but it's maybe very long) [y/n]: ")
	if copyornot != 'n':
		# also code..

if hybridornot != 'y':
	print('Unmounting device %s..' % device)
	os.system('sudo umount -f %s' % device)

	print ''
	wannacnt = raw_input("You really wanna continue and burn your flash drive? (WARNING: It's full reformating! Backup your data immediately!) [y/n]: ")	
	
	if wannacnt != 'y':
		print('Mounting back %s on /mnt/flash/' % device)
		os.system("sudo mount -o rw,force %s /mnt/flash" % device)
		sys.exit('Terminating...')

	print('Burning on %s..' % device)
	os.system("sudo dd if=%s of=%s status=progress" % (isofile, device))

print 'Done!'

sys.exit()

os.system("sudo dd if=")


os.system('hdiutil convert -format UDRW -o bootable.img %s' % sys.argv[1])
os.system('mv bootable.img.dmg bootable.img')

os.system('sudo diskutil unmount /dev/%s' % diskid)
print 'It is not stuck, just wait until it finishes.'
print 'Creating bootable usb...'
os.system('sudo dd bs=1m if=bootable.img of=/dev/r%s' % diskid)
os.system('rm -f bootable.img')

print 'Done!'
