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
    question = simpledialog.askstring
    correct = (title=" ", prompt= ' CORRECT!')
    #      // 2.  Ask the user a question 
    answer1 = simpledialog.askstring(title=" ", prompt="What is the name of an orange butterfly with black stripes on it's wings?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == "monarch":
        messagebox.showinfo(title=" ", prompt= ' CORRECT!')
        score = score + 1
    #      // 4.  if the user's answer was correct, add one to their score 
    else : score = score - 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer2 = question(title= '', prompt= 'What is the first color of the rainbow?')
    if answer2 == 'red' :
        question(correct)
        score = score + 1
    else : score = score - 1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
