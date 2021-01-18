import tkinter as tk

# sample: https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("test")
        self.master.geometry("400x300")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.create_menubar()

        #self.quit = tk.Button(self, text="QUIT", fg="red",
        #                      command=self.master.destroy)
        #self.quit.pack(side="bottom")

    def create_menubar(self):
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label="Open",command=lambda: print("Open"))
        self.filemenu.add_command(label="Save",command=lambda: print("save"))
        self.filemenu.add_command(label="Exit",command=lambda: print("exit"))
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.master.config(menu=self.menubar)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
