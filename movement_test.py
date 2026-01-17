from my_pycar import PyCar
import tkinter as tk


def on_key_press(event):
    k = event.keysym.lower()

def on_key_release(event):
    print("UP:", event.keysym)


def main():
    keys = {"w": False, "a": False, "s": False, "d": False}
    
    root = tk.Tk()
    root.title("Key test")
    root.geometry("300x100")

    label = tk.Label(root, text="Click here, then press keys")
    label.pack()
    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)

    root.mainloop()


        

            
if __name__ == "__main__":
    main()

