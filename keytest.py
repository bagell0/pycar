import tkinter as tk
root = tk.Tk()
root.title("Key test")
root.geometry("300x100")

label = tk.Label(root, text="Click here, then press keys")
label.pack()


def on_key_press(event):
    print("DOWN:", event.keysym)

def on_key_release(event):
    print("UP:", event.keysym)
    
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

root.mainloop()
