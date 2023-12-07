import serial
import keyboard

ser = serial.Serial('COM16', 9600)  # Replace 'COMx' with the correct COM port

while True:
    data = ser.readline().decode('utf-8').strip()
    if data:
        print("Received from Pico:", data)
        # Your processing logic here
        if data == 'left':
            keyboard.press_and_release('left')
        elif data == 'down':
            keyboard.press_and_release('down')
        elif data == 'Windows':
            keyboard.press_and_release('win')
        elif data == "up":
            keyboard.press_and_release('up')
        elif data == "right":
            keyboard.press_and_release('right')
        elif data == "zoom_in":
            keyboard.press_and_release('ctrl + =')
        elif data == "browser":
            keyboard.press_and_release("win + 4")
        elif data == "minimize":
            keyboard.press_and_release("win + m")
        elif data == "desktop":
            keyboard.press_and_release("win + d")
        elif data == "explorer":
            keyboard.press_and_release("win + e")
        elif data == "settings":
            keyboard.press_and_release("win + i")
        elif data == "snip":
            keyboard.press_and_release("win + shift + s")
        elif data == "zoom_out":
            keyboard.press_and_release("ctrl + -")
        elif data == "TM":
            keyboard.press_and_release("ctrl + shift + esc")
        elif data == "new_tab":
            keyboard.press_and_release("ctrl + t")
        elif data == "new_win":
            keyboard.press_and_release("ctrl + n")
        elif data == "tab_view":
            keyboard.press_and_release("win + tab")
        elif data == "refresh":
            keyboard.press_and_release("ctrl + r")
        elif data == "vd":
            keyboard.press_and_release("win + ctrl + d")
        elif data == "vdc":
            keyboard.press_and_release("win + ctrl + f4")
        elif data == "maximize":
            keyboard.press_and_release("win + up")
        elif data == "emoji":
            keyboard.press_and_release("win + .")
        elif data == "cut":
            keyboard.press_and_release("ctrl + x")
        elif data == "copy":
            keyboard.press_and_release("ctrl + c")
        elif data == "paste":
            keyboard.press_and_release("ctrl + v")
        elif data == "close":
            keyboard.press_and_release("ctrl + w")
        elif data == "tab":
            keyboard.press_and_release("tab")
        elif data == "run":
            keyboard.press_and_release("win + r")
        elif data == "select_all":
            keyboard.press_and_release("ctrl + a")
        elif data == "clip":
            keyboard.press_and_release("win + v")
        elif data == "enter":
            keyboard.press_and_release("enter")