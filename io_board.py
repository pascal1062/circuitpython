import os
import time
from importlib import reload

from analog_input import AnalogInput
from universal_output import UOutputA, UOutputB
from automation import Automation
from thermistor10KDegC import Thermistor10KCelsius
from percent0100_aic import PercentDirectAIC
from on_off_bdc import OnOffBDC
import pg1
import pg2



aic10K = Thermistor10KCelsius()
percentDir = PercentDirectAIC()
onOff = OnOffBDC()

temperature = AnalogInput(1, "analog", aic10K)
photocell = AnalogInput(2, "analog", percentDir)

sortie_1 = UOutputA(1, "analog")
sortie_2 = UOutputA(2, "analog")
sortie_3 = UOutputA(3, "analog")
sortie_4 = UOutputA(4, "analog")
sortie_5 = UOutputB(5, "analog")
sortie_6 = UOutputB(6, "analog")
sortie_7 = UOutputB(7, "analog")
sortie_8 = UOutputB(8, "analog")

sortie_1.value = 0
sortie_2.value = 0
sortie_3.value = 0
sortie_4.value = 0
sortie_5.value = False
sortie_6.value = 0
sortie_7.value = 0
sortie_8.value = False

#print(temperature.value, sortie_2.value, photocell.value)
pg2_curr_file = os.stat("/home/pi/pascal/circuitpython/pg2.py")

while 1:
    sortie_1.value = int(Automation.scale(photocell.value,0,100,0,255))
    #sortie_2.value = Automation.aswitch(sortie_2.value, temperature.value, 26, 24)
    #sortie_6.value = pg1.execute([sortie_6.value], 0.5)
    #sortie_7.value = pg2.execute(sortie_7.value, [photocell.value])

    pg2_new_file = os.stat("/home/pi/pascal/circuitpython/pg2.py")
    if pg2_new_file.st_mtime != pg2_curr_file.st_mtime:
        reload(pg2)
        pg2_curr_file = os.stat("/home/pi/pascal/circuitpython/pg2.py")

    time.sleep(0.1)

# End
