from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Put this sentence in a pop-up message box:
    # "If you find yourself having to cross a piranha-infested river, here's how to do it..."
    messagebox.showinfo( message = "If you find yourself having to cross a piranha-infested river here's how to do it...")
    # Get the player to enter an adjective
    adjetive = simpledialog.askstring(title='Greeter',prompt="Enter an adjetive")
    # Get the player to enter a type of liquid
    liquid = simpledialog.askstring(title='Greeter',prompt="Enter a type of liquid")
    # Get the player to enter a body part
    body_part = simpledialog.askstring(title='Greeter',prompt="Enter a body part")
    # Get the player to enter a verb
    verb = simpledialog.askstring(title='Greeter',prompt="Enter a verb")
    # Get the player to enter a place
    place = simpledialog.askstring(title='Greeter',prompt="Enter a place")
    # The story below has had been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        "Piranhas are more " + adjetive + " during the day, so cross the river at\n"
        "night. Piranhas are attracted to fresh " + liquid + " and will most\n"
        "likely take a bite out of your " + body_part + " if you " + verb + ". Whatever\n"
        "you do, if you have an open wound, try to find another way to get "
        "back to the " + place + " . Good luck!"
    )

    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up
    messagebox.showinfo(title="hello",message=story)
    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.

    # Run the window's .mainloop() method

    pass
