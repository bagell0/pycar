from my_pycar import PyCar, get_key
from time import sleep


px = PyCar(20, 20, 20)



while True:
    k = get_key()
    if k:
        print(repr(k))
    if k == "q" or k == "\x7f":
        break
    if k == "r":
        px.reset_angles_abs()
    if k == "s":
        px.reset_angles()

