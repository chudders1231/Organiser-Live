from login import *
from includes import *

parser = ConfigParser()
parser.read('config.ini')
    
class Profile(Frame):
            
            def __init__( self, parent, *args, **kwargs):

                    class changeIconWindow(Frame):
                        def __init__( self, parent, *args, **kwargs):
                            Frame.__init__( self, parent, *args, **kwargs)
                            self.parent = parent
                        
                            parent.minsize( width=600, height=255)
                            parent.title("Organiser Live")

                    def changeIcon(event):
                        if event:
                            new = Tk()
                            changeIconWindow(new).pack( side="top", fill="both", expand=True)

                            new.resizable( width=False, height=False)
                            new.mainloop()

                    Frame.__init__( self, parent, *args, **kwargs)
                    self.parent = parent
                
                    parent.minsize( width=600, height=255)
                    parent.title("Organiser Live")

                    load = Image.open('icons/' + parser['Account']['Icon'])
                    render = ImageTk.PhotoImage(load)

                    img = Label(self, image=render, width=100, height=100)
                    img.image = render
                    img.place(x=5, y=5)
                    img.config(cursor='hand2')
                    img.bind("<Button-1>", changeIcon)

                    nameLabel = Label(self, text=parser['Account']["Forename"].title() + ' ' + parser['Account']["Surname"].title())
                    nameLabel.pack()
                    nameLabel.config( font=("Courier", 20))
                    nameLabel.place( x=115, y=0 )

                    usernameLabel = Label(self, text="Username: " + parser['Account']["Username"].title())
                    usernameLabel.pack()
                    usernameLabel.config( font=("Courier", 14))
                    usernameLabel.place( x=115, y=35)
                    
                    if parser['Account']["Admin"]:
                        permissionLabel = Label(self, text="ADMIN", bg="#e74c3c")
                        permissionLabel.pack()
                        permissionLabel.config( font=("Segoe UI Semibold", 10), foreground="white")
                        permissionLabel.place( x=120, y=65)
                    else:
                        permissionLabel = Label(self, text="PLAYER", bg="#2ecc71")
                        permissionLabel.pack()
                        permissionLabel.config( font=("Segoe UI Semibold", 10), foreground="white")
                        permissionLabel.place( x=120, y=65)



                

if __name__ == "__main__":
	root = Tk()
	
	Profile(root).pack(side="top", fill="both", expand=True)
	
	root.resizable( width=False, height=False)
	root.mainloop()
	
