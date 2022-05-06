from cProfile import label
from cgitb import text
from ctypes import resize
from fileinput import filename
from http.client import FOUND
from multiprocessing.sharedctypes import Value
from time import strftime
from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image, ImageTk
import random,os
from tkinter import messagebox
import tempfile

from click import command
from time import strftime




class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1700x800+0+0")
        self.root.title("Grocery Billing software")

        # **========= Variables==========**

        self.Customername=StringVar()
        self.Customermobileno=StringVar()
        self.Billno=StringVar()
        z=random.randint(100,99999999)
        self.Billno.set(z)
        self.Customeremail=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.Prices=IntVar()
        self.qty=IntVar()
        self.Sub_total=StringVar()
        self.tax_input=StringVar()
        self.TotalAmount=StringVar()

        # Product Categories list

        self.Category=["Select Option","Vegetable","Milk and Dairy","Food Grains"]
        
        
        #Product subcategory list if Vegetables
        self.SubCatVegetables=["Onion","Potato","Carrot","Tomato","Cauliflower","Palak","Ginger"]
        # Onion
        self.onions=["onion"]
        self.price_onions=115
       
        # Potato
        self.Potato=["New","Old"]
        self.price_Newpotato=30
        self.price_Oldpotato=40
        #carrot
        self.Carrot=["Carrot"]
        self.price_Carrot=10
        #Tomato
        self.Tomato=["Tomato"]
        self.price_Tomato=30
        #Cauliflower
        self.Cauliflower=["Cauliflower"]
        self.price_Cauliflower=65
        #palak
        self.Palak=["Palak"]
        self.price_Palak=20
        #Ginger
        self.Giger=["Ginger"]
        self.price_Ginger=78

        #product Subcategory list of Milk and Dairy
        self.SubCatMilkandDairy=["Milk","Curd","Butter","Paneer"]

        self.Milk=["Amul","Dinshaw","Haldiram"]
        self.price_AmulMilk=99
        self.price_DinshawMilk=98
        self.price_HaldiramMilk=101

        self.Curd=["Amul","Dinshaw","Govardhan"]
        self.price_AmulCurd=50
        self.price_DinshawCurd=45
        self.price_GovardhanCurd=55

        self.Butter=["Amul","Haldiram","Dinshaw"]
        self.price_AmulButter=600
        self.price_HaldiramButter=550
        self.price_DinshawButter=620

        self.Paneer=["Amul","Dinshaw","Raw"]
        self.price_AmulPaneer=200
        self.price_DinshawPaneer=250
        self.price_RawPaneer=180

        #subcategory food grains
        self.SubCatFoodGrains=["Dal","Rice","Wheat","sugar","salt"]

        self.Dal=["Toor Dal","Urad Dal","Channa Dal","Moong Dal"]
        self.price_ToorDal=620
        self.price_uradDal=270
        self.price_ChannaDal=163
        self.price_MoongDal=340

        self.Rice=["Basmati Rice","Boiled & Steam Rice","Raw rice"]
        self.price_BasmatiRice=475
        self.price_BoiledsteamedRice=350
        self.price_RawRice=163

        self.Wheat=["Ashrivad","Royal","Raw"]
        self.price_Ashirvad=190
        self.price_Royal=140
        self.price_Raw=100

        self.Sugar=["Raw","Refined"]
        self.price_Rawsugar=250
        self.price_refinedSugar=260
        

        self.Salt=["Tata","Ashirvad"]
        self.price_Ashirvadsalt=36
        self.price_Tatasalt=22
        


        
        #Image 1
        img = Image.open("Image/b1.jpg")
        img = img.resize((500,200), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img)

        label1=Label(self.root,image=self.photoImg1)
        label1.place(x=0,y=0,width=500,height=200)

        #Image 2
        img2 = Image.open("Image/b3.jpg")
        img2 = img2.resize((500,200), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)

        label2=Label(self.root,image=self.photoImg2)
        label2.place(x=510,y=0,width=500,height=200)


        #Image 3
        img3 = Image.open("Image/b2.jpg")
        img3 = img3.resize((500,200), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)

        label3=Label(self.root,image=self.photoImg3)
        label3.place(x=1020,y=0,width=500,height=200)


        label_title=Label(self.root, text="GROCERY BILLING SOFTWARE ",font=("times new roman",35,"bold"),bg="black",fg="yellow")
        label_title.place(x=0,y=200,width=1700,height=50)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(label_title, font=("times new roman",16,"bold"),background="black",foreground="Yellow")
        lbl.place(x=0,y=0,width=120,height=50)
        time()


        Main_Frame= Frame(self.root,bd=5,relief=GROOVE,bg="White")
        Main_Frame.place(x=0,y=245,width=1700,height=620)

        # Customer_frame

        Customer_frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",18,"bold"),bg="white",fg="red")
        Customer_frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mobile=Label(Customer_frame,text="Mobile No. :",font=("arial",10,"bold"),bg="white")
        self.lbl_mobile.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mobileno=ttk.Entry(Customer_frame,textvariable=self.Customermobileno,font=("arial",10,"bold"),width=24)
        self.entry_mobileno.grid(row=0,column=1)

        self.lbl_customername=Label(Customer_frame,text="Customer Name :",font=("arial",10,"bold"),bg="white")
        self.lbl_customername.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_customername=ttk.Entry(Customer_frame,textvariable=self.Customername,font=("arial",10,"bold"),width=24)
        self.entry_customername.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbl_email=Label(Customer_frame,text="Email ID: ",font=("arial",10,"bold"),bg="white")
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_email=ttk.Entry(Customer_frame,textvariable=self.Customeremail,font=("arial",10,"bold"),width=24)
        self.entry_email.grid(row=2,column=1,sticky=W,padx=5, pady=2)

        #products Labelframe


        Product_frame=LabelFrame(Main_Frame,text="Product",font=("arial",18,"bold"),bg="white",fg="red")
        Product_frame.place(x=370,y=5,width=640,height=140)

        # category

        self.lbl_category=Label(Product_frame,text="Select Category : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_category.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(Product_frame,value=self.Category,font=("arial",10,"bold"),state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)

        #subcategory


        self.lbl_subcategory=Label(Product_frame,text="Sub Category : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.combo_subcategory=ttk.Combobox(Product_frame,value=[""],font=("arial",10,"bold"),state="readonly")
        self.combo_subcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_subcategory.bind("<<ComboboxSelected>>",self.Product_add)


        #product Name

        self.lbl_Productname=Label(Product_frame,text="Product Name : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_Productname.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.combo_Productname=ttk.Combobox(Product_frame,textvariable=self.product,font=("arial",10,"bold"),state="readonly")
        self.combo_Productname.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_Productname.bind("<<ComboboxSelected>>",self.price)

        #price


        self.lbl_Price=Label(Product_frame,text="Price : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_Price.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.combo_Price=ttk.Combobox(Product_frame,font=("arial",10,"bold"),state="readonly",textvariable=self.Prices)
        self.combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        # Quantity

        self.lbl_qyt=Label(Product_frame,text="Qyt : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_qyt.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.combo_qyt=ttk.Combobox(Product_frame,font=("arial",10,"bold"),state="readonly",textvariable=self.qty)
        self.combo_qyt.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Middle frame
        Middle_frame=Frame(Main_Frame,bd=10)
        Middle_frame.place(x=10,y=150,width=980,height=340)

        img11 = Image.open("Image/a3.jpg")
        img11 = img11.resize((490,340), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)

        
        label11=Label(Middle_frame,image=self.photoImg11)
        label11.place(x=0,y=0,width=490,height=340)

        img12 = Image.open("Image/a4.jpg")
        img12 = img12.resize((490,340), Image.ANTIALIAS)
        self.photoImg12 = ImageTk.PhotoImage(img12)

        
        label12=Label(Middle_frame,image=self.photoImg12)
        label12.place(x=490,y=0,width=490,height=340)


        #search
        Search_frame=Frame(Main_Frame,bd=2,bg="white")
        Search_frame.place(x=1020,y=10,width=500,height=40)

        self.lbl_Bill=Label(Search_frame,text=" Bill No.: ",font=("arial",10,"bold"),bg="orange",fg="black")
        self.lbl_Bill.grid(row=0,column=0,sticky=W,padx=1)

        self.entry_search=ttk.Entry(Search_frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.entry_search.grid(row=0,column=1,sticky=W,padx=12)

        self.btnsearch=Button(Search_frame,command=self.find_bill,height=2,text="Search",font=("arial",8,"bold"),bg="orangered",fg="black",width=15,cursor="hand2")
        self.btnsearch.grid(row=0,column=2)



        #Bill area

        rightlabelframe=LabelFrame(Main_Frame,text="Billing Area" ,font=("arial",18,"bold"),bg="white",fg="red")
        rightlabelframe.place(x=1020,y=45,width=500, height=420)

        Scrollbar_y=Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea=Text(rightlabelframe,yscrollcommand=Scrollbar_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #Bill counter 


        
        Bottom_frame=LabelFrame(Main_Frame,text="BILL Counter",font=("arial",18,"bold"),bg="white",fg="red")
        Bottom_frame.place(x=0,y=420,width=1700,height=135)


        self.lbl_subtotal=Label(Bottom_frame,text="SUB TOTAL : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_subtotal=ttk.Entry(Bottom_frame,font=("arial",10,"bold"),state="readonly")
        self.entry_subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_frame,text=" GOV Tax : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_tax=ttk.Entry(Bottom_frame,font=("arial",10,"bold"),state="readonly")
        self.entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        

        #totalamount


        self.lbl_Totalamount=Label(Bottom_frame,text="Total Amount : ",font=("arial",10,"bold"),bg="white",bd=4)
        self.lbl_Totalamount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_Totalamount=ttk.Entry(Bottom_frame,font=("arial",10,"bold"),state="readonly")
        self.entry_Totalamount.grid(row=2,column=1,sticky=W,padx=5,pady=2)



        #button frame

        Btn_frame=Frame(Bottom_frame,bd=2,bg="white")
        Btn_frame.place(x=320,y=0)
        
        self.btnaddtocart=Button(Btn_frame,command=self.Additem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="black",width=15,cursor="hand2")
        self.btnaddtocart.grid(row=0,column=0)

        self.btngbill=Button(Btn_frame,command=self.gen_bill,height=2,text="Generate BIll",font=("arial",15,"bold"),bg="orangered",fg="black",width=15,cursor="hand2")
        self.btngbill.grid(row=0,column=1)

        self.btnsavebill=Button(Btn_frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="black",width=15,cursor="hand2")
        self.btnsavebill.grid(row=0,column=2)

        self.btnprint=Button(Btn_frame,command=self.iprint,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="black",width=15,cursor="hand2")
        self.btnprint.grid(row=0,column=3)

        self.btnclear=Button(Btn_frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="black",width=15,cursor="hand2")
        self.btnclear.grid(row=0,column=4)

        self.btnexit=Button(Btn_frame,command=self.root.destroy,height=2,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="black",width=15,cursor="hand2")
        self.btnexit.grid(row=0,column=5)
        self.welcome()

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t \tWelcome Harshal Mini grocery shop")
        self.textarea.insert(END,f"\n Mobile No.: {self.Customermobileno.get()}")
        self.textarea.insert(END,f"\n Customer name: {self.Customername.get()}")
        self.textarea.insert(END,f"\n Mail Id: {self.Customeremail.get()}")
        self.textarea.insert(END,f"\n Bill Number: {self.Billno.get()}")
        

        self.textarea.insert(END,"\n===================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n===================================================\n")
    
    # ==========================Function Declaratiion=============
        self.l=[]

    def Additem(self):
        Tax=1
        self.n=self.Prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the product name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.Sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.Prices.get()))*Tax)/100)))
            self.TotalAmount.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.Prices.get()))*Tax)/100)))))
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n===================================================")
            self.textarea.insert(END,f"\n Sub Amount : \t\t\t{self.Sub_total.get()}")
            self.textarea.insert(END,f"\n Tax : \t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total: \t\t\t{self.TotalAmount.get()}")
            self.textarea.insert(END,"\n===================================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You want to save this Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("Bills/"+str(self.Billno.get())+".txt","w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.Billno.get()} saved succesfully")
            f1.close()
    
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"Print")
    
    def find_bill(self):
        found="no"
        for i in os.listdir("Bills/"):
            if i.spilt(".")[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
                messagebox.showerror("Error","Invalid Number")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.Customername.set("")
        self.Customermobileno.set("")
        self.Customeremail.set("")
        x=random.randint(1000,9999)
        self.Billno.set(str(x))
        self.product.set("")
        self.Prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.TotalAmount.set("")
        self.Sub_total.set("")
        self.tax_input.set("")
        self.welcome()

    

    




    def Categories(self,event=""):
        if self.combo_category.get()== "Vegetable":
            self.combo_subcategory.config(value=self.SubCatVegetables)
            self.combo_subcategory.current(0)

  
        if self.combo_category.get()=="Milk and Dairy":
            self.combo_subcategory.config(value=self.SubCatMilkandDairy)
            self.combo_subcategory.current(0)

    
        if self.combo_category.get()=="Food Grains":
            self.combo_subcategory.config(value=self.SubCatFoodGrains)
            self.combo_subcategory.current(0)

    def Product_add(self,event=""):
        if self.combo_subcategory.get()=="Onion":
            self.combo_Productname.config(value=self.onions)
            self.combo_Productname.current(0)

        if self.combo_subcategory.get()=="Potato":
            self.combo_Productname.config(value=self.Potato)
            self.combo_Productname.current(0)
        # Potato","Carrot","Tomato","Cauliflower","Palak","Ginger

        if self.combo_subcategory.get()=="Carrot":
            self.combo_Productname.config(value=self.Carrot)
            self.combo_Productname.current(0)

        if self.combo_subcategory.get()=="Tomato":
            self.combo_Productname.config(value=self.Tomato)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Cauliflower":
            self.combo_Productname.config(value=self.Cauliflower)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Palak":
            self.combo_Productname.config(value=self.Palak)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Ginger":
            self.combo_Productname.config(value=self.Giger)
            self.combo_Productname.current(0)
        # for MIlk and Dairy
        if self.combo_subcategory.get()=="Milk":
            self.combo_Productname.config(value=self.Milk)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Curd":
            self.combo_Productname.config(value=self.Curd)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Butter":
            self.combo_Productname.config(value=self.Butter)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Paneer":
            self.combo_Productname.config(value=self.Paneer)
            self.combo_Productname.current(0)
            # For food and grains
        if self.combo_subcategory.get()=="Dal":
            self.combo_Productname.config(value=self.Dal)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Rice":
            self.combo_Productname.config(value=self.Rice)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="Wheat":
            self.combo_Productname.config(value=self.Wheat)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="sugar":
            self.combo_Productname.config(value=self.Sugar)
            self.combo_Productname.current(0)
        if self.combo_subcategory.get()=="salt":
            self.combo_Productname.config(value=self.Salt)
            self.combo_Productname.current(0)
    def price(self,event=""):
        #onion
        if self.combo_Productname.get()=="onion":
            self.combo_Price.config(value=self.price_onions)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Productname.get()=="New":
            self.combo_Price.config(value=self.price_Newpotato)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Old":
            self.combo_Price.config(value=self.price_Oldpotato)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Productname.get()=="Carrot":
            self.combo_Price.config(value=self.price_Carrot)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Productname.get()=="Tomato":
            self.combo_Price.config(value=self.price_Tomato)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Cauliflower":
            self.combo_Price.config(value=self.price_Cauliflower)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Productname.get()=="Palak":
            self.combo_Price.config(value=self.price_Palak)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Ginger":
            self.combo_Price.config(value=self.price_Ginger)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Amul":
            self.combo_Price.config(value=self.price_AmulMilk)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Dinshaw":
            self.combo_Price.config(value=self.price_DinshawMilk)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Haldiram":
            self.combo_Price.config(value=self.price_HaldiramMilk)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Amul":
            self.combo_Price.config(value=self.price_AmulCurd)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Ginger":
            self.combo_Price.config(value=self.price_Ginger)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Dinshaw":
            self.combo_Price.config(value=self.price_DinshawCurd)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Govardhan":
            self.combo_Price.config(value=self.price_GovardhanCurd)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Amul":
            self.combo_Price.config(value=self.price_AmulButter)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Haldiram":
            self.combo_Price.config(value=self.price_HaldiramButter)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Dinshaw":
            self.combo_Price.config(value=self.price_DinshawButter)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Amul":
            self.combo_Price.config(value=self.price_AmulPaneer)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Dinshaw":
            self.combo_Price.config(value=self.price_DinshawPaneer)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Raw":
            self.combo_Price.config(value=self.price_RawPaneer)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Productname.get()=="Toor Dal":
            self.combo_Price.config(value=self.price_ToorDal)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Urad Dal":
            self.combo_Price.config(value=self.price_uradDal)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Channa Dal":
            self.combo_Price.config(value=self.price_ChannaDal)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Moong Dal":
            self.combo_Price.config(value=self.price_MoongDal)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Basmati Rice":
            self.combo_Price.config(value=self.price_BasmatiRice)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Boiled & Steam Rice":
            self.combo_Price.config(value=self.price_BoiledsteamedRice)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Raw rice":
            self.combo_Price.config(value=self.price_RawRice)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Ashrivad":
            self.combo_Price.config(value=self.price_Ashirvad)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Royal":
            self.combo_Price.config(value=self.price_Royal)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Raw":
            self.combo_Price.config(value=self.price_Raw)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Raw":
            self.combo_Price.config(value=self.price_Rawsugar)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Refined":
            self.combo_Price.config(value=self.price_refinedSugar)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Tata":
            self.combo_Price.config(value=self.price_Tatasalt)
            self.combo_Price.current(0)
            self.qty.set(1)
        if self.combo_Productname.get()=="Ashirvad":
            self.combo_Price.config(value=self.price_Ashirvadsalt)
            self.combo_Price.current(0)
            self.qty.set(1)

        
        





        

        
            



      





        
















    









if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
        