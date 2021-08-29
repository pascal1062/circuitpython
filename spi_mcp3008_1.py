import board
import busio
import digitalio

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D8)
cs.direction = digitalio.Direction.OUTPUT
cs.value = True

out_buf = bytearray(3)
in_buf = bytearray(3)

# According to data sheet, send the "Configure Bits" for reading desired input differential or single-ended
# example here is the reading of input #1 single-ended B11000000 (0xC0). Other 2 bytes are only fillers "Don't care bits"
out_buf = (b'\xc0\x00\x00')

while not spi.try_lock():
    pass

spi.configure(baudrate=5000000, phase=0, polarity=0)
cs.value = False
spi.write_readinto(out_buf, in_buf, out_start=0, out_end=len(out_buf), in_start=0, in_end=len(in_buf))
cs.value = True
result = (in_buf[0] & 0x01) << 9
result |= in_buf[1] << 1
result |= in_buf[2] >> 7
print(result)
#spi.unlock()

# End
