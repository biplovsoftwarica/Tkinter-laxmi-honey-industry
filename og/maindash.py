import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageOps,ImageFont
import sqlite3
import webbrowser
import io
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='laxmihoneyindustry@gmail.com'
EMAIL_HOST_PASSWORD='hxoh cjwp fnpx vwrq'
EMAIL_PORT=587

def send_html_email(receiver_email, subject, html_content):
    sender_email = EMAIL_HOST_USER
    sender_password = EMAIL_HOST_PASSWORD

    # Debug print statements
    print(f"Sender Email: {sender_email}")
    print(f"Receiver Email: {receiver_email}")
    print(f"Email Subject: {subject}")
    print(f"Email Body: {html_content}")

    msg = MIMEMultipart("alternative")
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
    else:
        print("Email sent successfully!")
        
userimage_path = "f:/college/1 semester/led projects/static/images/user.png"
userimg = Image.open(userimage_path)
userimg = userimg.resize((20, 20)) 

logoimage_path = "f:/college/1 semester/led projects/static/images/logo.png"
logoimg = Image.open(logoimage_path)
logoimg = logoimg.resize((140, 140)) 

webimage_path = r"F:\college\1 semester\led projects\static\images\websitelogo.png"
webimg = Image.open(webimage_path)
webimg = webimg.resize((20, 20)) 

camimage_path = r"F:\college\1 semester\led projects\static\images\camera.png"
camimg = Image.open(camimage_path)
camimg = camimg.resize((25, 22)) 

editimage_path = r"F:\college\1 semester\led projects\static\images\edit.png"
editimg = Image.open(editimage_path)
editimg = editimg.resize((20, 20)) 

moneydepoimage_path = r"F:\college\1 semester\led projects\static\images\moneydepo.png"
moneydepoimg = Image.open(moneydepoimage_path)
moneydepoimg = moneydepoimg.resize((25, 25))

refreshimage_path = r"F:\college\1 semester\led projects\static\images\refresh.png"
refreshimg = Image.open(refreshimage_path)
refreshimg = refreshimg.resize((23, 23))  

def open_website():
    url = "https://laxmibeekeeping.com.np"
    webbrowser.open(url)

set_appearance_mode("dark")

class Dash(CTk):    
    def __init__(self,user_id,session_id):
        super().__init__()
        self.user_id=user_id
        self.load_user_data()
        user = self.load_user_data()
        self.title("Laxmi Honey Industry")
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        self.geometry(f"{screen_width-100}x{screen_height-100}")
        self.resizable(False,False)
        self.after(1, lambda: self.state("zoomed"))
        
        
        logo1img = ImageTk.PhotoImage(logoimg)
        web1img = ImageTk.PhotoImage(webimg)
        user1img = ImageTk.PhotoImage(userimg)

        # Container for all frames
        
        self.topframe = CTkFrame(self,width=screen_width,height=115,fg_color="orange",corner_radius=0)
        self.topframe.pack(fill="x")
        self.topframe.lift()
        
        self.bottomframe = CTkFrame(self,width=screen_width,height=23,fg_color="#2b2b2b",corner_radius=0)  ##60707f
        self.bottomframe.pack(side="bottom",fill="x")
        self.bottomframe.lift()

        developerlbl = CTkLabel(self.bottomframe,height=24,text="Developed by : 36_AI Group",text_color="white")
        developerlbl.pack(side=RIGHT,padx=40)

        copyrightbutton = CTkButton(self.bottomframe,height=23,text="All rights reserved © Laxmi Honey Industry",fg_color="#2b2b2b",text_color="white",hover_color="#2b2b2b")
        copyrightbutton.pack(side=LEFT,padx=40)

        self.logolbl = CTkLabel(self.topframe,image=logo1img,text="")
        self.logolbl.place(relx=0.01,rely=(0.98-1))
        
        self.homebutton = CTkButton(self.topframe, width=110, height=40, text="Home", font=('verdana', 17), text_color="black", fg_color="orange", cursor="hand2", hover_color="slate gray", border_width=0, corner_radius=50, command=lambda: self.show_frame("HomePage"))
        self.homebutton.place(relx=0.32, rely=0.5, anchor=CENTER)
        self.productbutton = CTkButton(self.topframe, width=110, height=40, text="Products", font=('verdana', 17), text_color="black", fg_color="orange", cursor="hand2", hover_color="slate gray", border_width=0, corner_radius=50, command=lambda: self.show_frame("ProductPage"))
        self.productbutton.place(relx=0.47, rely=0.5, anchor=CENTER)
        self.cartbutton = CTkButton(self.topframe, width=110, height=40, text="Cart/Orders", font=('verdana', 17), text_color="black", fg_color="orange", cursor="hand2", hover_color="slate gray", border_width=0, corner_radius=50, command=lambda: self.show_frame("CartPage"))
        self.cartbutton.place(relx=0.62, rely=0.5, anchor=CENTER)
        self.aboutbutton = CTkButton(self.topframe, width=110, height=40, text="About Us", font=('verdana', 17), text_color="black", fg_color="orange", cursor="hand2", hover_color="slate gray", border_width=0, corner_radius=50, command=lambda: self.show_frame("AboutPage"))
        self.aboutbutton.place(relx=0.77, rely=0.5, anchor=CENTER)

        self.accountbutton = CTkButton(self.topframe, width=120,height=40, text=f" {user[1]}", font=('verdana', 17), text_color="black", fg_color="orange", hover_color="#e39300",cursor="hand2",border_color="black", border_width=2, corner_radius=20,command= lambda: self.show_frame("AccountPage") )
        self.accountbutton.place(relx=0.9, y=38)
        
        self.userlbl = CTkLabel(self.topframe,image=user1img,height=10,width=10,text="",corner_radius=50)
        self.userlbl.place(relx=0.903,y=49)
        
        def on_web_enter(event):
            self.userlbl.configure(fg_color="#e39300",bg_color="#e39300")
        self.accountbutton.bind("<Enter>", on_web_enter)

        def on_web_leave(event):
            if page_name=="AccountPage":
                self.userlbl.configure(fg_color="#e39300",bg_color="#e39300")
            else:
                self.userlbl.configure(fg_color="orange",bg_color="orange") 
        self.accountbutton.bind("<Leave>", on_web_leave)

        #for switching between pages

        self.maincontainer = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slate gray",bg_color="slate gray",corner_radius=0)
        self.maincontainer.pack(fill=BOTH)

        self.frames = {}
        for F in (HomePage,ProductPage,CartPage,AccountPage,AboutPage):
            page_name = F.__name__
            frame = F(parent=self.maincontainer, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")

    # loading users data
    def load_user_data(self):
        try:
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE ID = ?", (self.user_id,))
            user = c.fetchone()
            conn.close()
            if user:
                return user
            else:
                messagebox.showerror("Error", "User data not found!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
        
    # for showing selected page and to give current page indication    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.update_title()
        if page_name == "HomePage":
            self.configure_buttons_home()
        elif page_name == "ProductPage":
            self.configure_buttons_product()
        elif page_name == "CartPage":
            self.configure_buttons_cart()
        elif page_name == "AccountPage":
            self.configure_buttons_account()
        elif page_name == "AboutPage":
            self.configure_buttons_about()
        
    def configure_buttons_product(self):
        self.homebutton.configure(fg_color="orange")
        self.productbutton.configure(fg_color="slategray")
        self.cartbutton.configure(fg_color="orange")
        self.accountbutton.configure(fg_color="orange")
        self.aboutbutton.configure(fg_color="orange")

    def configure_buttons_home(self):
        self.homebutton.configure(fg_color="slate gray")
        self.productbutton.configure(fg_color="orange")
        self.cartbutton.configure(fg_color="orange")
        self.accountbutton.configure(fg_color="orange")
        self.aboutbutton.configure(fg_color="orange")

    def configure_buttons_cart(self):
        self.homebutton.configure(fg_color="orange")
        self.productbutton.configure(fg_color="orange")
        self.cartbutton.configure(fg_color="slate gray")
        self.accountbutton.configure(fg_color="orange")
        self.aboutbutton.configure(fg_color="orange")

    def configure_buttons_account(self):
        self.homebutton.configure(fg_color="orange")
        self.productbutton.configure(fg_color="orange")
        self.cartbutton.configure(fg_color="orange")
        self.aboutbutton.configure(fg_color="orange")

    def configure_buttons_about(self):
        self.homebutton.configure(fg_color="orange")
        self.productbutton.configure(fg_color="orange")
        self.cartbutton.configure(fg_color="orange")
        self.aboutbutton.configure(fg_color="slate gray")
        
        
    # manual popup message box for displaying any message for 6 second and auto disappears
def show_popup_message(parent_frame, message, duration=6000):
    popup_frame = CTkFrame(parent_frame, fg_color="#F0F0F0",height=60,width=200,border_width=1.5,border_color="darkgray", corner_radius=10)
    popup_frame.place(relx=0.47,y=5)
    popup_frame.pack_propagate(False)

    message_label = CTkLabel(popup_frame, text=f" {message} ", wraplength=150,text_color="black", font=("Verdana", 12))
    message_label.pack(padx=10, pady=10,side=LEFT)

    close_btn = CTkButton(popup_frame,text="X",font=("verdana",11),width=10,text_color="black",fg_color="#F0F0F0",hover_color="#F0F1F0",command=popup_frame.destroy)
    close_btn.pack(padx=3.5,pady=3,anchor="ne")
    parent_frame.after(duration, popup_frame.destroy)

class HomePage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        containermain = CTkFrame(self, fg_color="slategray", corner_radius=0)
        containermain.pack(fill=BOTH)

        logo1img = logoimg.resize((250, 250))
        logo1img = ImageTk.PhotoImage(logo1img)

        leftcontainer = CTkFrame(containermain, fg_color="slategray", height=610, width=500)
        leftcontainer.pack(side=LEFT, padx=60, pady=80, fill=Y)

        whytxt = CTkLabel(leftcontainer, text="Why Laxmi Honey?", font=("verdana", 30), text_color="black")
        whytxt.place(x=65, y=0)

        

        logoimg1 = CTkLabel(leftcontainer, image=logo1img, text="")
        logoimg1.place(x=80, y=40)

        benifits = [
            "15+ years of experience in bee keeping",
            "Pure Honey directly from BEE farm",
            "Your Family <==> Our Family",
            "Fastest delivery inside KTM valley",
            "Both Purified & Raw Honey",
        ]
        y = 280
        for benifit in benifits:
            text_label = CTkLabel(leftcontainer, text=f"• {benifit}", text_color="black", font=("comic sans ms", 18), anchor="w")
            text_label.place(x=70, y=y)
            y = y + 32

        # Image slideshow on the right
        rightcontainer = CTkFrame(containermain, fg_color="slategray", width=800)
        rightcontainer.pack(side=RIGHT, padx=100, pady=10, fill=Y)
        rightcontainer.pack_propagate(False)

        self.images = [
            ("F:\\college\\1 semester\\led projects\\static\\images\\SAM_1383.jpg", "15 Years of Experience,"),
            ("F:\\college\\1 semester\\led projects\\static\\images\\SAM_1386.jpg", "Women Empowered,"),
            ("F:\\college\\1 semester\\led projects\\static\\images\\SAM_1380.jpg", "Laxmi Honey Industry.\n    Always with you !"),
        ]
        self.index = 0

        self.image_label = CTkLabel(rightcontainer, width=908, height=656,text="",text_color="lightgray",font=("comic sans ms",20), bg_color="slategray")
        self.image_label.pack()

        self.back_button = CTkButton(rightcontainer, text="<", fg_color="orange", hover_color="#E69500", text_color="black", command=self.previous_image)
        self.back_button.place(x=220, y=535)

        self.next_button = CTkButton(rightcontainer, text=">", fg_color="orange", text_color="black", hover_color="#E69500", command=self.next_image)
        self.next_button.place(x=400, y=535)

        self.show_image()
        self.auto_slide_images()
        product_btn = CTkButton(containermain, text=" Wanna have Healthy Life ? \nHurry up!!!",fg_color="orange",hover_color="#e79500", font=("verdana", 15), text_color="black", command=lambda page="ProductPage": controller.show_frame(page))
        product_btn.place(x=150, y=550)
    def show_image(self):
        image_path, image_text = self.images[self.index]
        image = Image.open(image_path)
        image = image.resize((908, 656))
        radius = 30  # Radius of the rounded corners
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, image.width, image.height), radius, fill=255)
        image.putalpha(mask)
        draw = ImageDraw.Draw(image)
        font_size = 30
        font = ImageFont.truetype("verdana.ttf", font_size)
        text_bbox = draw.textbbox((0, 0), image_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = (image.width - text_width) / 2
        text_y = 20 
        draw.text((text_x, text_y), image_text, font=font, fill="white")
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=self.photo)
        self.image_label.image = self.photo
        
    def next_image(self):
        self.index = (self.index + 1) % len(self.images)
        self.show_image()
        
    def auto_slide_images(self):
        self.next_image()
        self.after(5000, self.auto_slide_images)
        
    def previous_image(self):
        self.index = (self.index - 1) % len(self.images)
        self.show_image()

    def update_title(self):
        self.controller.title("Home - Laxmi Honey Industry")

class ProductPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = controller.load_user_data()
        self.products = fetch_products()

        # Main container
        self.containermain = CTkFrame(self, height=1000, width=1000, fg_color="slategray", corner_radius=0)
        self.containermain.pack(fill=tk.BOTH, expand=True)
        
        self.leftcontainer = CTkFrame(self.containermain,fg_color="#4b5866",height=600,width=600)
        self.leftcontainer.place(x=40,y=50)
        
        self.rightcontainer=CTkFrame(self.containermain,fg_color="slategray",height=680,width=800)
        self.rightcontainer.place(x=750,y=10)
        
        self.productstext = CTkLabel(self.rightcontainer,text="All Products     ",width=800,anchor="e",text_color="black",font=("verdana",24))
        self.productstext.place(x=0,y=15)
        
        self.canvas = Canvas(self.rightcontainer, height=750, width=850, bg="slategray")
        self.canvas.place(x=100, y=58)
        
        self.scrollbar = CTkScrollbar(self.rightcontainer, height=600, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.place(x=750, y=60)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.inner_frame = CTkFrame(self.canvas, width=850, height=1200, fg_color="slategray", corner_radius=0)
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        
        self.canvas.bind("<Enter>", self._on_enter)
        self.canvas.bind("<Leave>", self._on_leave)
        self.emptyspace = CTkFrame(self.rightcontainer, height=3,width=685,fg_color="black")
        self.emptyspace.place(x=80,y=46)
        self.display_products()
        self.display_random_product()
        self.update_title()


    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mouse_wheel(self, event):
        if event.delta:  # Windows and MacOS
            self.canvas.yview_scroll(-int(event.delta /100), "units")
        
    def _on_enter(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
    def _on_leave(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def update_title(self):
        self.controller.title("Products - Laxmi Honey Industry")


    def display_products(self):
        products = self.products
        user = self.user
        card_width = 200
        card_height = 250
        padding_x = 20
        padding_y = 20
        start_x = 20
        start_y = 20
        x_offset = card_width + padding_x
        y_offset = card_height + padding_y
        random.shuffle(products)

        for index, product in enumerate(products):  
            row = index // 3
            column = index % 3
            x = start_x + column * x_offset
            y = start_y + row * y_offset
            self.product_card = CTkButton(self.inner_frame,
                                          text="",
                                        width=card_width,
                                        height=card_height,
                                        fg_color="#52606D",
                                        corner_radius=10,
                                        border_width=1,
                                        border_color="gray",
                                        hover_color="#52606D",
                                        command=lambda p=product: self.show_product_details(p)
                                        )
            self.product_card.place(x=x, y=y)
            
            image_data = product[2]
            image = Image.open(io.BytesIO(image_data))
            # Resize image to fit label dimensions
            label_width = 150
            label_height = 100
            image = image.resize((label_width, label_height), Image.LANCZOS)
            radius = 20 
            mask = Image.new('L', (label_width, label_height), 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, label_width, label_height), radius, fill=255)            
            image.putalpha(mask)
            photo = ImageTk.PhotoImage(image)
            product_image = CTkLabel(self.product_card, image=photo, height=label_height, width=label_width, text="")
            product_image.image = photo  # Keeping a reference to avoid garbage collection
            product_image.place(x=20, y=5)
            product_image.bind("<Button-1>", lambda event, product=product: self.show_product_details(product))
            product_name = CTkLabel(self.product_card, text=f"{product[0]}", wraplength=150,text_color="Black", font=("verdana", 15))
            product_name.place(x=15, y=110)
            product_name.bind("<Button-1>", lambda event, product=product: self.show_product_details(product))
            product_price = CTkLabel(self.product_card, text=f"Rs.{product[3]}", text_color="Black", font=("verdana", 12))
            product_price.place(x=15, y=165)
            product_stock = CTkLabel(self.product_card, text=f"Stock:{product[4]}", text_color="Black", font=("verdana", 11))
            product_stock.place(x=135, y=165)
            self.add_to_cart_button = CTkButton(
                self.product_card,
                text="Add to Cart",
                font=("verdana", 12),
                fg_color="aquamarine",
                text_color="black",
                hover_color="#6ce2ba",
                command=lambda p_id=product[5],u_id=user[0],rate=product[3]: self.add_to_cart(p_id,u_id,rate)
            )
            self.add_to_cart_button.place(x=30,y=202)
            Tooltip(self.add_to_cart_button, f"Add {product[0]} to your cart")

    def show_product_details(self, product):
        for widget in self.leftcontainer.winfo_children():
            widget.destroy()
        
        product_detail = CTkLabel(self.leftcontainer, text=f"Product Details", text_color="Black", font=("verdana", 18))
        product_detail.place(x=20, y=10)
        image_data = product[2]
        image = Image.open(io.BytesIO(image_data))
        label_width = 400
        label_height = 250
        image = image.resize((label_width, label_height), Image.LANCZOS)
        radius = 20 
        mask = Image.new('L', (label_width, label_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, label_width, label_height), radius, fill=255)
        image.putalpha(mask)
        photo = ImageTk.PhotoImage(image)
        product_image = CTkLabel(self.leftcontainer, image=photo, height=label_height, width=label_width, text="")
        product_image.image = photo  # Keeping a reference of every image to avoid garbage collection
        product_image.place(x=75, y=35)

        product_name = CTkLabel(self.leftcontainer, text=f"{product[0]}", text_color="Black", font=("verdana", 24))
        product_name.place(x=75, y=300)

        product_description = CTkLabel(self.leftcontainer, text=f"{product[1]}",wraplength=400, text_color="Black", justify="left",font=("verdana", 12.5))
        product_description.place(x=75, y=335)

        product_price = CTkLabel(self.leftcontainer, text=f"Rs.{product[3]}", text_color="Black", font=("verdana", 18))
        product_price.place(x=75, y=500)

        product_stock = CTkLabel(self.leftcontainer, text=f"Stocks:{product[4]}", text_color="Black", font=("verdana", 15))
        product_stock.place(x=475, y=500)

        add_to_cart_button = CTkButton(
            self.leftcontainer,
            text="Add to Cart",
            font=("verdana", 16),
            fg_color="aquamarine",
            text_color="black",
            hover_color="#6ce2ba",width=150,height=50,
            command=lambda p_id=product[5], u_id=self.user[0],rate=product[3]: self.add_to_cart(p_id, u_id,rate)
        )
        add_to_cart_button.place(x=220, y=530)
        Tooltip(add_to_cart_button, f"Add {product[0]} to your cart")
    
    def display_random_product(self):
        products = fetch_products()
        if products:
            random_product = random.choice(products)  # Select a random product
            self.show_product_details(random_product)

    
    def add_to_cart(self, product_id, user_id,rate):
        try:
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c = conn.cursor()
            # Check if the product is already in the cart for this user
            c.execute("SELECT * FROM cart WHERE user_id = ? AND product_id = ?", (user_id, product_id))
            existing_item = c.fetchone()
            d = conn.cursor()
            d.execute("SELECT name,stock FROM products WHERE ID = ?",(product_id,))
            productname=d.fetchone()
            if existing_item:
                show_popup_message(self.containermain,f"{productname[0]} is already in your cart!!!")
            else:
                if productname[1]<=0:
                    show_popup_message(self.containermain,f"{productname[0]} is curently out of stock!!!")
                else:    
                    c.execute("INSERT INTO cart (user_id, product_id, rate) VALUES (?, ?, ?)", (user_id, product_id,rate))
                    conn.commit()
                    show_popup_message(self.containermain,f"{productname[0]} added to your cart succesfully")

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

        finally:
            conn.close()

        
    def update_title(self):
        self.controller.title("Products - Laxmi Honey Industry")
        

class CartPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.topframe=controller.topframe
        screen_height = self.winfo_screenheight()
        self.user = controller.load_user_data()
        self.sidebuttoncontainer=CTkFrame(self,width=60,height=screen_height,fg_color="orange",corner_radius=0)
        self.sidebuttoncontainer.place(x=0,y=0)
        self.cartbtn = CTkButton(self.sidebuttoncontainer,width=48,height=320,fg_color="orange",hover_color="slategray",text="C\nA\nR\nT",text_color="black",corner_radius=7, command=lambda: self.show_frame("CartCartPage"))
        self.cartbtn.place(x=8,y=5)
        self.orderbtn = CTkButton(self.sidebuttoncontainer,width=48,height=320,fg_color="orange",hover_color="gray",text="O\nR\nD\nE\nR\nS",text_color="black",corner_radius=7, command=lambda: self.show_frame("CartOrderPage"))
        self.orderbtn.place(x=8,y=330)
        Tooltip(self.orderbtn," Your orders ")
        self.containermain = CTkFrame(self,fg_color="slate gray",corner_radius=0)
        self.containermain.pack(side=LEFT,padx=52)
        self.frames = {}
        for F in (CartCartPage,CartOrderPage):
            page_name = F.__name__
            frame = F(parent=self.containermain, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(fg_color="yellow")
        self.show_frame("CartCartPage")

        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "CartCartPage":
            self.configure_buttons_cartcart()
        elif page_name == "CartOrderPage":
            self.configure_buttons_cartorder()

    def configure_buttons_cartcart(self):
        self.orderbtn.configure(fg_color="orange",hover_color="slategray",)
        self.cartbtn.configure(fg_color="slategray",hover_color="slategray",)
    def configure_buttons_cartorder(self):
        self.orderbtn.configure(fg_color="gray",hover_color="gray",)
        self.cartbtn.configure(fg_color="orange",hover_color="gray")
    def update_title(self):
        self.controller.title("Cart/Orders - Laxmi Honey Industry")
            

class CartCartPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = controller.user
        self.containermain = CTkFrame(self,height=1000,width=1500,fg_color="slategray",corner_radius=0)
        self.containermain.pack(fill=BOTH)
        self.rightcontainer = CTkFrame(self.containermain,fg_color="slategray",height=650,width=700)
        self.rightcontainer.place(x=800,y=50)        
        self.net_total_label = CTkLabel(self.rightcontainer, text="Net Total: Rs. 00.0", text_color="black", font=("verdana", 20))
        self.net_total_label.place(x=40, y=620)
        place_order_button = CTkButton(
            self.rightcontainer,
            text="Place Order",
            font=("verdana", 16),
            fg_color="aquamarine",
            text_color="black",
            hover_color="#58b294",
            command= self.place_order,
            height = 40,
            width=140
        )
        place_order_button.place(x=450, y=620)   
        
        self.leftcontainer=CTkFrame(self.containermain,fg_color="slategray",height=700,width=800)
        self.leftcontainer.place(x=10,y=10)
        
        self.cartitemtext = CTkLabel(self.leftcontainer,text="Cart Items",text_color="black",width=780,font=("verdana",24),anchor="w")
        self.cartitemtext.place(x=20,y=10)
        
        self.refresh_cart = CTkButton(self.leftcontainer,text="↻",fg_color="slategray",text_color="black",font=("verdana",24,"bold"),hover_color="slategray",command=self.show_cart_products)
        self.refresh_cart.place(x=600,y=10)
        
        self.canvas = CTkCanvas(self.leftcontainer, height=830, width=850)
        self.canvas.place(x=0, y=58)
        
        self.scrollbar = CTkScrollbar(self.leftcontainer,height=500, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.place(x=0, y=65) 
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.inner_frame = CTkFrame(self.canvas, width=750, height=800,corner_radius=0,fg_color="slategray",bg_color="slategray")  # Adjust the height of inner_frame as needed
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        
        self.emptyspace = CTkFrame(self.leftcontainer, height=3,width=685,fg_color="black")
        self.emptyspace.place(x=0,y=45)
        
        self.show_cart_products()
            
        height_for_inner_frame = 800

        if len_products>4:
            height_for_inner_frame = len_products*150
        self.inner_frame.configure(height=height_for_inner_frame)
        self.leftcontainer.bind("<MouseWheel>", self._on_mouse_wheel)  # Bind to leftcontainer


    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mouse_wheel(self, event):
        if event.delta:
            self.canvas.yview_scroll(-int(event.delta / 120), "units")
        
        
    def get_cart_products(self, user_id):
        conn = None
        c = None
        try:
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c = conn.cursor()
            c.execute("""
                SELECT products.*, cart.quantity,cart.subtotal
                FROM cart
                JOIN products ON cart.product_id = products.ID
                WHERE cart.user_id = ?
            """, (user_id,))
            cart_products = c.fetchall()
            
            return cart_products

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

        finally:
            # Ensuring the cursor and connection are closed even if an error occurs
            if c is not None:
                c.close()
            if conn is not None:
                conn.close()
    
    
    def show_cart_products(self):

        # Clearing the inner_frame
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        user_id = self.user[0]

        # Fetching products from cart
        products = self.get_cart_products(user_id)
        # declearing global variable to increase or decrease the size of innerframe
        global len_products
        len_products= len(products)
        self.update_net_total(products)

        x_position = 40
        y_position = 10
        card_width = 600
        card_height = 120
        margin = 15
        for product in products:
        # Displaying products as cards
            self.card_frame = CTkFrame(self.inner_frame, width=card_width, height=card_height, fg_color="#52606D", corner_radius=10)
            self.card_frame.place(x=x_position, y=y_position)

            image_data = product[3]
            image = Image.open(io.BytesIO(image_data))
            label_width = 150
            label_height = 100
            image = image.resize((label_width, label_height), Image.LANCZOS)
            radius = 20  
            mask = Image.new('L', (label_width, label_height), 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, label_width, label_height), radius, fill=255)
            image.putalpha(mask)
            photo = ImageTk.PhotoImage(image)
            product_image = CTkLabel(self.card_frame, image=photo, height=label_height, width=label_width, text="")
            product_image.image = photo  
            product_image.place(x=5, y=2)

            # Add product details
            product_name = CTkLabel(self.card_frame, text=product[1], text_color="black", font=("verdana", 19))
            product_name.place(x=155, y=15)

            product_price = CTkLabel(self.card_frame, text=f"Rs. {product[4]}", text_color="black", font=("verdana", 14))
            product_price.place(x=155, y=45)

            product_quantity_text = CTkLabel(self.card_frame, text=f"Quantity:",width=50,text_color="black", font=("verdana", 14))
            product_quantity_text.place(x=455, y=65)
            
            product_quantity = CTkEntry(self.card_frame,width=35,fg_color="#52606D",justify="center",text_color="black",border_width=0)
            product_quantity.place(x=541,y=65)
            if len(str(product[6]))<2:
                product_quantity.insert(0, f"0{product[6]}")
            else:
                product_quantity.insert(0,f"{product[6]}")
            product_quantity.bind("<Return>", lambda event, entry=product_quantity, p_id=product[0], u_id=self.user[0]: self.update_quantity(entry, p_id, u_id))

            quantity_down = CTkButton(self.card_frame, text="▼", font=("arial", 12), text_color="black",fg_color="#52606D", hover_color="#3b3b3b", width=10,height=10,command=lambda e=product_quantity, p_id=product[0], u_id=self.user[0]: self.adjust_quantity(e, -1, p_id, u_id))
            quantity_down.place(x=525, y=67)
            
            quantity_up = CTkButton(self.card_frame, text="▲", font=("arial", 12), text_color="black", fg_color="#52606D", hover_color="#3b3b3b", width=10,height=10, command=lambda e=product_quantity, p_id=product[0], u_id=self.user[0]: self.adjust_quantity(e, 1, p_id, u_id))
            quantity_up.place(x=574, y=67)
            
            subtotal = CTkLabel(self.card_frame,text=f"Subtotal: {product[7]}",text_color="black",font=("arial", 15),)
            subtotal.place(x=455,y=90)

            product_delete = CTkButton(self.card_frame,text="X",font=("comic sans ms",20,"bold"),text_color="black",fg_color="#52606D",hover_color="#3b3b3b",width=20,command=lambda p_id=product[0],u_id=self.user[0]: self.del_cart_item(p_id,u_id))
            product_delete.place(x=568,y=2)
            Tooltip(product_delete," Remove from cart ")
            
            x_position += card_width + margin
            if x_position + card_width > self.inner_frame.winfo_width():
                x_position = 40
                y_position += card_height + margin
            self.update_net_total(products)
            self.show_receipt_products()
        
    def show_receipt_products(self):
        for widget in self.rightcontainer.winfo_children():
            widget.destroy()
        user_id = self.user[0]

        products = self.get_cart_products(user_id)

        self.receipt_card_frame_title = CTkFrame(self.rightcontainer, width=600, height=60, fg_color="gray", corner_radius=10)
        self.receipt_card_frame_title.place(x=30, y=0)

        product_sn_title = CTkLabel(self.receipt_card_frame_title, text=f"S.N.", width=50,text_color="black", font=("verdana", 18))
        product_sn_title.place(x=5, y=15)

        product_name_title = CTkLabel(self.receipt_card_frame_title, text="Product", wraplength=100,text_color="black", font=("verdana", 18))
        product_name_title.place(x=65, y=15)

        product_price_title = CTkLabel(self.receipt_card_frame_title, text=f"Price", text_color="black", font=("verdana", 18))
        product_price_title.place(x=255, y=15)

        product_quantity_text_title = CTkLabel(self.receipt_card_frame_title, text=f"Quantity",width=50,text_color="black", font=("verdana", 18))
        product_quantity_text_title.place(x=375, y=15)
            
        subtotal_title = CTkLabel(self.receipt_card_frame_title,text=f"Subtotal",text_color="black",font=("arial", 18),)
        subtotal_title.place(x=475,y=15)
 
        x_position = 30
        y_position = 50
        card_width = 600
        card_height = 60
        margin = 1
        x = 1
        for product in products:
            self.receipt_card_frame = CTkFrame(self.rightcontainer, width=card_width, height=card_height, fg_color="lightgray", corner_radius=10)
            self.receipt_card_frame.place(x=x_position, y=y_position)

            product_sn = CTkLabel(self.receipt_card_frame, text=f"{x}", width=50,text_color="black", font=("verdana", 15))
            product_sn.place(x=5, y=15)
            
            product_name = CTkLabel(self.receipt_card_frame, text=product[1], wraplength=200,text_color="black", font=("verdana", 15))
            product_name.place(x=65, y=15)

            product_price = CTkLabel(self.receipt_card_frame, text=f"Rs. {product[4]}", text_color="black", font=("verdana", 15))
            product_price.place(x=255, y=15)

            product_quantity_text = CTkLabel(self.receipt_card_frame, text=f"{product[6]}",width=50,text_color="black", font=("verdana", 15))
            product_quantity_text.place(x=375, y=15)
           
            subtotal = CTkLabel(self.receipt_card_frame,text=f"{product[7]}",text_color="black",font=("arial", 15),)
            subtotal.place(x=475,y=15)
            
            x_position += card_width + margin
            if x_position + card_width > self.inner_frame.winfo_width():
                x_position = 30
                y_position += card_height + margin
            x+=1

        place_order_button = CTkButton(
            self.rightcontainer,
            text="Place Order",
            font=("verdana", 16),
            fg_color="aquamarine",
            text_color="black",
            hover_color="#58b294",
            command= self.place_order,
            height = 40,
            width=140
        )
        place_order_button.place(x=450, y=y_position+100) 
        self.net_total_label = CTkLabel(self.rightcontainer, text="Net Total: Rs. 00.0", text_color="black", font=("verdana", 20))
        self.net_total_label.place(x=50, y=y_position+102)
        self.update_net_total(products)
        
            
    def update_net_total(self, products):
        net_total = sum(product[7] for product in products)
        self.net_total_label.configure(text=f"Net Total: Rs. {net_total}")

    
    
    def generate_html_receipt(self, user, order_id, products, net_total):
        receipt = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .container {{ padding: 20px; border: 1px solid #ccc; }}
                .header {{ text-align: center; }}
                .products {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                .products th, .products td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                .products th {{ background-color: #f2f2f2; }}
                .total {{ margin-top: 20px; font-size: 1.2em; font-weight: bold; }}
                .footer {{ margin-top: 20px; text-align: center; font-size: 0.9em; color: #777; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Laxmi Honey Industry</h1>
                    <h2>Order Reciept</h2>
                    <p>Order ID: {order_id}</p>
                    <p>Ordered By: {user[1]} {user[2]}</p>
                    <p>Email: {user[4]}</p>
                </div>
                <table class="products">
                    <tr>
                        <th>Product Name</th>
                        <th>Quantity</th>
                        <th>Price</th>
                    </tr>
                    {" ".join(f"<tr><td>{product[1]}</td><td>{product[6]}</td><td>Rs. {product[4]}</td></tr>" for product in products)}
                </table>
                <p class="total">Net Total: Rs. {net_total}</p>
                <p class="footer">Order Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        </body>
        </html>
        """
        return receipt

    def place_order(self):
        user = self.user
        user_id = user[0]
        products = self.get_cart_products(user_id)
        conn = None
        c = None
        try:
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c = conn.cursor()
            c.execute("SELECT balance FROM users WHERE ID = ?",(user_id,))
            user_balance = c.fetchone()[0]
            if not products:
                show_popup_message(self.containermain, "Cart is empty.")
                return
            net_total = sum(product[7] for product in products)
            if user_balance < net_total:
                show_popup_message(self.containermain, "Insufficient balance!!!")
            else:
                if messagebox.askyesno("Order Confirm", "I would like to ask you to check your address\nAre you sure you want to place this order?"):
                    order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    c.execute("INSERT INTO orders (user_id, order_date, total_amount) VALUES (?, ?, ?)", (user_id, order_date, net_total))
                    order_id = c.lastrowid
                    for product in products:
                        c.execute("INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)", (order_id, product[0], product[6], product[4]))
                    c.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))
                    show_popup_message(self.containermain, f"Order id : {order_id}\n placed successfully")
                    conn.commit()
                    # Refreshing the cart page after placing orders from cart
                    self.show_cart_products()
                    # Generating the HTML receipt
                    receipt = self.generate_html_receipt(user, order_id, products, net_total)
                    # Send the receipt via email
                    subject = "Your Order Receipt"
                    send_html_email(user[4], subject, receipt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            show_popup_message(self.containermain, "An error occurred while placing the order.")
        except Exception as e:
            print(f"General error: {e}")
            show_popup_message(self.containermain, "An unexpected error occurred.")
        finally:
            if c:
                c.close()
            if conn:
                conn.close()
                
                
    def adjust_quantity(self, entry_widget, adjustment, p_id, u_id):
        products = self.get_cart_products(u_id)
        try:
            # Fetch and validate current quantity
            current_value = int(entry_widget.get())
            new_value = current_value + adjustment

            if new_value < 1:
                show_popup_message(self.containermain, "Quantity cannot be less than 1")
                self.update_net_total(products)
                self.show_cart_products()
                return
            
            # Check stock availability
            with sqlite3.connect("laxmihoneyindustry.db") as conn:
                c = conn.cursor()
                c.execute("SELECT stock FROM products WHERE id = ?", (p_id,))
                stock_quantity = c.fetchone()[0]

                if new_value > stock_quantity:
                    show_popup_message(self.containermain, "Quantity exceeds stock available")
                    self.update_net_total(products)
                    self.show_cart_products()
                    return

                c.execute("UPDATE cart SET quantity = ? WHERE product_id = ? AND user_id = ?", (new_value, p_id, u_id))
                conn.commit()

            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, str(new_value).zfill(2))
            self.update_net_total(products)
            self.show_cart_products()

        except ValueError:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, "01")

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            
    def update_quantity(self, entry_widget, p_id, u_id):
        products = self.get_cart_products(u_id)
        try:
            new_value = int(entry_widget.get())
            if new_value < 1:
                show_popup_message(self.containermain, "Quantity can't be < 1")
                return
            
            with sqlite3.connect("laxmihoneyindustry.db") as conn:
                c = conn.cursor()
                c.execute("SELECT stock FROM products WHERE id = ?", (p_id,))
                stock_quantity = c.fetchone()[0]
                if new_value > stock_quantity:
                    show_popup_message(self.containermain, "Quantity exceeds stock available")
                    return
                c.execute("UPDATE cart SET quantity = ? WHERE product_id = ? AND user_id = ?", (new_value, p_id, u_id))
                conn.commit()
            self.update_net_total(products)
            self.show_cart_products()
        except ValueError:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, "01")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            
    def del_cart_item(self,p_id,u_id):
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this product from cart?"):
            try:
                conn = sqlite3.connect("laxmihoneyindustry.db")
                c = conn.cursor()
                c.execute("DELETE FROM cart WHERE product_id = ? and user_id = ?", (p_id,u_id))
                conn.commit()
                d = conn.cursor()
                d.execute("SELECT name FROM products WHERE ID = ? ", (p_id,))
                productname = d.fetchone()
                conn.close()
                self.show_cart_products()
                show_popup_message(self.containermain,f"{productname[0]} removed !")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                
class CartOrderPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = controller.user
        self.containermain = CTkFrame(self,height=1000,width=1000,fg_color="slategray",corner_radius=0)
        self.containermain.pack(fill=BOTH)
        
        self.ordereditemtext = CTkLabel(self.containermain,text="Your Orders",text_color="black",width=780,font=("verdana",24),anchor="w")
        self.ordereditemtext.place(x=40,y=10)
        
        self.orders_by = CTkButton(self.containermain,text="≡",fg_color="slategray",width=20,text_color="black",font=("comic sans ms",35,"bold"),hover_color="#52606D",command=self.show_menu)
        self.orders_by.place(x=1390,y=-10)
        self.menu = tk.Menu(self.containermain, tearoff=0)
        self.menu.add_command(label="Sort by Date", command=lambda: self.show_user_orders('date'))
        self.menu.add_command(label="Sort by Amount", command=lambda: self.show_user_orders('amount'))
        Tooltip(self.orders_by," Sort By ")
        
        self.canvas = CTkCanvas(self.containermain, height=830, width=2000)
        self.canvas.place(x=0, y=58)
        self.scrollbar = CTkScrollbar(self.containermain,height=700, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.place(x=1300, y=65)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.inner_frame = CTkFrame(self.canvas, width=2000, height=800,corner_radius=0,fg_color="slategray",bg_color="slategray")  # Adjust the height of inner_frame as needed
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        
        self.emptyspace = CTkFrame(self.containermain, height=3,width=2000,fg_color="black")
        self.emptyspace.place(x=0,y=45)
        
        self.show_user_orders(sort_by="date")
        
        height_for_inner_frame = 800
        if len_orders>4:
            height_for_inner_frame = len_orders*100
        self.inner_frame.configure(height=height_for_inner_frame)

    def show_menu(self):
        try:
            self.menu.tk_popup(self.orders_by.winfo_rootx(), self.orders_by.winfo_rooty() + self.orders_by.winfo_height())
        finally:
            self.menu.grab_release()
            
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def _on_mouse_wheel(self, event):
        if event.num == 5 or event.delta == -120:  # For Linux and Windows scrolling down
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:  # For Linux and Windows scrolling up
            self.canvas.yview_scroll(-1, "units")
    
    
    def get_user_orders(self, user_id, sort_by=None):
        conn = None
        c = None
        try:
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c = conn.cursor()
            query = "SELECT * FROM orders WHERE user_id = ?"
            params = [user_id]
            
            if sort_by == 'date':
                query += " ORDER BY order_date DESC"
            elif sort_by == 'amount':
                query += " ORDER BY total_amount DESC"
            
            c.execute(query, params)
            user_orders = c.fetchall()
            return user_orders

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

        finally:
            if c is not None:
                c.close()
            if conn is not None:
                conn.close()
                
        
    def show_user_orders(self,sort_by):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
            
        user_id = self.user[0]
        orders = self.get_user_orders(user_id, sort_by)
        global len_orders
        len_orders= len(orders)
        self.orders_title_frame = CTkFrame(self.inner_frame, width=800, height=60, fg_color="gray", corner_radius=10)
        self.orders_title_frame.place(x=360, y=10)

        order_sn_title = CTkLabel(self.orders_title_frame, text=f"S.N.", width=50,text_color="black", font=("verdana", 15))
        order_sn_title.place(x=15, y=15)

        order_id_title = CTkLabel(self.orders_title_frame, text="Order ID",text_color="black", font=("verdana", 15))
        order_id_title.place(x=125, y=15)

        order_date_title = CTkLabel(self.orders_title_frame, text=f"Ordered Date", text_color="black", font=("verdana", 15))
        order_date_title.place(x=275, y=15)

        nettotal_title = CTkLabel(self.orders_title_frame,text=f"Total Paid",text_color="black",font=("arial", 15),)
        nettotal_title.place(x=625,y=15)

        x_position = 360
        y_position = 60
        card_width = 800
        card_height = 60
        margin = 5
        x=1
        for order in orders:
            self.card_frame = CTkFrame(self.inner_frame, width=card_width, height=card_height, fg_color="lightgray", corner_radius=10)
            self.card_frame.place(x=x_position, y=y_position)

            snnbr = CTkLabel(self.card_frame, text=f"{x}",width=50, text_color="black", font=("verdana", 19))
            snnbr.place(x=15, y=15)

            order_id = CTkLabel(self.card_frame, text=f"{order[0]}", text_color="black", font=("verdana", 19),anchor="center")
            order_id.place(x=125, y=15)

            ordered_date = CTkLabel(self.card_frame, text=f"{order[2]}",text_color="black", font=("verdana", 19))
            ordered_date.place(x=275, y=15)
            
            nettotal = CTkLabel(self.card_frame,text=f"Rs. {order[3]}",text_color="black",font=("arial", 19),)
            nettotal.place(x=625,y=15)

            y_position += card_height + margin
            x+=1
        


class AccountPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        screen_height = self.winfo_screenheight()
        self.user = controller.load_user_data()
        self.sidebuttoncontainer = CTkFrame(self, width=60, height=screen_height, fg_color="orange", corner_radius=0)
        self.sidebuttoncontainer.place(x=0, y=0)
        self.userbtn = CTkButton(self.sidebuttoncontainer, width=48, height=320, fg_color="orange", hover_color="slategray", text="U\nS\nE\nR", text_color="black", corner_radius=7, command=lambda: self.show_frame("UserAccountPage"))
        self.userbtn.place(x=8, y=5)

        self.adminbtn = CTkButton(self.sidebuttoncontainer, width=48, height=320, fg_color="orange", hover_color="dark gray", text="A\nD\nM\nI\nN", text_color="black", corner_radius=7, command=lambda: self.handle_admin_button())
        self.adminbtn.place(x=8, y=330)

        self.containermain = CTkFrame(self, fg_color="slate gray", corner_radius=0)
        self.containermain.pack(side=LEFT, padx=52)

        self.frames = {}
        for F in (UserAccountPage, AdminAccountPage):
            page_name = F.__name__
            frame = F(parent=self.containermain, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("UserAccountPage")

    def handle_admin_button(self):
        if self.user[8]:  # Check if the user is an admin
            self.show_frame("AdminAccountPage")
        else:
            messagebox.showerror("Access Denied", "You cannot access the admin panel")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "UserAccountPage":
            self.configure_buttons_useraccount()
        elif page_name == "AdminAccountPage":
            self.configure_buttons_adminaccount()

    def configure_buttons_useraccount(self):
        self.adminbtn.configure(fg_color="orange", hover_color="slategray")
        self.userbtn.configure(fg_color="slategray", hover_color="slategray")

    def configure_buttons_adminaccount(self):
        self.adminbtn.configure(fg_color="dark gray", hover_color="darkgray")
        self.userbtn.configure(fg_color="orange", hover_color="darkgray")

    def update_title(self):
        self.controller.title("Account - Laxmi Honey Industry")

class UserAccountPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = controller.user

        self.containermain = CTkFrame(self, height=1000, width=1500, fg_color="slategray",bg_color="slategray", corner_radius=0)
        self.containermain.pack(fill=BOTH)

        self.profile_image_frame = CTkFrame(self.containermain, fg_color="slategray",height=500, width=400)
        self.profile_image_frame.place(x=150, y=100)
        self.emptyspace = CTkLabel(self.profile_image_frame, height=30,width=350,bg_color="slategray",text="")
        self.emptyspace.pack()
        self.profile_name = CTkLabel(self.profile_image_frame,text=f"Hi!, {self.user[1]}",text_color="black",font=("verdana",29,"underline",))
        self.profile_name.pack()
        text_label = CTkLabel(self.profile_image_frame, text=f"Welcome back!!", text_color="black", font=("comic sans ms", 18), anchor="w")
        text_label.pack()
        self.emptyspace = CTkLabel(self.profile_image_frame, height=30,width=350,bg_color="slategray",text="")
        self.emptyspace.pack()

        self.profile_pic = CTkLabel(self.profile_image_frame, bg_color="slategray",fg_color="slategray",text="")
        self.profile_pic.pack()

        self.upload_btn = CTkButton(self.profile_image_frame,height=30,width=120,bg_color="slategray",fg_color="light gray", text="      Upload",font=("arial",15),text_color="black",hover_color="gray" ,command=self.upload_profile_picture)
        self.upload_btn.pack(pady=0)
        cam1img = ImageTk.PhotoImage(camimg)

        self.camlbl = CTkLabel(self.upload_btn,image=cam1img,height=26,width=24,text="",bg_color="light gray",fg_color="light gray",corner_radius=50)
        self.camlbl.place(x=3,y=1)
        def on_web_enter(event):
            self.camlbl.configure(fg_color="gray",bg_color="gray")
        self.upload_btn.bind("<Enter>", on_web_enter)

        def on_web_leave(event):
            self.camlbl.configure(fg_color="light gray",bg_color="light gray")
        self.upload_btn.bind("<Leave>", on_web_leave)


        self.load_user_profile_picture()
        edit1img = ImageTk.PhotoImage(editimg)

        self.user_detail_frame = CTkFrame(self.containermain, fg_color="slategray",height=550, width=600)
        self.user_detail_frame.place(x=700, y=50)
        self.infolbl = CTkLabel(self.user_detail_frame,text="Your Information",text_color="black",font=("verdana",30))
        self.infolbl.place(x=140,y=20)
        self.edit = CTkButton(self.user_detail_frame,height=30,width=70,bg_color="slategray",fg_color="light gray",hover_color="dark gray",text="Edit",text_color="black",font=("arial",15),anchor="e")
        self.edit.place(x=500,y=40)
        self.editlogo = CTkLabel(self.edit,image=edit1img,height=20,text="",bg_color="light gray",fg_color="light gray",corner_radius=50)
        self.editlogo.place(x=0,y=5)
        def on_web_enter(event):
            self.editlogo.configure(fg_color="dark gray",bg_color="dark gray")
        self.edit.bind("<Enter>", on_web_enter)

        def on_web_leave(event):
            self.editlogo.configure(fg_color="light gray",bg_color="light gray")
        self.edit.bind("<Leave>", on_web_leave)
        
        self.userdict = {
            "UserName  : ":self.user[3],
            "Firstname : ":f"{self.user[1]}",
            "Lastname  : ":f"{self.user[2]}",
            "E-Address : ":f"{self.user[4]}",
        }
        exclude_keys = {'id'}  # Set of keys to exclude
        y=100
        for key, value in self.userdict.items():
            if key not in exclude_keys:
                print(f"Key: {key}, Value: {value}")

                self.attribute = CTkLabel(self.user_detail_frame,text=f"{key}",text_color="black",font=("verdana",20))
                self.attribute.place(x=90,y = y)
                self.value = CTkLabel(self.user_detail_frame,text=f" {value}",text_color="black",font=("verdana",19),width=200,height=30,fg_color="light gray",corner_radius=10,anchor="w")
                self.value.place(x=240,y=y)
                y+=60
        self.address = CTkLabel(self.user_detail_frame,text=f"B-Address : ",text_color="black",font=("verdana",20))
        self.address.place(x=90,y = y)
        self.avalue = CTkLabel(self.user_detail_frame,text=f"{self.user[13]}-{self.user[14]}, {self.user[15]}, {self.user[12]},\n{self.user[11]}, {self.user[10]}",text_color="black",font=("verdana",15),width=200,height=60,fg_color="light gray",corner_radius=10,)
        self.avalue.place(x=240,y=y)
        self.balance = CTkLabel(self.user_detail_frame,text=f"Balance : ",text_color="black",font=("verdana",20))
        self.balance.place(x=90,y = y+80)
        self.bvalue = CTkLabel(self.user_detail_frame,text=f"Rs. {self.user[16]}",text_color="black",font=("verdana",18),width=300,height=35,fg_color="light gray",corner_radius=10,anchor="w")
        self.bvalue.place(x=240,y=y+80)
        
        withdrawimg = ImageTk.PhotoImage(moneydepoimg)
        depoimg = moneydepoimg.transpose(Image.FLIP_TOP_BOTTOM)
        depoimg = ImageTk.PhotoImage(depoimg)


        self.deposit_btn = CTkButton(self.user_detail_frame,height=35,width=120,bg_color="slategray",fg_color="light gray", text="Deposit  ",font=("arial",15),text_color="black",hover_color="dark gray",anchor="e", command=self.open_deposit_dialog )
        self.deposit_btn.place(x=250,y=y+140)
        self.depolbl = CTkLabel(self.deposit_btn,image=depoimg,text="",bg_color="light gray",fg_color="light gray",corner_radius=50)
        self.depolbl.place(x=3,y=1)
        self.withdraw_btn = CTkButton(self.user_detail_frame,height=35,width=120,bg_color="slategray",fg_color="light gray", text="Withdraw",font=("arial",15),text_color="black",hover_color="dark gray",anchor="e", command=self.open_withdraw_dialog )
        self.withdraw_btn.place(x=420,y=y+140)
        self.withlbl = CTkLabel(self.withdraw_btn,image=withdrawimg,text="",bg_color="light gray",fg_color="light gray",corner_radius=50)
        self.withlbl.place(x=1,y=3)
        
        def on_web_enter(event):
            self.depolbl.configure(fg_color="dark gray",bg_color="dark gray")
        self.deposit_btn.bind("<Enter>", on_web_enter)

        def on_web_leave(event):
            self.depolbl.configure(fg_color="light gray",bg_color="light gray")
        self.deposit_btn.bind("<Leave>", on_web_leave)
        def on_web_enter(event):
            self.withlbl.configure(fg_color="dark gray",bg_color="dark gray")
        self.withdraw_btn.bind("<Enter>", on_web_enter)

        def on_web_leave(event):
            self.withlbl.configure(fg_color="light gray",bg_color="light gray")
        self.withdraw_btn.bind("<Leave>", on_web_leave)
        
        refimg = ImageTk.PhotoImage(refreshimg)
        self.ref_btn = CTkButton(self.containermain,height=35,width=120,bg_color="slategray",fg_color="light gray",hover_color="dark gray",text="  Refresh",text_color="black",font=("arial",15),anchor="e",corner_radius=50,command=self.refresh_balance_display)
        self.ref_btn.place(relx=0.41,y=600)
        self.reflogo = CTkLabel(self.ref_btn,image=refimg,height=20,width=20,text="",bg_color="light gray",fg_color="light gray",corner_radius=50)
        self.reflogo.place(x=5,y=8)
        def on_web_enter(event):
            self.reflogo.configure(fg_color="dark gray",bg_color="dark gray")
        self.ref_btn.bind("<Enter>", on_web_enter)

        def on_web_leave(event):
            self.reflogo.configure(fg_color="light gray",bg_color="light gray")
        self.ref_btn.bind("<Leave>", on_web_leave)
        
    def open_deposit_dialog(self):
        dialog = AmountDialog(self, "Deposit")
        dialog.grab_set()

    def open_withdraw_dialog(self):
        dialog = AmountDialog(self, "Withdraw")
        dialog.grab_set()

    def handle_transaction(self, action, amount):
        try:
            conn = sqlite3.connect("laxmihoneyindustry.db")
            c = conn.cursor()
            
            if action == "Deposit":
                c.execute("UPDATE users SET balance = balance + ? WHERE ID = ?", (amount, self.user[0]))
            elif action == "Withdraw":
                c.execute("SELECT balance FROM users WHERE ID = ?", (self.user[0],))
                current_balance = c.fetchone()[0]
                if amount > current_balance:
                    messagebox.showerror("Error", "Insufficient balance.")
                    return
                c.execute("UPDATE users SET balance = balance - ? WHERE ID = ?", (amount, self.user[0]))
            
            conn.commit()
            conn.close()
            show_popup_message(self.containermain,f"{action}  successful!")
            
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def refresh_balance_display(self):
        conn = sqlite3.connect("laxmihoneyindustry.db")
        c = conn.cursor()
        c.execute("SELECT balance FROM users WHERE ID = ?", (self.user[0],))
        new_balance = c.fetchone()[0]
        conn.close()
        
        self.bvalue.configure(text=f"Rs. {new_balance}")
        self.load_user_profile_picture()

        
    def load_user_profile_picture(self):
        conn = sqlite3.connect("laxmihoneyindustry.db")
        c = conn.cursor()
        user_id = self.user[0]  
        c.execute("SELECT * FROM users WHERE id=?", (user_id,))
        self.user = c.fetchone()
        conn.commit()
        conn.close()
        if self.user[9]:  
            profile_pic_blob = self.user[9]
            self.upload_btn.configure(text="    Edit")
            self.camlbl.place(x=7,y=1)
            try:
                image = Image.open(io.BytesIO(profile_pic_blob))
                image = image.resize((250, 250))
                mask = Image.new("L", (250, 250), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 250, 250), fill=255)
                image = image.convert("RGBA")
                image.putalpha(mask)
                self.profile_image = ImageTk.PhotoImage(image)
                self.profile_pic.configure(image=self.profile_image)
            except Exception as e:
                print(f"Error loading profile picture: {e}")
                
        elif not self.user[9]:
            self.upload_btn.configure(text="      Upload")
            self.camlbl.place(x=3,y=1)
            try:
                image = userimg.resize((250, 250))
                mask = Image.new("L", (250, 250), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 250, 250), fill=255)
                image = image.convert("RGBA")
                image.putalpha(mask)
                self.profile_pic.configure(image=self.profile_image)
            except Exception as e:
                print(f"Error loading profile picture: {e}")
        
        
    def upload_profile_picture(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            with open(file_path, "rb") as file:
                blob_data = file.read()
            self.save_profile_picture_blob(blob_data)
            self.load_user_profile_picture()
            

    def save_profile_picture_blob(self, blob_data):
        user_id = self.user[0]
        conn = sqlite3.connect("laxmihoneyindustry.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET profile_picture = ? WHERE ID = ?", (blob_data, user_id))
        conn.commit()
        conn.close()
        

class AmountDialog(CTkToplevel):
    def __init__(self, parent, action):
        super().__init__(parent)
        self.title(f"{action} Amount")
        self.geometry("300x150")
        
        self.action = action
        self.amount_var = tk.StringVar()
        
        self.label = CTkLabel(self, text=f"Enter amount to {action.lower()}:")
        self.label.pack(pady=10)
        
        self.entry = CTkEntry(self, textvariable=self.amount_var)
        self.entry.pack(pady=10)
        
        self.submit_button = CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def submit(self):
        try:
            amount = float(self.amount_var.get())
            self.destroy()
            self.master.handle_transaction(self.action, amount)
        except ValueError:
            show_popup_message(self.master.containermain,"Invalid input enter valid amount")
            
def fetch_products():
    conn = sqlite3.connect("laxmihoneyindustry.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, description,product_picture, price,stock,ID FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

class AdminAccountPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        containermain = CTkFrame(self, height=1000, width=1500, fg_color="dark gray", corner_radius=0)
        containermain.pack(fill=BOTH)

        self.user = controller.user
        self.leftcontainer = CTkFrame(containermain,fg_color="slategray",height=600,width=500)
        self.leftcontainer.pack(side=LEFT,padx=150,pady=53)
        
        self.rightcontainer=CTkFrame(containermain,fg_color="darkgray",height=600,width=500)
        self.rightcontainer.pack(side=LEFT,padx=75,pady=10)
        self.productstext = CTkLabel(self.rightcontainer,text="Products Management",text_color="Black",font=("verdana",24))
        self.productstext.place(x=125,y=15)
        
        self.canvas = CTkCanvas(self.rightcontainer, height=850, width=850)
        self.canvas.place(x=0, y=58)
        
        self.scrollbar = CTkScrollbar(self.rightcontainer,height=500, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.place(x=480, y=65)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        
        self.inner_frame = CTkFrame(self.canvas, width=750, height=800,corner_radius=0,fg_color="darkgray",bg_color="slategray")  # Adjust the height of inner_frame as needed
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        
        # Bind mouse wheel events
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        self.canvas.bind_all("<Button-4>", self._on_mouse_wheel)  # For Linux
        self.canvas.bind_all("<Button-5>", self._on_mouse_wheel)  # For Linux
        
        self.emptyspace = CTkFrame(self.rightcontainer, height=3,width=500,fg_color="black")
        self.emptyspace.place(x=0,y=46)

        self.display_products()
        self.display_random_product()

        height_for_inner_frame = 800

        if len_display_products>4:
            height_for_inner_frame = len_display_products*150
        self.inner_frame.configure(height=height_for_inner_frame)

    

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mouse_wheel(self, event):
        if event.num == 5 or event.delta == -120:  # For Linux and Windows scrolling down
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:  # For Linux and Windows scrolling up
            self.canvas.yview_scroll(-1, "units")

    def display_products(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        products = fetch_products()
        random.shuffle(products)
        
        
        global len_display_products
        len_display_products = len(products)
        y = 10
    
        for product in products:
            productscard = CTkButton(self.inner_frame,text="" ,hover_color="slategray",fg_color="slategray", width=450, height=100,border_width=1,border_color="gray",command=lambda product=product:self.show_product_details(product))
            productscard.place(x=25, y=y)
            image_data = product[2]
            image = Image.open(io.BytesIO(image_data))
            image.thumbnail((80, 80))
            photo = ImageTk.PhotoImage(image)

            product_image = CTkLabel(productscard,image=photo,text="")
            product_image.image = photo  # Keep a reference to avoid garbage collection
            product_image.place(x=5, y=10)
            product_image.bind("<Button-1>", lambda event, product=product: self.show_product_details(product))

            product_name = CTkLabel(productscard, text=f"{product[0]}", text_color="Black", font=("verdana", 18))
            product_name.place(x=90, y=10)
            truncated_description = self.truncate_text(product[1], 60)
            product_description = CTkLabel(productscard, text=f"{truncated_description}",wraplength=300, height=50,text_color="Black", font=("verdana", 12))
            product_description.place(x=90, y=40)
            product_name.bind("<Button-1>", lambda event, product=product: self.show_product_details(product))
            product_description.bind("<Button-1>", lambda event, product=product: self.show_product_details(product))


            product_price = CTkLabel(productscard, text=f"  Rs.{product[3]}", text_color="Black", font=("verdana", 14))
            product_price.place(x=5, y=65)
            
            product_stock = CTkLabel(productscard, text=f"Stock: {product[4]}", text_color="Black", font=("verdana", 13))
            product_stock.place(x=375, y=65)

            product_delete = CTkButton(productscard,text="X",font=("comic sans ms",20,"bold"),text_color="black",fg_color="slategray",hover_color="#3b3b3b",width=20, command=lambda product_id=product[5]: self.delete_product(product_id))
            product_delete.place(x=412,y=5)
            Tooltip(product_delete, f"Delete {product[0]}")
            y += 110
            def on_web_enter(event, button=productscard):
                button.configure(border_width=2, border_color="black")

            def on_web_leave(event, button=productscard):
                button.configure(border_width=1, border_color="gray")

            productscard.bind("<Enter>", on_web_enter)
            productscard.bind("<Leave>", on_web_leave)
      
        self.addproduct = CTkButton(self.inner_frame,fg_color="light blue",width=300,height=50,text="+",text_color="black",font=("verdana",33),command=self.open_add_product_dialog)
        self.addproduct.place(x=100,y=y+20)
    def display_random_product(self):
        products = fetch_products()
        if products:
            random_product = random.choice(products)  # Select a random product
            self.show_product_details(random_product)
            
    def truncate_text(self,text, max_length):
        if len(text) > max_length:
            return text[:max_length-3] + "..."
        return text
    def show_product_details(self, product):
        for widget in self.leftcontainer.winfo_children():
            widget.destroy()
        
        product_detail = CTkLabel(self.leftcontainer, text=f"Product Details", text_color="Black", font=("verdana", 18))
        product_detail.place(x=20, y=10)
        
        image_data = product[2]
        image = Image.open(io.BytesIO(image_data))

        # Resize image to fit label dimensions
        label_width = 400
        label_height = 250
        image = image.resize((label_width, label_height), Image.LANCZOS)

        # Create rounded corners
        radius = 20  # Change this to adjust the radius of the corners
        mask = Image.new('L', (label_width, label_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, label_width, label_height), radius, fill=255)
        
        image.putalpha(mask)

        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(image)

        product_image = CTkLabel(self.leftcontainer, image=photo, height=label_height, width=label_width, text="")
        product_image.image = photo  # Keep a reference to avoid garbage collection
        product_image.place(x=45, y=35)

        product_name = CTkLabel(self.leftcontainer, text=f"{product[0]}", text_color="Black", font=("verdana", 24))
        product_name.place(x=45, y=300)

        product_description = CTkLabel(self.leftcontainer, text=f"{product[1]}",wraplength=400,justify="left", text_color="Black", font=("verdana", 12))
        product_description.place(x=45, y=330)

        product_price = CTkLabel(self.leftcontainer, text=f"Rs.{product[3]}", text_color="Black", font=("verdana", 18))
        product_price.place(x=45, y=500)

        product_stock = CTkLabel(self.leftcontainer, text=f"Stocks:{product[4]}", text_color="Black", font=("verdana", 15))
        product_stock.place(x=345, y=500)

        deleting_button = CTkButton(
            self.leftcontainer,
            text="Delete X Product",
            font=("verdana", 16),
            hover_color="red",
            text_color="black",
            fg_color="#6ce2ba",width=150,height=50,
            command=lambda p_id=product[5]: self.delete_product(p_id)
        )
        deleting_button.place(x=150, y=525)

        Tooltip(deleting_button, f"delete {product[1]} ")
    
        
    def delete_product(self, product_id):
    # Show a confirmation dialog
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this product?"):
            try:
                # Connect to the SQLite database
                conn = sqlite3.connect("laxmihoneyindustry.db")
                c = conn.cursor()
                c.execute("DELETE FROM products WHERE ID = ?", (product_id,))

                # Commit the changes
                conn.commit()
                conn.close()
                for widget in self.leftcontainer.winfo_children():
                    widget.destroy()
                self.display_products()
                messagebox.showinfo("Success", "Product deleted successfully!")
            except sqlite3.Error as e:
                # Handle any database errors
                messagebox.showerror("Error", f"An error occurred: {e}")
    def open_add_product_dialog(self):
        self.addproduct= CTk()
        self.addproduct.geometry("600x600")
        self.addproduct.title("Add Product")
        self.product_name_label = CTkLabel(self.addproduct, text="Product Name:")
        self.product_name_label.pack(pady=10)
        self.product_name_entry = CTkEntry(self.addproduct)
        self.product_name_entry.pack(pady=10)

        self.product_description_label = CTkLabel(self.addproduct, text="Description:")
        self.product_description_label.pack(pady=10)
        self.product_description_entry = CTkEntry(self.addproduct)
        self.product_description_entry.pack(pady=10)

        self.product_price_label = CTkLabel(self.addproduct, text="Price:")
        self.product_price_label.pack(pady=10)
        self.product_price_entry = CTkEntry(self.addproduct)
        self.product_price_entry.pack(pady=10)

        self.product_stock_label = CTkLabel(self.addproduct, text="Stock:")
        self.product_stock_label.pack(pady=10)
        self.product_stock_entry = CTkEntry(self.addproduct)
        self.product_stock_entry.pack(pady=10)

        self.upload_button = CTkButton(self.addproduct, text="Upload Image",command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.submit_button = CTkButton(self.addproduct, text="Add Product",command=self.save_product)
        self.submit_button.pack(pady=10)
        
        self.addproduct.mainloop()
    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            with open(file_path, "rb") as file:
                self.blob_data = file.read()
            # self.save_product_picture_blob(blob_data)
    def save_product(self):
        try:
            name = self.product_name_entry.get().capitalize()
            description = self.product_description_entry.get()
            price = float(self.product_price_entry.get())
            stock = int(self.product_stock_entry.get())
            image_blob = self.blob_data
            conn = sqlite3.connect("laxmihoneyindustry.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO products (name, description, product_picture, price, stock)
                VALUES (?, ?, ?, ?, ?)
            """, (name, description, image_blob, price, stock))
            conn.commit()
            conn.close()

            # After successfully adding the product, show a confirmation message
            self.addproduct.destroy()  # Close the dialog
            self.display_products()
            messagebox.showinfo("Success", "Product added successfully.")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def update_title(self):
        self.controller.title("Account - Laxmi Honey Industry")

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        if self.tooltip:
            self.hide_tooltip(None)  # Hide any existing tooltip
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
        label = tk.Label(self.tooltip, text=self.text, fg="white",background="black", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

class AboutPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        user = controller.load_user_data()
        containermain = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slate gray",corner_radius=0)
        containermain.pack()
        
        
    def update_title(self):
        self.controller.title("About Us - Laxmi Honey Industry")

if __name__ == "__main__":
    
    app = Dash(1,1)
    app.mainloop()
