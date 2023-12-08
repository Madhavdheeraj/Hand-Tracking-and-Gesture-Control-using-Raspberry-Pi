This is a project done by our group which takes the inputs of 5 flex sensors input which read through a raspberry Pi pico microcontroller and sent to laptop to perform certain keyboard emulated functions on laptop.


The components used here are:-
1. Rpi pico microcontroller.
2.ADS 1115 16-bit 4-channel PGA ADC module.
3. 5 flex sensors
4. 4 pin connector UART cable.
5. USB power cable
6.resistors
7. hand glove

Based on bending of fingers, there is an increase in the resistance of the flex sensors which is used by the pico board to send a string to laptop through uart cable.

the laptop then read the strong from its serial port and performs a certain keyboard emulated function.

The file board.py contains the code that is run on the raspberry Pi pico. 

And the file pc.py contains the code that is run on the PC 


Here is the youtube link for the project show.

https://youtu.be/o89zl6n-40Q?feature=shared