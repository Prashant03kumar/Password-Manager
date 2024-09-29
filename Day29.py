from tkinter import * 
from tkinter import messagebox
import zipfile
import random
import pyperclip    #to copy text in clipboard
import json


FONT_NAME="Courier"


#GENERATE randm password
def generate_password():
    pass_input.delete(0,END)
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers=['0','2','3','4','5','6','7','8','9']
    symbols=['!','@','$','%','&','*','(',')','+' ]

    password_letter=[random.choice(letters) for _ in range (random.randint(8,10))]
    password_symbols=[random.choice(symbols) for _ in range (random.randint(2,4))]
    password_numbers=[random.choice(numbers) for _ in range (random.randint(2,4))]

    password_list=password_letter+password_numbers+password_symbols
    random.shuffle(password_list)

    password="".join(password_list)
    # for char in password_list:
    #     password+=char

    # print(f"Your password is:{password}")
    pass_input.insert(0,password)
    pyperclip.copy(password)
    # pass_input.delete(0,END)


# save the data........................................................................
def save():
    website=website_input.get().title()
    email=user_input.get()
    password=pass_input.get()
    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }
    # message box--------------
    if not website or not email or not password:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("Day29_data.json","r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("Day29_data.json","w") as data_file:
                #Saving updated data
                json.dump(new_data,data_file,indent=4) #->(data,to_file)
        else:
            # Updating old data wiith new data
            data.update(new_data)
            with open("Day29_data.json","w") as data_file:
                #Saving updated data
                json.dump(data,data_file,indent=4) #->(data,to_file)
        finally:
            website_input.delete(0,END)
            pass_input.delete(0,END)


def find_password():
    website=website_input.get().title()
    try:
        with open("Day29_data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found.")
    else:
        if website:
            if website in data:
                email=data[website]["email"]
                passwod=data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {passwod}")
            else:
                messagebox.showinfo(title="Oops",message=f"You haven't save details for {website}")

        else:
            messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")




# ----------------------------------------------------------------------------------------------------------
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200, height=200)
zip_file_path = r'C:\Users\pkrit\OneDrive\Desktop\100DaysOfCode\Resourses\password-manager-start.zip'
image_inside_zip = 'logo.png'
extracted_image_path = '100DaysOfCode/logo.png'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(image_inside_zip, '100DaysOfCode')

logo_image = PhotoImage(file=extracted_image_path)
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

#website label---------------------------------------------------------------
website_label=Label(text="Website:",font=(FONT_NAME,10))
website_label.grid(column=0,row=1)

website_input=Entry(width=25)
website_input.grid(column=1,row=1)
website_input.focus()

#search--------------------------------------------------------
search_buttom=Button(text="Search",width=14,command=find_password)
search_buttom.grid(column=2,row=1)

# Username----------------------------------------------------------------------------
user_label=Label(text="Email/Username:  ",font=(FONT_NAME,10))
user_label.grid(column=0,row=2)

user_input=Entry(width=45)
user_input.grid(column=1,row=2,columnspan=2)
user_input.insert(0,"abc@gmail.com")

# password--------------------------------------------------------------------------
pass_label=Label(text="Password:",font=(FONT_NAME,10))
pass_label.grid(column=0,row=3)

pass_input=Entry(width=26)
pass_input.grid(column=1,row=3)

generate_button=Button(text="Generate Password",width=14,command=generate_password)
generate_button.grid(column=2,row=3)

#add button-----------------------------------------------------------------

add=Button(text="Add",width=38,command=save)
add.grid(column=1,row=4,columnspan=2)



window.mainloop()