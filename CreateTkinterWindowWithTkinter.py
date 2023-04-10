from tkinter import *



class Main:
    def WindowSettings():
        global p

        p = Tk()
        p.title("Tkinter Settings")
        p.geometry("550x500+450+150")

        Main.Tools()

        p.mainloop()

    def Tools():
        MainTools()



class MainTools:
    def __init__(self):
        MainTools.LabelArea()
        MainTools.ButtonArea()
        MainTools.WindowConfigArea()
        MainTools.CreateWindow()


    def LabelArea():
        global AddLabel_Entry, AddLabel_PlaceXEntry, AddLabel_PlaceYEntry

        AddLabel_Label = Label(p,
                               text="Add Label :",
                               font=("arial",15,"bold"))
        AddLabel_Label.place(x = 10, y = 10)

        AddLabel_Entry = Entry(p,
                               font=("arial",10,"bold"), bd=5)
        AddLabel_Entry.place(x = 10, y = 45)

        AddLabel_PlaceXLabel = Label(p,
                                     text="X: ",
                                     font=("arial",14,"bold"))
        AddLabel_PlaceXLabel.place(x = 10, y = 75)

        AddLabel_PlaceXEntry = Entry(p,
                                     font=("arial",10,"bold"), bd=5, width=3)
        AddLabel_PlaceXEntry.place(x = 40, y = 75)

        AddLabel_PlaceYLabel = Label(p,
                                     text="Y: ",
                                     font=("arial",14,"bold"))
        AddLabel_PlaceYLabel.place(x = 80, y = 75)

        AddLabel_PlaceYEntry = Entry(p,
                                     font=("arial",10,"bold"), bd=5, width=3)
        AddLabel_PlaceYEntry.place(x = 110, y = 75)

        AddLabel_Button = Button(p,
                                 text="Add",
                                 font=("arial",15,"bold"),bd=4,command=MainToolsCommands.AddLabel,
                                 width=12, pady=0)
        AddLabel_Button.place(x = 8, y = 110)

        AddLabel_PlaceLeft = Button(p,
                                    text="L",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveLabelL)
        AddLabel_PlaceLeft.place(x = 20, y = 165)

        AddLabel_PlaceRight = Button(p,
                                    text="R",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveLabelR)
        AddLabel_PlaceRight.place(x = 55, y = 165)

        AddLabel_PlaceUp = Button(p,
                                    text="U",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveLabelU)
        AddLabel_PlaceUp.place(x = 90, y = 165)

        AddLabel_PlaceDown = Button(p,
                                    text="D",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveLabelD)
        AddLabel_PlaceDown.place(x = 125, y = 165)


    def ButtonArea():
        global AddButton_Entry, AddButton_PlaceXEntry, AddButton_PlaceYEntry

        AddButton_Label = Label(p,
                                text="Add Button: ",
                                font=("arial",15,"bold"))
        AddButton_Label.place(x = 350, y = 10)

        AddButton_Entry = Entry(p,
                               font=("arial",10,"bold"), bd=5)
        AddButton_Entry.place(x = 350, y = 45)

        AddButton_PlaceXLabel = Label(p,
                                     text="X: ",
                                     font=("arial",14,"bold"))
        AddButton_PlaceXLabel.place(x = 350, y = 75)

        AddButton_PlaceXEntry = Entry(p,
                                     font=("arial",10,"bold"), bd=5, width=3)
        AddButton_PlaceXEntry.place(x = 380, y = 75)

        AddButton_PlaceYLabel = Label(p,
                                     text="Y: ",
                                     font=("arial",14,"bold"))
        AddButton_PlaceYLabel.place(x = 420, y = 75)

        AddButton_PlaceYEntry = Entry(p,
                                     font=("arial",10,"bold"), bd=5, width=3)
        AddButton_PlaceYEntry.place(x = 450, y = 75)

        AddButton_Button = Button(p,
                                 text="Add",
                                 font=("arial",15,"bold"),bd=4,command=MainToolsCommands.AddButton,
                                  width=12, pady=0)
        AddButton_Button.place(x = 350, y = 110)

        AddButton_PlaceLeft = Button(p,
                                    text="L",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveButtonL)
        AddButton_PlaceLeft.place(x = 360, y = 165)

        AddButton_PlaceRight = Button(p,
                                    text="R",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveButtonR)
        AddButton_PlaceRight.place(x = 395, y = 165)

        AddButton_PlaceUp = Button(p,
                                    text="U",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveButtonU)
        AddButton_PlaceUp.place(x = 430, y = 165)

        AddButton_PlaceDown = Button(p,
                                    text="D",
                                    font=("arial",14,"bold"),bd=4,width=1,height=1,
                                    command=MainToolsCommands.MoveButtonD)
        AddButton_PlaceDown.place(x = 465, y = 165)


    def WindowConfigArea():
        global WConfig_TitleEntry, WConfig_GeometryEntry, WConfig_ResizableEntry

        WConfig_TitleLabel = Label(p,
                              text="Window Title: ",
                              font=("arial",14,"bold"))
        WConfig_TitleLabel.place(x = 10, y = 300)

        WConfig_TitleEntry = Entry(p,
                                   font=("arial",14,"bold"), bd=5, width=15)
        WConfig_TitleEntry.place(x = 140, y = 300)

        WConfig_GeometryLabel = Label(p,
                                       text="Window Geometry: ",
                                       font=("arial",14,"bold"))
        WConfig_GeometryLabel.place(x = 10, y = 340)

        WConfig_GeometryEntry = Entry(p,
                                       font=("arial",14,"bold"), bd=5, widt=10)
        WConfig_GeometryEntry.place(x = 190, y = 340)

        WConfig_ResizableLabel = Label(p,
                                       text="Resizable: ",
                                       font=("arial",14,"bold"))
        WConfig_ResizableLabel.place(x = 10, y = 380)

        WConfig_ResizableEntry = Entry(p,
                                       font=("arial",14,"bold"),bd=5,width=10)
        WConfig_ResizableEntry.place(x = 190, y = 380)
        WConfig_ResizableEntry.insert(0, "FALSE, FALSE")


    def CreateWindow():
        CreateWindow_Button = Button(p,
                                     text="Create Window",
                                     font=("arial",15,"bold"),
                                     bd=8,width=40,
                                     command=MainToolsCommands.CreateWindow)
        CreateWindow_Button.place(x = 18, y = 420)



class MainToolsCommands:
    def AddLabel():
        global new_label

        try:
            new_label = Label(p2,
                              text=AddLabel_Entry.get(),
                              font=("arial",14,"bold"))
            new_label.place(x = AddLabel_PlaceXEntry.get(), y = AddLabel_PlaceYEntry.get())

        except Exception:pass

    def MoveLabelR():
        try:
            new_label.place(x= (int(new_label.place_info()['x'])+1), y= (new_label.place_info()['y']))

        except Exception:pass
    def MoveLabelL():
        try:
            new_label.place(x= (int(new_label.place_info()['x'])-1), y= (new_label.place_info()['y']))

        except Exception:pass
    def MoveLabelU():
        try:
            new_label.place(x= (new_label.place_info()['x']), y= (int(new_label.place_info()['y'])-1))

        except Exception:pass
    def MoveLabelD():
        try:
            new_label.place(x= (new_label.place_info()['x']), y= (int(new_label.place_info()['y'])+1))

        except Exception:pass


    def AddButton():
        global new_button

        try:
            new_button = Button(p2,
                              text=AddButton_Entry.get(),
                              font=("arial", 14, "bold"))
            new_button.place(x=AddButton_PlaceXEntry.get(), y=AddButton_PlaceYEntry.get())

        except Exception:pass

    def MoveButtonR():
        try:
            new_button.place(x= (int(new_button.place_info()['x'])+1), y= (new_button.place_info()['y']))

        except Exception:pass
    def MoveButtonL():
        try:
            new_button.place(x= (int(new_button.place_info()['x'])-1), y= (new_button.place_info()['y']))

        except Exception:pass
    def MoveButtonU():
        try:
            new_button.place(x= (new_button.place_info()['x']), y= (int(new_button.place_info()['y'])-1))

        except Exception:pass
    def MoveButtonD():
        try:
            new_button.place(x= (new_button.place_info()['x']), y= (int(new_button.place_info()['y'])+1))

        except Exception:pass


    def CreateWindow():
        try:
            global p2

            p2 = Tk()
            p2.title(WConfig_TitleEntry.get())
            p2.geometry(WConfig_GeometryEntry.get())
            if(WConfig_ResizableEntry.get() == "FALSE, FALSE"):
                p2.resizable(FALSE, FALSE)
            elif(WConfig_ResizableEntry.get() == "TRUE, FALSE"):
                p2.resizable(TRUE, FALSE)
            elif(WConfig_ResizableEntry.get() == "TRUE, TRUE"):
                p2.resizable(TRUE, TRUE)
            elif(WConfig_ResizableEntry.get() == "FALSE, TRUE"):
                p2.resizable(FALSE, TRUE)

            p2.mainloop()

        except Exception:
            pass




if(__name__ == '__main__'):
    Main.WindowSettings()