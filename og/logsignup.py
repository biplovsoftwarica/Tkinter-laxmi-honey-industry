from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *
from PIL import Image,ImageTk
import sqlite3
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
from maindash import Dash  # Import the Dash class from maindash.py
import webbrowser


def open_website():
    url = "https://laxmibeekeeping.com.np"
    webbrowser.open(url)

#funtions for handling all database

def createdatabase():
    conn = sqlite3.connect("laxmihoneyindustry.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            is_active BOOLEAN DEFAULT 0,
            session_id TEXT,
            is_admin BOOLEAN DEFAULT 0,
            profile_picture BLOB,
            a_country TEXT DEFAULT Nepal,
            a_state TEXT DEFAULT Bagmati,
            a_district TEXT DEFAULT Kathmandu,
            a_municipality TEXT DEFAULT Kathmandu,
            a_ward INT DEFAULT 7,
            a_tole TEXT DEFAULT Mitrapark,
            balance REAL DEFAULT 1000
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS products(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            product_picture BLOB NOT NULL,
            price REAL NOT NULL,
            stock INT
            
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS orders(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            total_amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(ID)
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS cart(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_id INTEGER,
            rate REAL NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 01,
            subtotal REAL GENERATED ALWAYS AS (rate * quantity) STORED,
            FOREIGN KEY (user_id) REFERENCES users(ID),
            FOREIGN KEY (product_id) REFERENCES products(ID)
        )"""
    )
    
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS order_items(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            subtotal REAL GENERATED ALWAYS AS (price * quantity) STORED,
            FOREIGN KEY (order_id) REFERENCES orders(ID),
            FOREIGN KEY (product_id) REFERENCES products(ID)
        )"""
    )

    conn.commit()
    conn.close()
createdatabase()

#for logingin users

def authenticate_user(email, password):
    conn = sqlite3.connect("laxmihoneyindustry.db")
    c=conn.cursor()
    # Query to check username and password
    if not email or not password:
        messagebox.showerror("Error", "fillup all details")
    else:
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        if user:
            if user[5]==password: 
                if user[6]!=0:
                    print("correct password")
                    # Generate session ID
                    session_id = str(uuid.uuid4())
                    # Update session_id in users table
                    c.execute("UPDATE users SET session_id = ? WHERE ID = ?", (session_id, user[0]))
                    conn.commit()
                    return session_id, user[0]
                    
                else:
                    messagebox.showerror("Error","Account not verified yet")
                    verify = CTk()
                    verify.geometry("300x300")
                    verify.title("verify your account")
                    varcode = random_verification_code_generator()
                    send_verification_email(f"{email}",f"{varcode}")
                                
                    otpenter = CTkEntry(verify,placeholder_text="000000")
                    otpenter.pack()
                                
                    def verifycode():
                        if str(varcode)==otpenter.get():
                            c.execute("UPDATE users SET is_active = ? WHERE email = ?", (True, email))
                            conn.commit()
                            print("account activeted")
                            messagebox.showinfo("success", "account verified succesfully")
                            verify.destroy()
                        else:
                            messagebox.showerror("Error","otp didn't match")
                    verifybtn = CTkButton(verify,text="verify",command=verifycode)
                    verifybtn.pack()
                    verify.mainloop()
            else:
                messagebox.showerror("Error","wrong password")
                
                
        else:
            messagebox.showerror("Error","User dosenot exists!")

#image handling




logoimage_path = "f:/college/1 semester/led projects/static/images/logo.png" #for window icon
logoimg = Image.open(logoimage_path)
logoimg = logoimg.resize((250, 250)) 

webimage_path = r"F:\college\1 semester\led projects\static\images\websitelogo.png"
webimg = Image.open(webimage_path)
webimg = webimg.resize((20, 20)) 

userimage_path = "f:/college/1 semester/led projects/static/images/user.png"
userimg = Image.open(userimage_path)
userimg = userimg.resize((20, 20)) 
        
signup1image_path = "f:/college/1 semester/led projects/static/images/login1.png"
signup1img = Image.open(signup1image_path)
signup1img = signup1img.resize((500, 480)) 

passimage_path = "f:/college/1 semester/led projects/static/images/password.png"
passimg = Image.open(passimage_path)
passimg = passimg.resize((23, 23)) 


emailimage_path = "f:/college/1 semester/led projects/static/images/email.png"
emailimg = Image.open(emailimage_path)
emailimg = emailimg.resize((20, 24)) 

eyeimage_path = "f:/college/1 semester/led projects/static/images/openeye.png"  # Replace with the path to your image
eyeimg = Image.open(eyeimage_path)
eyeimg = eyeimg.resize((15, 15))


closedeyeimage_path = "f:/college/1 semester/led projects/static/images/closedeye.png"  # Replace with the path to your image
closedeyeimg = Image.open(closedeyeimage_path)
closedeyeimg = closedeyeimg.resize((15, 15))
        
#random code generator

def random_verification_code_generator():
    num = random.randint(100000,999999)
    return num

def send_verification_email(receiver_email, code):
    sender_email = EMAIL_HOST_USER
    sender_password = EMAIL_HOST_PASSWORD
    subject = "Email Verification Code"
    body = f"Your verification code is: {code}"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
    else:
        print("Email sent successfullyy!!!")



EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='laxmihoneyindustry@gmail.com'
EMAIL_HOST_PASSWORD='hxoh cjwp fnpx vwrq'
EMAIL_PORT=587



set_appearance_mode("dark")

class App(CTk):
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.update_title()
        if page_name == "LoginPage":
            self.configure_buttons_login()
        elif page_name == "SignupPage":
            self.configure_buttons_signup()
            
    def __init__(self):
        super().__init__()
        self.title("Account")
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        self.geometry(f"{screen_width-100}x{screen_height-100}")
        self.minsize(800,700)
        # self.resizable(False,False)
        self.after(1, lambda: self.state("zoomed"))
        self.iconbitmap("f:/college/1 semester/led projects/static/images/logo.ico")

        #image
        logo1img = ImageTk.PhotoImage(logoimg)
        web1img = ImageTk.PhotoImage(webimg)
        user1img = ImageTk.PhotoImage(userimg)

    
        # Container for all frames
        
        self.leftframe = CTkFrame(self,width=250,height=screen_height,fg_color="orange",corner_radius=0)
        self.leftframe.place(relx=0,rely=0)
        self.leftframe.lift()
        
        self.logolbl = CTkLabel(self.leftframe,image=logo1img,text="")
        self.logolbl.place(relx=0.1,rely=0)
        
        self.websitebutton = CTkButton(self.leftframe, width=120,height=40, text="   website", font=('verdana', 17), text_color="black", fg_color="orange", cursor="hand2", hover_color="orange",border_color="black", border_width=2, corner_radius=20,command=open_website )
        self.websitebutton.place(x=50, rely=0.85)
        
        self.weblbl = CTkLabel(self.leftframe,image=web1img,height=10,width=10,text="",bg_color="orange",fg_color="orange",corner_radius=50)
        self.weblbl.place(x=55,rely=0.865)
        
        self.signupbutton = CTkButton(self.leftframe, width=112, height=90, text="Sign Up", font=('verdana', 17), text_color="black", fg_color="orange", cursor="hand2", hover_color="slate gray", border_width=0, corner_radius=20, command=lambda: self.show_frame("SignupPage"))
        self.signupbutton.place(x=211, rely=0.4, anchor=CENTER)
        self.loginbutton = CTkButton(self.leftframe, width=115, height=90, text="Log In", font=('verdana', 17), text_color="black", fg_color="orange", cursor="hand2", hover_color="slate gray", border_width=0, corner_radius=20, command=lambda: self.show_frame("LoginPage"))
        self.loginbutton.place(x=211, rely=0.54, anchor=CENTER)
        



        self.maincontainer = CTkFrame(self,width=(screen_width-500),height=screen_height,fg_color="slate gray",corner_radius=0)
        self.maincontainer.place(x=249,rely=0)

        self.frames = {}
        for F in (SignupPage,LoginPage):
            page_name = F.__name__
            frame = F(parent=self.maincontainer, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")
    def configure_buttons_login(self):
        self.signupbutton.configure(fg_color="orange")
        self.loginbutton.configure(fg_color="slategray")
    def configure_buttons_signup(self):
        self.signupbutton.configure(fg_color="slate gray")
        self.loginbutton.configure(fg_color="orange")

class SignupPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        
        # loading images
        suserimg = ImageTk.PhotoImage(userimg)
        ssignup1img = ImageTk.PhotoImage(signup1img)
        spassimg = ImageTk.PhotoImage(passimg)
        semailimg = ImageTk.PhotoImage(emailimg)
        seyeimg = ImageTk.PhotoImage(eyeimg)
        sclosedeyeimg = ImageTk.PhotoImage(closedeyeimg)



        
        containermain = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slate gray",corner_radius=0)
        containermain.pack()
        
        signupframe = CTkFrame(containermain,width=1000,height=700,bg_color="slate gray",fg_color="slate gray",corner_radius=10,border_width=0,border_color="black")
        signupframe.place(x=150,y=50)
        
        signuptext = CTkLabel(signupframe,text="Sign Up",font=("verdana",35),text_color="black")
        signuptext.place(relx=0.48,rely=0.08)
        
        loginimg = CTkLabel(signupframe,text="",image=ssignup1img)
        loginimg.place(x=100,rely=0.2)
        
        xy = 100
        
        userflabel = CTkLabel(signupframe, image=suserimg, text="") 
        userflabel.place(x=535+xy, y=150+xy-50)

        userf=CTkEntry(master=signupframe, width=120, placeholder_text='Firstname',text_color="white",fg_color="black",border_color="slategray",border_width=1,corner_radius=10)
        userf.place(x=555+xy, y=150+xy-50)

        userllabel = CTkLabel(signupframe, image=suserimg, text="") 
        userllabel.place(x=695+xy, y=150+xy-50)

        userl=CTkEntry(master=signupframe, width=120, placeholder_text='Lastname',text_color="white",fg_color="black",border_color="slategray",border_width=1,corner_radius=10)
        userl.place(x=715+xy, y=150+xy-50)

        userlabel = CTkLabel(signupframe, image=suserimg, text="") 
        userlabel.place(x=535+xy, y=195+xy-40)

        usern=CTkEntry(master=signupframe, width=270, placeholder_text='Username',text_color="white",fg_color="black",border_color="slategray",border_width=1,corner_radius=10)
        usern.place(x=558+xy, y=195+xy-40)

        useremaillabel = CTkLabel(signupframe, image=semailimg, text="") 
        useremaillabel.place(x=535+xy, y=240+xy-30)

        useremail=CTkEntry(master=signupframe, width=270, placeholder_text='Email',text_color="white",fg_color="black",border_color="slategray",border_width=1,corner_radius=10)
        useremail.place(x=558+xy, y=240+xy-30)

        passlabel1 = CTkLabel(signupframe, image=spassimg, text="") 
        passlabel1.place(x=535+xy, y=285+xy-20)

        pass1=CTkEntry(master=signupframe, width=270, placeholder_text='Password',text_color="white",fg_color="black",border_color="slategray",border_width=1,corner_radius=10, show="*")
        pass1.place(x=558+xy, y=285+xy-20)

        passlabel2 = CTkLabel(signupframe, image=spassimg, text="") 
        passlabel2.place(x=535+xy, y=330+xy-10)
        pass2=CTkEntry(master=signupframe, width=270, placeholder_text='confirm password',text_color="white",fg_color="black",border_color="slategray",border_width=1,corner_radius=10, show="*")
        pass2.place(x=558+xy, y=330+xy-10)
        def on_entry_hover(event, entry_widget):
            entry_widget.configure(border_width=0)

        def on_entry_leave(event, entry_widget):
            entry_widget.configure(border_width=1)

        def on_text_changed(event, entry_widget):
            if entry_widget.get():
                entry_widget.configure(border_width=0)
            else:
                entry_widget.configure(border_width=0)
        for entry_widget in [userf, userl, usern, useremail, pass1, pass2]:
            entry_widget.bind("<Enter>", lambda event, ew=entry_widget: on_entry_hover(event, ew))
            entry_widget.bind("<Leave>", lambda event, ew=entry_widget: on_entry_leave(event, ew))
            entry_widget.bind("<KeyRelease>", lambda event, ew=entry_widget: on_text_changed(event, ew))

        def show():
            eyebutton.configure(image=sclosedeyeimg)
            pass1.configure(show="")
            pass2.configure(show="")
            eyebutton.configure(command=hide)

        def hide():
            eyebutton.configure(image=seyeimg)
            pass1.configure(show="*")
            pass2.configure(show="*")
            eyebutton.configure(command=show)



        eyebutton = CTkButton(signupframe, image=seyeimg, text="", width=15, height=20,fg_color="slategray",bg_color="black",hover_color="#647381",corner_radius=5, command=show)
        eyebutton.place(x=798+xy, y=289+xy-20)

#signing up and saving data into database

        def signup(firstname,lastname,username,email,pass1,pass2):
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c = conn.cursor()
            if pass1!=pass2:
                messagebox.showerror("Error", "Passwords do not match")
            elif not firstname or not lastname or not username or not email or not pass1:
                messagebox.showerror("Error", "fill up all details")
            else:
                c.execute("SELECT * FROM users WHERE username=? OR email=?", (username, email))
                existing_user = c.fetchone() 
                if existing_user:
                    if existing_user[6]==0:
                        messagebox.showerror("Error", "user exists but not verifyied!!!")
                        
                        verify = CTk()
                        verify.geometry("600x600")
                        verify.title("verify your account")
                        varcode = random_verification_code_generator()
                        send_verification_email(f"{email}",f"{varcode}")
                            
                        otpenter = CTkEntry(verify,placeholder_text="000000")
                        otpenter.pack()
                            
                        def verifycode():
                            if str(varcode)==otpenter.get():
                                c.execute("UPDATE users SET is_active = ? WHERE email = ?", (True, email))
                                conn.commit()
                                print("account activeted")
                                messagebox.showinfo("success", "account verified succesfully")
                                verify.destroy()
                            else:
                                messagebox.showerror("Error","otp didn't match")
                        verifybtn = CTkButton(verify,text="verify",command=verifycode)
                        verifybtn.pack()
                        verify.mainloop()
                        self.controller.show_frame("LoginPage")
                    elif existing_user[3] == username:
                        messagebox.showerror("Error", "Username already exists")
                    elif existing_user[4] == email:
                        messagebox.showerror("Error", "Email already exists")
                        
                else:
                    c.execute("INSERT INTO users (firstname, lastname, username, email, password) VALUES (?, ?, ?, ?, ?)", (firstname, lastname, username, email, pass1))
                    conn.commit()
                    messagebox.showinfo("Success", "Signedup to your account successfully verify now")
                    verify = CTk()
                    verify.geometry("600x600")
                    verify.title("verify your account")
                    varcode = random_verification_code_generator()
                    send_verification_email(f"{email}",f"{varcode}")
                            
                    otpenter = CTkEntry(verify,placeholder_text="000000")
                    otpenter.pack()
                            
                    def verifycode():
                        if str(varcode)==otpenter.get():
                            c.execute("UPDATE users SET is_active = ? WHERE email = ?", (True, email))
                            conn.commit()
                            print("account activeted")
                            messagebox.showinfo("success", "account verified succesfully")
                            verify.destroy()
                        else:
                            messagebox.showerror("Error","otp didn't match")
                    verifybtn = CTkButton(verify,text="verify",command=verifycode)
                    verifybtn.pack()
                    verify.mainloop()
                    self.controller.show_frame("LoginPage")
                    conn.close()

        
        signupbutton = CTkButton(signupframe,text="Sign Up",width=200,text_color="black",corner_radius=15,fg_color="Aquamarine",cursor="hand2",command= lambda :signup(userf.get().capitalize(),userl.get().capitalize(),usern.get().lower(),useremail.get().lower(),pass1.get(),pass2.get()))
        signupbutton.place(x=601+xy,y=390+xy)
        #function when enter key is pressed
        def on_enter_key(event):
            signup(
                userf.get().capitalize(),
                userl.get().capitalize(),
                usern.get().lower(),
                useremail.get().lower(),
                pass1.get(),
                pass2.get()
            )
        userf.bind('<Return>', on_enter_key)
        userl.bind('<Return>', on_enter_key)
        usern.bind('<Return>', on_enter_key)
        useremail.bind('<Return>', on_enter_key)
        pass1.bind('<Return>', on_enter_key)
        pass2.bind('<Return>', on_enter_key)
        # function to give hover effect on login button
        
        def on_sign_enter(event):
            signupbutton.configure(width=204)
            signupbutton.place(x=599+xy,y=390+xy)
        signupbutton.bind("<Enter>", on_sign_enter)

        def on_sign_leave(event):
            signupbutton.configure(width=200)
            signupbutton.place(x=601+xy,y=390+xy)
        signupbutton.bind("<Leave>", on_sign_leave)

        yesaccount = CTkLabel(signupframe,text="Already have an account?",font=("vedana",11),text_color="white")
        yesaccount.place(x=585+xy,y =440+xy)

        login_button = CTkButton(signupframe,text="Login",width=80,fg_color="black",corner_radius=15,text_color="Aquamarine",cursor="hand2",command=lambda: controller.show_frame("LoginPage"))
        login_button.place(x=735+xy,y=440+xy)

        #function to give hover effect on register button
        def on_reg_enter(event):
            login_button.configure(text_color="black",fg_color="aquamarine")
        login_button.bind("<Enter>", on_reg_enter)

        def on_reg_leave(event):
            login_button.configure(text_color="aquamarine",fg_color="black")
        login_button.bind("<Leave>", on_reg_leave)
        
        
        
    def update_title(self):
        self.controller.title("signup - Laxmi Honey Industry")


class LoginPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        
        # loading images
        luserimg = ImageTk.PhotoImage(userimg)
        loginimg = ImageTk.PhotoImage(signup1img)
        lpassimg = ImageTk.PhotoImage(passimg)
        lemailimg = ImageTk.PhotoImage(emailimg)
        leyeimg = ImageTk.PhotoImage(eyeimg)
        lclosedeyeimg = ImageTk.PhotoImage(closedeyeimg)
        
        containermain = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slate gray",corner_radius=0)
        containermain.pack()
        
        loginframe = CTkFrame(containermain,width=900,height=700,bg_color="slate gray",fg_color="slate gray",corner_radius=10,border_width=0,border_color="black")
        loginframe.place(x=250,y=50)
        
        logintext = CTkLabel(loginframe,text="Log In",font=("verdana",35),text_color="black")
        logintext.place(relx=0.4,rely=0.1)
        
        loginuserimg = CTkLabel(loginframe,text="",image=loginimg,corner_radius=50)
        loginuserimg.place(relx=0.51,rely=0.2)
        
        xy = 100

        useremaillabel = CTkLabel(loginframe, image=lemailimg, text="") 
        useremaillabel.place(x=135-xy, y=240)

        useremail=CTkEntry(master=loginframe, width=270, placeholder_text='Email',fg_color="black",text_color="white",border_color="gray",border_width=2,corner_radius=10)
        useremail.place(x=158-xy, y=240)

        passlabel1 = CTkLabel(loginframe, image=lpassimg, text="") 
        passlabel1.place(x=135-xy, y=285)

        pass1=CTkEntry(master=loginframe, width=270, placeholder_text='Password',fg_color="black",text_color="white",border_color="gray",border_width=2,corner_radius=10, show="*")
        pass1.place(x=158-xy, y=285)
        def on_entry_hover(event, entry_widget):
            entry_widget.configure(border_width=1)

        def on_entry_leave(event, entry_widget):
            entry_widget.configure(border_width=2)

        def on_text_changed(event, entry_widget):
            if entry_widget.get():
                entry_widget.configure(border_width=1)
            else:
                entry_widget.configure(border_width=0)
                
        for entry_widget in [useremail, pass1]:
            entry_widget.bind("<Enter>", lambda event, ew=entry_widget: on_entry_hover(event, ew))
            entry_widget.bind("<Leave>", lambda event, ew=entry_widget: on_entry_leave(event, ew))
            entry_widget.bind("<KeyRelease>", lambda event, ew=entry_widget: on_text_changed(event, ew))

        def show():
            eyebutton.configure(image=lclosedeyeimg)
            pass1.configure(show="")
            eyebutton.configure(command=hide)

        def hide():
            eyebutton.configure(image=leyeimg)
            pass1.configure(show="*")
            eyebutton.configure(command=show)



        eyebutton = CTkButton(loginframe, image=leyeimg, text="", width=15, height=20,fg_color="slategray",bg_color="black",hover_color="#647381",corner_radius=5, command=show)
        eyebutton.place(x=398-xy, y=289)


        def authenticate_user(self,controller,email, password):
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c=conn.cursor()
            # Query to check username and password
            if not email or not password:
                messagebox.showerror("Error", "fillup all details")
            else:
                c.execute("SELECT * FROM users WHERE email = ?", (email,))
                user = c.fetchone()
                if user:
                    if user[5]==password: 
                        if user[6]!=0:
                            print("correct password")
                            # Generate session ID
                            session_id = str(uuid.uuid4())
                            # Update session_id in users table
                            c.execute("UPDATE users SET session_id = ? WHERE ID = ?", (session_id, user[0]))
                            conn.commit()
                            controller.destroy()
                            # Instantiate Dash class and pass session_id and user_id
                            try:
                                app = Dash(user_id=user[0],session_id=session_id)  # Pass session_id and user_id
                                app.mainloop()
                                print("Go to home page with user data")
                            except Exception as e:
                                print(f"Failed to run maindash application: {e}")
                                # Handle error (e.g., show error message)
                        else:
                            messagebox.showerror("Error","Account not verified yet")
                            verify = CTk()
                            verify.geometry("300x300")
                            verify.title("verify your account")
                            varcode = random_verification_code_generator()
                            send_verification_email(f"{email}",f"{varcode}")                                        
                            otpenter = CTkEntry(verify,placeholder_text="000000")
                            otpenter.pack()
                            def verifycode():
                                if str(varcode)==otpenter.get():
                                    c.execute("UPDATE users SET is_active = ? WHERE email = ?", (True, email))
                                    conn.commit()
                                    print("account activeted")
                                    messagebox.showinfo("success", "account verified succesfully")
                                    verify.destroy()
                                else:
                                    messagebox.showerror("Error","otp didn't match")
                            verifybtn = CTkButton(verify,text="verify",command=verifycode)
                            verifybtn.pack()
                            verify.mainloop()
                    else:
                        messagebox.showerror("Error","wrong password")
                else:
                    messagebox.showerror("Error","User dosenot exists!")
                    self.controller.show_frame("SignupPage")


        loginbutton = CTkButton(loginframe,text="Log In",width=200,text_color="black",corner_radius=15,fg_color="Aquamarine",cursor="hand2",command=lambda: authenticate_user(self,controller,email=useremail.get().lower(),password=pass1.get()))
        loginbutton.place(x=201-xy,y=360)
        
        # Function when enter key is pressed
        def on_enter_key(event):
            authenticate_user(self, controller, useremail.get().lower(), pass1.get())
        useremail.bind('<Return>', on_enter_key)
        pass1.bind('<Return>', on_enter_key)        
        # function to give hover effect on login button
        def on_log_enter(event):
            loginbutton.configure(width=204)
            loginbutton.place(x=199-xy,y=360)
        loginbutton.bind("<Enter>", on_log_enter)

        def on_log_leave(event):
            loginbutton.configure(width=200)
            loginbutton.place(x=201-xy,y=360)
        loginbutton.bind("<Leave>", on_log_leave)

        noaccount = CTkLabel(loginframe,text="Don't have an account?",font=("vedana",11),text_color="white")
        noaccount.place(x=185-xy,y =440)

        signup_button = CTkButton(loginframe,text="Sign Up",width=80,fg_color="black",corner_radius=15,text_color="Aquamarine",cursor="hand2",command=lambda: controller.show_frame("SignupPage"))
        signup_button.place(x=335-xy,y=440)

        #function to give hover effect on register button
        def on_sign_enter(event):
            signup_button.configure(text_color="black",fg_color="aquamarine")
        signup_button.bind("<Enter>", on_sign_enter)

        def on_sign_leave(event):
            signup_button.configure(text_color="aquamarine",fg_color="black")
        signup_button.bind("<Leave>", on_sign_leave)
        
        
    def update_title(self):
        self.controller.title("login - Laxmi Honey Industry")
             

if __name__ == "__main__":
    app = App()
    app.mainloop()

