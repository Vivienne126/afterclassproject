from tkinter import *
window=Tk()
window.title("Length Converter")
window.geometry("400x400")

def cvt():
    inches=float(entry.get())
    global cm
    cm=inches*2.54

label=Label(window , text="Enter inches")
label.pack()

entry=Entry(window)
entry.pack()

btn=Button(window , text="Convert" , command=cvt)
btn.pack()

result=Label(window , text="CM=" + str(cm))
result.pack()

window.mainloop()