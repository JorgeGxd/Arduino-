import pyfirmata

import time

board = pyfirmata.Arduino('COM3')


while True:
    
    # led verde
    board.digital [7]. write (1)
    time.sleep(2)
    board.digital [7]. write (0)
    time.sleep(1)
    