from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username= user.get()
    code= password.get()

    if username== 'Pujan' and  code=='lkjp':
        screen= Toplevel(root)
        screen.title("App")
        screen.geometry('92x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello Pujan', bg='white', font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()
    elif username!= 'Pujan' and code !='lkjp':
        messagebox.showerror("Invalid","Invalid username and password")
    elif code!= 'lkjp':
        messagebox.showerror("Invalid","Invalid password")

frame= Frame(root,width=350, height=350, bg='#fff')
frame.place(x=480,y=70)

heading= Label(frame, text='Sign in', fg='blue',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)


#####================INPUT USER+===================

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name= user.get()
    if name == ' ':
        user.insert(0, 'Username')
user = Entry(frame,width=25, fg='black', border=2, bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=209, height=2, bg='black').place(x=27, y=107)
#######=========================================================

#####================INPUT Password+===================
def on_enter(e):
    password.delete(0, 'end')

def on_leave(e):
    name = password.get()
    if name == ' ':
        password.insert(0,'password')

password = Entry(frame,width=25, fg='black', border=2, bg='white',font=('Microsoft YaHei UI Light',11))
password.place(x=30,y=157)
password.insert(0, 'Password')

password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)



Frame(frame,width=209, height=2, bg='black').place(x=27, y=187)
#######=========================================================

Button(frame,width=28,pady=7, text='sign in', bg='#57a1f8',fg='white',border=0, command= signin).place(x= 30, y=250)

label= Label(frame, text="Don't have an account?", fg='black',bg='white', font=('Microsoft YaHei UI Light',11))
label.place(x=30, y=300)

sign_up= Button(frame, width=6, text='Sign Up', border=0, bg='white',cursor='hand2' ,fg='#57A1F8')


root.mainloop()