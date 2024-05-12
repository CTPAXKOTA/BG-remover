import cv2
import rembg as rebg
from tkinter import *
from tkinter import ttk

def createwindow():
    def removebg():
        input_file_path = entry.get()
        output_file = input_file_path[:-4] + "(1).png"
        img = cv2.imread(input_file_path)
        img_without_bg = rebg.remove(img)
        cv2.imwrite(output_file, img_without_bg)

    window = Tk()
    label = ttk.Label(text="Enter file path")
    label.pack(padx=200, pady=0)    
    window.title("Remove bg")
    window.geometry("500x100")
    entry = ttk.Entry()
    entry.pack(anchor=NW, padx=200, pady=5)
    remove_button = ttk.Button(text = "Remove bg", command = removebg)
    remove_button.pack()
    window.mainloop()    
    

        
createwindow()    
