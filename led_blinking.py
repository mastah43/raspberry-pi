import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

led_red_pin = 11
led_blue_pin = 12
led_green_pin = 13

GPIO.setup(led_red_pin, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial
GPIO.setup(led_blue_pin, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial
GPIO.setup(led_green_pin, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial


def red_on():
    GPIO.output(led_red_pin, GPIO.HIGH)


def red_off():
    GPIO.output(led_red_pin, GPIO.LOW)


def green_on():
    GPIO.output(led_green_pin, GPIO.HIGH)


def green_off():
    GPIO.output(led_green_pin, GPIO.LOW)


def blue_on():
    GPIO.output(led_blue_pin, GPIO.HIGH)


def blue_off():
    GPIO.output(led_blue_pin, GPIO.LOW)


def loop_linear():
    sleep_time = 0.5
    while True:
        GPIO.output(led_blue_pin, GPIO.HIGH)
        sleep(sleep_time)

        GPIO.output(led_blue_pin, GPIO.LOW)
        GPIO.output(led_red_pin, GPIO.HIGH)
        sleep(sleep_time)

        GPIO.output(led_red_pin, GPIO.LOW)
        GPIO.output(led_green_pin, GPIO.HIGH)
        sleep(sleep_time)

        GPIO.output(led_green_pin, GPIO.LOW)


def loop_super_flash():
    sleep_time = 0.15
    while True:
        blue_on()
        red_off()
        green_off()
        sleep(sleep_time)

        blue_off()
        red_on()
        green_off()
        sleep(sleep_time)

        blue_off()
        red_off()
        green_on()
        sleep(sleep_time)

        blue_off()
        red_on()
        green_off()
        sleep(sleep_time)


def destroy():
    GPIO.cleanup()


try:
    loop_super_flash()
except KeyboardInterrupt:
    destroy()
