#sudo nano /boot/config.txt
#dtoverlay=w1-gpio,gpiopin=4
#sudo reboot


from glob import glob

def get_values():
	result = []
	try:
		for device in glob('/sys/bus/w1/devices/28-*'):
			with open('%s/w1_slave' % device, 'r') as f:
				lines = f.read().split('\n')
				if len(lines) > 1:
					crc = lines[0].rsplit(' ', 1)
					crc = crc[1].replace('\n', '')
					if crc == 'YES':
						result.append(int(lines[1].rsplit('t=', 1)[1]))
	except:
		pass
	return result

if __name__ == '__main__':
	for value in get_values():
		print('Temperature: %.1f' % float(value/1000))
