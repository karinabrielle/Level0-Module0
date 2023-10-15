from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':


    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    #      // 2.  Ask the user a question 
    answer1 = simpledialog.askstring(title=" ", prompt="What is the name of an orange butterfly with black stripes on it's wings?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == "monarch":
        messagebox.showinfo(title=" ", message= ' CORRECT!')
        score = score + 1
    #      // 4.  if the user's answer was correct, add one to their score 
    else :
        score = score - 1
        messagebox.showinfo(title=" ", message='SORRY, INCORRECT!')
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer2 = simpledialog.askstring(title= '', prompt= 'What is the first color of the rainbow?')
    if answer2 == 'red' :
        messagebox.showinfo(title=" ", message= ' CORRECT!')
        score = score + 1
    else :
        score = score - 1
        messagebox.showinfo(title=" ", message='SORRY, INCORRECT!')
    answer3 = simpledialog.askstring(title = '', prompt= 'What is the most quickest and fastest land animal on earth?')
    if answer3 == 'cheatah' :
        messagebox.showinfo(title=" ", message= ' CORRECT!')
        score = score + 1
    else :
        messagebox.showinfo(title=" ", message= 'SORRY, INCORRECT!')
        score = score - 1
    answer4 = simpledialog.askstring(title= '', prompt= 'Is chess a sport?')
    if answer4 == 'yes':
        messagebox.showinfo(title=" ", message= ' CORRECT!')
        score = score + 1
    else:
        messagebox.showinfo(title=" ", message= 'SORRY, INCORRECT!')
        score = score - 1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(title="", message="Here is your score :"
    "(tap the ok button to see your score!)")
    messagebox.showinfo(title="", message= score)
    # Run the window's .mainloop() method

