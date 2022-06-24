import tkinter as tk
import tkinter.ttk as ttk
import time

#setting up the window
window = tk.Tk()
label = tk.Label(text = 'Progress Bar', width = 10, height = 1, fg = 'yellow', bg = 'purple')
label.pack()
button = tk.Button(text = 'OK', command = window.quit).pack()


#updating percent with new text. the widget gets updated when the stringvar variable changes
percent = tk.StringVar()

#creating the progress bar
bar = ttk.Progressbar(window, orient = 'horizontal', length = 300)
bar.pack(pady = 20)

percentLabel = tk.Label(window, textvariable = percent).pack()

#progress bar growing
tasks = 10
x = 0
while x<tasks:
    time.sleep(1) #delay
    bar['value'] += 10
    x += 1
    percent.set(str(int((x/tasks)*100)) + '%')
    window.update_idletasks() #updating the window each time to see the gradual progress

#popup window when the analysis is done:
if bar['value'] == 100:
    window_2 = tk.Tk()
    label2 = tk.Label(window_2, text = 'Analysis Done!', width = 50, height = 10, fg = 'yellow', bg = 'purple')
    label2.pack()
    button2 = tk.Button(window_2, text = 'OK', command = window_2.quit).pack()
    
    

window.mainloop()
exit(0)


