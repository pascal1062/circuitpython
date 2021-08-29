import busio
import digitalio
import board
#from adafruit_mcp3xxx.mcp3008 import MCP3008
#from adafruit_mcp3xxx.analog_in import AnalogIn

class IO_spi():
    
    def __init__(self):
        self._spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        self._cs0 = digitalio.DigitalInOut(board.D8)
        self._cs0.direction = digitalio.Direction.OUTPUT
        self._cs0.value = True
        self._cs1 = digitalio.DigitalInOut(board.D7)
        self._cs1.direction = digitalio.Direction.OUTPUT
        self._cs1.value = True

    def scan_in(self):
        while not self._spi.try_lock():
            pass
	
        out_buf = bytearray(3)
        in_buf = bytearray(3)
        out_buf = (b'\xc0\x00\x00')
        self._spi.configure(baudrate=100000, phase=0, polarity=0)
        self._cs0.value = False
        self._spi.write_readinto(out_buf, in_buf, out_start=0, out_end=len(out_buf), in_start=0, in_end=len(in_buf))
        self._cs0.value = True
        self._spi.unlock()
        result = (in_buf[0] & 0x01) << 9
        result |= in_buf[1] << 1
        result |= in_buf[2] >> 7
        return result
    
    def scan_out(self, wbuf):
        while not self._spi.try_lock():
            pass
    
        self._spi.configure(baudrate=100000, phase=0, polarity=0)
        self._cs1.value = False
        self._spi.write(wbuf)
        self._cs1.value = True
        self._spi.unlock()
        
    def tlv5621(self, wbuf): 
        while not self._spi.try_lock():
            pass
    
        self._spi.configure(baudrate=100000, phase=1, polarity=0)
        self._cs1.value = False
        self._cs1.value = True
        #self._spi.write(bytes([0x1f, 0xc0]))
        #self._spi.write(bytes([0xf7, 0xf0]))
        self._spi.write(wbuf)
        self._cs1.value = False
        #self._cs1.value = False
        self._cs1.value = True
        #self._spi.write(bytes([0x07, 0xc0]))
        self._spi.write(bytes([0x9f, 0xf0]))
        self._cs1.value = False
        #self._cs1.value = False
        self._cs1.value = True        
        self._spi.unlock()         

# End