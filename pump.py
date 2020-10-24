import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.HIGH)

try:
        GPIO.output(7,GPIO.LOW)
        print("PUMP ON")
        time.sleep(2)
        GPIO.cleanup()
        print("PUMP OFF")

except KeyboardInterrupt:
        print("QUIT")
        GPIO.cleanup()
