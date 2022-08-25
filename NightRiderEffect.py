from machine import Pin
import utime

led1 = Pin(15, Pin.OUT)
led2 = Pin(16, Pin.OUT)
led3 = Pin(17, Pin.OUT)
led4 = Pin(18, Pin.OUT)
led5 = Pin(19, Pin.OUT)


delay = .06

while True:
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    led5.value(0)
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    led5.value(0)
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(1)
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    led5.value(0)
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    led5.value(0)
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    utime.sleep(delay)