import tkinter as tk
from quadratic_solver_package.quadratic_solver import solve_quadratic

def solve_and_display():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    roots = solve_quadratic(a, b, c)
    if roots:
        root1, root2 = roots
        result_label.config(text=f"Root 1: {root1}, Root 2: {root2}")
    else:
        result_label.config(text="No real roots")

root = tk.Tk()
root.title("Quadratic Solver")

label_a = tk.Label(root, text="a:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text="b:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

label_c = tk.Label(root, text="c:")
label_c.grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

solve_button = tk.Button(root, text="Solve", command=solve_and_display)
solve_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
