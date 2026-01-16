from my_pycar import PyCar

px = PyCar()



run = True
while run:
    i = input()
    if i == "w":
        px.fwd()
    elif i == "s":
        px.bck()
    else:
        run = False
