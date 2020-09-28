import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

led_red_pin = 11
led_blue_pin = 12

GPIO.setup(led_red_pin, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial
GPIO.setup(led_blue_pin, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial

def loop():
    sleep_time = 0.2
    while True: # Run forever
        GPIO.output(led_red_pin, GPIO.HIGH)
        GPIO.output(led_blue_pin, GPIO.LOW)
        print("red  on, blue off")
        sleep(sleep_time)
        GPIO.output(led_red_pin, GPIO.LOW)
        GPIO.output(led_blue_pin, GPIO.HIGH)
        print("red  off, blue on")
        sleep(sleep_time)


def destroy():
    GPIO.cleanup()


try:
    loop()
except KeyboardInterrupt:
    destroy()
