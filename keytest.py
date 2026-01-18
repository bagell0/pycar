import tkinter as tk
import subprocess

key_released = True
label = None


def logic(root):
    if key_released:
        label.config(text="")
    root.after(1000, lambda: logic(root))


def on_key_press(event):
    global key_released
    k = event.keysym.lower()
    key_released = False            
    label.config(text=f"Key pressed: {k}") 

def on_key_release(event):
    global key_released
    k = event.keysym.lower()
    key_released = True
    label.config(text=f"Key released: {k}")
    
def main():
    subprocess.run(["xset", "r", "off"], check=False)
    root = tk.Tk()
    root.title("Key test")
    root.geometry("300x100")

    global label
    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack(pady=10)
        
    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)
    
    logic(root)
    
    try:
        root.mainloop()
    finally:
        subprocess.run(["xset", "r", "on"], check=False)

if __name__ == "__main__":
    main()