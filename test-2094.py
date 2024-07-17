def add_time(val, adt):
    time = float(val)
    durate = float(adt)
    new_time = time + durate
    return new_time

use = add_time('3.30', '2.12')
print(use)