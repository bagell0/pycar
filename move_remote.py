from my_pycar import PyCar
import tkinter as tk
import subprocess
import socket

label = None

HOST = "0.0.0.0"
PORT = 5000


px = PyCar(0, 2.7, 9) 

keys = {"w": False, "a": False, "s": False, "d": False, "space": False}

def car_logic(root, conn):
    
    try:
        raw = conn.recv(1024)
    except BlockingIOError:
        raw = b""
    
    data = raw.decode("utf-8", errors="replace")
    
    for line in data.splitlines():
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        action, k = parts[0], parts[1]
        if k in keys:
            keys[k] = (action == "DOWN")
    
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

    root.after(20, lambda : car_logic(root, conn)) #loop over #lambda makes it a callable function. otherwise either call immediately or try with no args
        
    
def main():
    subprocess.run(["xset", "r", "off"], check=False) #turns key autorepeat off
    root = tk.Tk()
    root.title("Key test")
    root.geometry("300x100")

    iplabel = tk.Label(root, text="")
    iplabel.pack(pady=10)

    global label
    label = tk.Label(root, text="")
    label.pack(pady=10)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a TCP IPv4 socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1) #one client at a time
    conn, addr = s.accept() #waits until another computer connects
    conn.setblocking(False) #makes the socket non-blocking. s.t. won't freeze
    
    iplabel.config(text=f"Connected from: {addr}")
    
    car_logic(root, conn) #starts car logic
    
    try:
        root.mainloop() #starts the interface loop
    finally:
        subprocess.run(["xset", "r", "on"], check=False) #turns key autorepeat back on
        try:
            conn.close()
        except:
            pass
        try:
            s.close()
        except:
            pass
        px.stop()
        
            

if __name__ == "__main__":
    main()
