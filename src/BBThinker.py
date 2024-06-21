from PIL import ImageTk, Image
import base64
import tkinter as tk, subprocess, os, sys

scratch_path = os.path.expandvars(r'%LOCALAPPDATA%\Programs\Scratch 3\Scratch 3.exe')
course_files_path = os.path.normpath(os.path.expanduser("~/Desktop/Course Files"))
# Opens Scratch if downloaded from website
def open_scratch():
    try:
        print("Opening Scratch...")
        os.startfile(scratch_path)
    except:
        print("Could not open Scratch! Try using a different path or download Scratch from https://scratch.mit.edu/download")
        sys.exit(1)
# Opens the course files folder or creates a new dir
def open_course_dir():
    try:
        print("Opening course files...")
        os.startfile(course_files_path)
    except:
        os.mkdir(course_files_path)  
        print("Could not open course files! A new directory has been made, try again!")     
# Opens IDLE if installed properly
def open_idle():
    try:
        print("Opening IDLE...")
        if sys.platform.startswith('win'):
            subprocess.Popen(['idle'])
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', '-a', 'IDLE'])
        else:
            subprocess.Popen(['idle3']) 
    except Exception:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'idle'])
        print("Could not open IDLE, try downloading from respective operating system store")
        print("Ff on Linux, download via your package manager")
        sys.exit(1)
# Opens the default text editor (For the web dev courses)
def open_text():
    print("Opening text editor...")
    if sys.platform.startswith('win'):
        subprocess.run(["notepad"])
    elif sys.platform.startswith('darwin'):
        subprocess.run(["open", "-a", "TextEdit"])
    else:
        print("Text Editor opening is not supported on this platform.\nFor Linux, try installing a package for a text editor.")

# Tkinter setup
root = tk.Tk()
root.iconbitmap("assets/bbicon.ico")
root.title("BestBrains Thinker")
root.geometry("400x425+300+120")
root.resizable(False, False)
# Label config
frame = tk.Frame(root, width=400, height=80)
frame.pack_propagate(False) 
frame.pack()
image_path = "assets/bblabel.PNG"
photo = ImageTk.PhotoImage(Image.open(image_path).resize((400,80)))
label = tk.Label(frame, image=photo)
label.image = photo
label.pack()
# Background config
canvas1 = tk.Canvas( root, width = 400, height = 400) 
canvas1.pack(fill = "both", expand = True) 
bg = tk.PhotoImage(file = "assets/bbcanvas.PNG")
canvas1.create_image( 0, 0, image = bg, anchor = "nw") 
# Button config
button_height, button_width, button_font = 3, 14, "Courier 12 bold"
file_button = tk.Button(root, text="Course Files", command=open_course_dir, 
                        height= button_height, width = button_width, 
                        font=button_font, 
                        highlightthickness=2, 
                        highlightbackground="orange", 
                        foreground="blue", 
                        background="white", 
                        activeforeground="white", 
                        activebackground="blue")
file_button.pack(pady=10)
scratch_button = tk.Button(root, text="Scratch", command=open_scratch, 
                           height= button_height, 
                           width = button_width, 
                           font=button_font, 
                           highlightthickness=2, 
                           highlightbackground="orange", 
                           foreground = "orange", 
                           background="white", 
                           activeforeground="white", 
                           activebackground="orange")
scratch_button.pack(pady=10)
idle_button = tk.Button(root, text="Python", command=open_idle, 
                        height= button_height, 
                        highlightthickness=2, 
                        highlightbackground="orange", 
                        foreground = "green", 
                        background="white", 
                        activeforeground="white", 
                        activebackground="green", 
                        width = button_width, 
                        font=button_font)
idle_button.pack(pady=10)
txt_button = tk.Button(root, text="Web Dev", command=open_text, 
                       height= button_height, 
                       highlightthickness=2, 
                       highlightbackground="orange", 
                       width = button_width, 
                       font=button_font, 
                       foreground = "red", 
                       background="white", 
                       activeforeground="white", 
                       activebackground="red")
txt_button.pack(pady=10)
# Canvas config
canvas_size = 125
button1_canvas = canvas1.create_window(canvas_size, 20, anchor = "nw", window = file_button) 
button2_canvas = canvas1.create_window(canvas_size, 100, anchor = "nw", window = scratch_button)   
button3_canvas = canvas1.create_window(canvas_size, 180, anchor = "nw", window = idle_button)                                       
button4_canvas = canvas1.create_window(canvas_size, 260, anchor = "nw", window = txt_button)

root.mainloop()