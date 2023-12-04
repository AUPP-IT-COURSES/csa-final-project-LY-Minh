import tkinter as tk


def caesar(text, shift, operation):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_list = []

    if not str(operation).lower() in ["e", "d"]:
        return "Invalid option"
    
    try:
        x = int(shift)
    except ValueError:
        return "Invalid shift number"
    
    if x <= 0 or x == 26:
        return "Invalid shift number"

    for letter in text:
        if letter.isalpha():
            y = alphabet.index(letter.lower())
            if str(operation).lower() == "e":
                z = alphabet[(y + x) % 26]
            else:
                z = alphabet[(y - x) % 26]
            new_list.append(z)
        else:
            new_list.append(letter)

    result = ''.join(new_list)
    return result

def encrypt_decrypt():
    text = entry_text.get()
    shift = entry_shift.get()
    operation = var.get()
    result = caesar(text, shift, operation)
    result_label.config(text="Result: " + result)

window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("800x800")

tk.Label(window, text="Enter Text:").pack()
entry_text = tk.Entry(window)
entry_text.pack()

tk.Label(window, text="Enter Shift:").pack()
entry_shift = tk.Entry(window)
entry_shift.pack()

tk.Label(window, text="Operation:").pack()
var = tk.StringVar(value="e")
tk.Radiobutton(window, text="Encrypt", variable=var, value="e").pack()
tk.Radiobutton(window, text="Decrypt", variable=var, value="d").pack()

tk.Button(window, text="Encrypt/Decrypt", command=encrypt_decrypt).pack()

result_label = tk.Label(window, text="Result: ")
result_label.pack()


window.mainloop()
