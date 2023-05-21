import tkinter as tk
import subprocess
import signal

processes = []

def start_program_1():
    process = subprocess.Popen(['python', 'eyecursor.py'])
    processes.append(process)

def stop_program_1():
    if processes:
        process = processes.pop()
        process.send_signal(signal.SIGTERM)

def start_program_2():
    process = subprocess.Popen(['python', 'handgesturemouse.py'])
    processes.append(process)

def stop_program_2():
    if processes:
        process = processes.pop()
        process.send_signal(signal.SIGTERM)

def start_program_3():
    process = subprocess.Popen(['python', 'subway.py'])
    processes.append(process)

def stop_program_3():
    if processes:
        process = processes.pop()
        process.send_signal(signal.SIGTERM)

root = tk.Tk()
root.title("App with Buttons")

button1_start = tk.Button(root, text="Start Program 1", command=start_program_1)
button1_start.pack()

button1_stop = tk.Button(root, text="Stop Program 1", command=stop_program_1)
button1_stop.pack()

button2_start = tk.Button(root, text="Start Program 2", command=start_program_2)
button2_start.pack()

button2_stop = tk.Button(root, text="Stop Program 2", command=stop_program_2)
button2_stop.pack()

button3_start = tk.Button(root, text="Start Program 3", command=start_program_3)
button3_start.pack()

button3_stop = tk.Button(root, text="Stop Program 3", command=stop_program_3)
button3_stop.pack()

root.mainloop()
