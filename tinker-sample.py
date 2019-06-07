from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit, relief=RIDGE, padx="50", pady="50")
        self.button.pack(side=TOP)
        self.sheet_view_button = Button(frame, text="SHEET", fg="black", command=self.view_sheet, padx="50", pady="50")
        self.sheet_view_button.pack(side=LEFT)
        self.log_button = Button(frame, text="LOG", fg="black", command=self.log_hours, padx="50", pady="50")
        self.log_button.pack(side=LEFT)
        self.profile_button = Button(frame, text="PROFILE", fg="black", command=self.lookup_profile, padx="50", pady="50")
        self.profile_button.pack(side=RIGHT)
        self.gross_pay_button = Button(frame, text="GROSS PAY", fg="black", command=self.calc_gross_pay, padx="50", pady="50")
        self.gross_pay_button.pack(side=RIGHT)
        self.hours_button = Button(frame, text="HOURS", fg="black", command=self.hours_from_date, padx="50", pady="50")
        self.hours_button.pack(side=LEFT)
        # self.hi_there = Button(frame, text="Hello there", command=self.say_hi)
        # self.hi_there.pack()
    # def say_hi(self):
    #     print('hi there, everyone!')
    def view_sheet(self):
        return
    def log_hours(self):
        return
    def lookup_profile(self):
        return
    def calc_gross_pay(self):
        return
    def hours_from_date(self):
        return
root = Tk()
app = App(root)
root.mainloop()