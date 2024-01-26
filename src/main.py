from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control
from hal import hal_led as led

#Empty list to store sequence of keypad presses
password = []

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    password.append(key)
    print(password)


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    #--------------------Exercise 1--------------------------------#

    # Display something on LCD
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off 1 :Blink", 2)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()


#inisde key pressed
    if keypad.get_key() == 1:
        led_control.led_control_init(0)
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Blink LED", 2)
    elif keypad.get_key() == 0:
        led_control.led_control_init(1)
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("OFF LED", 2)

# Main entry point
if __name__ == "__main__":
    main()
