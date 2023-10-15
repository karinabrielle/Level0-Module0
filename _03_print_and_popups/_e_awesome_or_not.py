from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randint(0, 3)
    something = random.randint(0, 3)
    # 2. Print your variable to the console
    print(something)
    # 3. Get the user to enter something that they think is awesome
    answer = simpledialog.askstring(title="", prompt="Enter something that you think is awsome!")
    # 4. If your variable is  0
    if something == 0 :
        messagebox.showinfo(title="", message='What you entered is so awsome!!!')
        # -- tell the user whatever they entered is awesome!

    # 5. If your variable is  1
    if something == 1 :
        messagebox.showinfo(title="", message='What you entered is ok.')
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
    if something == 2 :
        messagebox.showinfo(title="", message='What you entered is boring.')
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
    if something == 3 :
        messagebox.showinfo(title="", message='What you entered is...-- * meanwhile there is an explosion.')
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
