#build a calculator GUI using tkinter in python
import tkinter as tk 
def on_button_click(button_text):
    """
    Handles the click event for calculator buttons.

    This function processes the input from a button click in a calculator GUI.
    It clears the entry field if 'C' is pressed, evaluates the expression and displays
    the result if '=' is pressed, or appends the button text to the entry field otherwise.

    Args:
        button_text (str): The text of the button that was clicked (e.g., '1', '+', 'C', '=').

    Returns:
        None
    """
    if button_text == 'C':
        entry.delete(0, tk.END)
    elif button_text == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END) 
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, 'Error')  
    else:
        entry.insert(tk.END, button_text)   
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#2c2c2c')  # Dark background
root.resizable(False, False)
root.geometry("400x500")

entry = tk.Entry(root, width=16, font=('Courier New', 24, 'bold'), borderwidth=0, relief='flat',
                 bg='#1e1e1e', fg='white', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [ '7', '8', '9', '/',
            '4', '5', '6', '*',        
            '1', '2', '3', '-',
            '0', 'C', '=', '+' ]

for index, button_text in enumerate(buttons):   
    if button_text in ['/', '*', '-', '+', '=']:
        bg_color = '#ff9500'  # Orange for operators
        fg_color = 'white'
    elif button_text == 'C':
        bg_color = '#a6a6a6'  # Gray for clear
        fg_color = 'black'
    else:
        bg_color = '#333333'  # Dark gray for numbers
        fg_color = 'white'
    
    button = tk.Button(root, text=button_text, width=6, height=3, font=('Arial', 18, 'bold'),
                       bg=bg_color, fg=fg_color, borderwidth=0, relief='raised',
                       activebackground='#555555', activeforeground=fg_color,
                       command=lambda bt=button_text: on_button_click(bt))
    button.grid(row=(index // 4) + 1, column=index % 4, padx=5, pady=5) 

root.mainloop() 
