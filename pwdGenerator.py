'''
TASK 3 : PASSWORD GENERATOR
'''

from tkinter import *
import random
import string


def generate_password():
    length = int(length_entry.get())
    complexity = ''


    #weak level password generation
    if choice.get() == 1:
        complexity = string.ascii_uppercase + string.digits

    #medium level password generation
    elif choice.get() == 2:
        complexity = string.ascii_letters + string.digits

    #strong level password generation
    elif choice.get() == 3:
        complexity = string.ascii_letters + string.punctuation + string.digits

    #if no complexity is provided by user ->  Ask user to specify
    if complexity == '':
        password.config(text = "Please select a complexity level.")

    #else generate the password
    else:
        pwd_generated = ''.join(random.choice(complexity) for i in range(length))
        password.config(text = f"Generated Password : {pwd_generated}")

pwdgen = Tk()
pwdgen.geometry('300x300')
pwdgen.config(bg='#E13D77')
pwdgen.title("Random Password Generator")


#to get input the length
length_label = Label(
    pwdgen,
    text = "Enter password length : "
)
length_label.pack(pady = 5)
length_entry = Entry(pwdgen)
length_entry.pack(pady = 10)

#to get the complexity level
choice = IntVar()
weak_level = Radiobutton(
    pwdgen,
    text = "WEAK",
    variable = choice,
    value = 1
)
weak_level.pack(pady = 5)

medium_level = Radiobutton(
    pwdgen,
    text = "MEDIUM",
    variable = choice,
    value = 2
)
medium_level.pack(pady = 5)

strong_level = Radiobutton(
    pwdgen,
    text = "STRONG",
    variable = choice,
    value = 3
)
strong_level.pack(pady = 10)

#generate button
gen_btn = Button(
    pwdgen,
    text = "Generate Password",
    command = generate_password
)
gen_btn.pack()

password = Label(pwdgen,text='')
password.pack(pady = 3)

pwdgen.mainloop()
