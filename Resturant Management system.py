import os
import time
import random
from PIL import ImageTk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from fpdf import FPDF
import mysql.connector
import datetime
import math
import PIL.Image
from Send_Email import sendEmail
import configparser

config = configparser.ConfigParser()
config.read('DB_Setup.cfg')
con = mysql.connector.connect(host=config['DB_Details']['Host'],user=config['DB_Details']['User'],password=config['DB_Details']['Password'],database= config['DB_Details']['DB_Name'])

name = "Resturant Management System"
localtime=time.asctime(time.localtime(time.time()))
colors=['red','blue','yellow','pink','red2','gold2']
count = 0
text = ''
class login(tk.Tk):
    temp_table_name = ""
    email=""
    user_id=""
    username=""
    order_id_dropdown_value=""
    dropdown=""
    user=""
    email_id=""
    logout_enable = 1
    backbuttom_enable = 1
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Resturant Management System")
        self.geometry("1028x500+100+50")
        self.iconbitmap("images/icon.ico")
        self._frame = None
        self.back = []
        self.back_enable = 0
        self.stack = 0
        self.switch_frame(LoginPage,0,0,700,1500)

    def switch_frame(self,frame_class,padding_x,padding_y,height,width):
        if self.back_enable == 0 and (self.stack ==0 or self.back[self.stack-1]!=frame_class):
            self.back.insert(self.stack,frame_class)
            self.stack = self.stack + 1
        self.back_enable = 0
        self.new_frame = frame_class(self)
        # ______slider_______
        self.SliderLabel = tk.Label(self.new_frame, text=name, bg="#533b1d", font="{chiller} 30 italic bold", foreground="black", relief=GROOVE,width=79,bd=10)
        self.SliderLabel.place(x=0, y=0)
        self.sliderlabel()
        self.sliderlabelcolor()
        ######button#######

        if self.logout_enable == 1 :
            self.logout_button = tk.Button( self.new_frame, text="Logout", font=("times now", 15),
                                      fg="white",
                                      bg="#d77337",command=self.logout,width=10,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
            self.logout_button.place(x=90, y=8)

        if self.backbuttom_enable == 1:
            self.back_button = tk.Button(self.new_frame, text="Back", font=("times now", 15),
                                       fg="white",
                                       bg="#d77337",command=self.back_but,width=10,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
            self.back_button.place(x=1050, y=8)
        self.logout_enable = 1
        self.backbuttom_enable = 1

        localtime1 = tk.Label(self.new_frame, text=localtime, bg="white", foreground="steel blue")
        localtime1.place(x=550, y=55)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = self.new_frame
        self._frame.place(x=padding_x,y=padding_y,height=height,width=width)
    #######slider ######
    def sliderlabel(self):
        global count, text
        if (count >= len(name)):
            count = 0
            text = ''
            self.SliderLabel.configure(text=text)
        else:
            text = text + name[count]
            self.SliderLabel.configure(text=text)
            count += 1
        self.SliderLabel.after(200, self.sliderlabel)
        #######slider  colour######
    def sliderlabelcolor(self):
        fg = random.choice(colors)
        self.SliderLabel.configure(fg=fg)
        self.SliderLabel.after(20, self.sliderlabelcolor)

    ########database connection with exception handling########
    ######for button######
    def logout(self):
        try:
            cursor = con.cursor()
            create_sql = 'select User_Type from rms_db.RMS_USER_DETAILS WHERE USER_NAME=\'' + self.username + '\''
            cursor.execute(create_sql)
            data = cursor.fetchone()
            USER_TYPE = data[0]
            if (USER_TYPE == 'manager'):
                self.switch_frame(LoginPage, 0, 0, 700, 1500)
            elif(USER_TYPE == 'customer'):
                cursor = con.cursor()
                cursor.execute('DROP TABLE  `rms_db`.`' + self.temp_table_name + '`')
                con.commit()
                self.switch_frame(LoginPage, 0, 0, 700, 1500)
            else:
                self.switch_frame(LoginPage, 0, 0, 700, 1500)
        except mysql.connector. Error as e:
            print(e)


    def back_but(self):
        self.stack = self.stack - 1
        self.back.pop(self.stack)
        #print(self.back)
        self.back_enable = 1
        self.switch_frame(self.back[self.stack-1], 0, 0, 700, 1500)


class LoginPage(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master,bg="white")
        #--to open an image------
        self.image = PIL.Image.open("images/wood-table.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500,700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        ###### #######label bg img############
        self.bg_image1 = tk.Label(self, image= self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        self.master.logout_enable = 0
        self.master.backbuttom_enable = 0

        self. username = StringVar()
        self. password = StringVar()
        #########frame############
        Frame_login = tk.Frame(self,bg="#e5d8be", height=230, width=250,relief=RIDGE,bd=10)
        Frame_login.place(x=380, y=150, height=380, width=510)
        ###########title###########
        self.title = tk.Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="#e5d8be")
        self.title.place(x=40, y=20)
        #---usericon img------
        self.usericon = PhotoImage(file="images/user_icon.png")
        ###### #######label img############
        tk.Label(Frame_login, text="Username",image= self.usericon ,compound=LEFT,font=("Goudy old style", 19, "bold"),  fg="#d25d17", bg="#e5d8be").place(x=40, y=103)
        ##########entry########
        self.txt_user = tk.Entry(Frame_login, font=("times new roman", 15),bg="lightgray",textvariable= self.username,bd=5,relief=RIDGE)
        self.txt_user.place(x=40, y=150, width=410, height=35)
        #---passicon img------
        self.pass_icon = PhotoImage(file="images/password.png")
        ###### #######label img############
        tk.Label(Frame_login, text="Password", image= self.pass_icon,compound=LEFT,font=("Goudy old style", 19, "bold"), fg="#d25d17",
                        bg="#e5d8be").place(x=40, y=197)
        ##########entry########
        self.txt_pass = tk.Entry(Frame_login, font=("times new roman", 15), bg="lightgray",textvariable=self.password ,show="*",bd=5,relief=RIDGE)
        self.txt_pass.place(x=40, y=245, width=410, height=35)
        ###########button######
        self.forget_button = tk.Button(Frame_login, text="Forget Password?", font=("times now", 12), bg="#d77337",
                               fg="white",command=self.foget_password,relief=RIDGE,bd=7)
        self.forget_button.place(x=40, y=300)
        self.login_button = tk.Button(self, text="Login", command=self.login_function, font=("times now", 15), fg="white",
                              bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.login_button.place(x=510, y=530, width=220, height=50)


        self.Registration_button = tk.Button(self, text=" Registration",
                                      font=("times now", 12),command=self.new_account,
                                      fg="white",
                                      bg="#d77337",relief=RIDGE,bd=7)
        self.Registration_button.place(x=690, y=460, width=150, height=40)

        self.About_Us_button = tk.Button(self, text="About Us", command=self.About_Us,
                                     font=("times now", 15),
                                     fg="white",
                                     bg="#662f10",relief=RIDGE,bd=7)
        self.About_Us_button.place(x=545, y=590, width=150,height=40)


# ----function for customer registration----
    def new_account(self):
        self.master.switch_frame(RegistrationPage, 0, 0, 700, 1500)

    def About_Us(self):
        self.master.switch_frame(About_us, 0, 0, 700, 1500)

    def foget_password(self):

        self.master.switch_frame(forget_password, 0, 0, 700, 1500)

    ########database connection with exception handling########
    ######for button######

    def login_function(self):
        try:
            cursor = con.cursor()
            create_sql = 'select PASSWORD,USER_ID,EMAIL_ID,User_Type from rms_db.RMS_USER_DETAILS WHERE USER_NAME=\''+ self.username.get() + '\''
            cursor.execute(create_sql)
            data = cursor.fetchone()

            if self.password.get() == "" or self.username.get() == "":
                tk.messagebox.showerror("Error", "All fields are required", master=self)
            elif  data == None:
                tk.messagebox.showerror("Error", "No Such User", master=self)
            elif  self.password.get() != data[0]:
                tk.messagebox.showerror("Error", "Invalid Username/Password", master=self)
            else:
                USER_TYPE= data[3]
                if(USER_TYPE=='manager'):
                    tk.messagebox.showinfo("Welcome", f"Welcome to resturant management system", master=self)
                    self.master.username = self.username.get()
                    self.master.switch_frame(Manager_page, 0, 0, 700, 1500)

                elif(USER_TYPE == 'customer'):
                    # ----database connection--
                    cursor = con.cursor()
                    tk.messagebox.showinfo("Welcome", f"Welcome to resturant management system", master=self)
                    self.master.switch_frame(Customer_page, 0, 0, 700, 1500)
                    self.master.temp_table_name='TEMP_' + self.username.get() + '_cart'
                    self.master.email=data[2]
                    self.master.user_id=data[1]
                    self.master.username=self.username.get()
                    create_sql = 'create table '+ self.master.temp_table_name +'(order_item varchar(20),total_num_orders int)'
                    cursor.execute(create_sql)
                else:
                    tk.messagebox.showinfo("Welcome", f"Welcome to resturant management system", master=self)
                    self.master.switch_frame( cook_page, 0, 0, 700, 1500)
                    self.master.username = self.username.get()
        except mysql.connector.Error as e:
            print(e)

class forget_password(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/bg2.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        ###### #######label img############
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        #########frame############
        Frame_forget_pass = tk.Frame(self, height=230, width=250, relief=RIDGE, bd=10,bg="#a9795a")
        Frame_forget_pass.place(x=380, y=100, height=450, width=510)
        self.username1 = StringVar()
        ###########title###########
        self.title = tk.Label( Frame_forget_pass, text="Reset Password", font=("Impact", 35, "bold"), fg="#6c3523",bg="#a9795a")
        self.title.place(x=95, y=30)
        # ---usericon img------
        self.usericon = PhotoImage(file="images/user_icon.png")
        ###### #######label img############
        tk.Label(Frame_forget_pass, text="Username", image=self.usericon, compound=LEFT, font=("Goudy old style", 19, "bold"),
                fg="#6c3523",bg="#a9795a").place(x=95, y=103)
        ##########entry########
        self.txt_user = tk.Entry( Frame_forget_pass, font=("times new roman", 15), bg="lightgray", textvariable=self.username1,
                                 bd=5, relief=RIDGE)
        self.txt_user.place(x=95, y=150, width=350, height=35)
        # ---otpicon img------

        self.otp_icon = PhotoImage(file="images/otp.png")
        ###### #######label img############
        tk.Label( Frame_forget_pass, text="OTP",image=self.otp_icon, compound=LEFT,font=("Goudy old style", 19, "bold"), fg="#6c3523",bg="#a9795a").place(x=95, y=260)
        #########entry###########
        self.txt_OTP = tk.Entry( Frame_forget_pass, font=("times new roman", 15), bg="lightgray", bd=5, relief=RIDGE)
        self.txt_OTP.place(x=95, y=310, width=350, height=35)
        ###########button######
        self.verify_username_button = tk.Button(self, text="Verify Username", font=("times now", 15),
                                           fg="white",
                                           bg="#6c3523", relief=RIDGE, bd=7, activeforeground="blue",
                                           activebackground="yellow",command=self.username)
        self.verify_username_button.place(x=485, y=310, width=180, height=40)

        self.verify_otp_button = tk.Button(self, text="Verify OTP", font=("times now", 15),
                                      fg="white",
                                      bg="#6c3523", relief=RIDGE, bd=7, activeforeground="blue",
                                      activebackground="yellow",command=self.CkOTP)
        self.verify_otp_button.place(x=485, y=470, width=180, height=40)
    def GnOTP(self):
        # which stores all digits
        self.digits = "0123456789"
        self.OTP = ""
        # by changing value in range
        for i in range(4):
            self.OTP += self.digits[math.floor(random.random() * 10)]

        sendEmail( self.master.email_id, "OTP has been sent to your registered", 'Your OTP is -'  +  self.OTP)
        print( self.OTP)
    def CkOTP(self):
        OTP1 = self.txt_OTP.get()
        if (OTP1 == self.OTP):
            tk.messagebox.showinfo("OTP", f"OTP is correct", master=self)
            self.master.switch_frame(confirm_pass, 0, 0, 700, 1500)
        else:
            tk.messagebox.showerror("Error", "Invalid OTP", master=self)

    ########database connection with exception handling########
    ######for button######

    def username(self):
        try:
            cursor = con.cursor()
            self.master.user=self.username1.get()
            create_sql = 'select Email_id from rms_db.RMS_USER_DETAILS WHERE USER_NAME=\'' + self.master.user + '\''
            cursor.execute(create_sql)
            data = cursor.fetchone()
            if ( data == None or self.master.user == "" or self.master.user == None):
                tk.messagebox.showerror("Error", "Invalid Username", master=self)
            else:
                self.master.email_id=data[0]
                self.GnOTP()
                tk.messagebox.showinfo("OTP", f"OTP is send to your email id", master=self)
        except mysql.connector.Error as e:
            print(e)

class confirm_pass(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/bg3.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        ###### #######label img############
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_con_pass = tk.Frame(self, height=230, width=250, relief=RIDGE, bd=10,bg="#be723e")
        Frame_con_pass.place(x=380, y=120, height=350, width=510)
        #########title#############
        self.title = tk.Label( Frame_con_pass, text="New Password", font=("Impact", 35, "bold"), fg="#533b1d", bg="#be723e")
        self.title.place(x=95, y=30)
        self.new_pass = StringVar()
        self.con_password1 = StringVar()
        ####---usericon img----#####
        self.pass_icon1 = PhotoImage(file="images/password.png")
        ###### #######label img############
        tk.Label( Frame_con_pass, text="New Password", image=  self.pass_icon1 , compound=LEFT, font=("Goudy old style", 19, "bold"),
                 fg="#533b1d", bg="#be723e").place(x=95, y=103)
        ##########entry########
        self.txt_user = tk.Entry( Frame_con_pass, font=("times new roman", 15), bg="lightgray", textvariable=self.new_pass,
                                 bd=5, relief=RIDGE)
        self.txt_user.place(x=95, y=150, width=350, height=35)
        #####---passicon img------####
        self.pass_icon = PhotoImage(file="images/password.png")
        ###### #######label img############
        tk.Label( Frame_con_pass, text="Confirm Password", image=self.pass_icon, compound=LEFT,
                 font=("Goudy old style", 19, "bold"), fg="#533b1d", bg="#be723e").place(x=95, y=197)
        ###########entry############
        self.txt_pass = tk.Entry( Frame_con_pass, font=("times new roman", 15), bg="lightgray", textvariable=self.con_password1,
                                 show="*", bd=5, relief=RIDGE)
        self.txt_pass.place(x=95, y=245, width=350, height=35)
        ##########button###########
        self.confirm_button = tk.Button(self, text="Confirm Password", command=self.con_password, font=("times now", 15),
                                      fg="white",bg="#533b1d",relief=RIDGE, bd=7, activeforeground="blue", activebackground="yellow")
        self.confirm_button.place(x=550, y=452, width=180, height=40)
        ########database connection with exception handling########
        ######for button######
    def con_password(self):
        try:
            cursor = con.cursor()
            new_password = self.new_pass.get()
            confirm_password = self.con_password1.get()
            if(new_password != confirm_password):
                tk.messagebox.showerror("Error", "Password is not same", master=self)
            else:
                cursor.execute('UPDATE rms_db.RMS_USER_DETAILS SET PASSWORD = \''+ confirm_password + '\' where USER_NAME=\'' + self.master.user + '\'')
                con.commit()
                tk.messagebox.showinfo("New Password", f"New Password is Updated successfully", master=self)
                self.master.switch_frame(LoginPage, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)


class RegistrationPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master,bg="white")
        #----image----

        self.image = PIL.Image.open("images/wood1.jpg")
        #----- To resize image-------
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        #######label img############
        self.bg_image1 = tk.Label(self, image= self.new_pic1).place(x=0, y=0, relheight=1)
        self.master.logout_enable = 0
        self.username = StringVar()
        self.email_id = StringVar()
        self.mobile_no = StringVar()
        self.password = StringVar()

        #----frame-----
        Frame_registration = tk.Frame(self, height=230, width=250,relief=RIDGE,bd=10,bg="#e5d8be")
        Frame_registration.place(x=280, y=80, height=550, width=700)
        #----label------------
        self.title = tk.Label(Frame_registration, text="Create New Account", font=("Impact", 35, "bold"), fg="#d77337",bg="#e5d8be")
        self.title.place(x=90, y=10)
        # ---user_icon img
        self.usericon1 = PhotoImage(file="images/user_icon.png")
        tk.Label(Frame_registration, text="User Name", bg="#e5d8be",font=("Goudy old style", 19, "bold"),image= self.usericon1 ,compound=LEFT, fg="#d25d17").place(x=95, y=80)
        #---entry---------
        self.txt_user = tk.Entry(Frame_registration, font=("times new roman", 15), bg="lightgray",textvariable= self.username,bd=5,relief=RIDGE)
        self.txt_user.place(x=95, y=125, width=350, height=35)
        self.email_icon = PhotoImage(file="images/email.png")
        ###### #######label img############
        tk.Label(Frame_registration, text="Email ID",image= self.email_icon ,compound=LEFT, font=("Goudy old style", 19, "bold"), fg="#d25d17",
                 bg="#e5d8be").place(x=95, y=170)
        self.txt_email = tk.Entry(Frame_registration, font=("times new roman", 15), bg="lightgray",textvariable= self.email_id,bd=5,relief=RIDGE)
        self.txt_email.place(x=95, y=215, width=350, height=35)
        # ---mobilenoicon img------
        self.mobileno_icon = PhotoImage(file="images/mobile no.png")
        ###### #######label img############
        tk.Label(Frame_registration, text="Mobile No",image= self.mobileno_icon ,compound=LEFT, font=("Goudy old style", 19, "bold"), fg="#d25d17",
                 bg="#e5d8be").place(x=95, y=260)
        self.txt_mobile = tk.Entry(Frame_registration, font=("times new roman", 15), bg="lightgray",textvariable= self.mobile_no,bd=5,relief=RIDGE)
        self.txt_mobile.place(x=95, y=300, width=350, height=35)
        # ---passicon img------
        self.pass_icon = PhotoImage(file="images/password.png")
        ###### #######label img############
        tk.Label(Frame_registration, text="Enter Password",image= self.pass_icon ,compound=LEFT, font=("Goudy old style", 19, "bold"), fg="#d25d17",bg="#e5d8be").place(x=95, y=340)
        self.txt_pass = tk.Entry(Frame_registration, font=("times new roman", 15), bg="lightgray",textvariable= self.password,show="*",bd=5,relief=RIDGE)
        self.txt_pass.place(x=95, y=390, width=350, height=35)
        #---user_icon img
        self.usericon = PhotoImage(file="images/user_icon.png")
        ###### #######label img############
        tk.Label(Frame_registration, text="User Type",image= self.usericon ,compound=LEFT, font=("Goudy old style", 19, "bold"), fg="#d25d17",
                 bg="#e5d8be").place(x=95, y=430)
        # dropdown with usertype
        self.usertype = ["customer", "manager", "cook"]
        self.reg_variable= StringVar(Frame_registration)
        self.reg_variable.set("usertype")
        self.drop1 = OptionMenu(Frame_registration, self.reg_variable, * self.usertype)
        self.drop1.config(width=27, height=0, bg="lightgray", fg="#d77337", font=("bold"),bd=5,relief=RIDGE)
        self.drop1.place(x=95, y=472)

        self.new_account_button = tk.Button(self, text="Create an Account", font=("times now", 15),command=self.new_account,
                                      fg="white",
                                      bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.new_account_button.place(x=520, y=613, width=200, height=40)

    def new_account(self):
        try:
            cursor = con.cursor()
            cursor.execute('select USER_NAME from rms_db.RMS_USER_DETAILS where USER_NAME=\'' + self.username.get()+ '\'')
            data = cursor.fetchone()
            if(self.username.get()==""):
                tk.messagebox.showerror("Error", "Type your username", master=self)

            elif (bool(re.search(r"\s", self.username.get())) == True):
                tk.messagebox.showerror("Error", "Username consists space", master=self)
            elif(self.email_id.get()==""):
                tk.messagebox.showerror("Error", "Type your email id", master=self)
            elif (len(self.mobile_no.get()) !=10):
                tk.messagebox.showerror("Error", "Please provide 10 digit mobile no", master=self)

            elif self.password.get() == "":
                tk.messagebox.showerror("Error", "You have to fill the password", master=self)
            elif self.reg_variable.get() == 'usertype':
                tk.messagebox.showerror("Error", "You have to fill the user type", master=self)

            elif (data==None):
                name = self.username.get()
                self.master.email_id = self.email_id.get()
                mobile_no = self.mobile_no.get()
                password = self.password.get()
                type = self.reg_variable.get()
                cursor.execute('select max(USER_ID) from rms_db.RMS_USER_DETAILS')
                new_id = cursor.fetchone()[0] + 1
                cursor.execute(
                'insert into rms_db. RMS_USER_DETAILS (`USER_ID`,`USER_NAME`,`Email_id`,`Mobile_no`,`PASSWORD`,`User_Type`) values(%s,%s,%s,%s,%s,%s)',
                (new_id, name, self.master.email_id, mobile_no, password, type))
                con.commit()
                tk.messagebox.showinfo("Massage", f"Massage is sent to your email id.", master=self)
                sendEmail(self.master.email_id, "Your account has been successfully created",
                      "Thanks " + name + " for creating account. Your Password is - " + password)
                tk.messagebox.showinfo("Create Account", f"Account  created Succesfully.", master=self)
                self.master.switch_frame(LoginPage, 0, 0, 700, 1500)

            elif(self.username.get()==data[0]):
                tk.messagebox.showerror("Error", "User already exits", master=self)
        except mysql.connector.Error as e:
            print(e)

class About_us(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        # ----for bg------
        # ----image----
        self.image = PIL.Image.open("images/bg3.jpg")
        # To resize image
        self.resized = self.image.resize((1500, 700))
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image = tk.Label(self, image=self.new_pic).place(x=0, y=0, relwidth=1, relheight=1)
        # frame with borderwidth 6
        # ----frame-----
        Frame_About_us = tk.Frame(self, height=230, width=250, relief=RIDGE,bd=10, bg="#be723e")
        Frame_About_us.place(x=260, y=90, height=500, width=730)
        #----image of frame------
        # --to open  image------
        self.image = PIL.Image.open("images/arka.jpg")
        # To resize image
        self.resized1 = self.image.resize((200, 200))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        #######label img############
        image1_image1 = tk.Label( Frame_About_us, image=self.new_pic1,text="Arkapriya" ,compound=TOP,font=("Goudy old style", 19, "bold"),fg="#533b1d", bg="#be723e",height=230, width=250)
        image1_image1.place(x=0,y=75)
        #----title------------
        self.title = tk.Label(Frame_About_us, text="Developers", font=("Impact", 35, "bold"),fg="#533b1d", bg="#be723e")
        self.title.place(x=250, y=10)

        # --to open  image------
        self.image = PIL.Image.open("images/shreya.jpg")
        # To resize image
        self.resized2 = self.image.resize((200, 200))
        self.new_pic2 =ImageTk.PhotoImage(self.resized2)
        #######label img############
        image1_image2 = tk.Label(Frame_About_us,text="Shreya",compound=TOP,image=self.new_pic2,font=("Goudy old style", 19, "bold"),fg="#533b1d", bg="#be723e",height=230, width=250)
        image1_image2.place(x=230, y=75)

        # --to open  image------
        self.image = PIL.Image.open("images/subham.jpg")
        # To resize image
        self.resized3 = self.image.resize((200, 200))
        self.new_pic3 = ImageTk.PhotoImage(self.resized3)
        #######label img############
        image1_image3 = tk.Label(Frame_About_us, image=self.new_pic3, text="Shubham" ,compound=TOP,font=("Goudy old style", 19, "bold"),fg="#533b1d", bg="#be723e",height=230, width=250)
        image1_image3.place(x=455, y=75)
        # ----title------------
        self.title = tk.Label(Frame_About_us, text="About Us", font=("Impact", 35, "bold"), fg="#533b1d", bg="#be723e")
        self.title.place(x=260, y=310)

        #-------label-------########
        tk.Label(Frame_About_us, text="We are famous for our special chicken biryani,Large size pizza with\nmashrooms and Butter chicken with extra cheese and spice\nand special chicken burger with diet coke ",font=("Goudy old style", 19, "bold"),fg="#533b1d", bg="#be723e").place(x=10, y=365)



class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # --to open  image------
        self.image = PIL.Image.open("images/pageonebg1.jpg")
        # To resize image
        self.resized = self.image.resize((1500, 700))
        self.new_pic = ImageTk.PhotoImage(self.resized)
        #######label bg img#########
        self.bg_image = tk.Label(self, image=self.new_pic ).place(x=0, y=0, relwidth=1, relheight=1)
        #----frames in menu table------
        Frame1 = tk.Frame(self, height=230, width=250, bd=0)
        Frame1.grid(row=0, column=0, pady=60, padx=40)
        #--to open  image------##############
        self.image = PIL.Image.open("images/biryani.jpg")
        # To resize image
        self.resized1 = self.image.resize((250, 250))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
       # image in frame1##############
        image1_image1 = tk.Label(Frame1, image= self.new_pic1, height=230, width=250)
        image1_image1.pack()
        lb1 = tk.Label(Frame1, text="Biryani", font=("Goudy old style", 19, "bold"), fg="black")
        lb1.pack(side=tk.TOP, fill="x")
        #frame2-----##########
        Frame2 = tk.Frame(self, height=230, width=250, bd=0)
        Frame2.grid(row=0, column=1, pady=90, padx=30)
        #image-----############
        # For displaying jpg image of chef using label
        self.image = PIL.Image.open("images/pizza.jpg")
        #######To resize image########
        self.resized2 = self.image.resize((250, 250))
        self.new_pic2 = ImageTk.PhotoImage(self.resized2)
        image1_image2 = tk.Label(Frame2, image=self.new_pic2 , height=230, width=250)
        image1_image2.pack()
        lb1 = tk.Label(Frame2, text="Pizza", font=("Goudy old style", 19, "bold"), fg="black")
        lb1.pack(side=tk.TOP, fill="x")
        # frame3-----##########
        Frame3 = tk.Frame(self, height=230, width=250, bd=0)
        Frame3.grid(row=0, column=2, pady=60, padx=30)
        # --to open  image------
        self.image = PIL.Image.open("images/burger1.jpg")
        # To resize image
        self.resized3= self.image.resize((250, 250))
        self.new_pic3 = ImageTk.PhotoImage(self.resized3)
        # image label-----############
        image1_image3 = tk.Label(Frame3, image=self.new_pic3, height=230, width=250)
        image1_image3.pack()
        lb3= tk.Label(Frame3, text="Burger", font=("Goudy old style", 19, "bold"), fg="black")
        lb3.pack(side=tk.TOP, fill="x")
        # frame4-----##########
        Frame4 = tk.Frame(self, height=230, width=250, bd=0)
        Frame4.grid(row=0, column=3, pady=60, padx=30)
        # --to open  image------
        self.image = PIL.Image.open("images/butterchicken.jpg")
        # To resize image
        self.resized4 = self.image.resize((250, 250))
        self.new_pic4 = ImageTk.PhotoImage(self.resized4)
        # image label-----############
        image1_image4 = tk.Label(Frame4, image= self.new_pic4, height=230, width=250)
        image1_image4.pack()
        lb4 = tk.Label(Frame4, text="Butter Chicken", font=("Goudy old style", 19, "bold"), fg="black")
        lb4.pack(side=tk.TOP, fill="x")

        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        #---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'),background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        #---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar",foreground="red",background="orange")
        ##########creating scrollbar############
        scroll_y = ttk.Scrollbar(self, orient=VERTICAL,style="TScrollbar",cursor="dot")

        scroll_y.place(x=1045, y=400, height=242)
        ###########set scrollbar with treeview#######
        ########### menu  table using treeview############-----

        menutable=ttk.Treeview(self,column=('Item id','Item name','Item Description','Price','Availability'),yscrollcommand= scroll_y.set)
        scroll_y.config(command=menutable.yview)
        # Assigning the heading names to the
        # respective columns
        menutable.heading('#1', text='Item id')
        menutable.heading('#2',text='Item name')
        menutable.heading('#3', text='Item Description')
        menutable.heading('#4', text='Price')
        menutable.heading('#5', text='Availability')
        # Defining heading
        menutable['show']='headings'
        # Assigning the width and anchor to  the
        # respective columns
        menutable.column('#1', stretch=tk.YES,anchor ='c')
        menutable.column('#2', stretch=tk.YES,anchor ='c')
        menutable.column('#3', stretch=tk.YES,anchor ='c')
        menutable.column('#4', stretch=tk.YES,anchor ='c')
        menutable.column('#5', stretch=tk.YES,anchor ='c')

        menutable.place(x=40,y=400)
        ######button########
        self.order_button = tk.Button(self, text="Order Now", command=self.order, font=("times now", 15),
                                      fg="white",
                                      bg="#d77337", relief=RIDGE, bd=7, activeforeground="blue",
                                      activebackground="yellow")
        self.order_button.place(x=1080, y=600, width=180, height=40)

        ######----database connection with exception handling-------#######

        try:
            cursor = con.cursor()
            create_sql = 'select * from rms_db.RMS_MENU_TABLE'
            cursor.execute(create_sql)
            for ROWS in cursor:
                menutable.insert('','end',values=ROWS)
        except mysql.connector.Error as e:
            print(e)
    def order(self):
        self.master.switch_frame(Order_page, 0, 0, 700, 1500)



 #-----manageitem page----
class Manageitem_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/bg3.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        self.itemname=StringVar()
        self.itemdescription = StringVar()
        self.price=IntVar()
        #----create frame------
        Frame_manageitem_page1 = tk.Frame(self,bg="#fab56f",height=230, width=250, relief=RIDGE, bd=10)
        Frame_manageitem_page1.place(x=280, y=80, height=550, width=730)

        # ----label#########
        self.title = tk.Label( Frame_manageitem_page1, text="Manage Items", font=("Impact", 35, "bold"), fg="#d77337",bg="#fab56f")
        self.title.place(x=95, y=30)
        tk.Label(Frame_manageitem_page1, text=" Item Name *", font=("Goudy old style", 19, "bold"),
                 fg="#d25d17",bg="#fab56f").place(x=95, y=95)

        tk.Label(Frame_manageitem_page1, text=" Item Description", font=("Goudy old style", 19, "bold"),
                 fg="#d25d17",bg="#fab56f").place(x=95, y=170)
        tk.Label(Frame_manageitem_page1, text=" Price", font=("Goudy old style", 19, "bold"),
                 fg="#d25d17",bg="#fab56f").place(x=95, y=250)

        #----add button-----------
        self.add_button = tk.Button(self, text="Add Item", font=("times now", 15),
                                       fg="white",
                                       bg="#d77337",command=self. manage_item,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.add_button.place(x=390, y=427, width=180, height=40)
        # ---entry----
        self.txt_additems = tk.Entry(Frame_manageitem_page1, font=("times new roman", 15), bg="lightgray",textvariable= self.itemname,bd=5,relief=RIDGE)
        self.txt_additems.place(x=100, y=130, width=350, height=35)

        self.txt_additems2= tk.Entry(Frame_manageitem_page1, font=("times new roman", 15), bg="lightgray",
                                     textvariable=self.itemdescription,bd=5,relief=RIDGE)
        self.txt_additems2.place(x=100, y=210, width=350, height=35)
        self.txt_additems3=tk.Entry(Frame_manageitem_page1, font=("times new roman", 15), bg="lightgray",
                                     textvariable=self.price,bd=5,relief=RIDGE)
        self.txt_additems3.place(x=100, y=290, width=350, height=35)

        #---- del label-------
        tk.Label(Frame_manageitem_page1, text="Delete Items", font=("Goudy old style", 19, "bold"), fg="#d25d17",bg="#fab56f").place(x=95, y=385)
        # dropdown with dishes name in del button
        try:
            cursor = con.cursor()
            create_sql = 'select Item_Name from rms_db.RMS_MENU_TABLE'
            cursor.execute(create_sql)
            self.dishes = []
            i = 0
            for ROWS in cursor:
                self.dishes.insert(i, ROWS[0])
                i = i + 1
        except mysql.connector.Error as e:
            print(e)
        # -----del button----
        # dropdown with usertype
        self.reg_variable = StringVar(Frame_manageitem_page1)
        self.reg_variable.set("Items")
        self.drop1 = OptionMenu(Frame_manageitem_page1, self.reg_variable, *self.dishes )
        self.drop1.config(width=27, height=0, bg="lightgray", fg="#d77337", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop1.place(x=95, y=423)
        #-----del button----
        self.del_button = tk.Button(self, text="Delete Item", font=("times now", 15),
        fg="white",bg="#d77337",command=self.delitem,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.del_button.place(x=385, y=570, width=180, height=40)

        ######----database connection with exception handling-------#######
        # -----for button----
    def manage_item(self):
        if self.itemname.get() == "":
            tk.messagebox.showerror("Error", "All fields are required", master=self)
        else:
            itemname= self.itemname.get()
            itemnamedesc = self.itemdescription.get()
            price = self.price.get()

            try:
                cursor = con.cursor()
                cursor.execute('select max(Item_Id) from rms_db.RMS_MENU_TABLE')
                new_id= cursor.fetchone()[0]+1
                cursor.execute('insert into rms_db.RMS_MENU_TABLE (`Item_Id`,`Item_Name`,`Item_Description`,`Cost`) values(%s,%s,%s,%s)',(new_id,itemname,itemnamedesc,price))
                con.commit()
                tk.messagebox.showinfo("Add Item", f"Item is added Succesfully", master=self)
                self.master.switch_frame(Manageitem_page, 0, 0, 700, 1500)
            except mysql.connector.Error as e:
                print(e)

    ######----database connection with exception handling-------#######
    # -----for button----
    def delitem(self):
        try:
            cursor = con.cursor()
            type = self.reg_variable.get()
            cursor.execute('DELETE FROM  rms_db.RMS_MENU_TABLE WHERE Item_Name= \''+type+'\'')
            con.commit()
            tk.messagebox.showinfo("Delete Item", f"Item is deleted Succesfully", master=self)
            self.master.switch_frame(Manageitem_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)
# -----order  page--------
class Order_page(tk.Frame):
    temp_table_name = ""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----for bg
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/order3.jpg")
        # To resize image
        self.resized = self.image.resize((1500, 700))
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image = tk.Label(self, image=self.new_pic).place(x=0, y=0,relwidth=1, relheight=1)
        # frame for order page
        Frame_Order_PAGE = tk.Frame(self, bd=10,relief=RIDGE,bg="#f4a74e")
        self.config(bg="#d77337")
        Frame_Order_PAGE.place(x=250, y=80, height=550, width=750)
        # --to open  image------
        self.image = PIL.Image.open("images/FOOD.jpg")
        # To resize image
        self.resized1 = self.image.resize((270, 350))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        PIC_label =tk.Label(Frame_Order_PAGE, image=self.new_pic1)
        PIC_label.place(x=456, y=130)
        # label name title assigned
        label_order = tk.Label(Frame_Order_PAGE, text="Order Delicious Food", bd=2, width=17, height=3, fg="#bf2413",
                      font=("Impact", 35, "bold"),bg="#f4a74e")
        label_order.place(x=45, y=10)
        # label name order assigned
        order_item = tk.Label(Frame_Order_PAGE, text="Order Item", bd=2, padx=20, width=6, height=2, bg="#f4a74e",
                      font=("Goudy old style", 18, "bold"), fg="#bf2413")
        order_item.place(x=45, y=130)
        # dropdown with dishes name
        try:
            cursor = con.cursor()
            create_sql = 'select Item_Name from rms_db.RMS_MENU_TABLE where Availability= \'yes\''
            cursor.execute(create_sql)
            self.dishes = []
            i=0
            for ROWS in cursor:
                self.dishes.insert(i,ROWS[0])
                i=i+1
        except mysql.connector.Error as e:
            print(e)
        self.items = StringVar(Frame_Order_PAGE)
        self.items.set("Select ITEMS")
        self.drop1 = OptionMenu(Frame_Order_PAGE,self.items, * self.dishes)
        self.drop1.config(width=27, height=2, bg="#d77337", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop1.place(x=45, y=190)
        # numberoforder label made
        numberoforder =tk. Label(Frame_Order_PAGE, text="Total no of orders", padx=10, width=12, height=2,  bg="#f4a74e",
                              font=("Goudy old style", 18, "bold"),fg="#bf2413")
        numberoforder.place(x=45, y=263)
        # spinbox made whose name is spinbox1
        self.spinbox1 = tk.Spinbox(Frame_Order_PAGE, from_=0, to=20, width=29, bg="#d77337", font=(20), fg="black",relief=RIDGE,bd=7)
        self.spinbox1.place(x=45, y=320)
        order =tk. Label(Frame_Order_PAGE, text="Table Booking", bd=2, padx=20, width=8, height=2,
                     font=("Goudy old style", 18, "bold"), fg="#bf2413",bg="#f4a74e")
        order.place(x=45, y=360)

        # -----dropdown taking value from database--------
        try:
            cursor = con.cursor()
            create_sql = 'select  Table_no from rms_db.RMS_BOOK_TABLE where USER_NAME=\'' +  self.master.username + '\''
            cursor.execute(create_sql)
            self.table_no = ["Take away"]
            i = 1
            for ROWS in cursor:
                self.table_no.insert(i, str(ROWS[0]))
                i = i + 1
        except mysql.connector.Error as e:
            print(e)
        self.book_table_value = StringVar(Frame_Order_PAGE)
        self.book_table_value.set("Select Table No")
        self.drop2 = OptionMenu(Frame_Order_PAGE, self.book_table_value, * self.table_no )
        self.drop2.config(width=27, height=2, bg="#d77337",font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop2.place(x=45, y=420)
        #-------------button with text ADD TO CART-----------------
        self.button1 = tk.Button(self, text="Add to cart", width=15, height=0, bg="#d77337", font=("bold"), fg="white",command=self.addtocart,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.button1.place(x=300, y=600)
        # button with text CHECK OUT
        self.button2 = tk.Button(self, text="Check out", width=15, height=0, bg="#d77337", font=("bold"), fg="white",command=self.checkout,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.button2.place(x=700, y=600)
        ######----database connection with exception handling-------#######
        # -----for button----
    def addtocart(self):
        try:
            cursor = con.cursor()
            create_sql = 'select order_item from `rms_db`.`' + self.master.temp_table_name + '` where order_item = \'' +  self.items.get() + '\''
            cursor.execute(create_sql)
            data = cursor.fetchone()
            if self.items.get() == "ITEMS":
                tk.messagebox.showerror("Error", "you have to select at least one item ", master=self)
            elif self.spinbox1.get() == "0":
                tk.messagebox.showerror("Error", "select total no of order", master=self)
            elif self.book_table_value.get()=="Table No":
                tk.messagebox.showerror("Error", "you have to book your table ", master=self)

            elif not (data is None):
                cursor = con.cursor()
                cursor.execute('UPDATE `rms_db`.`' + self.master.temp_table_name + '` SET total_num_orders = \'' + self.spinbox1.get() + '\' where order_item = \'' + self.items.get() + '\'')
                con.commit()
                tk.messagebox.showinfo("Updated Quantity", f"Quantity is Updated", master=self)
            else:
                tk.messagebox.showinfo("Add to Cart", f"Order is added to our account", master=self)
                cursor = con.cursor()
                create_sql = ' insert into ' + self.master.temp_table_name + ' values(\''+ self.items.get() + '\',\''+self.spinbox1.get()+'\')'
                cursor.execute(create_sql)
                con.commit()
        except mysql.connector.Error as e:
            print(e)

    def checkout(self):

        if(self.items.get() == "ITEMS" or self.spinbox1.get() == "0" or  self.book_table_value.get()=="Table No"):
            tk.messagebox.showerror("Error", "you have no order", master=self)
        else:
            if (self.book_table_value.get() == "Take away"):
                self.master.dropdown = 0
            else:
                self.master.dropdown = self.book_table_value.get()
            self.master.switch_frame(Place_Order, 0, 0, 700, 1500)


#-----page for place order--------
class Place_Order(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/place order bg.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        #----for title-----
        self.title = tk.Label(self, text="Place Your Order", font=("Impact", 35, "bold"), fg="#693500",bg="#eeaa40")
        self.title.place(x=450, y=90)

        global temp_table_name
        #----for styling heading-----
        self.style=ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview.Heading',font=('chiller',20,'bold'),background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")
        #-----creating scrollbar---------########
        scroll_y1 = ttk.Scrollbar(self, orient=VERTICAL,cursor="dot",style="TScrollbar")
        ###########set scrollbar with treeview#######
        ########### order  table using treeview############-----
        ordertable = ttk.Treeview(self, column=('Item id', 'Item name', 'Price', 'Quantity','Total cost'), yscrollcommand=scroll_y1.set)
        scroll_y1.config(command=ordertable.yview)
        scroll_y1.place(x=1135,y=200,height=243)

        ordertable.heading('#1', text='Item id')
        ordertable.heading('#2', text='Item name')
        ordertable.heading('#3', text='Price')
        ordertable.heading('#4', text='Quantity')
        ordertable.heading('#5', text='Total cost')

        ordertable['show'] = 'headings'
        ordertable.column('#1', stretch=tk.YES)
        ordertable.column('#2', stretch=tk.YES)
        ordertable.column('#3', stretch=tk.YES)
        ordertable.column('#4', stretch=tk.YES)
        ordertable.column('#5', stretch=tk.YES)
        ordertable.place(x=130,y=200)

        #-----for button----

        self.order_button = tk.Button(self, text="Place order", font=("times now", 15),
                                      fg="white",
                                      bg="#d77337",command= self.place_order_database_con,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.order_button.place(x=530, y=430, width=180, height=40)

        #-----database connection---------
        try:
            cursor = con.cursor()
            create_sql = 'select a.`Item_Id`, a.`Item_Name`,a.`Cost`,b.`total_num_orders`,a.`Cost` * b.`total_num_orders` total_cost from `rms_db`.`rms_menu_table` a,`rms_db`.`' + self.master.temp_table_name + '`  b where b.order_item = a.Item_Name'
            cursor.execute(create_sql)
            for ROWS in cursor:
                ordertable.insert('', 'end', values=ROWS)
        except mysql.connector.Error as e:
            print(e)

    ######----database connection with exception handling-------#######
    # -----for button----
    def place_order_database_con(self):
        try:
            cursor = con.cursor(buffered=True)
            cursor.execute('select  order_item,total_num_orders from  `rms_db`.`' + self.master.temp_table_name + '`')
            data1 = cursor.fetchone()
            if(data1 is None):
                tk.messagebox.showinfo("Empty  cart", f"Your cart is empty", master=self)
            else:
                cursor.execute('select max(order_id) from rms_db.RMS_order_table')
                data = cursor.fetchone()
                if data is None:
                    new_order_id = 1
                else:
                    new_order_id = data[0] + 1
                if self.master.dropdown == 0:
                    table_num = 'null'
                else:
                    table_num = str(self.master.dropdown)
                self.a = datetime.datetime.now()
                cursor.execute('insert into rms_db.rms_order_table ( select \'' + str(new_order_id) + '\',\'' +str(self.master.user_id)+ '\', a.`Item_Id` , a.`Item_Name` , a.`Cost` ,b.total_num_orders, \'Order Placed\',null,' +  table_num + ',\''  + str(self.a) +'\'  from `rms_db`.`rms_menu_table` a,`rms_db`.`' +self.master.temp_table_name + '` b where b.order_item = a.Item_Name AND a.Availability=\'yes\')')
                cursor.execute('delete from `rms_db`.`' + self.master.temp_table_name + '`')
                con.commit()
                tk.messagebox.showinfo("place order", f"order placed", master=self)
                self.master.switch_frame(Customer_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)


class Cancel_Order(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/orderbg6.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        #---label
        tk.Label(self, text="Select Order Id", font=("Goudy old style", 19, "bold"), fg="blue",bg="#ac837a").place( x=95, y=100)
        # dropdown with order id in order select for cancel button
        try:
            cursor = con.cursor()
            create_sql = 'select DISTINCT order_id from rms_db.RMS_ORDER_TABLE where USER_ID=\'' +str(self.master.user_id)+ '\' AND Bill_id is null'
            cursor.execute(create_sql)
            self.userid = []
            i = 0
            for ROWS in cursor:
                self.userid.insert(i, ROWS[0])
                i = i + 1
        except mysql.connector.Error as e:
            print(e)
        # -----del button----
        # dropdown with usertype
        self.reg_variable = StringVar(self)
        self.reg_variable.set("Order id")
        if len(self.userid) > 0 :
            self.drop1 = OptionMenu(self, self.reg_variable, * self.userid)
            self.drop1.config(width=27, height=0, fg="blue", bg="#d77337", font=("bold"), relief=RIDGE, bd=7,
                              activeforeground="blue", activebackground="yellow")
            self.drop1.place(x=95, y=160)
        else:
            self.master.switch_frame(Customer_page, 0, 0, 700, 1500)

        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # ---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")
        #########creating scrollbar#########
        scroll_y1 = ttk.Scrollbar(self, orient=VERTICAL, style="TScrollbar",cursor="dot")
        ###########set scrollbar with treeview#######
        ########### order  table using treeview############-----
        ordertable = ttk.Treeview(self, column=('ORDER ID', 'USER  ID', 'ITEM ID','ITEM NAME', 'PRICE'), yscrollcommand=scroll_y1.set)
        scroll_y1.config(command=ordertable.yview)
        scroll_y1.place(x=1104,y=252,height=244)
        ordertable.heading('#1', text='ORDER ID')
        ordertable.heading('#2', text='USER  ID')
        ordertable.heading('#3', text='ITEM ID')
        ordertable.heading('#4', text='ITEM NAME')
        ordertable.heading('#5', text='PRICE')
        ordertable['show'] = 'headings'
        ordertable.column('#1', stretch=tk.YES)
        ordertable.column('#2', stretch=tk.YES)
        ordertable.column('#3', stretch=tk.YES)
        ordertable.column('#4', stretch=tk.YES)
        ordertable.column('#5', stretch=tk.YES)
        ordertable.place(x=100,y=250)
        self.cancel_order_button = tk.Button(self, text="Cancel order", command=self.cancel_order_button,
                                             font=("times now", 15),
                                             fg="white",
                                             bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.cancel_order_button.place(x=500, y=470, width=180, height=40)
        # -----database connection with order table-------
        try:
            cursor = con.cursor()
            create_sql = 'select order_id,USER_ID,Item_Id,Item_Name,Price from rms_db.RMS_ORDER_TABLE where USER_ID=\'' +str(self.master.user_id)+ '\' AND Bill_id is null'
            cursor.execute(create_sql)
            for ROWS in cursor:
                ordertable.insert('', 'end', values=ROWS)
        except mysql.connector.Error as e:
            print(e)
        ######----database connection with exception handling-------#######
        #-----for button----
    def cancel_order_button(self):
        orderid=self.reg_variable.get()
        try:
            cursor = con.cursor()
            cursor.execute('select TIMESTAMPDIFF(MINUTE,DATETIME,\''  + str(datetime.datetime.now()) +'\') FROM rms_db.RMS_ORDER_TABLE where Bill_id is null AND order_id=\'' + orderid + '\'')
            Timediff= cursor.fetchone()[0]
            if(Timediff>5):
                tk.messagebox.showerror("Cancel order", f"Selected Order can not be canceled! It has exceeded 15 minutes limit", master=self)
            else:
                cursor.execute('DELETE FROM rms_db.RMS_ORDER_TABLE where Bill_id is null AND order_id=\'' +orderid + '\'')
                con.commit()
                tk.messagebox.showinfo("Cancel order", f"order canceled", master=self)
                self.master.switch_frame(Customer_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)

class Table_booking_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/booktable.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        ########bg img#######
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        ########frame #########
        Frame_tablebooking_page = tk.Frame(self, bg="#bc926a",relief=RIDGE,bd=10)
        Frame_tablebooking_page.place(x=250, y=100, height=500, width=750)
        ##########title###########
        self.title = tk.Label( Frame_tablebooking_page, text="Book Your Table", font=("Impact", 35, "bold"), fg="#5c241e",bg="#bc926a")
        self.title.place(x=200, y=10)
        tk.Label(Frame_tablebooking_page, text="Table No", font=("Goudy old style", 19, "bold"), fg="#5c241e",bg="#bc926a").place(x=25, y=100)
        #-----dropdown taking value from database--------
        try:
            cursor = con.cursor()
            create_sql = 'select Table_no from rms_db.RMS_BOOK_TABLE where USER_NAME is null'
            cursor.execute(create_sql)
            self.table_no = []
            i = 0
            for ROWS in cursor:
                self.table_no.insert(i, ROWS[0])
                i= i + 1
        except mysql.connector.Error as e:
            print(e)

        self.booktable = StringVar(Frame_tablebooking_page)
        self.booktable.set("Table no")
        self.drop = OptionMenu(Frame_tablebooking_page, self.booktable, * self.table_no)
        self.drop.config(width=33, height=0, bg="lightgray", fg="#5c241e", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop.place(x=25, y=150)
        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # ---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")

        scroll_y1 = ttk.Scrollbar(Frame_tablebooking_page, orient=VERTICAL, style="TScrollbar",cursor="dot")
        ###########set scrollbar with treeview#######
        ########### book table using treeview############-----

        booktable = ttk.Treeview(Frame_tablebooking_page, column=('Table No', 'User Name'),
                              yscrollcommand=scroll_y1.set)

        scroll_y1.place(x=430, y=216, height=244)
        scroll_y1.config(command= booktable.yview)

        booktable.heading('#1', text='Table No')
        booktable.heading('#2', text='User Name')
        booktable['show'] = 'headings'
        booktable.column('#1', stretch=tk.YES)
        booktable.column('#2', stretch=tk.YES)
        booktable.place(x=25, y=215)
        ######----database connection with exception handling-------#######
        try:
            cursor = con.cursor()
            create_sql = 'select Table_no, USER_NAME from rms_db.RMS_BOOK_TABLE   where  USER_NAME = \'' +  self.master.username + '\' '
            cursor.execute(create_sql)
            for ROWS in cursor:
                booktable.insert('', 'end', values=ROWS)
        except mysql.connector.Error as e:
            print(e)
        # --to open  image------
        self.image = PIL.Image.open("images/table1.jpg")
        # To resize image
        self.resized2 = self.image.resize((260, 350))
        self.new_pic2 = ImageTk.PhotoImage(self.resized2)
        PIC_label = tk.Label(Frame_tablebooking_page, image=self.new_pic2)
        PIC_label.place(x=456, y=110)
        ######button#######
        self.booktable_button = tk.Button(self, text="Book Table",command=self.book_table, font=("times now", 15),
                                     fg="white",
                                     bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")

        self.booktable_button.place(x=530, y=580, width=180, height=40)

    def book_table(self):
        ######----database connection with exception handling-------#######
        try:
            cursor = con.cursor()
            tableno = self.booktable.get()
            cursor.execute('UPDATE rms_db.RMS_BOOK_TABLE SET USER_NAME = \'' +  self.master.username + '\' where Table_no=\'' +tableno + '\'')
            con.commit()
            tk.messagebox.showinfo("Table Booked", f"Table is booked", master=self)
            self.master.switch_frame(Table_booking_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)

class Manage_Table_booking_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/managetablebg.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        #---creating a frame-------
        Frame_manage_table_page = tk.Frame(self, bg="#d2984d",relief=RIDGE,bd=10)
        Frame_manage_table_page.place(x=270, y=100, height=500, width=750)

        self.title = tk.Label(Frame_manage_table_page, text="Manage Table Booking", font=("Impact", 35, "bold"),
                              fg="#805516",bg="#d2984d")
        self.title.place(x=25, y=25)
        style_table = ttk.Style()
        style_table.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        style_table.configure('Treeview', font=('times', 15, 'bold'), background="yellow", foreground="black")
        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # ---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")

        scroll_y1 = ttk.Scrollbar(Frame_manage_table_page, orient=VERTICAL, style="TScrollbar",cursor="dot")
        ###########set scrollbar with treeview#######
        ########### book table using treeview############-----

        book_table = ttk.Treeview(Frame_manage_table_page, column=('Table No', 'User Name'),
                             yscrollcommand=scroll_y1.set)
        scroll_y1.config(command=book_table.yview)
        scroll_y1.place(x=430, y=100, height=244)
        book_table.heading('#1', text='Table No')
        book_table.heading('#2', text='User Name')
        book_table['show'] = 'headings'
        book_table.column('#1', stretch=tk.YES)
        book_table.column('#2', stretch=tk.YES)
        book_table.place(x=25, y=100)
        #-----label-----
        tk.Label(Frame_manage_table_page, text="Table No", font=("Goudy old style", 19, "bold"), fg="#805516",bg="#d2984d").place(x=25, y=355)
        tk.Label(Frame_manage_table_page, text="User Name", font=("Goudy old style", 19, "bold"), fg="#805516",bg="#d2984d").place( x=350, y=355)
        # --to open  image------
        self.image = PIL.Image.open("images/managetable.jpg")
        # To resize image
        self.resized2 = self.image.resize((260, 245))
        self.new_pic2 = ImageTk.PhotoImage(self.resized2)
        PIC_label = tk.Label(Frame_manage_table_page, image=self.new_pic2)
        PIC_label.place(x=456, y=97)

        # -----database connection---------
        try:
            cursor = con.cursor()
            create_sql = 'select * from rms_db.RMS_BOOK_TABLE'
            cursor.execute(create_sql)
            for ROWS in cursor:
                book_table.insert('', 'end', values=ROWS)
         # -----dropdown taking value from database for clearing table booking--------
            cursor = con.cursor()
            create_sql = 'select  Table_no from rms_db.RMS_BOOK_TABLE'

            cursor.execute(create_sql)
            self.table_no = []
            i = 0
            for ROWS in cursor:
                self.table_no.insert(i, ROWS[0])
                i = i + 1
        except mysql.connector.Error as e:
            print(e)
        self.del_booktable = StringVar(Frame_manage_table_page)
        self.del_booktable.set("Table no")
        self.drop = OptionMenu(Frame_manage_table_page, self.del_booktable, *self.table_no)
        self.drop.config(width=20, height=0, bg="lightgray", fg="#805516", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop.place(x=25, y=400)
        #---button---
        self.clear_booktable_button = tk.Button(self, text="Clear Table", command=self.clear_booking, font=("times now", 15),
                                          fg="white",
                                          bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")

        self.clear_booktable_button.place(x=350, y=580, width=180, height=40)
        #----new booking dropdown------#####
        # -----dropdown taking value from database for booking table--------####
        try:
            cursor = con.cursor()
            create_sql = 'select  USER_NAME from rms_db.RMS_USER_DETAILS where User_Type= \'customer\''
            cursor.execute(create_sql)
            self.table_no = []
            i = 0
            for ROWS in cursor:
                self.table_no.insert(i, ROWS[0])
                i=i + 1
        except mysql.connector.Error as e:
            print(e)
        ######dropdown#######
        self.user_name = StringVar(Frame_manage_table_page)
        self.user_name.set("User Name")
        self.newbooking = OptionMenu(Frame_manage_table_page, self.user_name, * self.table_no)
        self.newbooking.config(width=20, height=0, bg="lightgray", fg="#805516", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.newbooking.place(x=350, y=400)
        self.new_booktable_button = tk.Button(self, text="Book Table", command=self.new_booking,
                                                font=("times now", 15),
                                                fg="white",
                                                bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")

        self.new_booktable_button.place(x=670, y=580, width=180, height=40)
    def clear_booking(self):
        ######----database connection with exception handling-------#######
        try:
            cursor = con.cursor()
            tableno = self.del_booktable.get()
            cursor.execute('UPDATE rms_db.RMS_BOOK_TABLE SET USER_NAME= NULL where Table_no=\'' + tableno + '\'')
            con.commit()
            tk.messagebox.showinfo("Table Empty", f"Table is now empty", master=self)
            self.master.switch_frame(Manage_Table_booking_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)

    def new_booking(self):
        ######----database connection with exception handling-------#######
        try:
            cursor = con.cursor()
            username = self.user_name .get()
            tableno1 = self.del_booktable.get()
            cursor.execute('UPDATE rms_db.RMS_BOOK_TABLE SET USER_NAME = \'' +  username+ '\' where Table_no=\'' + tableno1 + '\'')
            con.commit()
            tk.messagebox.showinfo("Table Booked", f"Table is Booked", master=self)
            self.master.switch_frame(Manage_Table_booking_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)
class Generate_bill(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/generate6.jpg")
        # -------To resize image---------
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        ####label####
        self.title = tk.Label(self, text="Billing counter", font=("Impact", 35, "bold"), fg="#d77337",bg="#27200d")
        self.title.place(x=25, y=90)
        tk.Label(self, text="Order id", font=("Goudy old style", 19, "bold"),
                 fg="#d25d17",bg="#27200d").place(x=25, y=180)
        try:
            ######----database connection with exception handling-------#######
            cursor = con.cursor()
            create_sql = 'select DISTINCT order_id from rms_db.RMS_ORDER_TABLE where Bill_id is null'
            cursor.execute(create_sql)
            self.orderid = []
            i = 0
            for ROWS in cursor:
                self.orderid.insert(i, ROWS[0])
                i=i+1
        except mysql.connector.Error as e:
            print(e)
        ######dropdown#########
        self.order = StringVar(self)
        self.order.set("Order Id")
        self.drop1 = OptionMenu(self, self.order, *self.orderid)
        self.drop1.config(width=27, height=0, fg="#27200d",bg="#d25d17", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop1.place(x=25, y=230)
        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # ---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")

        scroll_y1 = ttk.Scrollbar(self, orient=VERTICAL, style="TScrollbar",cursor="dot")
        ###########set scrollbar with treeview#######
        ########### order table using treeview############-----

        ordertable = ttk.Treeview(self, column=('User Name','order_id', 'Item name', 'Price', 'Quantity', 'Total cost'),
                              yscrollcommand=scroll_y1.set)
        scroll_y1.config(command=ordertable.yview)
        scroll_y1.place(x=1227, y=300,height=244)
        ordertable.heading('#1', text='User Name')
        ordertable.heading('#2', text='Order id')
        ordertable.heading('#3', text='Item name')
        ordertable.heading('#4', text='Price')
        ordertable.heading('#5', text='Quantity')
        ordertable.heading('#6', text='Total cost')
        #####defining heading########
        ordertable['show'] = 'headings'
        ordertable.column('#1', stretch=tk.YES)
        ordertable.column('#2', stretch=tk.YES)
        ordertable.column('#3', stretch=tk.YES)
        ordertable.column('#4', stretch=tk.YES)
        ordertable.column('#5', stretch=tk.YES)
        ordertable.column('#6', stretch=tk.YES)
        ordertable.place(x=25, y=300)

        ######----database connection with exception handling-------#######
        try:
            cursor = con.cursor()
            create_sql = 'select b.`USER_NAME`,a.`order_id`, a.`Item_Name`,a.`Price`,a.`Quantity`,a.`Price` * a.`Quantity` total_cost from `rms_db`.`rms_ORDER_table` a,`rms_db`.`rms_USER_DETAILS`b where a.USER_ID = b.USER_ID AND a.Bill_id is null'
            cursor.execute(create_sql)
            for ROWS in cursor:
                ordertable.insert('', 'end', values=ROWS)
        except mysql.connector.Error as e:
            print(e)

        self.Bill_button = tk.Button(self, text="Generate Bill",command=self.printbill,font=("times now", 15),
                                         fg="white",
                                         bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")

        self.Bill_button.place(x=530, y=545,width=180,height=40)
    def printbill(self):
        self.master.order_id_dropdown_value = self.order.get()
        if(self.master.order_id_dropdown_value=="Order Id"):
            tk.messagebox.showinfo("Order Id", f"Please select a order id", master=self)
        else:
            ######----database connection with exception handling-------#######
            try:
                cursor = con.cursor()
                cursor.execute('UPDATE rms_db.RMS_ORDER_TABLE SET Food_status = \'Bill Generated\' where order_id=\'' +self.master.order_id_dropdown_value + '\'')
                con.commit()
                tk.messagebox.showinfo("Generate Bill", f"Bill is Genarated", master=self)
                self.master.switch_frame(print_bill, 0, 0, 700, 1500)
            except mysql.connector.Error as e:
                print(e)
#-----print bill-------
class print_bill(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/orderbg3.jpg")
        # -------To resize image---------
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        ######label########
        tk.Label(self, text="Print Bill", font=("Impact", 35, "bold"),
                 fg="#fbb760",bg="#2f2d22").place(x=525, y=90)
        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # ---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')
        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")

        scroll_y1 = ttk.Scrollbar(self, orient=VERTICAL, style="TScrollbar",cursor="dot")
        ###########set scrollbar with treeview#######
        ########### order table using treeview############-----
        ordertable = ttk.Treeview(self, column=('Bill Id', 'User Name','order_id', 'Item name', 'Price', 'Quantity', 'Total cost'),
                              yscrollcommand=scroll_y1.set)
        #------linking scrollbar to treeview---------
        scroll_y1.config(command=ordertable.yview)
        scroll_y1.place(x=1005,y=200,height=244)
        ordertable.heading('#1', text='Bill id')
        ordertable.heading('#2', text='User Name')
        ordertable.heading('#3', text='Order id')
        ordertable.heading('#4', text='Item name')
        ordertable.heading('#5', text='Price')
        ordertable.heading('#6', text='Quantity')
        ordertable.heading('#7', text='Total cost')
        #####defining heading########
        ordertable['show'] = 'headings'
        ordertable.column('#1', width=100)
        ordertable.column('#2', width=100)
        ordertable.column('#3', width=100)
        ordertable.column('#4', width=100)
        ordertable.column('#5', width=100)
        ordertable.column('#6', width=100)
        ordertable.column('#7', width=100)
        ordertable.place(x=300,y=200)
        ######----database connection-------#######
        try:
            cursor = con.cursor()
            cursor.execute('select max(Bill_id) from rms_db.RMS_order_table')
            data = cursor.fetchone()
            if data[0] is None:
                new_bill_id = 1
            else:
                new_bill_id = data[0] + 1
            cursor.execute('UPDATE  rms_db.rms_order_table SET Bill_id=\''+ str(new_bill_id) + '\' where order_id= \'' + self.master.order_id_dropdown_value+ '\'')
            con.commit()
            create_sql = 'select a.`Bill_id`,b.`USER_NAME`,a.`order_id`, a.`Item_Name`,a.`Price`,a.`Quantity`,a.`Price` * a.`Quantity` total_cost from `rms_db`.`rms_ORDER_table` a,`rms_db`.`rms_USER_DETAILS`b where a.USER_ID = b.USER_ID AND  order_id= \'' + self.master.order_id_dropdown_value+ '\''
            cursor.execute(create_sql)
            for ROWS in cursor:
                ordertable.insert('','end', values=ROWS)
            cursor.execute('select sum(a.`Price` * a.`Quantity`) total_cost from `rms_db`.`rms_order_table` a, `rms_db`.`rms_USER_DETAILS` b where a.USER_ID = b.USER_ID AND order_id= \'' + self.master.order_id_dropdown_value+ '\'')
            data=cursor.fetchone()
        except mysql.connector.Error as e:
            print(e)
        #######label########
        tk.Label(self, text='Total Amount =  ' + str( data[0]) , font=("Goudy old style", 19, "bold"),fg="#6c4739",bg="#fae7c9").place(x=540, y=480)
        ######button########
        self.print_Bill_button = tk.Button(self, text="Print Bill", font=("times now", 15),fg="#fbb760", bg="#6c4739",command=self.printbill_but,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.print_Bill_button.place(x=555, y=540, width=180, height=40)
    def printbill_but(self):
        tk.messagebox.showinfo("Collect Bill", f"Collect your Bill", master=self)
        ########save FPDF() class into a fpdf module######
        # variable pdf
        self.pdf = FPDF()
        # Add a page
        self.pdf.add_page()

        #######Effective page width, or just epw#########
        self.effective_page_width = self.pdf.w - 2 *self. pdf.l_margin

        ######Set column width to 1/4 of effective page width to distribute content########
        # evenly across table and page
        self.col_width = self.effective_page_width / 6
        ######set font########
        self.pdf.set_font('Times', 'B', 14.0)
        self.pdf.cell(self.effective_page_width, 0.0, 'Resturant Management System ', align='C')
        self.pdf.set_font('Times', '', 10.0)
        self.pdf.ln(0)
        #######Text height is the same as current font size
        self.font= self.pdf.font_size
        # Line break equivalent to 4 lines
        self.pdf.ln(4 * self.font)
        # -----database connection---------
        cursor = con.cursor()
        create_sql = 'select b.`USER_NAME`,a.`order_id`, a.`Item_Name`,a.`Price`,a.`Quantity`,a.`Price` * a.`Quantity` total_cost from `rms_db`.`rms_ORDER_table` a,`rms_db`.`rms_USER_DETAILS`b where a.USER_ID = b.USER_ID AND order_id= \'' + self.master.order_id_dropdown_value + '\''
        cursor.execute(create_sql)

        for row in ['User Name','Order Id','Item Name','Per Unit Cost','Quantity', 'Total Cost']:
            # create a cell
            self.pdf.set_fill_color(235, 180, 52)
            self.pdf.cell(self.col_width, 2 * self.font, str(row), border=1,fill=True)
        self.pdf.ln(2 * self.font)
        for row in cursor:
            username = row[0]
            for data_value in row:
                # Enter data in colums
                self.pdf.cell(self.col_width, 2 * self.font, str(data_value), border=1)
            self.pdf.ln(2 * self.font)
        self.pdf.ln(2* self.font)
     #fetch data from database to calculate total cost
        cursor.execute('select sum(a.`Price` * a.`Quantity`) total_cost from `rms_db`.`rms_order_table` a,`rms_db`.`rms_USER_DETAILS` b where a.USER_ID = b.USER_ID AND order_id= \'' + self.master.order_id_dropdown_value + '\'')
        data = cursor.fetchone()
        self.pdf.set_font('Times','B', 14.0)
        self.pdf.cell(self.effective_page_width, 0.0, 'Total Amount is = '+ str( data[0]) , align='L')
        self.pdf.set_font('Times', '', 10.0)
        self.pdf.ln(8)
        self.pdf.set_font('Times', 'B', 14.0)
        self.pdf.cell(self.effective_page_width, 0.0, 'Thank You Very much for ordering  !', align='L')
        self.pdf.set_font('Times', '', 10.0)
        self.pdf.ln(9)
        # save the pdf with name .pdf
        self.pdf.output(username+'_Bill.pdf')
        os.startfile(username+'_Bill.pdf')
        self.master.switch_frame(Manager_page, 0, 0, 700, 1500)

class Feedback_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # --to open  image------
        self.image = PIL.Image.open("images/wood1.jpg")
        # To resize image
        self.resized = self.image.resize((1500, 700))
        self.new_pic = ImageTk.PhotoImage(self.resized)
        #####bg img#########

        self.bg_image = tk.Label(self, image=self.new_pic).place(x=0, y=0, relwidth=1, relheight=1)
        self.feedback=StringVar()
        #----create frame------
        Frame_feedbackpage = tk.Frame(self, height=230, width=400, relief=RIDGE,bd=10,bg="#e5d8be")
        Frame_feedbackpage.place(x=345, y=100, height=450, width=600)
        self.title = tk.Label(Frame_feedbackpage,text="Feedback Page", font=("Impact", 35, "bold"), fg="#d77337",bg="#e5d8be")
        self.title.place(x=90, y=30)
        #-----create label----------
        tk.Label(Frame_feedbackpage, text="Provide feedback", font=("Goudy old style", 19, "bold"),fg="#d25d17",bg="#e5d8be").place(x=90, y=99)\
        #---------create test box---------
        self.txt_user = tk.Text(Frame_feedbackpage, font=("times new roman", 15), bg="lightgray",bd=5,relief=RIDGE)
        self.txt_user.place(x=90, y=150, width=400, height=250)
        ######button##########

        self.submit_button = tk.Button(self, text="Submit", font=("times now", 15),
                                      fg="white",
                                      bg="#d77337",command=self.feedback_connection,relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.submit_button.place(x=550, y=530, width=180, height=40)
    def feedback_connection(self):
        if  self.txt_user.get("1.0",END) == "":
            tk.messagebox.showerror("Error", "Please provide your feedback here", master=self)
        else:
            #---database connection---------
            feedback = self.txt_user.get("1.0",END)
            try:
                cursor = con.cursor()
                cursor.execute('select max(Feedback_id) from rms_db.RMS_FEEDBACK_TABLE')
                new_feedback_id = cursor.fetchone()[0] + 1
                cursor.execute('insert into rms_db.RMS_FEEDBACK_TABLE (`Feedback_id`,`USER_NAME`,`Feedbacks`) values(%s,%s,%s)',(new_feedback_id, self.master.username, feedback))
                con.commit()
                tk.messagebox.showinfo("Create Account", f"Feedback is added Succesfully", master=self)
                self.master.switch_frame(Customer_page, 0, 0, 700, 1500)
            except mysql.connector.Error as e:
                print(e)


 # -----track order page--------
class track_order_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----images-----
        # --to open an image------
        self.image = PIL.Image.open("images/track order.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)

        self.title = tk.Label(self, text="Track Your Current Order", font=("Impact", 35, "bold"), fg="#d77337",bg="#0861c4")
        self.title.place(x=380, y=100)
        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # ---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")

        scroll_y1 = ttk.Scrollbar(self, orient=VERTICAL, style="TScrollbar", cursor="dot")
        ###########set scrollbar with treeview#######
        ########### order table using treeview############-----
        ordertable = ttk.Treeview(self, column=( 'User id', 'Item id', 'Item name'),yscrollcommand=scroll_y1.set)
        scroll_y1.config(command=ordertable.yview)
        scroll_y1.place(x=935, y=200, height=247)
        ordertable.heading('#1', text='User Name')
        ordertable.heading('#2', text='Item id')
        ordertable.heading('#3', text='Item name')
        ordertable['show'] = 'headings'

        ordertable.column('#1', stretch=tk.YES)
        ordertable.column('#2', stretch=tk.YES)
        ordertable.column('#3', stretch=tk.YES)

        ordertable.place(x=330, y=200)
        # -----database connection with order table-------
        try:
            cursor = con.cursor()
            create_sql = 'select b.USER_NAME,a.Item_Id,a.Item_Name,a.Quantity from `rms_db`.`rms_order_table` a, `rms_db`.`rms_USER_DETAILS` b where  a.USER_ID = b.USER_ID AND b.USER_NAME= \'' +  self.master.username + '\' AND Bill_id is null'
            cursor.execute(create_sql)
            for ROWS in cursor:
                ordertable.insert('', 'end', values=ROWS)
        except mysql.connector.Error as e:
            print(e)
        #####labels########
        label1 = tk.Label(self, text="Order received", font=("arial", 15, "bold"))
        label1.place(x=150, y=480)
        label2 = tk.Label(self, text="Food is preparing", font=("arial", 15, "bold"))
        label2.place(x=425, y=480)
        label3 =tk. Label(self, text="Order Ready", font=("arial", 15, "bold"))
        label3.place(x=720, y=480)
        label4 = tk.Label(self, text="Bill Generated", font=("arial", 15, "bold"))
        label4.place(x=1010, y=480)
        #####button##########

        self.refresh_button = tk.Button(self, text='Refresh', command=self.bar, width=13, height=1, font=("arial", 15, "bold"),
                                 foreground="white", background="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.refresh_button.place(x=540, y=580)
        ######progressbar########
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TProgressbar", foreground="#d77337", background="#3f7abe")
        self.progress =  ttk.Progressbar(self, style="TProgressbar",length=1000, mode="determinate")
        self.progress.place(x=150, y=530)


    def bar(self):
        ###################database connection
        try:
            cursor = con.cursor()
            cursor.execute('select a.Food_status from `rms_db`.`rms_order_table` a, `rms_db`.`rms_USER_DETAILS` b where  a.USER_ID = b.USER_ID AND b.USER_NAME= \'' + self.master.username + '\' AND a.Bill_id is null ')
            data = cursor.fetchone()
            Track_order = data[0]
            if   Track_order == 'Order Placed':
                self.progress['value'] = 7
            elif  Track_order =='Food is preparing':
                self.progress['value'] = 37
            elif Track_order == 'Order ready':
                self.progress['value'] = 63
            else:
                self.progress['value'] = 100
        except mysql.connector.Error as e:
            print(e)

class cook_order_list_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----images-----####
        # --to open an image------#####
        self.image = PIL.Image.open("images/cookorderlist.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        #####---label----###
        tk.Label(self, text="Select User Id", font=("Goudy old style", 19, "bold"), fg="black",bg="#cf8a51").place(
            x=95, y=100)
        tk.Label(self, text="Select Food Status", font=("Goudy old style", 19, "bold"), fg="black",bg="#cf8a51").place(
            x=95, y=220)
        ###########dropdown with food status###############
        self.foodstatus = [ "Food is preparing", "Order ready"]
        self.reg_variable = StringVar(self)
        self.reg_variable.set("Food status")
        self.drop1 = OptionMenu(self, self.reg_variable, *self.foodstatus)
        self.drop1.config(width=27, height=0, bg="lightgray", fg="black", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop1.place(x=95, y=280)

        # ----for styling heading of table-----
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # ---styling table-----
        self.style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), background='orange', foreground='blue')
        self.style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')

        # ---styling scrollbar-------
        self.style.theme_use('clam')
        self.style.configure("TScrollbar", foreground="red", background="orange")

        scroll_y1 = ttk.Scrollbar(self, orient=VERTICAL, style="TScrollbar", cursor="dot")
        ###########set scrollbar with treeview#######

        ordertable = ttk.Treeview(self, column=('Order id', 'User id', 'Item id', 'Item name','Food Status'),
                             yscrollcommand=scroll_y1.set)
        scroll_y1.config(command=ordertable.yview)
        scroll_y1.place(x=1100, y=370, height=243)
        ###########table using treeview############
        ordertable.heading('#1', text='Order id')
        ordertable.heading('#2', text='User id')
        ordertable.heading('#3', text='Item id')
        ordertable.heading('#4', text='Item name')
        ordertable.heading('#5', text='Food Status')

        ordertable['show'] = 'headings'

        ordertable.column('#1', stretch=tk.YES)
        ordertable.column('#2', stretch=tk.YES)
        ordertable.column('#3', stretch=tk.YES)
        ordertable.column('#4', stretch=tk.YES)
        ordertable.column('#5', stretch=tk.YES)
        ordertable.place(x=95, y=370)
        ######button########
        self.order_status_button = tk.Button(self, text="Update Status", command=self.order_status,
                                             font=("times now", 15),
                                             fg="white",
                                             bg="#d77337",relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.order_status_button.place(x=500, y=590, width=180, height=40)
        ########dropdown with user id from database table##############
        try:
            cursor = con.cursor()
            create_sql = 'select DISTINCT USER_ID from rms_db.RMS_ORDER_TABLE where Bill_id is null'
            cursor.execute(create_sql)
            self.userid = []
            i = 0
            for ROWS in cursor:
                self.userid.insert(i, ROWS[0])
                i = i + 1
        except mysql.connector.Error as e:
            print(e)
        # -----del button----

        #######dropdown with userid##########

        self.user_variable = StringVar(self)
        self.user_variable.set("USER ID")
        self.drop1 = OptionMenu(self, self.user_variable, *self.userid)
        self.drop1.config(width=27, height=0, bg="lightgray", fg="black", font=("bold"),relief=RIDGE,bd=7,activeforeground="blue",activebackground="yellow")
        self.drop1.place(x=95, y=150)
        #-----database connection with order table-------
        try:
            cursor = con.cursor()
            create_sql = 'select order_id,USER_ID,Item_Id,Item_Name,Quantity,Food_status from rms_db.RMS_ORDER_TABLE where Bill_id is null'
            cursor.execute(create_sql)
            for ROWS in cursor:
                ordertable.insert('', 'end', values=ROWS)
        except mysql.connector.Error as e:
            print(e)

    def order_status(self):
        ###################database connection
        try:
            cursor = con.cursor()
            userid = self.user_variable.get()
            status=  self.reg_variable.get()
            cursor.execute('UPDATE rms_db.RMS_ORDER_TABLE SET Food_status = \'' +status + '\' where USER_ID=\'' +userid + '\'')
            con.commit()
            tk.messagebox.showinfo("Updated status", f"Status is updated successfully", master=self)
            self.master.switch_frame(cook_order_list_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)
# -----customer page--------
class Customer_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.backbuttom_enable = 0
        # ----for bg------
        # ----image----
        self.image = PIL.Image.open("images/wood-texture.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        # frame with borderwidth 6
        frame_customerpage = tk.Frame(self, bg="#e5d8be",relief=RIDGE,bd=10)
        frame_customerpage.place(x=250, y=90, height=550, width=750)
        # label name title assigned
        title = tk.Label(frame_customerpage, text="Customer Page", bd=2, width=17, height=2,bg="#e5d8be", fg="#d77337",
                      font=("Impact", 35, "bold"))
        title.place(x=150, y=0)
        # button with text MENU
        self.button1 = tk.Button(frame_customerpage, text="MENU", width=28, height=2, borderwidth=15, bg="#d77337",
                                 font=("bold"), fg="white",command=self.Menu,relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button1.place(x=10, y=120)
        # button with text ORDER ITEM
        self.button2 = tk.Button(frame_customerpage, text="Order An Item", width=28, height=2, borderwidth=15,
                                 bg="#d77337", font=("bold"), fg="white",command=self.Order_page,relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button2.place(x=10, y=260)
        # button with text CANCEL ORDER
        self.button3 = tk.Button(frame_customerpage, text="Cancel Order", width=28, height=2, borderwidth=15,
                                 bg="#d77337", font=("bold"), fg="white",command=self.Cancel_Order,relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button3.place(x=10, y=400)
        # button with text TRACK ORDER
        self.button4 = tk.Button(frame_customerpage, text="Book table", width=28, height=2, borderwidth=15,
                                 bg="#d77337", font=("bold"), fg="white",command=self.book_table_page,relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button4.place(x=380, y=120)
        # button with text REPORT
        self.button5 = tk.Button(frame_customerpage, text="Feedback", width=28, height=2, borderwidth=15, bg="#d77337",
                                 font=("bold"), fg="white",command=self.Feedback_page,relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button5.place(x=380, y=260)
        self.button6 = tk.Button(frame_customerpage, text="Track Order", width=28, height=2, borderwidth=15, bg="#d77337",
                                 font=("bold"), fg="white", command=self.track_order_page,relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button6.place(x=379, y=400)

    # ---------linking customer page buttons to another pages--------
    def Menu(self):
        self.master.switch_frame(Menu, 0, 0, 700, 1500)

    def book_table_page(self):
        self.master.switch_frame(Table_booking_page, 0, 0, 700, 1500)

    def Order_page(self):
        self.master.switch_frame(Order_page, 0, 0, 700, 1500)

    def Cancel_Order(self):
        ###################database connection
        try:
            cursor = con.cursor()
            create_sql = 'select COUNT(*) from rms_db.RMS_ORDER_TABLE  where USER_ID=\'' + str(self.master.user_id) + '\' AND Food_status=\'order placed\''
            cursor.execute(create_sql)
            data = cursor.fetchall()
            count= data[0]
            print(count[0])
            if count[0] == 0:
                tk.messagebox.showinfo("Order", f"No Order ", master=self)
            else:
                self.master.switch_frame(Cancel_Order, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)
    def Feedback_page(self):
        self.master.switch_frame(Feedback_page, 0, 0, 700, 1500)
    def track_order_page(self):
        self.master.switch_frame( track_order_page, 0, 0, 700, 1500)
# -----order  page--------
class Manager_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.backbuttom_enable = 0
        # ----for bg------
        # ----image----
        self.image = PIL.Image.open("images/wood-texture.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        frame_managerpage = tk.Frame(self,relief=RIDGE,bd=10,bg="#e5d8be")
        frame_managerpage.place(x=270, y=90, height=500, width=770)
        # label name page assigned
        page =tk.Label(frame_managerpage, text="Manager Page", bd=2, width=17, height=2, bg="#e5d8be", fg="#d77337",
                     font=("Impact", 35, "bold"))
        page.place(x=150, y=0)
        # button with text MENU
        self.button1 = tk.Button(frame_managerpage, text="MENU", width=28, height=2, borderwidth=15, bg="#d77337",command=self.Menu,
                                 font=("bold"), fg="white",relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button1.place(x=10, y=150)
        # button with text ORDER ITEM
        self.button2 = tk.Button(frame_managerpage, text="Manage Table Booking", width=28, height=2, borderwidth=15,
                                 bg="#d77337", font=("bold"), fg="white",command=self.managetable_page,relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button2.place(x=10, y=280)
        #####--- button with text CANCEL ORDER-----#####
        # button with text MANAGE ITEM
        self.button4 = tk.Button(frame_managerpage, text="Manage Item", width=28, height=2, borderwidth=15,command=self.Manage_item,
                                 bg="#d77337", font=("bold"), fg="white",relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button4.place(x=390, y=150)
        # button with text BILL
        self.button5 = tk.Button(frame_managerpage, text="Generate Bill", width=28, height=2, borderwidth=15,bg="#d77337",command=self.Generate_bill,
                                 font=("bold"), fg="white",relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button5.place(x=390, y=280)

    ##--------linking manager page buttons to another pages--------##
    def Menu(self):
        self.master.switch_frame(Menu, 0, 0, 700, 1500)
    def Manage_item(self):
        self.master.switch_frame(Manageitem_page, 0, 0, 700, 1500)
    def managetable_page(self):
        self.master.switch_frame(Manage_Table_booking_page, 0, 0, 700, 1500)
    def Generate_bill(self):
        try:
            ###################database connection
            cursor = con.cursor()
            create_sql = 'select COUNT(*) from rms_db.RMS_ORDER_TABLE where Bill_id is null '
            cursor.execute(create_sql)
            data=cursor.fetchall()
            count=data[0]
            if count[0] == 0:
                tk.messagebox.showinfo("Order", f"No pending order to generate bill ", master=self)
            else:
                self.master.switch_frame(Generate_bill, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)

#-----cook page--------
class cook_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # ----for bg------
        # ----image----
        self.image = PIL.Image.open("images/wood-texture.jpg")
        # To resize image
        self.resized1 = self.image.resize((1500, 700))
        self.new_pic1 = ImageTk.PhotoImage(self.resized1)
        self.bg_image1 = tk.Label(self, image=self.new_pic1).place(x=0, y=0, relwidth=1, relheight=1)
        # frame with borderwidth 6
        Frame_Order_PAGE = Frame(self,relief=RIDGE,bd=10,bg="#e5d8be")
        Frame_Order_PAGE.place(x=300, y=100, height=500, width=750)
        # label name cook assigned
        cook = tk.Label(Frame_Order_PAGE, text="Cook Page", bd=2, width=17, height=2, fg="#d77337",font=(" Impact", 35, "bold"),bg="#e5d8be")
        cook.place(x=130, y=0)
        # For displaying jpg image of chef using label
        self.image =PIL.Image.open("images/COOK.jpg")
        # To resize image
        self.resized = self.image.resize((300, 250))
        self.new_pic = ImageTk.PhotoImage(self.resized)
        PIC_label =tk. Label(Frame_Order_PAGE, image=self.new_pic,bg="#e5d8be")
        PIC_label.place(x=225, y=100)

        # button with button name ORDER LIST
        self.button1 = tk.Button(Frame_Order_PAGE,text="Order list", width=25, height=2, borderwidth=15,bg="#d77337", font=("bold"),
                                 fg="white",relief=RIDGE,activeforeground="blue",activebackground="yellow",command=self.orderlist)
        self.button1.place(x=30, y=370)
        # button with button name CHANGE MENU
        self.button2 = tk.Button(Frame_Order_PAGE, text="Manage Item", width=25, height=2,bg="#d77337",command=self.manageitem, borderwidth=15,
                                 font=("bold"), fg="white",relief=RIDGE,activeforeground="blue",activebackground="yellow")
        self.button2.place(x=390, y=370)

        ##--------linking cook page buttons to another pages--------##

    def orderlist(self):
        try:
            ###################database connection
            cursor = con.cursor()
            create_sql = 'select COUNT(*) from rms_db.RMS_ORDER_TABLE where Bill_id is null '
            cursor.execute(create_sql)
            data = cursor.fetchall()
            count = data[0]
            if count[0] == 0:
                tk.messagebox.showinfo("Order", f"No pending order ", master=self)
            else:
                self.master.switch_frame(cook_order_list_page, 0, 0, 700, 1500)
        except mysql.connector.Error as e:
            print(e)

    def manageitem(self):
        self.master.switch_frame(Manageitem_page, 0, 0, 700, 1500)


if __name__ == "__main__":
    root = login()
    root.mainloop()