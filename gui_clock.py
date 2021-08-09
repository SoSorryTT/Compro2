import tkinter as tk
import tkinter.ttk as ttk
from datetime import date
from datetime import datetime
 
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x100")
        self.style = ttk.Style()
        self.style.configure(".",font=("Arial",24))
        #day
        self.str_date = tk.StringVar()
        self.str_time = tk.StringVar()
        self.date = ttk.Label(self, textvariable=self.str_date)
        self.date.pack()
        #time
        self.time = ttk.Label(self, textvariable=self.str_time)
        self.update_time()
        self.time.pack()
        #quit
        self.btnQuit = tk.Button(self, text="Quit", command=self.destroy)
        self.btnQuit.pack()

    def update_time(self):
        self.str_date.set(str(date.today().strftime("%d %B, %Y")))
        self.str_time.set(str(datetime.now().strftime("%H:%M:%S")))
        self.time.after(1000,self.update_time)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
