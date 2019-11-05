import RPi.GPIO as GPIO

FRONT_DOOR = 13
BACK_DOOR = 15

chan_list = [FRONT_DOOR,BACK_DOOR]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(chan_list, GPIO.IN)

#print(GPIO.input(FRONT_DOOR))
GPIO.add_event_detect(FRONT_DOOR, GPIO.FALLING)  # add rising edge detection on a channel
GPIO.add_event_detect(BACK_DOOR, GPIO.FALLING)  # add rising edge detection on a channel
while True:
    try:
        if GPIO.event_detected(FRONT_DOOR):
            print('Front Door Opened!')

        if GPIO.event_detected(BACK_DOOR):
            print('Back Door Opened!')
    except KeyboardInterrupt:
        stored_exception=sys.exc_info()

if stored_exception:
    print("Forcably Closing App! Cleaning up...")

GPIO.cleanup()

print("Cleaning completed.")
exit(1)
