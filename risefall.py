# import RPi.GPIO as GPIO
#
# FRONT_DOOR = 13
# BACK_DOOR = 15
#
# chan_list = [FRONT_DOOR,BACK_DOOR]
#
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(chan_list, GPIO.IN)
#
# def my_callback(channel):
#     if GPIO.input(channel):     # if port 25 == 1
#         print "Rising edge detected on {}".format(channel)
#     else:                  # if port 25 != 1
#         print "Falling edge detected on {}".format(channel)
#
# # when a changing edge is detected on port 25, regardless of whatever
# # else is happening in the program, the function my_callback will be run
# GPIO.add_event_detect(FRONT_DOOR, GPIO.BOTH, callback=my_callback)
# GPIO.add_event_detect(BACK_DOOR, GPIO.BOTH, callback=my_callback)


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
        for channel in chan_list:
            if GPIO.event_detected(channel):
                if GPIO.input(channel):
                    print "{} closed".format(channel)
                else:
                    print "{} opened".format(channel)

    except KeyboardInterrupt:
        stored_exception=sys.exc_info()

if stored_exception:
    print("Forcably Closing App! Cleaning up...")

GPIO.cleanup()

print("Cleaning completed.")
exit(1)
