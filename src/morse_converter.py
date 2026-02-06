import tkinter as tk
from tkinter import messagebox
import time
import sys

# Sound support
if sys.platform.startswith("win"):
    import winsound
    def beep_dot():
        winsound.Beep(800, 150)

    def beep_dash():
        winsound.Beep(800, 400)
else:
    def beep_dot():
        root.bell()

    def beep_dash():
        root.bell()

# Morse dictionaries
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

reverse_morse_dict = {v: k for k, v in morse_dict.items()}

# Conversion logic
def text_to_morse(text):
    output = []
    invalid = set()

    for char in text.upper():
        if char == ' ':
            output.append('/')
        elif char in morse_dict:
            output.append(morse_dict[char])
        else:
            invalid.add(char)

    result = ' '.join(output)
    if invalid:
        result += f"\n\nIgnored characters: {', '.join(invalid)}"
    return result

def morse_to_text(morse):
    result = []
    words = morse.split(' / ')

    for word in words:
        letters = word.split()
        for l in letters:
            if l not in reverse_morse_dict:
                return f"Invalid Morse Code: {l}"
            result.append(reverse_morse_dict[l])
        result.append(' ')
    return ''.join(result).strip()

def play_morse_sound(morse):
    for symbol in morse:
        if symbol == '.':
            beep_dot()
        elif symbol == '-':
            beep_dash()
        time.sleep(0.15)

# Button actions
def convert_text():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Enter text")
        return
    result = text_to_morse(text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)
    play_morse_sound(result)

def convert_morse():
    morse = input_box.get("1.0", tk.END).strip()
    if not morse:
        messagebox.showwarning("Warning", "Enter Morse")
        return
    result = morse_to_text(morse)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

# GUI
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("560x450")
root.configure(bg="#121212")
root.resizable(False, False)

style_fg = "#E0E0E0"
style_bg = "#121212"
box_bg = "#1E1E1E"
btn_bg = "#2D2D2D"

tk.Label(root, text="Input", fg=style_fg, bg=style_bg, font=("Segoe UI", 12, "bold")).pack()
input_box = tk.Text(root, height=5, width=65, bg=box_bg, fg=style_fg, insertbackground="white")
input_box.pack(pady=6)

frame = tk.Frame(root, bg=style_bg)
frame.pack(pady=10)

tk.Button(frame, text="Text → Morse", width=18, bg=btn_bg, fg=style_fg, command=convert_text).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Morse → Text", width=18, bg=btn_bg, fg=style_fg, command=convert_morse).grid(row=0, column=1, padx=10)

tk.Label(root, text="Output", fg=style_fg, bg=style_bg, font=("Segoe UI", 12, "bold")).pack()
output_box = tk.Text(root, height=8, width=65, bg=box_bg, fg=style_fg)
output_box.pack(pady=6)

root.mainloop()
