import RPi.GPIO as GPIO
import time

# GPIO Mode (Board / BCM)
GPIO.setmode(GPIO.BCM)

# DEFINE PINS
TRIG = 23
ECHO = 24

# SETUP PINS
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def Distance():
        
        #GPIO.output(TRIG, False)
        #print("Waitin For sensor to settle")
        #time.sleep(2)
        
        # Set trig to True
        GPIO.output(TRIG, True)
        
        # Set trig after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
                pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

if __name__ == '__main':
        try:
                while True:
                        dist = Distance()
                        print("Distance: %0.1f" % dist)
                        time.sleep(0.5)
        except KeyboardInterrupt:
                print("Stopped by user")
                GPIO.cleanup()
        

