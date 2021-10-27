#pip install pyautogui
#pip install tkinter

import pyautogui    
import tkinter as tk    

root = tk.Tk()
root.title('Screenshot Taker')

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def myScreenshot():
    
    myScreenshot = pyautogui.screenshot()
    # Enter path were to save screenshot
    myScreenshot.save(r'A:\Screenshot in Python\screenshot.png') 

myButton = tk.Button(text='Take Screenshot', command=myScreenshot, bg='red',fg='white',font= 15)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()