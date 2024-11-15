# Tkinter library ko import karte hain GUI banane ke liye
import tkinter as tk
import math  # Math library ko import karte hain advanced operations ke liye

# Main window create karte hain calculator ke liye
root = tk.Tk()
root.title("Advanced Calculator")  # Window ka title set karte hain
root.geometry("400x600")  # Window size set karte hain

# Display variable jisme hum input aur result show karenge
display_var = tk.StringVar()

# Display area banate hain jaha calculations aur result dikhaye jayenge
display_entry = tk.Entry(root, textvariable=display_var, font=('Arial', 24), bd=8, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Button click hone par value display me add karenge
def btn_click(item):
    current = display_var.get()
    display_var.set(current + str(item))

# Clear button ka function jo display ko reset karega
def btn_clear():
    display_var.set("")

# Equal button ka function jo expression ko evaluate karega
def btn_equal():
    try:
        result = str(eval(display_var.get()))  # eval() function ka use karte hain expression evaluate karne ke liye
        display_var.set(result)
    except:
        display_var.set("Error")  # Agar error ho to "Error" display karte hain

# Kuch advanced operations ke liye functions banate hain
def btn_sqrt():
    try:
        result = str(math.sqrt(float(display_var.get())))  # Square root function
        display_var.set(result)
    except:
        display_var.set("Error")

def btn_square():
    try:
        result = str(float(display_var.get()) ** 2)  # Square calculation
        display_var.set(result)
    except:
        display_var.set("Error")

def btn_power():
    try:
        base, exponent = map(float, display_var.get().split('^'))  # Base aur exponent ko split aur float me convert karte hain
        result = str(base ** exponent)  # Power calculate karte hain
        display_var.set(result)
    except:
        display_var.set("Error")

# Button layout ke liye buttons banate hain
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('sqrt', 5, 1), ('x^2', 5, 2), ('x^y', 5, 3)
]

# Sabhi buttons ke liye loop chalaate hain aur buttons create karte hain
for (text, row, col) in button_texts:
    if text == '=':
        # Equal button ke liye alag se function bind karte hain
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=btn_equal)
    elif text == 'C':
        # Clear button ke liye alag se function bind karte hain
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=btn_clear)
    elif text == 'sqrt':
        # Square root button ke liye function bind karte hain
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=btn_sqrt)
    elif text == 'x^2':
        # Square button ke liye function bind karte hain
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=btn_square)
    elif text == 'x^y':
        # Power button ke liye function bind karte hain
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda: btn_click('^'))
    else:
        # Baki sabhi numeric aur basic operation buttons ke liye
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: btn_click(t))
    button.grid(row=row, column=col)  # Grid me button place karte hain

# GUI main loop start karte hain
root.mainloop()
