# Restaurant Manager
import tkinter

# ---------------------------- Window Setup ---------------------------------#
# Initialize window
application = tkinter.Tk()

# Application size
# +50+50 tells the location at which the window should show up
# First + is the x-axis from top left corner and second + is the y-axis from top left corner
# x moves to the right and y moves down (pixels specified after +)
application.geometry("1020x630+50+50")

# Prevent resizing the window
application.resizable(False, False)

# Window title
application.title("My Restaurant - Invoicing System")

# Window background color
application.config(bg="burlywood")

# ---------------------------- Panels Setup ---------------------------------#

# ------------------------------ Top Panel ----------------------------------#
top_panel = tkinter.Frame(application, bd=1, relief=tkinter.FLAT)
top_panel.pack(side=tkinter.TOP)

# Title for Top Panel
top_panel_title = tkinter.Label(top_panel,
                                text="Invoicing System",
                                fg="azure4",
                                font=("Dosis", 50),
                                bg="burlywood",
                                width=27)
top_panel_title.grid(row=0, column=0)

# ------------------------------ Left Panel ----------------------------------#
# Left panel
left_panel = tkinter.Frame(application, bd=1, relief=tkinter.FLAT)
left_panel.pack(side=tkinter.LEFT)

# Cost panel
cost_panel = tkinter.Frame(left_panel, bd=1, relief=tkinter.FLAT)
cost_panel.pack(side=tkinter.BOTTOM)

# Food panel
food_panel = tkinter.LabelFrame(left_panel,
                                text="Food",
                                fg="azure4",
                                font=("Dosis", 19),
                                bd=1,
                                relief=tkinter.FLAT)
food_panel.pack(side=tkinter.LEFT)

# Drink panel
drink_panel = tkinter.LabelFrame(left_panel,
                                 text="Drinks",
                                 fg="azure4",
                                 font=("Dosis", 19),
                                 bd=1,
                                 relief=tkinter.FLAT)
drink_panel.pack(side=tkinter.LEFT)

# Dessert panel
dessert_panel = tkinter.LabelFrame(left_panel,
                                   text="Desserts",
                                   fg="azure4",
                                   font=("Dosis", 19),
                                   bd=1,
                                   relief=tkinter.FLAT)
dessert_panel.pack(side=tkinter.LEFT)

# ------------------------------ Right Panel ----------------------------------#
right_panel = tkinter.Frame(application, bd=1, relief=tkinter.FLAT)
right_panel.pack(side=tkinter.RIGHT)

# Calculator panel
calculator_panel = tkinter.Frame(right_panel, bd=1, relief=tkinter.FLAT, bg="burlywood")
calculator_panel.pack()

# Invoice panel
invoice_panel = tkinter.Frame(right_panel, bd=1, relief=tkinter.FLAT, bg="burlywood")
invoice_panel.pack()

# Button panel
button_panel = tkinter.Frame(right_panel, bd=1, relief=tkinter.FLAT, bg="burlywood")
button_panel.pack()

application.mainloop()
