
import sys
sys.path.append(r" C:\Users\Saptadeep\Desktop\Python")


from pyfirmata import Arduino, util
import time

# Replace COM3 with your Arduino's port
board = Arduino('COM9')

# Pin 13 LED blinking
while True:
    board.digital[13].write(1)   # LED ON
    time.sleep(1)                # 1 second delay
    board.digital[13].write(0)   # LED OFF
    time.sleep(1)                # 1 second delay
