from machine import Pin, I2C
#Setting Variables
sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, sda=sda, scl=scl, freq=400000)
#i2c.scan gets the address in decimal
#hex converts it to hex for the script to use
print(hex(i2c.scan()[0]))
