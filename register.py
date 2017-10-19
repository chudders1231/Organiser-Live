from includes import *

parser = ConfigParser()
parser.read('config.ini')

conn = sqlite3.connect('register.db', timeout=10)
c = conn.cursor()

class Register(Frame):

        if not(parser.has_option('MusicPlayer', 'Created') == 'True'):
                parser['MusicPlayer'] = { 'Volume': '20',
                                  'MusicDir': 'sounds/BaB.wav',
                                  'Created': 'True'}
        def __init__( self, parent, *args, **kwargs):
                        
                Frame.__init__( self, parent, *args, **kwargs)
                self.parent = parent
                
                def login(event):
                        print('Loading login window!')
                        root.destroy()
                        os.system(sys.exec_prefix + '\python login.py')
                        
                def returnLogin():
                        
                        print('Loading login window!')
                        root.destroy()
                        os.system(sys.exec_prefix + '\python login.py')
                
                parent.minsize( width=300, height=425)
                parent.title("Organiser Live")

                title = Label(self, text="Register")
                title.config( font=("Courier", 44))
                
                title.pack()
                
                title.update_idletasks()
                
                title.place( x=((300) - title.winfo_reqwidth()) - ( ( 300 - title.winfo_reqwidth() ) / 2 ) )

                ## Username Input ##
                usernameLabel = Label(self, text="Username")
                usernameLabel.pack()
                usernameLabel.place( x=20, y = 75 )
                usernameLabel.config( font=("Courier", 16))

                username = Entry( self, width= 22)
                username.pack()
                username.place( x=30 + usernameLabel.winfo_reqwidth(),y = 80 )

                ## Email Input ##
                emailLabel = Label(self, text="Email")
                emailLabel.pack()
                emailLabel.place( x=20, y = 110 )
                emailLabel.config( font=("Courier", 16))

                email = Entry( self, width= 22)
                email.pack()
                email.place( x=30 + 110,y = 115 )

                ## First Name Input ##
                firstLabel = Label(self, text="Forename")
                firstLabel.pack()
                firstLabel.place( x=20, y = 145 )
                firstLabel.config( font=("Courier", 16))

                first = Entry( self, width= 22)
                first.pack()
                first.place( x=30 + 110,y = 150 )
                
                ## Second Name Input ##
                secondLabel = Label(self, text="Surname")
                secondLabel.pack()
                secondLabel.place( x=20, y = 180 )
                secondLabel.config( font=("Courier", 16))

                second = Entry( self, width= 22)
                second.pack()
                second.place( x=30 + 110,y = 185 )

                ## Password Input ##
                passwordLabel = Label(self, text="Password")
                passwordLabel.pack()
                passwordLabel.place( x=20, y = 215 )
                passwordLabel.config( font=("Courier", 16))
                
                password = Entry( self, width= 22, show="*" )          
                password.pack()
                password.place( x=30 + passwordLabel.winfo_reqwidth(),y = 220 )

                ## Retype Password Input ##
                retypeLabel = Label(self, text="Retype")
                retypeLabel.pack()
                retypeLabel.place( x=20, y = 250 )
                retypeLabel.config( font=("Courier", 16))
                
                retype = Entry( self, width= 22, show="*")          
                retype.pack()
                retype.place( x=30 + 110,y = 255 )

                ## Form Group Input ##

                formGroupLabel = Label(self, text="Form")
                formGroupLabel.pack()
                formGroupLabel.place( x=20, y = 285 )
                formGroupLabel.config( font=("Courier", 16))
                
                variable = StringVar(self)
                variable.set("12.1 Odogwu")
                
                formGroup = OptionMenu(self, variable, "12.1 Odogwu", "12.2 Lockston", "12.3 Holden", "12.4 Curwin")
                formGroup.pack()
                formGroup.place( x=30 + 108, y = 285 )
                formGroup.config(width=16)
                
                def valueCheck():
                        if not ( username.get() == "") and not ( email.get() == "") and not ( first.get() == "") and not ( second.get() == "") and not ( password.get() == "") and not ( retype.get() == "") and not (variable.get() == ""):
                                c.execute('SELECT * FROM Accounts WHERE email = ?', (email.get(),))
                                data = c.fetchall()
                                conn.commit()
                                
                                if '@' in email.get() and (password.get() == retype.get()):
                                                password_hashed = pbkdf2_sha256.hash(password.get())

                                                if not(len(data)==0):
                                                        
                                                        print('The email %s has already been registered'%email.get())

                                                else:
                                                        print("Inserting")
                                                        c.execute('INSERT INTO Accounts VALUES( ?, ?, ?, ?, ?, ?, ?, ?)', ( username.get(), email.get(), first.get(), second.get(), password_hashed, variable.get(), datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'False'))
                                                        conn.commit()
                                                        returnLogin()


                ## Register Button ##
                register = Button(self, text="Register", width=19, height=2, command=valueCheck)
                register.pack()
                register.config( font=("Courier", 16), cursor='hand2')
                register.place( x=20, y = 325)

                ## Already have an account clickable text ##
                loginLabel = Label(self, text="Already have an account?")
                loginLabel.pack()
                loginLabel.config( font=("Courier", 10), foreground='blue', cursor='hand2')
                loginLabel.place( x=((300) - loginLabel.winfo_reqwidth()) - ( ( 300 - loginLabel.winfo_reqwidth() ) / 2 ), y=395 )
                loginLabel.bind("<Button-1>",login)

c.execute('SELECT * FROM Accounts ')
data = c.fetchall()
conn.commit()


if __name__ == "__main__":
	root = Tk()
	
	Register(root).pack(side="top", fill="both", expand=True)
	
	root.resizable( width=False, height=False)
	
	root.mainloop() 

with open('config.ini', 'w') as configfile:
        parser.write(configfile)
