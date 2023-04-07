import tkinter as tk
from tkinter import *
import pymysql


win = tk.Tk()
win.geometry("500x600")
win.title("Data Entry")

db_con = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "vasanth",
    database = "python_db_03032023"
)

my_db = db_con.cursor()
print("Connection made")


def refresh():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    ep1.delete(0,END)
    ep2.delete(0,END)
    ep3.delete(0,END)
    ep4.delete(0,END)
    ep5.delete(0,END)


def save():
    def add_products(list_products,list_price):
        print(list_products,list_price)
        # count = 0
        for p in range(0,len(list_products)):
            print("product = ",list_products[p],"price = ",list_price[p])
            # print()
        # count=count+1
            query_add_prod = "insert into dataentry(products,price) values(%s,%s)"
            values = (list_products[p],list_price[p])
            my_db.execute(query_add_prod,values)
            output = db_con.commit()
            print("executed successfully")
        spaces.destroy()
        succes_l = Label(frame1, text="Products added successfully!",bg='#90EE90',fg='green')
        succes_l.place(x=140, y=300)





    epd1 = e1.get()
    epd2 = e2.get()
    epd3 = e3.get()
    epd4 = e4.get()
    epd5 = e5.get()
    epr1 = ep1.get()
    epr2 = ep2.get()
    epr3 = ep3.get()
    epr4 = ep4.get()
    epr5 = ep5.get()
    # print(epd1,epd2,epd3,epd4,epd5)
    # print(epr1,epr2,epr3,epr4,epr5)
    list_products = [epd1,epd2,epd3,epd4,epd5]
    list_price = [epr1, epr2, epr3, epr4, epr5]

    if '' in list_products or '' in list_price:
        print("empty space not allowed")
        spaces = Label(frame1, text="No empty spaces are allowed", bg='#90EE90', fg='red')
        spaces.place(x=140, y=300)
    else:
        # print(list_products)
        # print(list_price)

        add_products(list_products,list_price)








def add_customer():
    def ref():
        name_en.delete(0,END)
        phone_en.delete(0,END)
        adrs_en.delete(0,END)
        details_added.destroy()
        empty_details.destroy()


    def save_cust():
        def add_cust(list_customer):
            # for c in list_customer:
            #     print(c)
            name_1 = list_customer[0]
            phone_1 = list_customer[1]
            adrs_1 = list_customer[2]
            print("name :",name_1,"phone :",phone_1,"adrs :",adrs_1)
            query_add_cutomer = "insert into customer (customer_name, phone, address) values(%s,%s,%s)"
            values = (name_1,phone_1,adrs_1)
            my_db.execute(query_add_cutomer,values)
            out= db_con.commit()
            print("query executed")
            details_added.place(x=170, y=300)



        name = name_en.get()
        phone = phone_en.get()
        adrs = adrs_en.get()
        list_customer = [name,phone,adrs]
        if '' in list_customer:

            empty_details.place(x=140, y=300)
        else:
            add_cust(list_customer)
        pass
    win1 = tk.Tk()
    win1.geometry("500x600")
    win1.title("Add Customer")
    frame2 = Frame(win1, bg="#90EE90", highlightthickness=3, highlightbackground="black")
    frame2.pack(padx=10, pady=10, ipadx=50, ipady=50, expand=True, fill='both')
    header_cust_l = Label(frame2, text="ADD CUSTOMER DETAILS", font='Helvetica 24 bold', bg="#90EE90")
    header_cust_l.pack()

    name_l1 = Label(frame2,text = "Name",font = 'Helvetica 16 bold',bg = "#90EE90")
    name_l1.place(x = 20, y = 100)

    name_en1 = StringVar()
    name_en = Entry(frame2,width=25,textvariable=name_en1)
    name_en.place(x = 180, y = 105)

    phone_l1 = Label(frame2, text = "Contact",font = 'Helvetica 16 bold',bg = "#90EE90")
    phone_l1.place(x = 20, y = 150)

    phone_en1 = StringVar()
    phone_en = Entry(frame2,width=25,textvariable=phone_en1)
    phone_en.place(x = 180, y = 155)

    adrs_l = Label(frame2,text = "Address",font = 'Helvetica 16 bold',bg = "#90EE90")
    adrs_l.place(x = 20, y = 200)

    adrs_en1 = StringVar()
    adrs_en = Entry(frame2,width=45,textvariable=adrs_en1)
    adrs_en.place(x = 180,y = 205)

    save_customer_btn = Button(frame2,text = "SAVE",fg = "white", bg = 'green',font='Helvetica 10 bold', width=10,command=save_cust)
    save_customer_btn.place(x = 170, y = 350)

    ref_btn = Button(frame2,text = "REFRESH", bg = 'green',font='Helvetica 10 bold',fg = "white", width=10,command=ref)
    ref_btn.place(x = 170, y = 400)


    # -----------message throw
    empty_details = Label(frame2, text="No empty spaces are allowed !", bg='#90EE90', fg='red')
    details_added = Label(frame2, text="Details Added !", bg='#90EE90', fg='green')





frame1 = Frame(win, bg = "#90EE90",highlightthickness=3,highlightbackground="black")
frame1.pack(padx=10,pady=10,ipadx=50,ipady=50,expand=True,fill = 'both')



# ---------Label-------
header_l = Label(frame1,text = "DATA ENTRY",font = 'Helvetica 24 bold',bg = "#90EE90")
header_l.pack()

# products----
l1 = Label(frame1,text = "PRODUCTS",font = 'Helvetica 18 bold',bg = "#90EE90")
l1.place(x = 55, y = 100)

l2 = Label(frame1,text = "PRICE",font = 'Helvetica 18 bold',bg = "#90EE90")
l2.place(x = 250, y = 100)

# ENTRIES---------
# products-----
en1 = StringVar()
e1 = Entry(frame1,width=20,textvariable=en1)
e1.place(x = 60, y = 140)

en2 = StringVar()
e2 = Entry(frame1,width=20,textvariable=en2)
e2.place(x = 60, y = 170)

en3 = StringVar()
e3 = Entry(frame1,width=20,textvariable=en3)
e3.place(x = 60, y = 200)

en4 = StringVar()
e4 = Entry(frame1,width=20,textvariable=en4)
e4.place(x = 60, y = 230)

en5 = StringVar()
e5= Entry(frame1,width=20,textvariable=en5)
e5.place(x = 60, y = 260)

# price----
enp1 = StringVar()
ep1 = Entry(frame1,width=10,textvariable=enp1)
ep1.place(x = 250, y = 140)

enp2 = StringVar()
ep2 = Entry(frame1,width=10,textvariable=enp2)
ep2.place(x = 250, y = 170)

enp3 = StringVar()
ep3 = Entry(frame1,width=10,textvariable=enp3)
ep3.place(x = 250, y = 200)

enp4 = StringVar()
ep4 = Entry(frame1,width=10,textvariable=enp4)
ep4.place(x = 250, y = 230)

enp5 = StringVar()
ep5= Entry(frame1,width=10,textvariable=enp5)
ep5.place(x = 250, y = 260)



# Button------
save = Button(frame1,text = "SAVE",fg = "white", bg = 'green',font='Helvetica 10 bold', width=10,command=save)
save.place(x = 170, y = 350)

refresh = Button(frame1,text = "REFRESH", bg = 'green',font='Helvetica 10 bold',fg = "white", width=10,command=refresh)
refresh.place(x = 170, y = 400)

cust_det = Button(frame1,text = "Add Customer", bg = 'green',font='Helvetica 10 bold',fg = "white", width=15,command=add_customer)
cust_det.place(x = 150, y= 450)

win.mainloop()

#------
