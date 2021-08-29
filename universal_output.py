'''
    Universal output class
    output can be create as on/off digital or analog dc voltage
    IC chip is TLV5621 connected through SPI serial interface. resoltion is 8 bits 0-255
'''

import busio
import digitalio
import board

class UOutputA():

    def __init__(self, instance, type):
        self._spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        self._cs = digitalio.DigitalInOut(board.D7)
        self._cs.direction = digitalio.Direction.OUTPUT
        self._cs.value = False
        self._instance = instance
        self._type = type
        self._dac = None
        self._buf = bytearray(2)

    def dac_write(self, wbuf):
        while not self._spi.try_lock():
            pass

        self._spi.configure(baudrate=100000, phase=1, polarity=0)
        self._cs.value = False
        self._cs.value = True
        self._spi.write(wbuf)
        self._cs.value = False
        self._cs.value = True
        self._spi.write(bytes([0x9f, 0xf0]))
        self._cs.value = False
        self._spi.unlock()

    def get_value(self):
        return self._dac

    def set_value(self, val):
        self._dac = val

        if isinstance(self._dac, bool):
            if self._dac == True:
                dac_value = 255
            else:
                dac_value = 0
        elif isinstance(self._dac, int):
            dac_value = self._dac
        else:
            dac_value = 0

        dac_adress =  self._instance - 1
        self._buf[0] = ((3 << 14) | (dac_adress << 12) | (dac_value << 4)) >> 8
        self._buf[1] = ((3 << 14) | (dac_adress << 12) | (dac_value << 4)) & 255
        self.dac_write(self._buf)

    value = property(fget=get_value, fset=set_value, fdel=None, doc=None)

class UOutputB():

    def __init__(self, instance, type):
        self._spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        self._cs = digitalio.DigitalInOut(board.D12)
        self._cs.direction = digitalio.Direction.OUTPUT
        self._cs.value = False
        self._instance = instance
        self._type = type
        self._dac = None
        self._buf = bytearray(2)

    def dac_write(self, wbuf):
        while not self._spi.try_lock():
            pass

        self._spi.configure(baudrate=100000, phase=1, polarity=0)
        self._cs.value = False
        self._cs.value = True
        self._spi.write(wbuf)
        self._cs.value = False
        self._cs.value = True
        self._spi.write(bytes([0x9f, 0xf0]))
        self._cs.value = False
        self._spi.unlock()

    def get_value(self):
        return self._dac

    def set_value(self, val):
        self._dac = val

        if isinstance(self._dac, bool):
            if self._dac == True:
                dac_value = 255
            else:
                dac_value = 0
        elif isinstance(self._dac, int):
            dac_value = self._dac
        else:
            dac_value = 0

        dac_adress =  self._instance - 5
        self._buf[0] = ((3 << 14) | (dac_adress << 12) | (dac_value << 4)) >> 8
        self._buf[1] = ((3 << 14) | (dac_adress << 12) | (dac_value << 4)) & 255
        self.dac_write(self._buf)

    value = property(fget=get_value, fset=set_value, fdel=None, doc=None)

# End
