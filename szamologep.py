import tkinter as tk
from math import sqrt

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Számológép")
        self.master.geometry("600x600")

        self.current_input = ""
        self.log = []

        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 1), ('8', 1, 2), ('9', 1, 3),
            ('4', 2, 1), ('5', 2, 2), ('6', 2, 3),
            ('1', 3, 1), ('2', 3, 2), ('3', 3, 3),
            ('0', 4, 1), ('+', 1, 4), ('-', 2, 4),
            ('*', 3, 4), ('/', 4, 4), ('^2', 4, 2),
            ('sqrt', 4, 3), ('(', 5, 1), (')', 5, 2),
            ('C', 5, 3), ('AC', 5, 4)
        ]

        for (text, row, col) in buttons:
            self.add_button(text, row, col)

        self.add_button('=', 4, 0, self.evaluate)

        self.add_button('Log', 2, 0, self.show_log)

    def add_button(self, text, row, col, command=None):
        if not command:
            btn = tk.Button(self.master, text=text, padx=40, pady=20, command=lambda: self.button_click(text))
        else:
            btn = tk.Button(self.master, text=text, padx=40, pady=20, command=command)
        btn.grid(row=row, column=col)

    def button_click(self, value):
        if value == "C":
            self.current_input = self.current_input[:-1]
        elif value == "AC":
            self.current_input = ""
        else:
            self.current_input += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)

    def evaluate(self):
        try:
            if '^2' in self.current_input:
                self.current_input = self.current_input.replace('^2', '**2')

            if 'sqrt' in self.current_input:
                self.current_input = self.current_input.replace('sqrt', 'sqrt(') + ')'

            result = str(eval(self.current_input))
            self.log.append(f"{self.current_input} = {result}")
            self.current_input = result

        except Exception as e:
            result = "Error"
            self.current_input = ""

        self.display.delete(0, tk.END)
        self.display.insert(0, result)

    def show_log(self):
        log_window = tk.Toplevel(self.master)
        log_window.title("Log")
        log_text = tk.Text(log_window, width=40, height=20)
        log_text.pack()

        for entry in self.log:
            log_text.insert(tk.END, entry + "\n")

root = tk.Tk()
calc = Calculator(root)
root.mainloop()