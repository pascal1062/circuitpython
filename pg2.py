import time
from automation import Automation

t = time.time()

def code(value, values):
    """ code goes here"""
    val = value
    photocell = values[0]
    val = not val
    #val = Automation.aswitch(val, photocell, 30, 70)
    #val = False

    return val

def execute(return_val, calc_val):
    global t
    scan_rate = 1
    rv = return_val

    if time.time() - t > scan_rate:
        t = time.time()
        try:
            rv = code(return_val, calc_val)
        except:
            print("program error")
        finally:
            pass

    return rv

# End
