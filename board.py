import utime
from machine import I2C, Pin, ADC, UART

i2c = I2C(1, scl=Pin(15), sda=Pin(14))
adc = ADC(Pin(26))
uart = UART(0, baudrate=9600, tx=0, rx=1)

address = 72


def readConfig():
    i2c.writeto(address, bytearray([1]))
    result = i2c.readfrom(address, 2)
    return result[0] << 8 | result[0]


def readValueFromChannel(channel):
    config = readConfig()
    config &= ~(7 << 12)
    config &= ~(7 << 9)
    config |= (7 & (4 + channel)) << 12
    config |= (1 << 15)
    config |= (1 << 9)
    config = [int(config >> i & 0xff) for i in [8, 0]]
    i2c.writeto(address, bytearray([1] + config))
    config = readConfig()
    while config & 0x8000 == 0:
        config = readConfig()
    i2c.writeto(address, bytearray([0]))
    result = i2c.readfrom(address, 2)
    return result[0] << 8 | result[0]


val = [0, 0, 0, 0, 0]

while True:
    val[0] = readValueFromChannel(0)
    val[1] = readValueFromChannel(1)
    val[2] = readValueFromChannel(2)
    val[3] = readValueFromChannel(3)
    val[4] = adc.read_u16()
    print(val)
    if val[0] > 16000 and val[1] < 16000 and val[2] < 16000 and val[3] < 16000 and val[4] < 55000:
        uart.write("left" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] < 16000 and val[3] < 16000 and val[4] < 55000:
        uart.write("down" + "\n")
    elif val[0] < 16000 and val[1] < 16000 and val[2] > 16000 and val[3] < 16000 and val[4] < 55000:
        uart.write("Windows" + "\n")
    elif val[0] < 16000 and val[1] < 16000 and val[2] < 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("up" + "\n")
    elif val[0] < 16000 and val[1] < 16000 and val[2] < 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("right" + "\n")
    elif val[0] > 16000 and val[1] > 16000 and val[2] < 16000 and val[3] < 16000 and val[4] < 55000:
        uart.write("zoom_in" + "\n")
    elif val[0] > 16000 and val[1] < 16000 and val[2] > 16000 and val[3] < 16000 and val[4] < 55000:
        uart.write("browser" + "\n")
    elif val[0] > 16000 and val[1] < 16000 and val[2] < 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("minimize" + '\n')
    elif val[0] > 16000 and val[1] < 16000 and val[2] < 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("desktop" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] > 16000 and val[3] < 16000 and val[4] < 55000:
        uart.write("explorer" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] < 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("settings" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] < 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("snip" + '\n')
    elif val[0] < 16000 and val[1] < 16000 and val[2] > 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("zoom_out" + '\n')
    elif val[0] < 16000 and val[1] < 16000 and val[2] > 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("TM" + '\n')
    elif val[0] < 16000 and val[1] < 16000 and val[2] < 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("new_tab" + '\n')
    elif val[0] > 16000 and val[1] > 16000 and val[2] > 16000 and val[3] < 16000 and val[4] < 55000:
        uart.write("new_win" + '\n')
    elif val[0] > 16000 and val[1] > 16000 and val[2] < 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("tab_view" + '\n')
    elif val[0] > 16000 and val[1] > 16000 and val[2] < 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("refresh" + '\n')
    elif val[0] > 16000 and val[1] < 16000 and val[2] > 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("vd" + '\n')
    elif val[0] > 16000 and val[1] < 16000 and val[2] > 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("vdc" + '\n')
    elif val[0] > 16000 and val[1] < 16000 and val[2] < 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("maximize" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] > 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("emoji" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] > 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("cut" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] < 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("copy" + '\n')
    elif val[0] < 16000 and val[1] < 16000 and val[2] > 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("paste" + '\n')
    elif val[0] > 16000 and val[1] > 16000 and val[2] > 16000 and val[3] > 16000 and val[4] < 55000:
        uart.write("close" + '\n')
    elif val[0] > 16000 and val[1] > 16000 and val[2] > 16000 and val[3] < 16000 and val[4] > 55000:
        uart.write("tab" + '\n')
    elif val[0] > 16000 and val[1] > 16000 and val[2] < 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("run" + '\n')
    elif val[0] > 16000 and val[1] < 16000 and val[2] > 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("select_all" + '\n')
    elif val[0] < 16000 and val[1] > 16000 and val[2] > 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("clip" + '\n')
    elif val[0] > 16000 and val[1] > 16000 and val[2] > 16000 and val[3] > 16000 and val[4] > 55000:
        uart.write("enter" + '\n')
    utime.sleep(2)


