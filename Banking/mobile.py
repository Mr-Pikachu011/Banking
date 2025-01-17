from tkinter import *
import os
import random
from tkinter import messagebox
import customtkinter
import datetime
from PIL import Image
import customtkinter as ctk
from datetime import date


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

create_folder("C:/Bank API/Mr_Pikachu Bank OFFICE/Customer/Account" )
create_folder("C:/Bank API/Mr_Pikachu Bank API/Customer" )




 
otp_file = "C:/Bank API/otp.txt"
def generate_otp():
    otp = str(random.randint(100000, 999999))  # Generate a 6-digit OTP
    with open(otp_file, "w") as file:
        file.write(otp) 
        messagebox.showinfo("OTP Info",f"Access OTP In {otp_file}")
        result_label.configure(text="OTP has been generated and stored.", text_color="green")

def verify_otp():
    entered_otp = otp_entry.get()
    try:
        with open(otp_file, "r") as file:
            stored_otp = file.read()  # Read the OTP from the file
            if entered_otp == stored_otp:
                result_label.configure(text="OTP Verified Successfully!", text_color="green")
                show_page(change_pass_page)
            else:
                result_label.configure(text="Invalid OTP. Try again.", text_color="red")
    except FileNotFoundError:
        result_label.configure(text="No OTP found. Generate one first.", text_color="red")



def submit_application():
    global addhar
    name = entry_name.get()
    mobile_no = entry_mobile_no.get()
    gender = gender_var.get()
    local_address = entry_local_Addres.get()
    per_address = entry_per_Addres.get()
    addhar = entry_addhar_no.get()
    DOBe = entry_DOB.get()
    email = entry_email.get()
    create_folder(f"C:/Bank API/Mr_Pikachu Bank OFFICE/mail/{addhar}")
    create_folder(f"C:/Bank API/Mr_Pikachu Bank OFFICE/mail/{addhar}/Account")
    create_folder(f"C:/Bank API/Mr_Pikachu Bank OFFICE/mail/{addhar}/pass")
    aplication_file = f"C:/Bank API/Mr_Pikachu Bank OFFICE/mail/{addhar}/{addhar}.txt"
    balence = f"C:/Bank API/Mr_Pikachu Bank OFFICE/mail/{addhar}/Account/balence.txt"
    
    if name and mobile_no and gender and local_address and per_address and addhar and DOBe and email:
        with open(aplication_file, "a") as file:
            file.write(f"{name},{mobile_no},{gender},{local_address},{per_address},{addhar},{DOBe},{email}\n")
            messagebox.showinfo("Info", "Aplication Successful!")
            
            show_page(mobile_login_page)
    else:
        messagebox.showinfo("Info", "Aplication Error")
        
    
    with open(balence, "a") as file:
        file.write(f"Account,Date,ADD,Withdraw,Balence\n")
        file.write(f"{addhar},Date,0,0,0\n")
    TE = entry_name.delete(0, END)
    TE = entry_addhar_no.delete(0, END)
    TE = entry_DOB.delete(0, END)
    TE = entry_email.delete(0, END)
    TE = entry_mobile_no.delete(0, END)
    TE = entry_local_Addres.delete(0, END)
    TE = entry_per_Addres.delete(0, END)
    

# # # # # # # # # # password create block # # # # # # # # # #
def password_show_content():
    global pass1
    directory = f"C:\Bank API\Mr_Pikachu Bank API\Customer/{stored_addhar_entry1}/pass"
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
                            pass1 = file.read()
                      
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")



def find_addhar_no():
    global item,stored_addhar_entry
    stored_addhar_entry = addhar_entry.get()
    folder_path = "C:\Bank API\Mr_Pikachu Bank API\Customer"
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # List all folders in the folder
    try:
        folder_list = os.listdir(folder_path)
        print("Folders in the selected folder:")
        for item in folder_list:
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                print(item)
                if item == f"{stored_addhar_entry}":
                    print("hello")
                    show_page(verify_OTP_page)
                    
    except Exception as e:
        print(f"Error while listing folders: {e}")
        
        
        

def login_with_file():
    global item,stored_addhar_entry1
    stored_addhar_entry1 = username_entry.get()
    password = password_entry.get()
    folder_path = "C:\Bank API\Mr_Pikachu Bank API\Customer"
    password_show_content()
    # List all folders in the folder
    try:
        folder_list = os.listdir(folder_path)
        for item in folder_list:
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                if item == f"{stored_addhar_entry1}":
                    if pass1 == password:
                        show_page(app_main_page)

    except Exception as e:
        print(f"Error while listing folders: {e}")
    TE = username_entry.delete(0, END)
    TE = password_entry.delete(0, END)
    
def show_detail_show_content():
    global file_path1,show_detail
    
    file_path1 = f"C:\Bank API\Mr_Pikachu Bank API\Customer\{stored_addhar_entry1}\{stored_addhar_entry1}.txt"

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
                show_page(page7)


def send_balence():
    # send money 
    send_money = send_money_entry.get()
    addhar_to = addhar_to_entry.get()
    
    
    aplication_file = f"C:/Bank API/Mr_Pikachu Bank API/Customer/{addhar_to}/Account/balence.txt"
    if os.path.exists(aplication_file):
        with open(aplication_file, "r") as file:
                credentials = file.readlines()
                for line in credentials:
                    global balence,withdraw,add
                    account_name, date, add, withdraw, balence = line.strip().split(",")
    else:
        messagebox.showinfo("Info", "Can Not Find Account")
        
                    
    balence1 = int(balence)+int(send_money)
    withdraw = 0
    with open(aplication_file, "a") as file:
            file.write(f"{account_name},{date},{send_money},{withdraw},{balence1}\n")
            # messagebox.showinfo("Info", "Send Money Successful")


    # withdraw money
    aplication_file = f"C:/Bank API/Mr_Pikachu Bank API/Customer/{stored_addhar_entry1}/Account/balence.txt"
    if os.path.exists(aplication_file):
        with open(aplication_file, "r") as file:
                credentials = file.readlines()
                for line in credentials:
                    account_name, date, add, withdraw, balence = line.strip().split(",")
    
    balence1 = int(balence)-int(send_money)
    add = 0
    with open(aplication_file, "a") as file:
            file.write(f"{account_name},{date},{add},{send_money},{balence1}\n")
            messagebox.showinfo("Info", "Send Money Successful")


def check_balence():
    aplication_file = f"C:/Bank API/Mr_Pikachu Bank API/Customer/{stored_addhar_entry1}/Account/balence.txt"
    if os.path.exists(aplication_file):
        with open(aplication_file, 'r') as file:
            lines = file.readlines()
            if lines:
                last = lines[-1].strip()
                account_name, date, add, withdraw, balence = last.strip().split(",")
                # print(account_name, date, add, withdraw, balence)
                balence_label.configure(text=f"Balence :  {balence}", text_color="white")
                show_page(page9)



def change_pass():
    file_path=f"C:\Bank API\Mr_Pikachu Bank API\Customer\{stored_addhar_entry}\pass\password.txt"
    old_pass = old_pass_entry.get()
    new_pass = new_pass_entry.get()
    with open(file_path, "r") as file:
        credentials = file.read()
        if credentials == old_pass:
            updated_content = credentials.replace(f"{old_pass}", f"{new_pass}")
            with open(file_path, 'w') as file:
                file.write(updated_content)      
                show_page(mobile_login_page)
        else:
            messagebox.showerror("Error","Password Can Not Change")
        

def mobile_API_page_layout(pageno,backpageno):
    label = customtkinter.CTkLabel(pageno, text= date , font=("Cambria",15) ,bg_color="black").place(x=10,y=5)

    label = customtkinter.CTkLabel(pageno, text= time , font=("Cambria",15) ,bg_color="black").place(x=130,y=5)

    my_image = customtkinter.CTkImage(light_image=Image.open("battry.jpg"),dark_image=Image.open("battry.jpg"),size=(60, 23))
    image_label = customtkinter.CTkLabel(pageno, image=my_image, text="").place(x=230,y=5)

    label = customtkinter.CTkLabel(
        pageno, text="____________________________________________________________________________", font=("Cambria",10) )
    label.place(x=0,y=30)

    btn_to_mobile_API_page = customtkinter.CTkButton(pageno, text="Home", command=lambda: show_page(mobile_API_page)).place(x=10,y=465)
    btn_to_back_page = customtkinter.CTkButton(pageno, text="Back", command=lambda: show_page(backpageno)).place(x=155,y=465)


def show_page(page):
    """Switches to the specified page."""
    page.tkraise()
    

current_time = datetime.datetime.now()
date = date.today()
# date =  current_time.day,":",current_time.month,":",current_time.year 
time = current_time.hour,":",current_time.minute


# Create the main application window
root = customtkinter.CTk()
root.title("Mobile Phone")
root.geometry("300x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

gender_var = ctk.StringVar(value="")  # Default to no selection

# Create a container for pages
container = customtkinter.CTkFrame(root)
container.grid(row=0, column=0, sticky="nsew")
container.rowconfigure(0, weight=1)
container.columnconfigure(0, weight=1)

# Create pages
mobile_API_page = customtkinter.CTkFrame(container)
mobile_login_page = customtkinter.CTkFrame(container)
create_account_page = customtkinter.CTkFrame(container)
forgate_page = customtkinter.CTkFrame(container)
verify_OTP_page = customtkinter.CTkFrame(container)
change_pass_page = customtkinter.CTkFrame(container)
app_main_page = customtkinter.CTkFrame(container)
page7 = customtkinter.CTkFrame(container)
page8 = customtkinter.CTkFrame(container)
page9 = customtkinter.CTkFrame(container)
page10 = customtkinter.CTkFrame(container)
# page7 = customtkinter.CTkFrame(container)

for frame in (mobile_API_page, mobile_login_page, create_account_page, forgate_page, verify_OTP_page, change_pass_page, app_main_page, page7, page8, page9, page10):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)


# # # # # # # # # # Home Page Content # # # # # # # # # #
mobile_API_page_layout(mobile_API_page,mobile_API_page)

my_image1 = customtkinter.CTkImage(light_image=Image.open("bank.jpg"),dark_image=Image.open("bank.jpg"),size=(80, 80))
button = customtkinter.CTkButton(mobile_API_page,image=my_image1,text="",height=70,width=20, command=lambda: show_page(mobile_login_page))
button.place(x=100,y=100)

home_label = customtkinter.CTkLabel(mobile_API_page, text="Mr_Pikachu", font=("Arial", 18))
home_label.place(x=100,y=200)

home_label = customtkinter.CTkLabel(mobile_API_page, text="Bank", font=("Arial", 18))
home_label.place(x=125,y=230)


# # # # # # # # # # login page # # # # # # # # # #
mobile_API_page_layout(mobile_login_page,mobile_API_page)

username_entry = ctk.CTkEntry(mobile_login_page, placeholder_text="Enter your username",width=200)
username_entry.place(x=50,y=80)

password_entry = ctk.CTkEntry(mobile_login_page, placeholder_text="Enter your password",width=200, show="*")
password_entry.place(x=50,y=120)

btn_to_mobile_login_page = customtkinter.CTkButton(mobile_login_page, text="Create Account ?",height=1,width=60,fg_color="grey", command=lambda: show_page(create_account_page))
btn_to_mobile_login_page.place(x=50,y=160)

btn_to_mobile_login_page = customtkinter.CTkButton(mobile_login_page, text="Forgote",height=1,width=90,fg_color="grey", command=lambda: show_page(forgate_page))
btn_to_mobile_login_page.place(x=160,y=160)

btn_to_mobile_login_page = customtkinter.CTkButton(mobile_login_page, text="Login",width=200, command= login_with_file)
btn_to_mobile_login_page.place(x=50,y=200)

result_label = ctk.CTkLabel(mobile_login_page, text="")
result_label.place(x=50,y=240)


# # # # # # # # # # create account # # # # # # # # # #
mobile_API_page_layout(create_account_page,mobile_login_page)

scroll_frame = customtkinter.CTkScrollableFrame(create_account_page, width=260, height=380)
scroll_frame.place(x=10,y=60)

label_title = customtkinter.CTkLabel(scroll_frame, text="Mr_Pikachu Bank", font=("Arial", 18, "bold"))
label_title.pack(pady=(10, 20))

label_name = customtkinter.CTkLabel(scroll_frame, text="Full Name:")
label_name.pack(anchor="w", padx=10)
entry_name = customtkinter.CTkEntry(scroll_frame, placeholder_text="Enter your Full Name")
entry_name.pack(fill="x", padx=10, pady=(0, 10))

label_gender = customtkinter.CTkLabel(scroll_frame, text="Gender:")
label_gender.pack(anchor="w", padx=10)

radio_male = customtkinter.CTkRadioButton(scroll_frame,text="Male",variable=gender_var,value="Male",)
radio_male.pack(fill="x", padx=10, pady=(0, 10))
radio_female = customtkinter.CTkRadioButton(scroll_frame,text="Female",variable=gender_var,value="Female",)
radio_female.pack(fill="x", padx=10, pady=(0, 10))

label_mobile_no = customtkinter.CTkLabel(scroll_frame, text="Mobile number:")
label_mobile_no.pack(anchor="w", padx=10)
entry_mobile_no = customtkinter.CTkEntry(scroll_frame, placeholder_text="Enter your Mobile number")
entry_mobile_no.pack(fill="x", padx=10, pady=(0, 10))

label_local_Addres = customtkinter.CTkLabel(scroll_frame, text="local Address:")
label_local_Addres.pack(anchor="w", padx=10)
entry_local_Addres = customtkinter.CTkEntry(scroll_frame, placeholder_text="Enter your local Address")
entry_local_Addres.pack(fill="x", padx=10, pady=(0, 10))

label_per_Addres = customtkinter.CTkLabel(scroll_frame, text="Permanent Address:")
label_per_Addres.pack(anchor="w", padx=10)
entry_per_Addres = customtkinter.CTkEntry(scroll_frame, placeholder_text="Enter your Permanent Address")
entry_per_Addres.pack(fill="x", padx=10, pady=(0, 10))

label_addhar_no = customtkinter.CTkLabel(scroll_frame, text="Addhar no:")
label_addhar_no.pack(anchor="w", padx=10)
entry_addhar_no = customtkinter.CTkEntry(scroll_frame, placeholder_text="Enter your Addhar no")
entry_addhar_no.pack(fill="x", padx=10, pady=(0, 10))

label_DOB = customtkinter.CTkLabel(scroll_frame, text="Date of Birth:")
label_DOB.pack(anchor="w", padx=10)
entry_DOB = customtkinter.CTkEntry(scroll_frame, placeholder_text="Enter your Date of Birth")
entry_DOB.pack(fill="x", padx=10, pady=(0, 10))

label_email = customtkinter.CTkLabel(scroll_frame, text="Email Address:")
label_email.pack(anchor="w", padx=10)
entry_email = customtkinter.CTkEntry(scroll_frame, placeholder_text="Enter your Email Address")
entry_email.pack(fill="x", padx=10, pady=(0, 10))

label_name = customtkinter.CTkLabel(scroll_frame, text="")
label_name.pack(anchor="w", padx=10)

button_upload = customtkinter.CTkButton(scroll_frame, text="Submit Aplication",command=submit_application)
button_upload.pack(fill="x", padx=10, pady=(0, 10))

result_label = customtkinter.CTkLabel(scroll_frame, text="")
result_label.pack(pady=10)


# # # # # # # # # # forgote password # # # # # # # # # #
mobile_API_page_layout(forgate_page,mobile_login_page)

addhar_entry = customtkinter.CTkEntry(forgate_page, placeholder_text="Addhar no",width=200)
addhar_entry.place(x=50,y=80)

btn_to_mobile_login_page = customtkinter.CTkButton(forgate_page, text="Forgote",width=200, command=find_addhar_no)
btn_to_mobile_login_page.place(x=50,y=120)


# # # # # # # # # # generate and verify OTP # # # # # # # # # #
mobile_API_page_layout(verify_OTP_page,forgate_page)

otp_entry = ctk.CTkEntry(verify_OTP_page, placeholder_text="Enter OTP",width=200)
otp_entry.place(x=50,y=80)

verify_button = ctk.CTkButton(verify_OTP_page, text="Verify OTP",width=200, command=verify_otp)
verify_button.place(x=50,y=120)

generate_button = ctk.CTkButton(verify_OTP_page, text="Generate OTP",width=200, command=generate_otp)
generate_button.place(x=50,y=160)

result_label = ctk.CTkLabel(verify_OTP_page, text="")
result_label.place(x=50,y=200)

# # # # # # # # # # change password # # # # # # # # # #
mobile_API_page_layout(change_pass_page,verify_OTP_page)

old_pass_entry = customtkinter.CTkEntry(change_pass_page, placeholder_text="Old Password",width=200)
old_pass_entry.place(x=50,y=80)
new_pass_entry = customtkinter.CTkEntry(change_pass_page, placeholder_text="New Password",width=200)
new_pass_entry.place(x=50,y=120)

btn_to_mobile_login_page = customtkinter.CTkButton(change_pass_page, text="Submit",width=200, command=change_pass)
btn_to_mobile_login_page.place(x=50,y=160)


# # # # # # # # # # App main frame # # # # # # # # # #
mobile_API_page_layout(app_main_page,mobile_login_page)

login_page = customtkinter.CTkButton(app_main_page, text="Show Profile",width=200,command=show_detail_show_content)
login_page.place(x=50,y=80)
login_page = customtkinter.CTkButton(app_main_page, text="Send Money to Bank",width=200, command=lambda: show_page(page8))
login_page.place(x=50,y=120)
login_page = customtkinter.CTkButton(app_main_page, text="Check Balence",width=200,command=check_balence)
login_page.place(x=50,y=160)


# # # # # # # # # # page7 # # # # # # # # # #
mobile_API_page_layout(page7,app_main_page)

inside_scroll_frame = customtkinter.CTkFrame(page7, width=280, height=390,border_color="white",border_width=2)
inside_scroll_frame.place(x=10,y=60)

photo_label = ctk.CTkLabel(inside_scroll_frame,image=my_image1, text="")
photo_label.place(x=10,y=10)

name_label = ctk.CTkLabel(inside_scroll_frame, text="")
name_label.place(x=10,y=100)

adharno_label = ctk.CTkLabel(inside_scroll_frame, text="")
adharno_label.place(x=10,y=135)

gender_label = ctk.CTkLabel(inside_scroll_frame, text="")
gender_label.place(x=10,y=165)

phoneno_label = ctk.CTkLabel(inside_scroll_frame, text="")
phoneno_label.place(x=10,y=195)

DOB_label = ctk.CTkLabel(inside_scroll_frame, text="")
DOB_label.place(x=10,y=225)

ladd_label = ctk.CTkLabel(inside_scroll_frame, text="")
ladd_label.place(x=10,y=255)

padd_label = ctk.CTkLabel(inside_scroll_frame, text="")
padd_label.place(x=10,y=285)

email_label = ctk.CTkLabel(inside_scroll_frame, text="")
email_label.place(x=10,y=315)


# # # # # # # # # # page8 # # # # # # # # # #
mobile_API_page_layout(page8,app_main_page)

addhar_to_entry = ctk.CTkEntry(page8, placeholder_text="Addhar No to Send",width=200)
addhar_to_entry.place(x=50,y=80)

send_money_entry = ctk.CTkEntry(page8, placeholder_text="Enter Money To send",width=200)
send_money_entry.place(x=50,y=120)

send_button = ctk.CTkButton(page8, text="Send",width=200,command=send_balence)
send_button.place(x=50,y=160)


# # # # # # # # # # page9 # # # # # # # # # #
mobile_API_page_layout(page9,app_main_page)

balence_label = ctk.CTkLabel(page9, text="",font=("Arrial",20,"bold"))
balence_label.place(x=20,y=80)

show_page(mobile_API_page)
root.mainloop()