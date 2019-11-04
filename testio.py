import RPi.GPIO as GPIO

pins = [13,15]

print 'RASPBERRY INFO:'
for key, value in GPIO.RPI_INFO.iteritems():
    print '\t{}: {}'.format(key,value)

print 'RPi.GIPO INFO:'

print '\tVersion: {}'.format(GPIO.VERSION)

mode = GPIO.getmode()
if mode == None:
    GPIO.setmode(GPIO.BOARD)
    mode = GPIO.getmode()

print '\tMODE: {}'.format(mode)

GPIO.setup(pins, GPIO.IN)

print 'PINS'
for pin in pins:
    print '\t{}: {}'.format(pin, GPIO.gpio_function(pin))

GPIO.cleanup(pins)
