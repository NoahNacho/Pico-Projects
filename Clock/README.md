# Pico-Clock
This folder is for the clock I made in micropython.
# Things I used for this project
* Raspberry Pi Pico & Power cable, with soldered pins.
* Micropython.
* Minium of a 1602A LCD screen, Although most will work with some tweaking.
* Two buttons.
* 9 Male-Male jumper wires.
* BreadBoard.
* [RPI-PICO-I2C-LCD](https://github.com/T-622/RPI-PICO-I2C-LCD)

# Wiring
I do not have a diagram for this setup yet...
So instead I will explain what needs to be done.
Here is a link to the pinout for the [RPI-PICO](https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf).

The LCD has 4 pins to be wired up. 
* GND
  * Must go to ground pin on the Pico, refer to GND labeled pins in the PDF linked above
* VCC
  * Power, Goes to VBUS pin on the Pico.
* SDA
* SCL
  * Both of these pins can go to any GPIO on the Pico

The Buttons each have 4 pins, although the ones across from each other serve the same purpose so just chose one side to connect them all to.
* One Pin needs to be connected to the 3v3(OUT) on the Pico.
* The other needs to be connected to any GPIO pin on the Pico.

# Code & Installing
Download the three .py files from [RPI-PICO-I2C-LCD](https://github.com/T-622/RPI-PICO-I2C-LCD) and save them on to your Pico.

If you do not have your screens address already download my get_lcd_address.py file and run it after you have pugged everything in. Make sure to read the file right so you can fill in the pins correctly for the variables.

Download My main.py file from this directory and save it onto your Pico.

