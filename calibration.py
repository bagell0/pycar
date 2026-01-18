from my_pycar import PyCar
from time import sleep
import tkinter as tk
import subprocess

keylabel = None
menulabel = None
dscrlabel = None
actionlabel = None
infolabel = None

keypressed = False
step = 0.5
menu = None

keys = {
    "w": False, "a": False, "s": False, "d": False,
    "left": False, "right": False,
    "equal": False, "minus": False,
    }
menu_keys = ["1", "2"]

px = PyCar()

def logic(root):
    global step
    
    #only used for reset
    if menu is None:
        menulabel.config(text="Main menu")
        dscrlabel.config(text="Reset would affect all")
    if menu == "1":
        menulabel.config(text="Camera menu")
        dscrlabel.config(text="Reset would affect only the camera")
    if menu == "2":
        menulabel.config(text="Servo menu")
        dscrlabel.config(text="Reset would affect only the servos")
        
    if keys["w"] and not keys["s"]:
        px.tilt(step, up=True)
        actionlabel.config(text=f"Tilting up by {round(step, 1)}")
    if keys["s"] and not keys["w"]:
        px.tilt(step, down=True)
        actionlabel.config(text=f"Tilting down by {round(step, 1)}")
    if keys["a"] and not keys["d"]:
        px.pan(step, left=True)
        actionlabel.config(text=f"Panning left by {round(step, 1)}")
    if keys["d"] and not keys["a"]:
        px.pan(step, right=True)
        actionlabel.config(text=f"Panning right by {round(step, 1)}")
    
    if keys["left"] and not keys["right"]:
        px.steer(step, left=True)
        actionlabel.config(text=f"Steering left by {round(step, 1)}")
    if keys["right"] and not keys["left"]:
        px.steer(step, right=True)
        actionlabel.config(text=f"Steering right by {round(step, 1)}")
    
    if keys["equal"] and not keys["minus"]:
        step += 0.1
        actionlabel.config(text="Increasing step")
        sleep(0.2)
    if keys["minus"] and not keys["equal"] and round(step, 1) > 0:
        step -= 0.1
        actionlabel.config(text="Decreasing step")
        sleep(0.2)
    
    q = None
    for key in keys:
        if keys[key]:
            q = key
    
    if keys["equal"]: #if you press + on a keyboard without holding shift then it's =
        q = "plus"
    
        
    infolabel.config(text=f"""
Servo: {round(px.servodir, 1)}, Pan: {round(px.pandir, 1)}, Tilt: {round(px.tiltdir, 1)}
Step: {round(step, 1)}
Key pressed: {q}
                                """)
    
    if not keypressed:
        actionlabel.config(text="No action done")
    
    #call again after 20ms
    root.after(20, lambda: logic(root))



def on_key_press(event):
    global keypressed
    global menu
    keypressed = True
    k = event.keysym.lower()
    
    if k in keys:
        keys[k] = True
    if k in menu_keys:
        menu = k
    if k == "backspace":
        menu = None
        return
    
    if k == "r":
        match menu:
            case "1":
                actionlabel.config(text="Resetting the camera")
                px.set_neutral(cam=True)
            case "2":
                actionlabel.config(text="Resetting the servo")
                px.servodir = 0
            case _:
                actionlabel.config(text="Resetting all")
                px.set_neutral()
        px.upd_dir()

        
def on_key_release(event):
    global keypressed
    keypressed = False
    k = event.keysym.lower()
    if k in keys:
        keys[k] = False
    
def main():
    subprocess.run(["xset", "r", "off"], check=False)
    root = tk.Tk()
    root.title("Calibration")
    root.geometry("800x600")
    
    header = tk.Label(root, text="Calibration program", font=("Arial", 20))
    header.pack(pady=10)
    
    manual = tk.Label(root, text="""
To move the camera use w/a/s/d
To move the servos use the arrows left/right
To increase/decrease the step by which the angles are changing press +/-
To reset press r
To pick reset option press 1 for camera, 2 for servos, none for all
To exit the current menu (reset option) press backspace
""", font=("Arial", 12))
    manual.pack(pady=10)
    
    global keylabel
    keylabel = tk.Label(root, text="", font=("Arial", 14))
    keylabel.pack(pady=10)
    
    global menulabel
    menulabel = tk.Label(root, text="", font=("Arial", 16))
    menulabel.pack(pady=10)
    
    global dscrlabel #description label
    dscrlabel = tk.Label(root, text="", font=("Arial", 12))
    dscrlabel.pack(pady=10)
    
    global actionlabel
    actionlabel = tk.Label(root, text="", font=("Arial", 14))
    actionlabel.pack(pady=10)
    
    global infolabel
    infolabel = tk.Label(root, text="", font=("Arial", 14))
    infolabel.pack(pady=20)
    
    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)
    
    logic(root)
    
    try:
        root.mainloop()
    finally:
        subprocess.run(["xset", "r", "on"], check=False)

if __name__ == "__main__":
    main()
