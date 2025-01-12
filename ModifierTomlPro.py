# MIT License
#
# Copyright (c) 2025 Tu Nombre o el nombre de tu organización
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import toml

# Global variable to store the loaded configuration
config = {}

def load_config():
    """Load the TOML file from the specified path."""
    global config  # Using the global variable
    file_path = file_path_var.get()
    if file_path:
        try:
            progress_window = show_progress_bar()  # Show the progress bar while loading
            with open(file_path, "r") as file:
                config = toml.load(file)
                generate_tabs(config)
                messagebox.showinfo("Success", "File loaded successfully.")  # Success message
            progress_window.destroy()  # Close progress window after loading
        except Exception as e:
            progress_window.destroy()
            messagebox.showerror("Error", f"Could not open the file: {e}")  # Error message
    else:
        messagebox.showerror("Error", "Please enter a valid path.")  # Error message

def save_config():
    """Save the changes made to the TOML file."""
    global config  # Using the global variable
    file_path = file_path_var.get()
    if file_path:
        try:
            # Save changes to the TOML file
            for key, var in input_vars.items():
                section, option = key.split(".")
                config[section][option] = (
                    True if var.get() == "true" else 
                    False if var.get() == "false" else 
                    var.get()
                )
            with open(file_path, "w") as file:
                toml.dump(config, file)  # Write the updated config to the TOML file
            messagebox.showinfo("Success", "Configuration saved successfully.")  # Success message
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the file: {e}")  # Error message
    else:
        messagebox.showerror("Error", "Please select a TOML file.")  # Error message

def browse_file():
    """Open a file dialog to select a TOML file."""
    file_path = filedialog.askopenfilename(filetypes=[("TOML Files", "*.toml")])
    if file_path:
        file_path_var.set(file_path)  # Set the file path variable

def generate_tabs(config):
    """Generate tabs for each section in the TOML file."""
    global input_vars
    input_vars = {}

    # Clear previous tabs
    for tab in notebook.tabs():
        notebook.forget(tab)

    # Dynamically generate tabs for each section
    for section, values in config.items():
        tab_frame = ttk.Frame(notebook)  # Create a frame for each tab
        notebook.add(tab_frame, text=section)  # Add the frame as a tab

        # Create the Canvas and scrollbar
        canvas = tk.Canvas(tab_frame)
        scrollbar = ttk.Scrollbar(tab_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Create a Frame inside the Canvas
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Update the size of the canvas when the content changes size
        frame.bind("<Configure>", lambda e, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create content inside each tab
        section_label = tk.Label(frame, text=f"[{section}]", font=("Arial", 12, "bold"))
        section_label.pack(anchor="w", pady=5)

        for key, value in values.items():
            if isinstance(value, bool):
                var = tk.StringVar(value="true" if value else "false")
                checkbox = ttk.Checkbutton(frame, text=key, variable=var, onvalue="true", offvalue="false")
                checkbox.pack(anchor="w", padx=10, pady=5)
            else:
                var = tk.StringVar(value=str(value))
                entry_label = tk.Label(frame, text=key, font=("Arial", 10))
                entry_label.pack(anchor="w", padx=10, pady=5)
                entry = tk.Entry(frame, textvariable=var, width=40)
                entry.pack(anchor="w", padx=10, pady=5)

            input_vars[f"{section}.{key}"] = var

def show_progress_bar():
    """Show a progress bar when loading large files."""
    progress_window = tk.Toplevel(root)
    progress_window.title("Loading...")
    progress_window.geometry("300x100")
    progress_window.config(bg="#2C3E50")
    
    progress_label = tk.Label(progress_window, text="Loading Configuration...", bg="#2C3E50", fg="white", font=("Arial", 12))
    progress_label.pack(pady=10)
    
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=250, mode="indeterminate")
    progress_bar.pack(pady=10)
    progress_bar.start()

    progress_window.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
    return progress_window

# Create the main window
root = tk.Tk()
root.title("Advanced TOML Modifier")  # Title of the window
root.geometry("1280x720")  # Adjusted window size
root.config(bg="#2C3E50")  # Dark background for the window

# Style for buttons and entries
style = ttk.Style()
style.configure("TButton", background="#3498DB", foreground="white", font=("Arial", 10, "bold"), padding=10)
style.map("TButton", background=[("active", "#2980B9")])
style.configure("TEntry", font=("Arial", 10), padding=5)

# Variable for the file path
file_path_var = tk.StringVar()

# Field for entering or selecting the file
file_frame = tk.Frame(root, bg="#2C3E50")
file_frame.pack(pady=20)
file_entry = tk.Entry(file_frame, textvariable=file_path_var, width=50, font=("Arial", 10), bd=2, relief="solid")
file_entry.pack(side="left", padx=5)
browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
browse_button.pack(side="left", padx=5)

# Load and save buttons
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)
load_button = tk.Button(button_frame, text="Load Configuration", command=lambda: load_config())
load_button.pack(side="left", padx=5)
save_button = tk.Button(button_frame, text="Save Changes", command=save_config)
save_button.pack(side="left", padx=5)

# Create a notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(pady=20, padx=20, fill="both", expand=True)

# Dictionary to store input variables
input_vars = {}

root.mainloop()
