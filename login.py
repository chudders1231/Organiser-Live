from includes import *

parser = ConfigParser()
parser.read('config.ini')

conn = sqlite3.connect('register.db')
c = conn.cursor()

global account

def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS Accounts( username TEXT, email TEXT, forename TEXT, surname TEXT, password TEXT, form TEXT, regDate TEXT, admin TEXT)')

        c.execute('SELECT * FROM Accounts WHERE email = "LouisRhythms@gmail.com"')
        data = c.fetchall()
        conn.commit()

        if not (len(data) == 1):
                c.execute('INSERT INTO Accounts VALUES( "LouisThompson", "LouisRhythms@gmail.com", "Louis", "Thompson", "' + pbkdf2_sha256.hash("AdminChangeMe") +'", "12.4 Curwin", "' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "True")')

create_table()

class Login(Frame):

        if not(parser.has_option('Organiser Live', 'Created')):
                parser['Organiser Live'] = {
                                  'created': 'True',}
         
        def __init__( self, parent, *args, **kwargs):
                        
                Frame.__init__( self, parent, *args, **kwargs)
                self.parent = parent

                def register(event):
                        print('Loading register window!')
                        root.destroy()
                        exec(open("register.py").read())

                def forgotPassword(event):
                        print('Loading forgot my password window!')
                        root.destroy()
                        exec(open("forgot_password.py").read())
                        
                parent.minsize( width=300, height=255)
                parent.title("Organiser Live")

                title = Label(self, text="Login")
                title.config( font=("Courier", 44))
                
                title.pack()
                
                title.update_idletasks()
                
                title.place( x=((300) - title.winfo_reqwidth()) - ( ( 300 - title.winfo_reqwidth() ) / 2 ) )
                
                usernameLabel = Label(self, text="Email")
                usernameLabel.pack()
                usernameLabel.place( x=20, y = 75 )
                usernameLabel.config( font=("Courier", 16))

                username = Entry( self, width= 22)
                username.pack()
                username.place( x=30 + 110,y = 80 )
                
                passwordLabel = Label(self, text="Password")
                passwordLabel.pack()
                passwordLabel.place( x=20, y = 110 )
                passwordLabel.config( font=("Courier", 16))
                
                password = Entry( self, width= 22, show="*" )          
                password.pack()
                password.place( x=30 + passwordLabel.winfo_reqwidth(),y = 115 )

                def valueCheck():
                        if not ( username.get() == "") and not ( password.get() == ""):
                                c.execute('SELECT * FROM Accounts WHERE email = ?', (username.get(),))
                                data = c.fetchall()
                                conn.commit()

                                if not (len(data) == 0):

                                        if (pbkdf2_sha256.verify(password.get(), data[0][4]) == True):
                                                
                                                print("Logging in!")
                                                
                                                parser['Account'] = {'Username': data[0][0],
                                                           'Email': data[0][1],
                                                           'Forename': data[0][2],
                                                           'Surname': data[0][3],
                                                           'Password': data[0][4],
                                                           'Form': data[0][5],
                                                           'RegDate': data[0][6],
                                                           'Admin': data[0][7],
                                                           'Icon': 'Icon (64).png',
                                                           'Created': 'True',}
                                                
                                                root.destroy()

                                                exec(open("main_menu.py").read())

                                        else:
                                                print("Wrong Password")

                                
                
                login = Button(self, text="Login", width=19, height=2, command=valueCheck)
                login.pack()
                login.config( font=("Courier", 16), cursor='hand2')
                login.place( x=20,y = 155 )

                registerLabel = Label(self, text="Register")
                registerLabel.pack()
                registerLabel.config( font=("Courier", 10), foreground='blue', cursor='hand2')
                registerLabel.place( x=(30), y=225 )
                registerLabel.bind("<Button-1>",register)

                forgotLabel = Label(self, text="Forgot my Password")
                forgotLabel.pack()
                forgotLabel.config( font=("Courier", 10), foreground='blue', cursor='hand2')
                forgotLabel.place( x=((300) - forgotLabel.winfo_reqwidth()) - 30, y=225 )
                forgotLabel.bind("<Button-1>", forgotPassword)

if __name__ == "__main__":
        if parser.has_option('Account', 'Created'):
                exec(open("main_menu.py").read())
        else:
                root = Tk()

                Login(root).pack(side="top", fill="both", expand=True)
                root.resizable( width=False, height=False)
                root.mainloop()
                
with open('config.ini', 'w') as configfile:
        parser.write(configfile)
