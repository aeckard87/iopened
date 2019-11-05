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


#HANDLE EVENT
def my_callback(channel):
    if GPIO.input(channel):
        print "{} opened!".format(locations.get(channel, "none"))
    else:
        print "{} closed!".format(locations.get(channel, "none"))
        
# INIT VALUES
chan_list = []
locations = {
		13 : "Front Door",
		15 : "Back Door"
	}

for key, value in locations.items():
    chan_list.append(key)


#SETUP GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(chan_list, GPIO.IN)

for key, value in locations.items():
    GPIO.add_event_detect(key, GPIO.BOTH, callback=my_callback)


#KEEP ON RUNNING!
while True:
    try:
        pass

    except KeyboardInterrupt:
        stored_exception=sys.exc_info()
#EXIT
if stored_exception:
    print("Forcably Closing App! Cleaning up...")

GPIO.cleanup()

print("Cleaning completed.")
exit(1)
