import re
import tkinter as tk
from tkinter import filedialog, messagebox

def clean_text(text):
    """
    Removes special characters from the text, leaving only plain text. including underscores.
    """
    # Regular expression to remove all characters except letters, digits, spaces, and basic punctuation.
    return re.sub(r'[^\w\s.,!?\'"-]|_', '', text)

def load_file():
    """
    Allows the user to select a text file, cleans the text, and saves the result to a new file.
    """
    # Open a file dialog to select a text file
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not filepath:
        return  # User canceled the selection
    
    # Read the file content
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
    
    # Clean the text
    cleaned_text = clean_text(text)
    
    # Save the cleaned text to a new file
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        with open(save_path, "w", encoding="utf-8") as output_file:
            output_file.write(cleaned_text)
        messagebox.showinfo("Success", f"Cleaned text saved to: {save_path}")

def clean_from_input():
    """
    Cleans the text entered by the user in the input box.
    """
    # Get the text from the input text box
    input_text = text_input.get("1.0", tk.END)
    # Clean the text
    cleaned_text = clean_text(input_text)
    # Display the cleaned text in the output text box
    text_output.config(state=tk.NORMAL)  # Enable editing temporarily
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", cleaned_text)
    text_output.config(state=tk.DISABLED)  # Make it read-only again

# Create the main Tkinter window
root = tk.Tk()
root.title("Text Cleaner")

# Button to load and clean a file
file_button = tk.Button(root, text="Load and Clean File", command=load_file)
file_button.pack(pady=10)

# Input area for entering or pasting text
text_input_label = tk.Label(root, text="Enter or paste text:")
text_input_label.pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=5)

# Add a scroll bar for the input area
input_scrollbar = tk.Scrollbar(root, command=text_input.yview)
input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_input.config(yscrollcommand=input_scrollbar.set)

# Button to clean the text entered in the input box
clean_button = tk.Button(root, text="Clean Input Text", command=clean_from_input)
clean_button.pack(pady=10)

# Output area to display the cleaned text
text_output_label = tk.Label(root, text="Cleaned text:")
text_output_label.pack()
text_output = tk.Text(root, height=10, width=50, state=tk.DISABLED)  # Make it read-only
text_output.pack(pady=5)

# Add a scroll bar for the output area
output_scrollbar = tk.Scrollbar(root, command=text_output.yview)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_output.config(yscrollcommand=output_scrollbar.set)

# Run the Tkinter main loop
root.mainloop()
