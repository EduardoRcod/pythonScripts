import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def GeneratePassword(minLength, numbers=True, specialCharacters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialCharacters:
        characters += special_chars

    password = ""
    requirements = False
    hasNumber = False
    hasSpecialCharacter = False

    while not requirements or len(password) < minLength:
        newChar = random.choice(characters)
        password += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special_chars:
            hasSpecialCharacter = True

        requirements = True
        if numbers:
            requirements = hasNumber
        if specialCharacters:
            requirements = requirements and hasSpecialCharacter
        
    return password

# Function to handle the password generation when the button is clicked
def generate_password():
    try:
        minLength = int(entry_minLength.get())
        hasNumber = var_numbers.get()
        hasSpecialCharacter = var_specialCharacters.get()
        password = GeneratePassword(minLength, hasNumber, hasSpecialCharacter)
        
        # Display the password in the output entry and copy to clipboard
        output_password.delete(0, tk.END)
        output_password.insert(0, password)
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Ensures clipboard is updated
        messagebox.showinfo("Password Generated", "The password has been copied to the clipboard!")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for minimum length.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Widgets for input and options
tk.Label(root, text="Minimum Length:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_minLength = tk.Entry(root)
entry_minLength.grid(row=0, column=1, padx=10, pady=10)

var_numbers = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

var_specialCharacters = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=var_specialCharacters).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)

# Output password entry (read-only for display)
tk.Label(root, text="Generated Password:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
output_password = tk.Entry(root, state="normal")
output_password.grid(row=3, column=1, padx=10, pady=10)

# Generate button
btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
