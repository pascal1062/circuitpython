
#value1 = io1.scan_in()


value1 = io1.value
value2 = io2.value
print(value1,value2)

bo1 = False
led1 = 0 #digitalio.DigitalInOut(board.D4)
#led1.direction = digitalio.Direction.OUTPUT

bo2 = False
led2 = 0 # digitalio.DigitalInOut(board.D17)
#led2.direction = digitalio.Direction.OUTPUT

#bo1 = Automation.aswitch(bo1,19.1,19,21)

w_buf = bytearray(2)
tlv = bytearray(2)
dac = 3
value = 127

#value1 = io1.scan_in()
#value1 = io1.avg()
#value2 = io2.scan()
#bo1 = Automation.aswitch(bo1,value1,300,800)
#time.sleep(0.01)

#led1 = 255 if bo1 else 0
led2 = 255 if bo2 else 0
#led1 = int(Automation.scale(value1,0,1024,0,255))
#value = int(Automation.scale(value1,0,1024,0,255))

# write to MCP4902 DACA
w_buf[0] = 48 | (led1 >> 4)
# w_buf[0] = 16 | (led1 >> 4) gain set to 2, vref tied to voltage divider
w_buf[1] = (led1 & 15) << 4
#io1.scan_out(w_buf)

# write to MCP4902 DACB
w_buf[0] = 176 | (led2 >> 4)
# w_buf[0] = 144 | (led2 >> 4) gain set to 2, vref tied to voltage divider
w_buf[1] = (led2 & 15) << 4
#io1.scan_out(w_buf)

tlv[0] = ((3 << 14) | (dac << 12) | (value << 4)) >> 8
tlv[1] = ((3 << 14) | (dac << 12) | (value << 4)) & 255
#io1.tlv5621(tlv)

t1 = time.time()

if time.time() - t1 > 1:
    t1 = time.time()
    #print(value1,str(bo1),led1,led2)
    #bo2 = pg1.execute([bo2])
    #print(value1,value)
    #print(value1,value2)
    value1 = io1.value
    value2 = io2.value
    print(value1,value2)


Out = [None, None, None, None, None, None, None, None]
Out[0] = UOutputA(1, "analog")
Out[1] = UOutputA(2, "analog")
Out[2] = UOutputA(3, "analog")
Out[3] = UOutputA(4, "analog")
Out[4] = UOutputB(5, "analog")
Out[5] = UOutputB(6, "analog")
Out[6] = UOutputB(7, "analog")
Out[7] = UOutputB(8, "analog")

while 1:
    for i in range(0,7):
        Out[i].value = True
        time.sleep(0.5)
        Out[i].value = False
    for i in range(0,7):
        Out[7-i].value = True
        time.sleep(0.5)
        Out[7-i].value = False
