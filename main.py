# login Window

from tkinter import *
from tkinter import messagebox
import pymysql as mys
import menu

# variables
themeBack = "#ffffed"
fontBack = themeBack
fontColor = "red"
entryBack = "white"
toShow = '*'
databaseName = 'mysql'


def connect(username, password, loginWindow):
    uname = username.get()
    upass = password.get()
    if uname == '':
        uname = 'root'

    try:
        conn = mys.connect(host='localhost', user=uname, passwd=upass)
        messagebox.showinfo("Status", "Connection Successful")
        loginWindow.destroy()
        myCursor = conn.cursor()
        menu.setcursor(myCursor, conn)
        menu.start()

    except:
        messagebox.showerror("Status", "Connection failed  \n")


def setup():
    loginWin = Tk()
    loginWin.title("Connecting to mysql server")
    loginWin.config(background=themeBack)
    loginWin.state("zoomed")
    Label(loginWin, text="Login to mysql \n\n", bg=fontBack, fg=fontColor, font="Agency_fb 20 bold")\
        .grid(column=0, row=0, columnspan=3)

    Label(loginWin, text="Enter user (Default 'root'): ", bg=fontBack, fg=fontColor,
          font="Agency_fb 12 bold").grid(column=0, row=1)
    username = Entry(loginWin, width=20, bg=entryBack)
    username.insert(0, 'root')
    username.grid(column=2, row=1, sticky=E)

    Label(loginWin, text="", bg=fontBack, fg=fontColor).grid(column=1, row=2)
    Label(loginWin, text="", bg=fontBack, fg=fontColor).grid(column=1, row=4)

    Label(loginWin, text="Enter your mysql password\n(leave empty for no password):", bg=fontBack, fg=fontColor,
          font="Agency_fb 12 bold").grid(column=0, row=3, sticky=S)
    password = Entry(loginWin, width=20, bg=entryBack, show=toShow)
    password.grid(column=2, row=3, sticky=S)

    loginWin.bind('<Return>', lambda e: connect(username, password, loginWin))

    Button(loginWin, text="Login", width=15, command=lambda: connect(username, password, loginWin)).grid(
        column=1, row=5, sticky=S)

    mainloop()


if __name__ == '__main__':
    setup()
