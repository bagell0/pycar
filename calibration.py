from my_pycar import PyCar, get_key
from time import sleep


def main():
    #Introduction
    print("""
    This is a calibration program to set the correct initial angles.

    To go back or exit click backspace.
    """)

    backspace = "\x7f" #this is the ASCII code for a backspace

    px = PyCar() #this is our car object

    #I am using while loops and the get_key function to imitate a keyboard listener.
    #In simpler words, I am removing the need to press enter every time you hit a key on your keyboard.


    #Boolean variables to control the while loops
    run = True
    run1 = True
    run2 = True

    print("""
        You are currently in the main menu.

        Menu:
        Calibrate the camera - Press 1
        Calibrate the servos - Press 2
        Reset all angles - Press 3
        Reset cam angles - Press 4
        Reset servo angles - Press 5
        
        """)
    while run:
        k = get_key()
        if k == backspace:
            print("Exiting the program.")
            print(f"""
    The final angles are:
    servo - {px.get_servo()}
    pan - {px.get_pan()}
    tilt - {px.get_tilt()}
            """)
            run = False
        if k == "1":
            print("""
            You are in the camera mode.
            
            To tilt up/down press w/s on your keyboard.
            To pan left/right press a/d on your keyboard.
            """)
            
            step = float(input("Type the value by which the angle will be changed each time. E.g. 0.5"))
            print(f"Step: {step}")
            
            run1 = True
            while run1:
                px.reset_position()
                tilt = px.get_tilt()
                pan = px.get_pan()
                q = get_key()
                
                if q == backspace:
                    print("Exiting the cam menu.")
                    print("1 - cam mode. 2 - servo mode. 3 - reset all. 4 - reset cam. 5 - reset servo. 6 - show angles. Backspace - exit")
                    run1 = False
                    
                if q == "w":
                    tilt += step
                    px.set_tilt(tilt)
                    print(f"pan: {px.get_pan()}, tilt: {px.get_tilt()}") #getter instead of variable to check memory
                if q == "s":
                    tilt -= step
                    px.set_tilt(tilt)
                    print(f"pan: {px.get_pan()}, tilt: {px.get_tilt()}")
                if q == "a":
                    pan -= step
                    px.set_pan(pan)
                    print(f"pan: {px.get_pan()}, tilt: {px.get_tilt()}") 
                if q == "d":
                    pan += step
                    px.set_pan(pan)
                    print(f"pan: {px.get_pan()}, tilt: {px.get_tilt()}")
                    
        if k == "2":
            print("""
            You are in the servo mode.
            
            To turn left/right press a/d on your keyboard.
            """)
            
            step = float(input("Type the value by which the angle will be changed each time. E.g. 0.5"))
            print(f"Step: {step}")
            
            run2 = True
            while run2:
                px.reset_position()
                servo = px.get_servo()
                r = get_key()
                
                if r == backspace:
                    print("Exiting the servo menu.")
                    print("1 - cam mode. 2 - servo mode. 3 - reset all. 4 - reset cam. 5 - reset servo. 6 - show angles. Backspace - exit")
                    run2 = False
                
                if r == "a":
                    servo -= step
                    px.set_servo(servo)
                    print(f"The angle now is: {px.get_servo()}") #get_servo instead of servo to check memory
                if r == "d":
                    servo += step
                    px.set_servo(servo)
                    print(f"The angle now is: {px.get_servo()}")                

        if k == "3":
            print("Resetting all angles.")
            px.reset_angles()
            px.reset_position()
            print(f"""
    The angles now are:
    servo - {px.get_servo()}
    pan - {px.get_pan()}
    tilt - {px.get_tilt()}
            """)
            
        if k == "4":
            print("Resetting cam angles.")
            px.set_pan(0)
            px.set_tilt(0)
            px.reset_position()
            print(f"""
    The angles now are:
    servo - {px.get_servo()}
    pan - {px.get_pan()}
    tilt - {px.get_tilt()}
            """)
        if k == "5":
            print("Resetting servo angles.")
            px.set_servo(0)
            px.reset_position()
            print(f"""
    The angles now are:
    servo - {px.get_servo()}
    pan - {px.get_pan()}
    tilt - {px.get_tilt()}
            """)
        if k == "6":
            print(f"""
    The angles now are:
    servo - {px.get_servo()}
    pan - {px.get_pan()}
    tilt - {px.get_tilt()}
            """)
            
if __name__ == "__main__":
    main()