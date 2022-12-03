# Restaurant Manager
import tkinter

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

application.mainloop()
