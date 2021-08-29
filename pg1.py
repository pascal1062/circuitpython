import time

t = time.time()

def execute(values, scan_rate):
    global t
    val = values[0]

    """ code goes here"""
    if time.time() - t > scan_rate:
        t = time.time()
        val = not val

    return val

# End
