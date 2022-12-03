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

# ------------------------------ Products List ----------------------------------#
food_list = ["Chicken", "Lamb", "Salmon", "Hake", "Kebabs", "Pizza", "Chinese", "Fish"]
drinks_list = ["Lemonade", "Soda", "Juice", "Cola", "Wine1", "Wine2", "Beer1", "Beer2"]
dessert_list = ["Ice cream", "Fruit", "Brownies", "Pudding", "Cheesecake", "Cake1", "Cake2", "Cake3"]

# Create food items
food_items = []
food_box = []
food_text = []
food_counter = 0

for food in food_list:

    # Create checkboxes
    food_items.append("")
    food_items[food_counter] = tkinter.IntVar()
    food_checkbox = tkinter.Checkbutton(food_panel,
                                        text=food.title(),
                                        font=("Dosis", 19),
                                        onvalue=1,
                                        offvalue=0,
                                        variable=food_items[food_counter])
    food_checkbox.grid(row=food_counter, column=0, sticky=tkinter.W)

    # Create Input boxes
    food_box.append("")
    food_text.append("")
    food_text[food_counter] = tkinter.StringVar()
    food_text[food_counter].set('0')

    food_box[food_counter] = tkinter.Entry(food_panel,
                                           font=("Dosis", 19),
                                           bd=1,
                                           width=6,
                                           state=tkinter.DISABLED,
                                           textvariable=food_text[food_counter])
    food_box[food_counter].grid(row=food_counter, column=1)

    food_counter += 1

# Create drink items
drink_items = []
drink_box = []
drink_text = []
drink_counter = 0

for drink in drinks_list:

    # Create checkboxes
    drink_items.append("")
    drink_items[drink_counter] = tkinter.IntVar()
    drink_checkbox = tkinter.Checkbutton(drink_panel,
                                         text=drink.title(),
                                         font=("Dosis", 19),
                                         onvalue=1,
                                         offvalue=0,
                                         variable=drink_items[drink_counter])
    drink_checkbox.grid(row=drink_counter, column=0, sticky=tkinter.W)

    # Create Input boxes
    drink_box.append("")
    drink_text.append("")
    drink_text[drink_counter] = tkinter.StringVar()
    drink_text[drink_counter].set('0')

    drink_box[drink_counter] = tkinter.Entry(drink_panel,
                                             font=("Dosis", 19),
                                             bd=1,
                                             width=6,
                                             state=tkinter.DISABLED,
                                             textvariable=drink_text[drink_counter])
    drink_box[drink_counter].grid(row=drink_counter, column=1)

    drink_counter += 1

# Create dessert items
dessert_items = []
dessert_box = []
dessert_text = []
dessert_counter = 0

for dessert in dessert_list:

    # Create checkboxes
    dessert_items.append("")
    dessert_items[dessert_counter] = tkinter.IntVar()
    dessert_checkbox = tkinter.Checkbutton(dessert_panel,
                                           text=dessert.title(),
                                           font=("Dosis", 19),
                                           onvalue=1,
                                           offvalue=0,
                                           variable=dessert_items[dessert_counter])
    dessert_checkbox.grid(row=dessert_counter, column=0, sticky=tkinter.W)

    # Create Input boxes
    dessert_box.append("")
    dessert_text.append("")
    dessert_text[dessert_counter] = tkinter.StringVar()
    dessert_text[dessert_counter].set('0')

    dessert_box[dessert_counter] = tkinter.Entry(dessert_panel,
                                                 font=("Dosis", 19),
                                                 bd=1,
                                                 width=6,
                                                 state=tkinter.DISABLED,
                                                 textvariable=dessert_text[dessert_counter])
    dessert_box[dessert_counter].grid(row=dessert_counter, column=1)

    dessert_counter += 1

application.mainloop()
