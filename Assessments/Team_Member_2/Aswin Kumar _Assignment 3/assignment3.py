from gpiozero import LED
import time


#For raspberry pi 
red = LED(5)
yellow = LED(6)
green = LED(13)



while True:
    
    green.off()    #Execute in raspberry pi
    red.on()       #Execute in raspberry pi

    print("\033[91m Red light! GET ")
    time.sleep(3)
    print("\033[37m Blink!")
    time.sleep(1)

    red.off()     #Execute in raspberry pi
    yellow.on()   #Execute in raspberry pi
    
    print("\033[93m Yellow light! SET ")
    time.sleep(2)
    print("\033[37m Blink!")
    time.sleep(1)

    yellow.off()   #Execute in raspberry pi
    green.off()    #Execute in raspberry pi
    
    print("\033[92m Green light! GO")
    time.sleep(3)
    print("\033[37m Blink!")
    time.sleep(1)
