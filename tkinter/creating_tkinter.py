'''To create a basic Tkinter GUI, follow these steps:

Import Tkinter: Start by importing the Tkinter module.
Create a Main Window: Create the main application window.
Add Widgets: Add various widgets to the window.
Run the Main Loop: Start the Tkinter event loop to display the window.
'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter GUI")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Start the Tkinter event loop
root.mainloop()
