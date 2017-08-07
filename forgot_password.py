from tkinter import *
from tkinter import messagebox
import time
import sqlite3
from configparser import ConfigParser
from passlib.hash import pbkdf2_sha256
import os
import random
import smtplib
from email.parser import Parser
from email.mime.multipart import MIMEMultipart

parser = ConfigParser()
parser.read('config.ini')

conn = sqlite3.connect('register.db')
c = conn.cursor()

class Login(Frame):

        if not(parser.has_option('MusicPlayer', 'Created') == 'True'):
                parser['MusicPlayer'] = { 'Volume': '20',
                                  'MusicDir': 'sounds/BaB.wav',
                                  'Created': 'True'}
        
        def __init__( self, parent, *args, **kwargs):
                def loginBox(event):
                        print('Loading login window!')
                        root.destroy()
                        os.system(sys.exec_prefix + '\python login.py')
                        
                Frame.__init__( self, parent, *args, **kwargs)
                self.parent = parent
                
                parent.minsize( width=300, height=215)
                parent.title("Organiser Live")

                title = Label(self, text="Password Recovery")
                title.config( font=("Courier", 20))

                title.pack()
                
                title.update_idletasks()
                
                title.place( x=((300) - title.winfo_reqwidth()) - ( ( 300 - title.winfo_reqwidth() ) / 2 ), y=20 )
                
                usernameLabel = Label(self, text="Email")
                usernameLabel.pack()
                usernameLabel.place( x=20, y = 75 )
                usernameLabel.config( font=("Courier", 16))

                username = Entry( self, width= 22)
                username.pack()
                username.place( x=30 + 110,y = 80 )

                registerLabel = Label(self, text="Login")
                registerLabel.pack()
                registerLabel.config( font=("Courier", 10), foreground='blue', cursor='hand2')
                registerLabel.place( x=((300) - registerLabel.winfo_reqwidth()) - ( ( 300 - registerLabel.winfo_reqwidth() ) / 2 ), y=185 )
                registerLabel.bind("<Button-1>", loginBox)
                
                def valueCheck():
                                    
                        if not ( username.get() == ""):
                                c.execute('SELECT * FROM Accounts WHERE email = ?', (username.get(),))
                                data = c.fetchall()
                                conn.commit()
                                
                                if not (len(data) == 0):
                                        if "@" in username.get() and "." in username.get():

                                                email = username.get()
                                                recoveryCode = random.randint( 10000, 99999)

                                                username.destroy()
                                                usernameLabel.destroy()
                                                login.destroy()
                                        
                                                codeLabel = Label(self, text="Code")
                                                codeLabel.pack()
                                                codeLabel.place( x=20, y = 75 )
                                                codeLabel.config( font=("Courier", 16))

                                                code = Entry( self, width= 22)
                                                code.pack()
                                                code.place( x=30 + 110,y = 80 )

                                                def recoverPassword():

                                                        if str(code.get()) == str(recoveryCode):
                                                                codeLabel.destroy()
                                                                code.destroy()
                                                                
                                                                passwordLabel = Label(self, text="Password")
                                                                passwordLabel.pack()
                                                                passwordLabel.place( x=20, y = 75 )
                                                                passwordLabel.config( font=("Courier", 16))

                                                                password= Entry( self, width= 22, show="*")
                                                                password.pack()
                                                                password.place( x=30 + 110,y = 80 )
                
                                                                retypeLabel = Label(self, text="Retype")
                                                                retypeLabel.pack()
                                                                retypeLabel.place( x=20, y = 110 )
                                                                retypeLabel.config( font=("Courier", 16))
                
                                                                retype = Entry( self, width= 22, show="*" )          
                                                                retype.pack()
                                                                retype.place( x=30 + 110,y = 115 )
                                                                parent.minsize( width=300, height=255)
                                                        
                                                                registerLabel.destroy()
                                                                returnLabel = Label(self, text="Login")
                                                                returnLabel.pack()
                                                                returnLabel.config( font=("Courier", 10), foreground='blue', cursor='hand2')
                                                                returnLabel.place( x=((300) - returnLabel.winfo_reqwidth()) - ( ( 300 - returnLabel.winfo_reqwidth() ) / 2 ), y=225 )
                                                                returnLabel.bind("<Button-1>", loginBox)

                                                                def login():
                                                                        if password.get() == retype.get():

                                                                                password_hashed = pbkdf2_sha256.hash(password.get())
                                                                                c.execute('UPDATE Accounts SET password = ? WHERE email = ?', ( password_hashed, email,))

                                                                                conn.commit()
                                                                        
                                                                                print('Loading login window!')
                                                                                root.destroy()
                                                                                os.system(sys.exec_prefix + '\python login.py')

                                                                recover.destroy()
                                                                update = Button(self, text="Update", width=19, height=2, command=login)
                                                                update.pack()
                                                                update.config( font=("Courier", 16), cursor='hand2')
                                                                update.place( x=20,y = 155 )

                                                        
                                                recover = Button(self, text="Recover", width=19, height=2, command=recoverPassword)
                                                recover.pack()
                                                recover.config( font=("Courier", 16), cursor='hand2')
                                                recover.place( x=20,y = 115 )

                                                server = smtplib.SMTP('smtp-mail.outlook.com', 587)
                                                server.starttls()
                                                server.login('organiser.live@outlook.com', 'giguzivert123')
                                                
                                                headers = ['organiser.live@outlook.com', 'Hey,\n You have forgot your password and have requested a recovery code, your code is: ' +str(recoveryCode), 'Account Recovery']
                                                message = 'Subject: {}\n\n{}'.format(headers[2], headers[1]) 
                                                server.sendmail(headers[0], email, message)
                                                server.close()
                                                messagebox.showinfo("Email Sent!" , "We have sent you an email with your recovery code!")
                                                
                                        else:
                                                messagebox.showinfo("Invalid Email" , "This email isn't a valid email adress and couldn't send the recovery message to it!")

                                else:
                                        print("This email hasn't been registered! Try registering an account!")
                                
                
                login = Button(self, text="Send Email", width=19, height=2, command=valueCheck)
                login.pack()
                login.config( font=("Courier", 16), cursor='hand2')
                login.place( x=20,y = 115 )


if __name__ == "__main__":
	root = Tk()
	
	Login(root).pack(side="top", fill="both", expand=True)
	
	root.resizable( width=False, height=False)
	root.mainloop() 

with open('config.ini', 'w') as configfile:
        parser.write(configfile)
