import os
import shutil
from tkinter import messagebox
import customtkinter
import datetime
from PIL import Image
import customtkinter as ctk
from datetime import date

current_date = date.today()

# # # # # # # # # # create folders # # # # # # # # # #
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

create_folder("C:/Bank API/Mr_Pikachu Bank OFFICE/Customer" )
create_folder("C:/Bank API/Mr_Pikachu Bank OFFICE/mail" )
create_folder("C:/Bank API/Mr_Pikachu Bank API/Customer" )


def customer_content():
    global photo_label1,name_label1,adharno_label1,gender_label1,phoneno_label1,DOB_label1,ladd_label1,padd_label1,email_label1
 
    inside_scroll_frame = customtkinter.CTkFrame(scroll_frame, width=650, height=110,border_color="white",border_width=2,)
    inside_scroll_frame.pack()

    photo_label1 = ctk.CTkLabel(inside_scroll_frame,image=my_image3, text="")
    photo_label1.place(x=10,y=10)

    name_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    name_label1.place(x=80,y=5)

    adharno_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    adharno_label1.place(x=80,y=35)

    gender_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    gender_label1.place(x=80,y=65)

    phoneno_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    phoneno_label1.place(x=270,y=35)

    DOB_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    DOB_label1.place(x=270,y=65)

    ladd_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    ladd_label1.place(x=450,y=5)

    padd_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    padd_label1.place(x=450,y=35)

    email_label1 = ctk.CTkLabel(inside_scroll_frame, text="")
    email_label1.place(x=450,y=65)


# # # # # # # # # # Get and displey data # # # # # # # # # #
def customer_show_content():
    global file_path,stored_name, stored_mobile_no, stored_gender, stored_local_address, stored_per_address, stored_addhar, stored_DOBe, stored_email
    
    directory = "C:\Bank API\Mr_Pikachu Bank OFFICE\Customer\\"
    if not os.path.exists(directory):
        print("The C: drive does not exist or is not accessible.")
        return

    for base, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(base, file)
                try:
                    if os.path.exists(file_path):
                        with open(file_path, "r") as file:
                            credentials = file.readlines()
                            for line in credentials:
                                stored_name, stored_mobile_no, stored_gender, stored_local_address, stored_per_address, stored_addhar, stored_DOBe, stored_email= line.strip().split(",")
                                name_label1.configure(text=f"Name :  {stored_name}", text_color="white")
                                gender_label1.configure(text=f"Gender : {stored_gender}", text_color="white")
                                ladd_label1.configure(text=f"Local : {stored_local_address}", text_color="white")
                                padd_label1.configure(text=f"Permanent Addr : {stored_per_address}", text_color="white")
                                phoneno_label1.configure(text=f"Phone NO : {stored_mobile_no}", text_color="white")
                                adharno_label1.configure(text=f"Addhar No : {stored_addhar}", text_color="white")
                                DOB_label1.configure(text=f"Date of Birth : {stored_DOBe}", text_color="white")
                                email_label1.configure(text=f"Email : {stored_email}", text_color="white")
                                customer_content()
                               
                except Exception as e:
                    pass
                    # print(f"Error reading file {file_path}: {e}")



def balence_content():
    global photo_label,account_name_label,date_balence_label,add_balece_label,withdraw_label,total_balence_label,ladd_label,padd_label,email_label
 
    inside_scroll_frame1 = customtkinter.CTkFrame(scroll_frame, width=650, height=30)
    inside_scroll_frame1.pack()

    account_name_label = ctk.CTkLabel(inside_scroll_frame1, text="")
    account_name_label.place(x=10,y=5)

    date_balence_label = ctk.CTkLabel(inside_scroll_frame1, text="")
    date_balence_label.place(x=100,y=5)

    add_balece_label = ctk.CTkLabel(inside_scroll_frame1, text="")
    add_balece_label.place(x=300,y=5)

    withdraw_label = ctk.CTkLabel(inside_scroll_frame1, text="")
    withdraw_label.place(x=400,y=5)

    total_balence_label = ctk.CTkLabel(inside_scroll_frame1, text="")
    total_balence_label.place(x=500,y=5)


def show_balence_interface():    
    global aplication_file
    aplication_file = f"C:/Bank API/Mr_Pikachu Bank API/Customer/{show_detail}/Account/balence.txt"
    if os.path.exists(aplication_file):
        with open(aplication_file, "r") as file:
                credentials = file.readlines()
                for line in credentials:
                    global balence,withdraw,add
                    account_name, date, add, withdraw, balence = line.strip().split(",")
                    account_name_label.configure(text=f"{account_name}", text_color="white")
                    date_balence_label.configure(text=f"{date}", text_color="white")
                    add_balece_label.configure(text=f"{add}", text_color="white")
                    withdraw_label.configure(text=f"{withdraw}", text_color="white")
                    total_balence_label.configure(text=f"{balence}", text_color="white")
                    balence_content()


       
def add_balence():
    aplication_file = f"C:/Bank API/Mr_Pikachu Bank API/Customer/{show_detail}/Account/balence.txt"
    if os.path.exists(aplication_file):
        with open(aplication_file, "r") as file:
                credentials = file.readlines()
                for line in credentials:
                    global balence,withdraw,add
                    account_name, date, add, withdraw, balence = line.strip().split(",")
                    
    add_balence_in_account = balence_entry.get()
    balence1 = int(balence)+int(add_balence_in_account)
    withdraw = 0
    with open(aplication_file, "a") as file:
            file.write(f"{show_detail},{current_date},{add_balence_in_account},{withdraw},{balence1}\n")
            messagebox.showinfo("Info", "Add Balence Successful")


    with open(aplication_file, 'r') as file:
        lines = file.readlines()
        if lines:
            last = lines[-1].strip()
            account_name, date, add, withdraw, balence = last.strip().split(",")
            print(account_name, date, add, withdraw, balence)
            account_name_label.configure(text=f"{account_name}", text_color="white")
            date_balence_label.configure(text=f"{date}", text_color="white")
            add_balece_label.configure(text=f"{add}", text_color="white")
            withdraw_label.configure(text=f"{withdraw}", text_color="white")
            total_balence_label.configure(text=f"{balence}", text_color="white")
            balence_content()
                

def withdraw_balence():
    aplication_file = f"C:/Bank API/Mr_Pikachu Bank API/Customer/{show_detail}/Account/balence.txt"
    if os.path.exists(aplication_file):
        with open(aplication_file, "r") as file:
                credentials = file.readlines()
                for line in credentials:
                    global balence,withdraw,add
                    account_name, date, add, withdraw, balence = line.strip().split(",")
    

    add_balence_in_account = balence_entry.get()
    balence1 = int(balence)-int(add_balence_in_account)
    add = 0
    with open(aplication_file, "a") as file:
            file.write(f"{show_detail},{current_date},{add},{add_balence_in_account},{balence1}\n")
            messagebox.showinfo("Info", "Withdraw Balence Successful")
            
            
    with open(aplication_file, 'r') as file:
        lines = file.readlines()
        if lines:
            last = lines[-1].strip()
            account_name, date, add, withdraw, balence = last.strip().split(",")
            account_name_label.configure(text=f"{account_name}", text_color="white")
            date_balence_label.configure(text=f"{date}", text_color="white")
            add_balece_label.configure(text=f"{add}", text_color="white")
            withdraw_label.configure(text=f"{withdraw}", text_color="white")
            total_balence_label.configure(text=f"{balence}", text_color="white")
            balence_content()



def accept():
    stored_addhar_entry = addhar_entry.get()
    
    source_folder = f"C:\Bank API\Mr_Pikachu Bank OFFICE\mail\{stored_addhar_entry}"
    destination_folder1 = "C:\Bank API\Mr_Pikachu Bank OFFICE\Customer"
    destination_folder2 = "C:\Bank API\Mr_Pikachu Bank API\Customer"
    
    destination_folder_path1 = os.path.join(destination_folder1, os.path.basename(source_folder))
    destination_folder_path2 = os.path.join(destination_folder2, os.path.basename(source_folder))

    shutil.copytree(source_folder, destination_folder_path1)
    shutil.copytree(source_folder, destination_folder_path2)
    shutil.rmtree(source_folder)
    
    folder_path = f"C:\Bank API\Mr_Pikachu Bank API\Customer\{stored_addhar_entry}\pass"
    file_name = "password.txt"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(folder_path):
        with open(file_path, "w") as file:
            file.write("pass@123")
    # else:
    #     print(f"The folder '{folder_path}' does not exist. Please create it first.")


def decline():
    stored_addhar_entry = addhar_entry.get()
    source_folder = f"C:\Bank API\Mr_Pikachu Bank OFFICE\mail\{stored_addhar_entry}"
    shutil.rmtree(source_folder)


def email_content():
    global photo_label,name_label,adharno_label,gender_label,phoneno_label,DOB_label,ladd_label,padd_label,email_label
 
    inside_scroll_frame = customtkinter.CTkFrame(scroll_frame, width=650, height=110,border_color="white",border_width=2)
    inside_scroll_frame.pack()

    photo_label = ctk.CTkLabel(inside_scroll_frame,image=my_image3, text="")
    photo_label.place(x=10,y=10)

    name_label = ctk.CTkLabel(inside_scroll_frame, text="")
    name_label.place(x=80,y=5)

    adharno_label = ctk.CTkLabel(inside_scroll_frame, text="")
    adharno_label.place(x=80,y=35)

    gender_label = ctk.CTkLabel(inside_scroll_frame, text="")
    gender_label.place(x=80,y=65)

    phoneno_label = ctk.CTkLabel(inside_scroll_frame, text="")
    phoneno_label.place(x=270,y=35)

    DOB_label = ctk.CTkLabel(inside_scroll_frame, text="")
    DOB_label.place(x=270,y=65)

    ladd_label = ctk.CTkLabel(inside_scroll_frame, text="")
    ladd_label.place(x=450,y=5)

    padd_label = ctk.CTkLabel(inside_scroll_frame, text="")
    padd_label.place(x=450,y=35)

    email_label = ctk.CTkLabel(inside_scroll_frame, text="")
    email_label.place(x=450,y=65)


# # # # # # # # # # Get and displey data # # # # # # # # # #
def email_show_content():
    global file_path,stored_name, stored_mobile_no, stored_gender, stored_local_address, stored_per_address, stored_addhar, stored_DOBe, stored_email
    
    directory = "C:\Bank API\Mr_Pikachu Bank OFFICE\mail\\"
    if not os.path.exists(directory):
        print("The C: drive does not exist or is not accessible.")
        return

    for base, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(base, file)
                try:
                    if os.path.exists(file_path):
                        with open(file_path, "r") as file:
                            credentials = file.readlines()
                            for line in credentials:
                                stored_name, stored_mobile_no, stored_gender, stored_local_address, stored_per_address, stored_addhar, stored_DOBe, stored_email= line.strip().split(",")
                                name_label.configure(text=f"Name :  {stored_name}", text_color="white")
                                gender_label.configure(text=f"Gender : {stored_gender}", text_color="white")
                                ladd_label.configure(text=f"Local : {stored_local_address}", text_color="white")
                                padd_label.configure(text=f"Permanent Addr : {stored_per_address}", text_color="white")
                                phoneno_label.configure(text=f"Phone NO : {stored_mobile_no}", text_color="white")
                                adharno_label.configure(text=f"Addhar No : {stored_addhar}", text_color="white")
                                DOB_label.configure(text=f"Date of Birth : {stored_DOBe}", text_color="white")
                                email_label.configure(text=f"Email : {stored_email}", text_color="white")
                                email_content()
                            
                except Exception as e:
                    pass
                    # print(f"Error reading file {file_path}: {e}")


def show_detail_show_content():
    global file_path1,show_detail
    show_detail = addhar_entry1.get()
    show_balence_interface()
    
    file_path1 = f"C:\Bank API\Mr_Pikachu Bank API\Customer\{show_detail}\{show_detail}.txt"

    if os.path.exists(file_path1):
        with open(file_path1, "r") as file:
            credentials = file.readlines()
            for line in credentials:
                stored_name, stored_mobile_no, stored_gender, stored_local_address, stored_per_address, stored_addhar, stored_DOBe, stored_email= line.strip().split(",")
                name_label.configure(text=f"Name :  {stored_name}", text_color="white")
                gender_label.configure(text=f"Gender : {stored_gender}", text_color="white")
                ladd_label.configure(text=f"Local : {stored_local_address}", text_color="white")
                padd_label.configure(text=f"Permanent Addr : {stored_per_address}", text_color="white")
                phoneno_label.configure(text=f"Phone NO : {stored_mobile_no}", text_color="white")
                adharno_label.configure(text=f"Addhar No : {stored_addhar}", text_color="white")
                DOB_label.configure(text=f"Date of Birth : {stored_DOBe}", text_color="white")
                email_label.configure(text=f"Email : {stored_email}", text_color="white")
                show_page(page4)



def login():
    login_file = "C:/Bank API/Mr_Pikachu Bank OFFICE/password.txt"
    username = username_entry.get()
    password = password_entry.get()
    if os.path.exists(login_file):
        with open(login_file, "r") as file:
            credentials = file.readlines()
            for line in credentials:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    show_page(Desktop_API_page)
                    return
        result_label.configure(text="Invalid Credentials", text_color="red")
    else:
        result_label.configure(text="No credentials found. Please register first.", text_color="red")


def destop_page_layout(pageno):
    label = customtkinter.CTkLabel(pageno, text= time , font=("Cambria",15)).place(x=650,y=471)

    my_image = customtkinter.CTkImage(light_image=Image.open("destop_battry.jpg"),dark_image=Image.open("destop_battry.jpg"),size=(60, 23))
    image_label = customtkinter.CTkLabel(pageno, image=my_image, text="").place(x=585,y=471)

    label = customtkinter.CTkLabel(
        pageno, text="_________________________________________________________________________________________________________________________________________________________________________________", font=("Cambria",10) )
    label.place(x=0,y=440)
    
    my_image1 = customtkinter.CTkImage(light_image=Image.open("bank.jpg"),dark_image=Image.open("bank.jpg"),size=(21, 21))
    button = customtkinter.CTkButton(pageno,image=my_image1,text="",height=10,width=1, command=lambda: show_page(login_page))
    button.place(x=50,y=470)
    
    my_image2 = customtkinter.CTkImage(light_image=Image.open("window_.jpg"),dark_image=Image.open("window_.jpg"),size=(21, 21))
    button = customtkinter.CTkButton(pageno,image=my_image2,text="",height=10,width=1, command=lambda: show_page(login_page))
    button.place(x=10,y=470)

def app_page_layout(pageno,back):
    button = customtkinter.CTkButton(pageno,text="Back", font=("Arial", 18,"bold"),fg_color="white",text_color="black",height=50,width=35,corner_radius=50, command=lambda: show_page(back))
    button.place(x=600,y=5)

def show_page(page):
    """Switches to the specified page."""
    page.tkraise()


current_time = datetime.datetime.now()
date =  current_time.day,":",current_time.month,":",current_time.year 
time = current_time.hour,":",current_time.minute


# # # # # # # # # # Create the main application window # # # # # # # # # #
root = customtkinter.CTk()
root.title("Mobile Phone")
root.geometry("700x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# # # # # # # # # # Create a container for pages # # # # # # # # # #
container = customtkinter.CTkFrame(root)
container.grid(row=0, column=0, sticky="nsew")
container.rowconfigure(0, weight=1)
container.columnconfigure(0, weight=1)

# # # # # # # # # # Create pages # # # # # # # # # #
Desktop_page = customtkinter.CTkFrame(container)
login_page = customtkinter.CTkFrame(container)
Desktop_API_page = customtkinter.CTkFrame(container)
email_page = customtkinter.CTkFrame(container)
page4 = customtkinter.CTkFrame(container)
page5 = customtkinter.CTkFrame(container)
page6 = customtkinter.CTkFrame(container)
page7 = customtkinter.CTkFrame(container)

for frame in (Desktop_page, login_page, Desktop_API_page, email_page, page4, page5, page6, page7):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)


# # # # # # # # # #  Desktop_page  # # # # # # # # # # 
destop_page_layout(Desktop_page)

my_image3 = customtkinter.CTkImage(light_image=Image.open("bank.jpg"),dark_image=Image.open("bank.jpg"),size=(60, 80))
my_image1 = customtkinter.CTkImage(light_image=Image.open("bank.jpg"),dark_image=Image.open("bank.jpg"),size=(60, 60))

button = customtkinter.CTkButton(Desktop_page,image=my_image1,text="",height=70,width=20, command=lambda: show_page(login_page))
button.place(x=20,y=20)

home_label = customtkinter.CTkLabel(Desktop_page, text="Mr_Pikachu", font=("Arial", 13))
home_label.place(x=23,y=90)

home_label = customtkinter.CTkLabel(Desktop_page, text="Bank", font=("Arial", 13))
home_label.place(x=42,y=115)


# # # # # # # # # #  login_page  # # # # # # # # # # 
destop_page_layout(login_page)
app_page_layout(login_page,Desktop_page)

username_entry = ctk.CTkEntry(login_page, placeholder_text="Enter your username",width=200)
username_entry.place(x=250,y=80)

password_entry = ctk.CTkEntry(login_page, placeholder_text="Enter your password",width=200, show="*")
password_entry.place(x=250,y=120)

btn_to_login_page = customtkinter.CTkButton(login_page, text="Login",width=200, command=lambda:show_page(Desktop_API_page))
btn_to_login_page.place(x=250,y=160)

result_label = ctk.CTkLabel(login_page, text="")
result_label.place(x=250,y=200)



# # # # # # # # # #  Desktop_API_page  # # # # # # # # # # 
destop_page_layout(Desktop_API_page)
app_page_layout(Desktop_API_page,Desktop_page)

my_image2 = customtkinter.CTkImage(light_image=Image.open("mail_photo.png"),dark_image=Image.open("mail_photo.png"),size=(40, 40))
button = customtkinter.CTkButton(Desktop_API_page,image=my_image2,text="",height=50,fg_color="white",width=10,corner_radius=50, command=lambda: show_page(email_page))
button.place(x=500,y=5)

customer_show_content()

scroll_frame = customtkinter.CTkScrollableFrame(Desktop_API_page, width=660, height=320)
scroll_frame.place(x=10,y=65)

customer_content()

addhar_entry1 = ctk.CTkEntry(Desktop_API_page, placeholder_text="Enter Addhar No",width=260)
addhar_entry1.place(x=10,y=415)

Show_button = customtkinter.CTkButton(Desktop_API_page,text="Show Detail",fg_color="green",width=200,command=show_detail_show_content)
Show_button.place(x=280,y=415)

customer_show_content()



# # # # # # # # # #  email_page  # # # # # # # # # # 
destop_page_layout(email_page)
app_page_layout(email_page,Desktop_API_page)

email_show_content()

scroll_frame = customtkinter.CTkScrollableFrame(email_page, width=660, height=325)
scroll_frame.place(x=10,y=65)

email_content()

addhar_entry = ctk.CTkEntry(email_page, placeholder_text="Enter Addhar No",width=260)
addhar_entry.place(x=10,y=415)

Accept_button = customtkinter.CTkButton(email_page,text="Accept",fg_color="green",width=200,command=accept)
Accept_button.place(x=280,y=415)

decline_button = customtkinter.CTkButton(email_page,text="Decline",fg_color="red",width=200,command=decline)
decline_button.place(x=490,y=415)

email_show_content()


# # # # # # # # # # info detail of customer # # # # # # # # # #
destop_page_layout(page4)
app_page_layout(page4,Desktop_API_page)

scroll_frame = customtkinter.CTkScrollableFrame(page4, width=660, height=325)
scroll_frame.place(x=10,y=65)

inside_scroll_frame = customtkinter.CTkFrame(scroll_frame, width=650, height=110,border_color="white",border_width=2)
inside_scroll_frame.pack()

photo_label = ctk.CTkLabel(inside_scroll_frame,image=my_image1, text="")
photo_label.place(x=10,y=10)

name_label = ctk.CTkLabel(inside_scroll_frame, text="")
name_label.place(x=80,y=5)

adharno_label = ctk.CTkLabel(inside_scroll_frame, text="")
adharno_label.place(x=80,y=35)

gender_label = ctk.CTkLabel(inside_scroll_frame, text="")
gender_label.place(x=80,y=65)

phoneno_label = ctk.CTkLabel(inside_scroll_frame, text="")
phoneno_label.place(x=270,y=35)

DOB_label = ctk.CTkLabel(inside_scroll_frame, text="")
DOB_label.place(x=270,y=65)

ladd_label = ctk.CTkLabel(inside_scroll_frame, text="")
ladd_label.place(x=450,y=5)

padd_label = ctk.CTkLabel(inside_scroll_frame, text="")
padd_label.place(x=450,y=35)

email_label = ctk.CTkLabel(inside_scroll_frame, text="")
email_label.place(x=450,y=65)

balence_content()
show_balence_interface

balence_entry = ctk.CTkEntry(page4, placeholder_text="Enter Balence",width=260)
balence_entry.place(x=10,y=415)

add_button = customtkinter.CTkButton(page4,text="add",fg_color="green",width=200,command=add_balence)
add_button.place(x=280,y=415)

withdraw_button = customtkinter.CTkButton(page4,text="Withdraw",fg_color="green",width=200,command=withdraw_balence)
withdraw_button.place(x=490,y=415)


show_page(Desktop_page)
root.mainloop()
