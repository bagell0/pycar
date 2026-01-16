from my_pycar import PyCar, get_key

def main():
    backspace = "\x7f"

    run = True
    
    px = PyCar(-15.5, 4, 6.5)
    
    while run:
        k = get_key()
        
        if k == backspace:
            run = False
        if k == "w":
            px.fwd()
        if k == "s":
            px.bck()
        if k == "a":
            px.turn_left()
        if k == "d":
            px.turn_right()
        
        if k is None:
            px.stop()
            
if __name__ == "__main__":
    main()

