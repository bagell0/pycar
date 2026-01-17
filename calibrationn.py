from my_pycar import PyCar, get_key
from time import sleep
import tkinter as tk
import subprocess

label = None
keypressed = False


menu_keys = {"1": False, "2": False, "3": False}
keys = {"w": False, "a": False, "s": False, "d": False, "equal": False, "minus": False}


def logic(root):
    #logic
    for key in keys:
        if keys[key]:
            label.config(text=f"Key pressed: {key}")
    if not keypressed:
        label.config(text="No key pressed")
    root.after(20, lambda: logic(root))



def on_key_press(event):
    global keypressed
    keypressed = True
    k = event.keysym.lower()
    if k == "backspace":
        menu = None
        
    if k in keys:
        keys[k] = True
    if k in menu_keys:
        menu = menu_keys[k]
        
        
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
    root.geometry("500x500")
    
    intro = tk.Label(root, text="Calibration program", font=("Arial", 20))
    intro.pack(pady=10)
    
    global label
    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack(pady=100)
    
    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)
    
    logic(root)
    
    try:
        root.mainloop()
    finally:
        subprocess.run(["xset", "r", "on"], check=False)

if __name__ == "__main__":
    main()
