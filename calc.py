from tkinter import*

def click(event):
    global calcvalue
    text = event.widget.cget("text")

    if text == "=":
        if calcvalue.get().isdigit():
            value = int(calcvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)

                value = "Error"
                
                # calcvalue.set("Error")
                # screen.update()


        calcvalue.set(value)
        screen.update()

    elif text == "C":
        calcvalue.set.set("")
        screen.update()

    else:
        calcvalue.set(calcvalue.get()+ text)
        screen.update()



root = Tk()

root.geometry("350x700")
calcvalue = StringVar()
calcvalue.set("")
screen = Entry(root, textvar=calcvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=18,padx=12, pady=10)

frame1 = Frame(root, bg="grey")
button = Button(frame1, text="9" ,padx=6, pady=4, font="lucida 35 bold")    

button.pack(side=LEFT ,padx=12, pady=12)
button.bind("<Button-1>", click)

button = Button(frame1, text="8" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame1, text="7" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT,padx=10,pady=8)
button.bind("<Button-1>", click)



frame1.pack()


frame1 = Frame(root, bg="grey")
button = Button(frame1, text="6" ,padx=6, pady=4, font="lucida 35 bold")    

button.pack(side=LEFT ,padx=12, pady=12)
button.bind("<Button-1>", click)

button = Button(frame1, text="5" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame1, text="4" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT,padx=10,pady=8)
button.bind("<Button-1>", click)



frame1.pack()





frame1 = Frame(root, bg="grey")
button = Button(frame1, text="3" ,padx=6, pady=4, font="lucida 35 bold")    

button.pack(side=LEFT ,padx=12, pady=12)
button.bind("<Button-1>", click)

button = Button(frame1, text="2" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame1, text="1" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT,padx=10,pady=8)
button.bind("<Button-1>", click)



frame1.pack()


frame1 = Frame(root, bg="grey")
button = Button(frame1, text="-" ,padx=8, pady=4, font="lucida 35 bold")    

button.pack(side=LEFT ,padx=14, pady=6)
button.bind("<Button-1>", click)

button = Button(frame1, text="0" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame1, text="+" ,padx=5.5, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT,padx=10,pady=8)
button.bind("<Button-1>", click)



frame1.pack()



frame1 = Frame(root, bg="grey")
button = Button(frame1, text="*" ,padx=8, pady=4, font="lucida 35 bold")    

button.pack(side=LEFT ,padx=12, pady=12)
button.bind("<Button-1>", click)

button = Button(frame1, text="/" ,padx=12, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame1, text="=" ,padx=6, pady=4, font="lucida 35 bold")    
button.pack(side=LEFT,padx=12,pady=8)
button.bind("<Button-1>", click)



frame1.pack()




root.mainloop()