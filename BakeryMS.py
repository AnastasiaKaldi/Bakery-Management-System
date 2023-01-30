import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import date
import csv


app = customtkinter.CTk()
app.title('Bakery')
app.geometry("1500x600")
app.config(bg = "#DF541F")
app.resizable(True, True)

font1 = ('Courier New', 25, 'bold')
font2 = ('Courier New', 15, 'bold')
font3 = ('Courier New', 12,'bold')


price_list = [1, 5, 1, 3, 2, 3, 2, 1]

TotalPrice = 0

bill_frame = customtkinter.CTkFrame(app, width = 350, height = 600, fg_color = "#B65733")
bill_frame.place(x=1190, y=0)

menu_label = customtkinter.CTkLabel(app, text = "The Bakery", text_color = "#FFFFFF", font = font1, fg_color = "#DF541F", bg_color = "#DF541F")
menu_label.place(x= 230, y=5)

img1 = PhotoImage(file = "baguette.png")
img2 = PhotoImage(file = "BirthdayCake.png")
img3 = PhotoImage(file = "bread.png")
img4 = PhotoImage(file = "buiscuits.png")
img5 = PhotoImage(file = "cupcake.png")
img6 = PhotoImage(file = "naan.png")
img7 = PhotoImage(file = "pretzel.png")
img8 = PhotoImage(file = "samosa.png")

def pay():
    global total_price
    if(customer_entry.get() == ''):
        messagebox.showerror(title= "Error", message = "Please enter your name")
    else:
        total_price = int(quantity1_combobox.get())*price_list[0] + int(quantity2_combobox.get())*price_list[1] + int(quantity3_combobox.get())*price_list[2] + int(quantity4_combobox.get())*price_list[3] + int(quantity5_combobox.get())*price_list[4]  + int(quantity6_combobox.get())*price_list[5] + int(quantity7_combobox.get())*price_list[6] + int(quantity8_combobox.get())*price_list[7]
        if(total_price ==0):
            messagebox.showerror(title= "Error", message = "Please select some items")
        else:
            name_label = customtkinter.CTkLabel(bill_frame, text =f'Customer Name: {customer_entry.get()}', font = font3, bg_color = "#B65733", width = 320, anchor = N)
            name_label.place(x =100, y=100)
            tprice_label = customtkinter.CTkLabel(bill_frame, text =f'Total Price: {total_price} £', font = font3, bg_color = "#B65733", width = 320, anchor = N)
            tprice_label.place(x=100, y=150)
            date_label = customtkinter.CTkLabel(bill_frame, text =f'Bill Date: {date.today()}', font = font3, bg_color = "#B65733", width = 320, anchor = N)
            date_label.place(x =100, y= 200)


def new():
    costumer_entry.delete(0, END)
    quantity1_combobox.set(0)
    quantity2_combobox.set(0)
    quantity3_combobox.set(0)
    quantity4_combobox.set(0)
    quantity5_combobox.set(0)
    quantity6_combobox.set(0)
    quantity7_combobox.set(0)
    quantity8_combobox.set(0)

def save():
    with open('Bill.csv', 'w', newline ='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['customer name','total price','date'])
        writer.writerow([customer_entry.get(),total_price,date.today()])
        
        





img1_label = customtkinter.CTkLabel(app, image = img1, text = "Baguette\n Price: 1£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img1_label.place(x= 30, y=70)

img2_label = customtkinter.CTkLabel(app, image = img2, text = "Birthday Cake\n Price: 5£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img2_label.place(x= 250, y=70)

img3_label = customtkinter.CTkLabel(app, image = img3, text = "Bread\n Price: 1£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img3_label.place(x= 470, y=70)

img4_label = customtkinter.CTkLabel(app, image = img4, text = "Biscuits\n Price: 3£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img4_label.place(x= 690, y=70)

img5_label = customtkinter.CTkLabel(app, image = img5, text = "Cupcake\n Price: 2£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img5_label.place(x= 30, y=300)

img6_label = customtkinter.CTkLabel(app, image = img6, text = "Naan\n Price: 3£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img6_label.place(x= 250, y=300)

img7_label = customtkinter.CTkLabel(app, image = img7, text = "Pretzel\n Price: 2£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img7_label.place(x= 470, y=300)

img8_label = customtkinter.CTkLabel(app, image = img8, text = "Samosa\n Price: 1£", font = font2, 
text_color = "#FFFFFF", fg_color = "#DF541F", width = 100, height = 100, corner_radius = 20, compound = TOP, anchor = N)
img8_label.place(x= 690, y= 300)

quantity1_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity1_combobox.place(x=25 , y= 175)
quantity1_combobox.set(0)

quantity2_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity2_combobox.place(x=258 , y= 175)
quantity2_combobox.set(0)

quantity3_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity3_combobox.place(x=465 , y= 175)
quantity3_combobox.set(0)

quantity4_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity4_combobox.place(x=685, y= 175)
quantity4_combobox.set(0)

quantity5_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity5_combobox.place(x=25 , y= 407)
quantity5_combobox.set(0)

quantity6_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity6_combobox.place(x=245 , y= 407)
quantity6_combobox.set(0)

quantity7_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity7_combobox.place(x=465 , y= 407)
quantity7_combobox.set(0)

quantity8_combobox = customtkinter.CTkComboBox(app, font = font3, text_color = "#000000", fg_color = "#FFFFFF", values = ('0', '1', '2', '3', '4', '5'), state = "readonly")
quantity8_combobox.place(x=685 , y= 407)
quantity8_combobox.set(0)

customer_label = customtkinter.CTkLabel(app, text = "Customer Name:", text_color = "#FFFFFF", font = font2, bg_color = "#DF541F")
customer_label.place(x=870, y=100)

customer_entry = customtkinter.CTkEntry(app, font = font2, bg_color = "#FFFFFF")
customer_entry.place(x= 1000, y=100)


pay_button = customtkinter.CTkButton(app, text = "Pay the bill",command = pay ,font = font2, fg_color = "#57411C", hover_color = "#57411C", corner_radius = 20, cursor = "hand2")
pay_button.place(x= 900, y= 160)

save_button = customtkinter.CTkButton(app,command = save,text = "Save the bill", font = font2, fg_color = "#61790B", hover_color = "#61790B", corner_radius = 20, cursor = "hand2")
save_button.place(x= 900, y= 210)

new_button = customtkinter.CTkButton(app,command = new,text = "Create a new bill", font = font2, fg_color = "#A9941F", hover_color = "#A9941F", corner_radius = 20, cursor = "hand2")
new_button.place(x= 900, y= 250)



app.mainloop()


