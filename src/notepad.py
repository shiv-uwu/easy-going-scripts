# ---------------- #
# MADE BY SHIV-UWU #
# ---------------- #

import os  # Used to get the basename of the file.
import tkinter as tk  # Used to create the GUI.
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo


def new_file():
    global file_path  # Use the global variable file_path.
    root.title("Untitled - Notepad")  # Set the title of the window.
    file_path = None  # Reset the file path.
    text_area.delete("1.0", tk.END)  # Delete all the text in the text area.


def open_file():
    global file_path  # Use the global variable file_path.
    file_path = askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )  # Open the file dialog.
    if not file_path:  # If the file path is empty, return.
        return
    # Set the title of the window.
    root.title(os.path.basename(file_path) + " - Notepad")
    text_area.delete("1.0", tk.END)  # Delete all the text in the text area.
    with open(file_path, "r") as file:  # Open the file.
        # Insert the text into the text area.
        text_area.insert("1.0", file.read())


def save_file():
    global file_path  # Use the global variable file_path.
    if not file_path:  # If the file path is empty, ask the user to save the file.
        file_path = asksaveasfilename(
            initialfile="Untitled.txt",
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
        )  # Open the file dialog.
        if not file_path:  # If the file path is empty, return.
            return
    with open(file_path, "w") as file:  # Open the file.
        file.write(text_area.get("1.0", tk.END))  # Write the text to the file.
        # Set the title of the window.
        root.title(os.path.basename(file_path) + " - Notepad")


def quit_app():
    root.destroy()  # Destroy the window.


def cut_text():
    text_area.event_generate("<<Cut>>")  # Generate the cut event.


def copy_text():
    text_area.event_generate("<<Copy>>")  # Generate the copy event.


def paste_text():
    text_area.event_generate("<<Paste>>")  # Generate the paste event.


def show_about():
    showinfo("Notepad", "Notepad by shiv-uwu on github"
             "\n\nMade with tkinter and os module")  # Show the about dialog.


if __name__ == "__main__":
    root = tk.Tk()  # Create the window.
    root.title("Untitled - Notepad")  # Set the title of the window.
    root.geometry("1920x1080")  # Set the size of the window.
    file_path = None    # Create the global variable file_path.

    text_area = tk.Text(root, font="lucida 13")  # Create the text area.
    text_area.pack(expand=True, fill="both")   # Pack the text area.

    menu_bar = tk.Menu(root)   # Create the menu bar.

    file_menu = tk.Menu(menu_bar, tearoff=0)  # Create the file menu.
    # Add the new file command.
    file_menu.add_command(label="New", command=new_file)
    # Add the open file command.
    file_menu.add_command(label="Open", command=open_file)
    # Add the save file command.
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()  # Add a separator.
    # Add the exit command.
    file_menu.add_command(label="Exit", command=quit_app)
    # Add the file menu to the menu bar.
    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu_bar, tearoff=0)    # Create the edit menu.
    # Add the cut command.
    edit_menu.add_command(label="Cut", command=cut_text)
    # Add the copy command.
    edit_menu.add_command(label="Copy", command=copy_text)
    # Add the paste command.
    edit_menu.add_command(label="Paste", command=paste_text)
    # Add the edit menu to the menu bar.
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    help_menu = tk.Menu(menu_bar, tearoff=0)   # Create the help menu.
    # Add the about command.
    help_menu.add_command(label="About Notepad", command=show_about)
    # Add the help menu to the menu bar.
    menu_bar.add_cascade(label="Help", menu=help_menu)

    root.config(menu=menu_bar)  # Configure the menu bar.

    scroll_bar = tk.Scrollbar(text_area)   # Create the scroll bar.
    scroll_bar.pack(side="right", fill="y")  # Pack the scroll bar.
    scroll_bar.config(command=text_area.yview)  # Configure the scroll bar.
    text_area.config(yscrollcommand=scroll_bar.set)  # Configure the text area.

    root.mainloop()  # Run the window.
