import time
import board
import digitalio
import rotaryio
import busio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# --- ECRAN OLED ---
displayio.release_displays()
try:
    i2c = busio.I2C(board.SCL, board.SDA) # Broches D5 et D4
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
    splash = displayio.Group()
    display.root_group = splash
    text_area = label.Label(terminalio.FONT, text="HACKPAD READY", color=0xFFFFFF, x=15, y=15)
    splash.append(text_area)
    has_screen = True
except Exception as e:
    has_screen = False

def update_screen(text):
    if has_screen:
        text_area.text = text

# --- CONTROLE MEDIA & BOUTONS ---
cc = ConsumerControl(usb_hid.devices)

encoder = rotaryio.IncrementalEncoder(board.D0, board.D1) 
encoder_button = digitalio.DigitalInOut(board.D2)
encoder_button.direction = digitalio.Direction.INPUT
encoder_button.pull = digitalio.Pull.UP

sw1 = digitalio.DigitalInOut(board.D10) # Précédent
sw1.direction = digitalio.Direction.INPUT
sw1.pull = digitalio.Pull.UP

sw2 = digitalio.DigitalInOut(board.D9) # Pause
sw2.direction = digitalio.Direction.INPUT
sw2.pull = digitalio.Pull.UP

sw3 = digitalio.DigitalInOut(board.D8) # Suivant
sw3.direction = digitalio.Direction.INPUT
sw3.pull = digitalio.Pull.UP

sw4 = digitalio.DigitalInOut(board.D7) # Play
sw4.direction = digitalio.Direction.INPUT
sw4.pull = digitalio.Pull.UP

last_encoder_position = encoder.position
encoder_button_state = encoder_button.value
sw1_state = sw1.value
sw2_state = sw2.value
sw3_state = sw3.value
sw4_state = sw4.value

# --- BOUCLE PRINCIPALE ---
while True:
    current_position = encoder.position
    if current_position > last_encoder_position:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        update_screen("VOLUME +")
        last_encoder_position = current_position
    elif current_position < last_encoder_position:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        update_screen("VOLUME -")
        last_encoder_position = current_position

    if not encoder_button.value and encoder_button_state:
        cc.send(ConsumerControlCode.MUTE)
        update_screen("MUTE")
        time.sleep(0.2)
    encoder_button_state = encoder_button.value

    if not sw1.value and sw1_state:
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        update_screen("PRECEDENT")
        time.sleep(0.2)
    sw1_state = sw1.value

    if not sw2.value and sw2_state:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        update_screen("PAUSE")
        time.sleep(0.2)
    sw2_state = sw2.value

    if not sw3.value and sw3_state:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        update_screen("SUIVANT")
        time.sleep(0.2)
    sw3_state = sw3.value

    if not sw4.value and sw4_state:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        update_screen("PLAY")
        time.sleep(0.2)
    sw4_state = sw4.value

    time.sleep(0.01)