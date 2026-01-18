from my_pycar import PyCar
import tkinter as tk
import subprocess

label = None

px = PyCar(2.5, 3.6, 7.9) 

keys = {"w": False, "a": False, "s": False, "d": False, "space": False}

def car_logic(root):
    if keys["w"] and not keys["s"]:
        px.fwd()
        label.config(text="Forward")
    elif keys["s"] and not keys["w"]:
        px.bck()
        label.config(text="Backward")
    else:
        px.stop()
        
    if keys["a"] and not keys["d"]:
        px.steer(left=True)
        label.config(text="Left")
    if keys["d"] and not keys["a"]:
        px.steer(right=True)
        label.config(text="Right")

    root.after(20, lambda : car_logic(root)) #loop over #lambda makes it a callable function. otherwise either call immediately or try with no args

def on_key_press(event):
    k = event.keysym.lower()
    
    if k in keys:
        keys[k] = True
        
    if k == "space":
        for key in keys:
            keys[key] = False
            
def on_key_release(event):
    k = event.keysym.lower()
    
    if k in keys:
        keys[k] = False
        
    
def main():
    subprocess.run(["xset", "r", "off"], check=False) #turns key autorepeat off
    root = tk.Tk()
    root.title("Key test")
    root.geometry("300x100")

    global label
    label = tk.Label(root, text="")
    label.pack()
        
    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)
    
    car_logic(root) #starts car logic
    
    try:
        root.mainloop() #starts the interface loop
    finally:
        subprocess.run(["xset", "r", "on"], check=False) #turns key autorepeat back on

if __name__ == "__main__":
    main()
