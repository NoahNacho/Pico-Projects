import utime, _thread

from lcd_api import LcdApi
from machine import I2C, Pin, ADC
from pico_i2c_lcd import I2cLcd

#"var" determines what we put on the screen
#0 = Temp
#1 = Time
var = 0
#define how long to wait
wait = 2
#defines what Temp unit to use
Temp_M = "F"
#conversion factor for temp sensor
conversion_factor = 3.3 / (65535)

#setting up CPU temp sensor stuff
sensor_temp = ADC(4)

#setting up the screen
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#setting up led and buttons
led = machine.Pin(25, machine.Pin.OUT)
btn = Pin(16, Pin.IN, Pin.PULL_DOWN)
btn_2 = Pin(17, Pin.IN, Pin.PULL_DOWN)

#preparing screen to see it is working.
lcd.clear()
lcd.move_to(2,0)
lcd.putstr("Hello World!")
utime.sleep(2)

#Functions
def CPU_TEMP(T):
  """
  Gets CPU Temp from the Pico
  Returns Temperatures in C and F
  """
    global conversion_factor
    reading = T * conversion_factor
    temperatureC = 27 - (reading - 0.706)/0.001721
    temperatureF = (temperatureC * 9/5) + 32
    return str(temperatureC), str(temperatureF)

def Blink():
  """
  Function to Blink on-board Led light
  """
    while True:
        led.toggle()
        utime.sleep(0.5)

def Temp_Unit(pin):
    """
    Changes Temp_M depending on what unit is being used
    """
    global Temp_M
    global wait
    if Temp_M == "F":
        Temp_M = "C"
        wait = 2
    else:
        Temp_M = "F"
        wait = 2

def Display_Var(pin):
    """
    Changes what displays on screen
    Using a global Variable
    0 = Display Temperature
    1 = Display Date
    """
    global var
    global wait
    if var == 0:
        var = 1
        wait = 1
    else:
        var = 0
        wait = 2
    
# Interrupt Request
btn.irq(Temp_Unit, Pin.IRQ_RISING)
btn_2.irq(Display_Var, Pin.IRQ_RISING)

#Using second core to blink the On-Board LED
_thread.start_new_thread(Blink, ( ))

#Main_Loop
while True:
    lcd.clear()
    if var == 0:
        if Temp_M == "F":
            temps = CPU_TEMP(sensor_temp.read_u16())
            lcd.putstr(temps[1])
            lcd.move_to(int(len(temps[1]))+1,0)
            lcd.putstr(Temp_M)
        else:
            lcd.putstr(temps[0])
            lcd.move_to(int(len(temps[0]))+1,0)
            lcd.putstr(Temp_M)
    elif var == 1:
        time = utime.localtime()
        hour = int(time[3])
        if hour > 12:
            hour = hour - 12
        elif hour == 0:
            hour = 12
        lcd.move_to(4,0)
        lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=hour, MM=time[4], SS=time[5]))
        lcd.move_to(3,1)
        lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d}".format(year=time[0], month=time[1], day=time[2]))
    utime.sleep(wait)




