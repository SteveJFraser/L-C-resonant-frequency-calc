
from math import sqrt
from PIL import ImageTk, Image
import tkinter as tk


def calculate(*args):
    """
    for more info, check out the website for an online calculator
    https://www.omnicalculator.com/physics/resonant-frequency-lc
    this is the calculator i test my calculator with
    """
    PI = 3.14159265359
    induct = float(inductance.get()) * 10 ** -6  # microhenry
    cap = float(capacitance.get()) * 10 ** -12  # picofarads
    resonance_formula = 1/(2 * PI * sqrt(induct*cap))
    out_label.config(text=f"Resonant Frequency: {resonance_formula* 10 ** -6:.4f} MHz")
        
        
root = tk.Tk()
root.geometry("400x350")
inductance = tk.StringVar()
capacitance = tk.StringVar()
circuit_image = Image.open("LC-Circuit.png")
circuit_image = circuit_image.resize((230, 140), Image.ANTIALIAS)
render = ImageTk.PhotoImage(circuit_image)

l_label = tk.Label(root, text="Inductance µH: ", font=("ARIAL", 15))
l_label.pack()

l_entry = tk.Entry(root, textvariable=inductance)
l_entry.pack()
l_entry.focus()

c_label = tk.Label(root, text="Capacitance pF: ", font=("ARIAL", 15))
c_label.pack()

c_entry = tk.Entry(root, textvariable=capacitance)
c_entry.pack()

calc_btn = tk.Button(root,text="Calculate", command=calculate, font=("ARIAL", 12))
calc_btn.pack()

img = tk.Label(root, image=render)
img.pack()
out_label = tk.Label(root, font=("ARIAL", 15))
out_label.pack()

root.bind("<Return>", calculate)
root.mainloop()