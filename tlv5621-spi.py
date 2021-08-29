import sys
import board
import busio
import digitalio

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D12)
cs.direction = digitalio.Direction.OUTPUT
cs.value = False
buf = bytearray(2)

def dac_write(address, value):

    dac_adress =  address - 1
    buf[0] = ((3 << 14) | (dac_adress << 12) | (value << 4)) >> 8
    buf[1] = ((3 << 14) | (dac_adress << 12) | (value << 4)) & 255

    while not spi.try_lock():
        pass

    spi.configure(baudrate=100000, phase=1, polarity=0)
    cs.value = True
    spi.write(buf)
    cs.value = False
    cs.value = True
    spi.write(bytes([0x9f, 0xf0]))
    cs.value = False
    spi.unlock()

addr = int(sys.argv[1])
val = int(sys.argv[2])

dac_write(addr,val)

# End
