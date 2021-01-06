from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import sqlite3
import random

totaldrink=0
total1=0
limca_variable2=sprite_variable2=pepsi_variable2=frooti_variable2=mojito_variable2=water_variable2=coffee_variable2=0
pasta_variable2=fries_variable2=chowmein_variable2=hotdog_variable2=sandwich_variable2=momos_variable2=samosa_variable2=0
chilli_variable2=idlii_variable2=dosa_variable2=pulses_variable2=shahipaneer_variable2=matarpaneer_variable2=0
kofta_variable2=roti_variable2=nanroti_variable2=rice_variable2=salad_variable2=desert_variable2=icecream_variable2=0

def recipt():
    tmsg.showinfo("INFORMATION","Generating the recipt ")
    tex.delete("1.0", END)
    tex.insert(END, "Recipt Info    :\t\t\t\t"+q+"\n")
    tex.insert(END, "Name           :\t\t\t\t"+name.get()+"\n")
    tex.insert(END, "Phone Number   :\t\t\t\t"+Phone.get()+"\n")
    tex.insert(END, "--------------------------------------------------------------------------------\n")
    tex.insert(END, "NAME\t\t      QUANTITY\t\t           COST"+"\n")

    tex.insert(END, "Sprite:      \t\t\t"+sprite_variable.get()+"\t\t"+str(sprite_variable2)+"\n")
    tex.insert(END, "Pepsi:       \t\t\t"+pepsi_variable.get()+"\t\t "+str(pepsi_variable2)+"\n")
    tex.insert(END, "Limca:       \t\t\t"+limca_variable.get()+"\t\t "+str(limca_variable2)+"\n")
    tex.insert(END, "Frooti:      \t\t\t"+frooti_variable.get()+"\t\t "+str(frooti_variable2)+"\n")
    tex.insert(END, "Mojito:      \t\t\t"+mojito_variable.get()+"\t\t "+str(mojito_variable2)+"\n")
    tex.insert(END, "Water:       \t\t\t"+water_variable.get()+"\t\t "+str(water_variable2)+"\n")
    tex.insert(END, "Coffee:      \t\t\t"+coffee_variable.get()+"\t\t "+str(coffee_variable2)+"\n")
    tex.insert(END, "Pasta:       \t\t\t"+pasta_variable.get()+"\t\t "+str(pasta_variable2)+"\n")
    tex.insert(END, "Fries:       \t\t\t"+fries_variable.get()+"\t\t "+str(fries_variable2)+"\n")
    tex.insert(END, "Chowmein:    \t\t\t"+chowmein_variable.get()+"\t\t "+str(chowmein_variable2)+"\n")
    tex.insert(END, "Hot Dog:     \t\t\t"+hotdog_variable.get()+"\t\t "+str(hotdog_variable2)+"\n")
    tex.insert(END, "Sandwich:    \t\t\t "+sandwich_variable.get()+"\t\t "+str(sandwich_variable2)+"\n")
    tex.insert(END, "Momos:       \t\t\t"+momos_variable.get()+"\t\t "+str(momos_variable2)+"\n")
    tex.insert(END, "Samosa:      \t\t\t"+samosa_variable.get()+"\t\t "+str(samosa_variable2)+"\n")
    tex.insert(END, "Chilli:      \t\t\t"+chilli_variable.get()+"\t\t "+str(chilli_variable2)+"\n")
    tex.insert(END, "Idlii:       \t\t\t"+idlii_variable.get()+"\t\t "+str(idlii_variable2)+"\n")
    tex.insert(END, "Plain Dosa:  \t\t\t"+dosa_variable.get()+"\t\t "+str(dosa_variable2)+"\n")
    tex.insert(END, "Pulses:      \t\t\t"+pulses_variable.get()+"\t\t "+str(pulses_variable2)+"\n")
    tex.insert(END, "Shahi Paneer:\t\t\t"+shahiPaneer_variable.get()+"\t\t "+str(shahipaneer_variable2)+"\n")
    tex.insert(END, "Matar Paneer:\t\t\t"+matarPaneer_variable.get()+"\t\t "+str(matarpaneer_variable2)+"\n")
    tex.insert(END, "Kofta:       \t\t\t"+kofta_variable.get()+"\t\t "+str(kofta_variable2)+"\n")
    tex.insert(END, "Roti:        \t\t\t"+roti_variable.get()+"\t\t "+str(roti_variable2)+"\n")
    tex.insert(END, "Nan Roti:    \t\t\t"+nanroti_variable.get()+"\t\t "+str(nanroti_variable2)+"\n")
    tex.insert(END, "Special Rice:\t\t\t"+rice_variable.get()+"\t\t "+str(rice_variable2)+"\n")
    tex.insert(END, "Salad:       \t\t\t"+salad_variable.get()+"\t\t "+str(salad_variable2)+"\n")
    tex.insert(END, "Desert:      \t\t\t"+desert_variable.get()+"\t\t "+str(desert_variable2)+"\n")
    tex.insert(END, "Ice-Cream:   \t\t\t"+icecream_variable.get()+"\t\t "+str(icecream_variable2)+"\n")
    tex.insert(END, "--------------------------------------------------------------------------------\n")
    tex.insert(END, "--------------------------------------------------------------------------------\n")
    tex.insert(END, "Cost of Drinks:\t\t\t"+"\t\t "+CostofDrink.get()+"\n")
    tex.insert(END, "Cost of Foods:\t\t\t"+"\t\t "+CostofFood.get()+"\n")
    tex.insert(END, "Cost of Snacks:\t\t\t"+"\t\t "+CostofSnacks.get()+"\n")
    tex.insert(END, "****************************************************************\n")
    tex.insert(END, "Total:\t\t\t"+"\t\t "+Total.get()+"\n")
    tex.insert(END, "Taxes:\t\t\t"+"\t\t "+Taxes.get()+"\n")
    tex.insert(END, "Grand Total:\t\t\t"+"\t\t"+Gtotal.get()+"\n")
    tex.insert(END, "Paid:\t\t\t"+"\t\t"+Paid.get()+"\n")
    tex.insert(END, "Returned:\t\t\t"+"\t\t"+Return.get()+"\n")

def reset():
    Entry(textvariable=sprite_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=133)
    Entry(textvariable=pepsi_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=170)
    Entry(textvariable=limca_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=209)
    Entry(textvariable=frooti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=249)
    Entry(textvariable=mojito_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=290)
    Entry(textvariable=water_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=332)
    Entry(textvariable=coffee_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=373)
    Entry(textvariable=pasta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=414)
    Entry(textvariable=fries_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=455)
    Entry(textvariable=chowmein_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=133)
    Entry(textvariable=hotdog_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=170)
    Entry(textvariable=sandwich_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=209)
    Entry(textvariable=momos_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=249)
    Entry(textvariable=samosa_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=290)
    Entry(textvariable=chilli_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=332)
    Entry(textvariable=idlii_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=373)
    Entry(textvariable=dosa_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=414)
    Entry(textvariable=pulses_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=455)
    Entry(textvariable=shahiPaneer_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=133)
    Entry(textvariable=matarPaneer_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=170)
    Entry(textvariable=kofta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=209)
    Entry(textvariable=roti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=249)
    Entry(textvariable=nanroti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=290)
    Entry(textvariable=rice_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=332)
    Entry(textvariable=salad_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=373)
    Entry(textvariable=desert_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=414)
    Entry(textvariable=icecream_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=455)
    Entry(textvariable=Paid, font="Cappuccino 14 bold ", borderwidth=5, width=9,state=DISABLED).place(x=690, y=518)
    name.set("")
    Phone.set("")
    Return.set("")
    Total.set("")
    Paid.set("")
    tex.delete("1.0", END)
    Taxes.set("")
    Gtotal.set("")
    CostofDrink.set("")
    CostofFood.set("")
    CostofSnacks.set("")
    expression.set("")
    sprite_variable.set("")
    sprite_variable1.set(0)
    pepsi_variable.set("")
    pepsi_variable1.set(0)
    limca_variable.set("")
    limca_variable1.set(0)
    frooti_variable.set("")
    frooti_variable1.set(0)
    mojito_variable.set("")
    mojito_variable1.set(0)
    water_variable.set("")
    water_variable1.set(0)
    mojito_variable.set("")
    mojito_variable1.set(0)
    water_variable.set("")
    water_variable1.set(0)
    coffee_variable.set("")
    coffee_variable1.set(0)
    pasta_variable.set("")
    pasta_variable1.set(0)
    fries_variable.set("")
    fries_variable1.set(0)
    chowmein_variable.set("")
    chowmein_variable1.set(0)
    hotdog_variable.set("")
    hotdog_variable1.set(0)
    sandwich_variable.set("")
    sandwich_variable1.set(0)
    momos_variable.set("")
    momos_variable1.set(0)
    samosa_variable.set("")
    samosa_variable1.set(0)
    chilli_variable.set("")
    chilli_variable1.set(0)
    idlii_variable.set("")
    idlii_variable1.set(0)
    dosa_variable.set("")
    dosa_variable1.set(0)
    pulses_variable.set("")
    pulses_variable1.set(0)
    shahiPaneer_variable.set("")
    shahiPaneer_variable1.set(0)
    matarPaneer_variable.set("")
    matarPaneer_variable1.set(0)
    kofta_variable.set("")
    kofta_variable1.set(0)
    roti_variable.set("")
    roti_variable1.set(0)
    nanroti_variable.set("")
    nanroti_variable1.set(0)
    rice_variable.set("")
    rice_variable1.set(0)
    salad_variable.set("")
    salad_variable1.set(0)
    desert_variable.set("")
    desert_variable1.set(0)
    icecream_variable.set("")
    icecream_variable1.set(0)

def pay1():
    if Paid.get()=="" or Gtotal.get()=="":
        tmsg.showwarning("Warning","Please Enter a valid amount")
    p1=(eval(Paid.get()))
    p2=(eval(Gtotal.get()))
    Return.set(p1-p2)
    
    s0=q
    s1=name.get()
    s2=Phone.get()
    s3=sprite_variable.get()
    s4=pepsi_variable.get()
    s5=limca_variable.get()
    s6=frooti_variable.get()
    s7=mojito_variable.get()
    s8=water_variable.get()
    s9=coffee_variable.get()
    s10=pasta_variable.get()
    s11=fries_variable.get()
    s12=chowmein_variable.get()
    s13=hotdog_variable.get()
    s14=sandwich_variable.get()
    s15=momos_variable.get()
    s16=samosa_variable.get()
    s17=chilli_variable.get()
    s18=idlii_variable.get()
    s19=dosa_variable.get()
    s20=pulses_variable.get()
    s21=shahiPaneer_variable.get()
    s22=matarPaneer_variable.get()
    s23=kofta_variable.get()
    s24=roti_variable.get()
    s25=nanroti_variable.get()
    s26=rice_variable.get()
    s27=salad_variable.get()
    s28=desert_variable.get()
    s29=icecream_variable.get()
    s30=CostofDrink.get()
    s31=CostofFood.get()
    s32=CostofSnacks.get()
    s33=Total.get()
    s34=Taxes.get()
    s35=Gtotal.get()
    s36=Paid.get()
    s37=Return.get()

    conn=sqlite3.connect('FBS1.db')
    with conn:
        cursor=conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS O3(ReciptNo TEXT,Name TEXT,Phone TEXT\
        ,Sprite TEXT,Pepsi TEXT,Limca TEXT,Frooti TEXT,Mojito TEXT,Water TEXT,Coffee TEXT\
        ,Pasta TEXT,Fries TEXT,Chowmein TEXT,HotDog TEXT,Sandwich TEXT,Momos TEXT\
        ,Samosa TEXT,Chilli TEXT,Idlii TEXT,PlainDosa TEXT,Pulses TEXT\
        ,ShahiPaneer TEXT,MatarPaneer TEXT,Kofta TEXT,Roti TEXT,NanRoti TEXT\
        ,Rice TEXT,Salad TEXT,Desert TEXT,IceCream TEXT,CostofDrink TEXT\
        ,CostofFood TEXT,CostofSnacks TEXT,Total TEXT,Taxes TEXT,GrandTotal TEXT\
        ,Paid TEXT,Returned TEXT)")
        
        cursor.execute("INSERT INTO O3(ReciptNo,Name,Phone,Sprite,Pepsi,Limca,Frooti,Mojito\
        ,Water,Coffee,Pasta,Fries,Chowmein,HotDog,Sandwich,Momos,Samosa,Chilli,Idlii\
        ,PlainDosa,Pulses,ShahiPaneer,MatarPaneer,Kofta,Roti,NanRoti,Rice,Salad,Desert,\
        IceCream,CostofDrink,CostofFood,CostofSnacks,Total,Taxes,GrandTotal,Paid,Returned    \
        ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        ,(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,\
        s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37))

        conn.commit()

def PressAnyKey(event):
    value=event.char
    if value=='\x1b':
        exit()
    else:
        pass
def dishes(i):

    if sprite_variable1.get():
        Entry(textvariable=sprite_variable, width=5, font="lucida 15 bold ",bg="red").place(x=188, y=133)
    else:
         Entry(textvariable=sprite_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=133)
         sprite_variable.set("")

    if pepsi_variable1.get():
        Entry(textvariable=pepsi_variable, width=5, font="lucida 15 bold ",bg="red").place(x=188, y=170)
    else:
        Entry(textvariable=pepsi_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=170)
        pepsi_variable.set("")

    if limca_variable1.get():
        Entry(textvariable=limca_variable, width=5, font="lucida 15 bold ",bg="red").place(x=188, y=209)
    else:
        Entry(textvariable=limca_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=209)
        limca_variable.set("")

    if frooti_variable1.get():
        Entry(textvariable=frooti_variable, width=5, font="lucida 15 bold ",bg="red").place(x=188, y=249)
    else:
        Entry(textvariable=frooti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=249)
        frooti_variable.set("")

    if mojito_variable1.get():
        Entry(textvariable=mojito_variable, width=5, font="lucida 15 bold ",bg="red").place(x=188, y=290)
    else:
        Entry(textvariable=mojito_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=290)
        mojito_variable.set("")

    if water_variable1.get():
        Entry(textvariable=water_variable, width=5, font="lucida 15 bold ",bg="red").place(x=188, y=332)
    else:
        Entry(textvariable=water_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=332)
        water_variable.set("")

    if coffee_variable1.get():
        Entry(textvariable=coffee_variable, width=5, font="lucida 15 bold ", bg="red").place(x=188, y=373)
    else:
        Entry(textvariable=coffee_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=373)
        coffee_variable.set("")

    if pasta_variable1.get():
        Entry(textvariable=pasta_variable, width=5, font="lucida 15 bold ", bg="red").place(x=188, y=414)
    else:
        Entry(textvariable=pasta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=414)
        pasta_variable.set("")

    if fries_variable1.get():
        Entry(textvariable=fries_variable, width=5, font="lucida 15 bold ",bg="red").place(x=188, y=455)
    else:
        Entry(textvariable=fries_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=455)
        fries_variable.set("")

    if chowmein_variable1.get():
        Entry(textvariable=chowmein_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=133)
    else:
        Entry(textvariable=chowmein_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=133)
        chowmein_variable.set("")

    if hotdog_variable1.get():
        Entry(textvariable=hotdog_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=170)
    else:
        Entry(textvariable=hotdog_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=170)
        hotdog_variable.set("")

    if sandwich_variable1.get():
        Entry(textvariable=sandwich_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=209)
    else:
        Entry(textvariable=sandwich_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=209)
        sandwich_variable.set("")

    if momos_variable1.get():
        Entry(textvariable=momos_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=249)
    else:
        Entry(textvariable=momos_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=249)
        momos_variable.set("")

    if samosa_variable1.get():
        Entry(textvariable=samosa_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=290)
    else:
        Entry(textvariable=samosa_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=290)
        samosa_variable.set("")

    if chilli_variable1.get():
        Entry(textvariable=chilli_variable, width=5, font="lucida 15 bold ",bg="red").place(x=520, y=332)
    else:
        Entry(textvariable=chilli_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=332)
        chilli_variable.set("")

    if idlii_variable1.get():
        Entry(textvariable=idlii_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=373)
    else:
        Entry(textvariable=idlii_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=373)
        idlii_variable.set("")

    if dosa_variable1.get():
        Entry(textvariable=dosa_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=414)
        print(dosa_variable.get())
    else:
        Entry(textvariable=dosa_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=414)
        dosa_variable.set("")

    if pulses_variable1.get():
        Entry(textvariable=pulses_variable, width=5, font="lucida 15 bold ", bg="red").place(x=520, y=455)
    else:
        Entry(textvariable=pulses_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=455)
        pulses_variable.set("")

    if shahiPaneer_variable1.get():
        Entry(textvariable=shahiPaneer_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=133)
    else:
        Entry(textvariable=shahiPaneer_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=133)
        shahiPaneer_variable.set("")

    if matarPaneer_variable1.get():
        Entry(textvariable=matarPaneer_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=170)
    else:
        Entry(textvariable=matarPaneer_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=170)
        matarPaneer_variable.set("")

    if kofta_variable1.get():
        Entry(textvariable=kofta_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=209)
    else:
        Entry(textvariable=kofta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=209)
        kofta_variable.set("")

    if roti_variable1.get():
        Entry(textvariable=roti_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=249)
    else:
        Entry(textvariable=roti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=249)
        roti_variable.set("")

    if nanroti_variable1.get():
        Entry(textvariable=nanroti_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=290)
    else:
        Entry(textvariable=nanroti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=290)
        nanroti_variable.set("")

    if rice_variable1.get():
        Entry(textvariable=rice_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=332)
    else:
        Entry(textvariable=rice_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=332)
        rice_variable.set("")

    if salad_variable1.get():
        Entry(textvariable=salad_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=373)
    else:
        Entry(textvariable=salad_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=373)
        salad_variable.set("")

    if desert_variable1.get():
        Entry(textvariable=desert_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=414)
    else:
        Entry(textvariable=desert_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=414)
        desert_variable.set("")

    if icecream_variable1.get():
        Entry(textvariable=icecream_variable, width=5, font="lucida 15 bold ", bg="red").place(x=900, y=455)
    else:
        Entry(textvariable=icecream_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=455)
        icecream_variable.set("")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$getting total$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def total():
    c=Phone.get()
    l=len(c)
    if l>10:
        tmsg.showerror("Error","Please Enter a Valid Phone Number  ")
        Phone.set("")

    global limca_variable2,sprite_variable2, pepsi_variable2 ,frooti_variable2 ,mojito_variable2 ,water_variable2, \
    coffee_variable2,pasta_variable2,fries_variable2,chowmein_variable2,hotdog_variable2,sandwich_variable2,\
    momos_variable2,samosa_variable2,chilli_variable2,idlii_variable2,dosa_variable2,pulses_variable2,\
    shahipaneer_variable2,matarpaneer_variable2,kofta_variable2,roti_variable2,nanroti_variable2,rice_variable2,\
    salad_variable2,desert_variable2,icecream_variable2

    Entry(textvariable=sprite_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=188, y=133)
    digit=sprite_variable.get().isdigit()
    if (sprite_variable.get()=="" or digit==False ):
        sprite_variable2=0
    else:
        sprite_variable2 = int(sprite_variable.get())*10

    Entry(textvariable=pepsi_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=170)
    digit=pepsi_variable.get().isdigit()
    if(pepsi_variable.get()=="" or digit==False):
        pepsi_variable2=0
    else:
        pepsi_variable2 = int(pepsi_variable.get())*15

    Entry(textvariable=limca_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=188, y=209)
    digit=limca_variable.get().isdigit()
    if(limca_variable.get()=="" or digit==False ):
        limca_variable2=0
    else:
        limca_variable2  = int(limca_variable.get())*10
        print(limca_variable2*10)

    Entry(textvariable=frooti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=249)
    digit = frooti_variable.get().isdigit()
    if(frooti_variable.get()=="" or digit==False):
        frooti_variable2=0
    else:
        frooti_variable2 = int(frooti_variable.get())*10

    Entry(textvariable=mojito_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=290)
    digit = mojito_variable.get().isdigit()
    if(mojito_variable.get()=="" or digit==False):
        mojito_variable2=0
    else:
        mojito_variable2 = int(mojito_variable.get())*30

    Entry(textvariable=water_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=332)
    digit = water_variable.get().isdigit()
    if(water_variable.get()=="" or digit==False):
        water_variable2=0
    else:
        water_variable2  = int(water_variable.get())*10

    Entry(textvariable=coffee_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=373)
    digit = coffee_variable.get().isdigit()
    if(coffee_variable.get()=="" or digit==False):
        coffee_variable2=0
    else:
        coffee_variable2 = int(coffee_variable.get())*50

##############Adding the total of  drinks ##################################################################
    totaldrink=coffee_variable2+mojito_variable2+sprite_variable2+pepsi_variable2\
                +limca_variable2+frooti_variable2+water_variable2
    CostofDrink.set(totaldrink)


    Entry(textvariable=pasta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=414)
    digit=pasta_variable.get().isdigit()
    if (pasta_variable.get()=="" or digit==False):
        pasta_variable2=0
    else:
        pasta_variable2=int(pasta_variable.get())*60


    Entry(textvariable=fries_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=188, y=455)
    digit=fries_variable.get().isdigit()
    if (fries_variable.get()==""or digit==False):
        fries_variable2=0
    else:
        fries_variable2 = int(fries_variable.get())*60

    Entry(textvariable=chowmein_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=133)
    digit=chowmein_variable.get().isdigit()
    if chowmein_variable.get()=="" or digit==False:
        chowmein_variable2=0
    else:
        chowmein_variable2=int(chowmein_variable.get())*80

    Entry(textvariable=hotdog_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=170)
    digit=hotdog_variable.get().isdigit()
    if (hotdog_variable.get()=="" or digit==False):
        hotdog_variable2=0
    else:
        hotdog_variable2=int(hotdog_variable.get())*70

    Entry(textvariable=sandwich_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=209)
    digit=sandwich_variable.get().isdigit()
    if (sandwich_variable.get()=="" or digit==False):
        sandwich_variable2=0
    else:
        sandwich_variable2=int(sandwich_variable.get())*80

    Entry(textvariable=momos_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=249)
    digit=momos_variable.get().isdigit()
    if (momos_variable.get()=="" or digit==False):
        momos_variable2=0
    else:
        momos_variable2=int(momos_variable.get())*40

    Entry(textvariable=samosa_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=290)
    digit=samosa_variable.get().isdigit()
    if (samosa_variable.get()=="" or digit==False):
        samosa_variable2=0
    else:
        samosa_variable2=int(samosa_variable.get())*10

    Entry(textvariable=chilli_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=332)
    digit = chilli_variable.get().isdigit()
    if (chilli_variable.get()=="" or digit==False):
        chilli_variable2=0
    else:
        chilli_variable2=int(chilli_variable.get())*70

    Entry(textvariable=idlii_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=373)
    digit=idlii_variable.get().isdigit()
    if (idlii_variable.get()=="" or digit==False):
        idlii_variable2=0
    else:
        idlii_variable2=int(idlii_variable.get())*80

    Entry(textvariable=dosa_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=414)
    digit = dosa_variable.get().isdigit()
    if (dosa_variable.get()=="" or digit==False):
        dosa_variable2=0
    else:
        dosa_variable2=int(dosa_variable.get())*80
        print(dosa_variable.get())

    totalsnacks = pasta_variable2 + fries_variable2+chowmein_variable2+hotdog_variable2\
                  + sandwich_variable2+momos_variable2+samosa_variable2+chilli_variable2\
                  + idlii_variable2+dosa_variable2
    CostofSnacks.set(totalsnacks)

    Entry(textvariable=pulses_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=520, y=455)
    digit=pulses_variable.get().isdigit()
    if (pulses_variable.get()=="" or digit==False):
        pulses_variable2=0
    else:
        pulses_variable2=int(pulses_variable.get())*90

    Entry(textvariable=shahiPaneer_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=900, y=133)
    digit=shahiPaneer_variable.get().isdigit()
    if (shahiPaneer_variable.get()=="" or digit==False):
        shahipaneer_variable2=0
    else:
        shahipaneer_variable2=int(shahiPaneer_variable.get())*120

    Entry(textvariable=matarPaneer_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=900, y=170)
    digit=matarPaneer_variable.get().isdigit()
    if (matarPaneer_variable.get()=="" or digit==False):
        matarpaneer_variable2=0
    else:
        matarpaneer_variable2=int(matarPaneer_variable.get())*100

    Entry(textvariable=kofta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=209)
    digit=kofta_variable.get().isdigit()
    if (kofta_variable.get()=="" or digit==False):
        kofta_variable2=0
    else:
        kofta_variable2=int(kofta_variable.get())*90

    Entry(textvariable=roti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=249)
    digit=roti_variable.get().isdigit()
    if (roti_variable.get()=="" or digit==False):
        roti_variable2=0
    else:
        roti_variable2=int(roti_variable.get())*5

    Entry(textvariable=nanroti_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=900, y=290)
    digit=nanroti_variable.get().isdigit()
    if (nanroti_variable1.get()=="" or digit==False):
        nanroti_variable2=0
    else:
        nanroti_variable2 = int(nanroti_variable.get()) * 10

    Entry(textvariable=rice_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=332)
    digit=rice_variable.get().isdigit()
    if (rice_variable.get()=="" or digit==False):
        rice_variable2=0
    else:
        rice_variable2=int(rice_variable.get())*50

    Entry(textvariable=salad_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=373)
    digit=salad_variable.get().isdigit()
    if (salad_variable.get()=="" or digit==False):
        salad_variable2=0
    else:
        salad_variable2=int(salad_variable.get())*15

    Entry(textvariable=desert_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=900, y=414)
    digit=desert_variable.get().isdigit()
    if (desert_variable1.get()=="" or digit==False):
        desert_variable2=0
    else:
        desert_variable2=int(desert_variable.get())*30

    Entry(textvariable=icecream_variable, width=5, font="lucida 15 bold ",state=DISABLED).place(x=900, y=455)
    digit=icecream_variable.get().isdigit()
    if (icecream_variable.get()=="" or digit==False):
        icecream_variable2=0
    else:
        icecream_variable2=int(icecream_variable.get())*60

    totalfood = pulses_variable2 + shahipaneer_variable2+matarpaneer_variable2+kofta_variable2 \
                +roti_variable2+ nanroti_variable2 +rice_variable2+salad_variable2+desert_variable2\
                + icecream_variable2
    CostofFood.set(totalfood)

    total1=totalfood+totaldrink+totalsnacks
    Total.set(total1)
    taxes=(total1*10)/100
    Taxes.set(taxes)
    Gtotal.set(taxes+total1)
    Entry(textvariable=Paid, font="Cappuccino 14 bold ", borderwidth=5, width=9,bg="red").place(x=690, y=518)

expression1=""
def press(i):
    global expression1
    expression1=expression1+str(i)
    expression.set(expression1)
def equ():
    global expression1
    try:
        exp=eval(expression1)
        expression.set(exp)
        expression1=""
    except:
        expression.set("PLEASE")
def c():
    global expression1
    expression1=""
    expression.set("")


if __name__=="__main__":
    q=""
    ran=random.randint(100,6000)
    q=str(ran)
    canwidth = 2000
    canheight = 1000
    root = Tk()
    root.title("Food Billing")
    root.geometry("1360x750")
    root.resizable(False,False)
    root.config(background="red")

    canwidget = Canvas(width=canwidth, height=canheight)
    canwidget.pack()

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Heading@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    canwidget.create_rectangle(6,6,600,110,fill="red")
    l1 = Label(text="Food Billing System",font="lucida 40 bold italic",bg="red",fg="white").place(x=20, y=12)

    canwidget.create_rectangle(640, 6, 1000, 110, fill="orange")
    Label(text="Name        :",font="lucida 15 bold ",bg="orange").place(x=645,y=15)
    name=StringVar()
    Entry(textvariable=name,font="lucida 15 bold ",borderwidth=5).place(x=750,y=15)

    Label(text="Phone No  :", font="lucida 15 bold ", bg="orange").place(x=645, y=60)
    Phone=StringVar()
    Entry(textvariable=Phone,font="lucida 15 bold ",borderwidth=5).place(x=750,y=60)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^adding the dishes^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    canwidget.create_rectangle(6,120,1000,500,fill="orange")

    sprite_variable1 = IntVar()
    sprite_variable = StringVar()
    Checkbutton(text="Sprite\t10", font="Cappuccino 18 bold ", bg="orange", var=sprite_variable1,
                command=lambda: dishes(sprite_variable1.get())).place(x=20, y=125)
    e1=Entry(textvariable=sprite_variable, width=5, font="lucida 15 bold ", state=DISABLED)
    e1.place(x=188, y=133)  # +10

    pepsi_variable1 = IntVar()
    pepsi_variable = StringVar()
    Checkbutton(text="Pepsi\t15", font="Cappuccino 18 bold ", bg="orange", var=pepsi_variable1,
                command=lambda: dishes(pepsi_variable1.get())).place(x=20, y=165)
    Entry(textvariable=pepsi_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=170)
   # pepsi_variable.set("")

    limca_variable1 = IntVar()
    limca_variable = StringVar()
    Checkbutton(text="Limca\t10", font="Cappuccino 18 bold ", bg="orange", var=limca_variable1,
                command=lambda: dishes(limca_variable1.get())).place(x=20, y=205)
    Entry(textvariable=limca_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=209)
    #limca_variable.set("")

    frooti_variable1 = IntVar()
    frooti_variable = StringVar()
    Checkbutton(text="Frooti\t10", font="Cappuccino 18 bold ", bg="orange", var=frooti_variable1,
                command=lambda: dishes(frooti_variable1.get())).place(x=20, y=245)
    Entry(textvariable=frooti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=249)
   # frooti_variable.set("")

    mojito_variable1 = IntVar()
    mojito_variable = StringVar()
    Checkbutton(text="Mojito\t30", font="Cappuccino 18 bold ", bg="orange", var=mojito_variable1,
                command=lambda: dishes(mojito_variable1.get())).place(x=20, y=285)
    Entry(textvariable=mojito_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=290)
    #mojito_variable.set("")

    water_variable1 = IntVar()
    water_variable = StringVar()
    Checkbutton(text="Water\t10", font="Cappuccino 18 bold ", bg="orange", var=water_variable1,
                command=lambda: dishes(water_variable1.get())).place(x=20, y=325)
    Entry(textvariable=water_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=332)
    #water_variable.set("")

    coffee_variable1 = IntVar()
    coffee_variable = StringVar()
    Checkbutton(text="Coffee\t50", font="Cappuccino 18 bold ", bg="orange", var=coffee_variable1,
                command=lambda: dishes(coffee_variable1.get())).place(x=20, y=365)
    Entry(textvariable=coffee_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=373)
    #coffee_variable.set("")

    pasta_variable1 = IntVar()
    pasta_variable = StringVar()
    Checkbutton(text="Pasta\t60", font="Cappuccino 18 bold ", bg="orange", var=pasta_variable1,
                command=lambda: dishes(pasta_variable1.get())).place(x=20, y=405)
    Entry(textvariable=pasta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=414)
    #pasta_variable.set("")

    fries_variable1 = IntVar()
    fries_variable = StringVar()
    Checkbutton(text="Fries\t60", font="Cappuccino 18 bold ", bg="orange", var=fries_variable1,
                command=lambda: dishes(fries_variable1.get())).place(x=20, y=445)
    Entry(textvariable=fries_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=188, y=455)
    #fries_variable.set("")

    ###################################################################################################################

    chowmein_variable1 = IntVar()
    chowmein_variable = StringVar()
    Checkbutton(text="Chowmein   80", font="Cappuccino 18 bold ", bg="orange", var=chowmein_variable1,
                command=lambda: dishes(chowmein_variable1.get())).place(x=300, y=125)
    Entry(textvariable=chowmein_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=133)

    hotdog_variable1 = IntVar()
    hotdog_variable = StringVar()
    Checkbutton(text="Hot Dog       70", font="Cappuccino 18 bold ", bg="orange", var=hotdog_variable1,
                command=lambda: dishes(hotdog_variable1.get())).place(x=300, y=165)
    Entry(textvariable=hotdog_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=170)

    sandwich_variable1 = IntVar()
    sandwich_variable = StringVar()
    Checkbutton(text="Sandwich    80", font="Cappuccino 18 bold ", bg="orange", var=sandwich_variable1,
                command=lambda: dishes(sandwich_variable1.get())).place(x=300, y=205)
    Entry(textvariable=sandwich_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=209)

    momos_variable1 = IntVar()
    momos_variable = StringVar()
    Checkbutton(text="Momos        40", font="Cappuccino 18 bold ", bg="orange", var=momos_variable1,
                command=lambda: dishes(momos_variable1.get())).place(x=300, y=245)
    Entry(textvariable=momos_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=249)

    samosa_variable1 = IntVar()
    samosa_variable = StringVar()
    Checkbutton(text="Samosa       10", font="Cappuccino 18 bold ", bg="orange", var=samosa_variable1,
                command=lambda: dishes(samosa_variable1.get())).place(x=300, y=285)
    Entry(textvariable=samosa_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=290)

    chilli_variable1 = IntVar()
    chilli_variable = StringVar()
    Checkbutton(text="Chilli            70", font="Cappuccino 18 bold ", bg="orange", var=chilli_variable1,
                command=lambda: dishes(chilli_variable1.get())).place(x=300, y=325)
    Entry(textvariable=chilli_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=332)

    idlii_variable1 = IntVar()
    idlii_variable = StringVar()
    Checkbutton(text="Idlii              80", font="Cappuccino 18 bold ", bg="orange", var=idlii_variable1,
                command=lambda: dishes(idlii_variable1.get())).place(x=300, y=365)
    Entry(textvariable=idlii_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=373)

    dosa_variable1 = IntVar()
    dosa_variable = StringVar()
    Checkbutton(text="Plain Dosa   80", font="Cappuccino 18 bold ", bg="orange", var=dosa_variable1,
                command=lambda: dishes(dosa_variable1.get())).place(x=300, y=405)
    Entry(textvariable=dosa_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=414)

    pulses_variable1 = IntVar()
    pulses_variable =StringVar()
    Checkbutton(text="Pulses          90", font="Cappuccino 18 bold ", bg="orange", var=pulses_variable1,
                command=lambda: dishes(pulses_variable1.get())).place(x=300, y=445)
    Entry(textvariable=pulses_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=520, y=455)
    #########################################################################################################################################
    shahiPaneer_variable1 = IntVar()
    shahiPaneer_variable = StringVar()
    Checkbutton(text="Shahi Paneer      120", font="Cappuccino 18 bold ", bg="orange", var=shahiPaneer_variable1,
                command=lambda: dishes(shahiPaneer_variable1.get())).place(x=625, y=125)
    Entry(textvariable=shahiPaneer_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=133)

    matarPaneer_variable1 = IntVar()
    matarPaneer_variable = StringVar()
    Checkbutton(text="Matar Paneer      100", font="Cappuccino 18 bold ", bg="orange", var=matarPaneer_variable1,
                command=lambda: dishes(matarPaneer_variable1.get())).place(x=625, y=165)
    Entry(textvariable=matarPaneer_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=170)

    kofta_variable1 = IntVar()
    kofta_variable = StringVar()
    Checkbutton(text="Kofta                    90", font="Cappuccino 18 bold ", bg="orange", var=kofta_variable1,
                command=lambda: dishes(kofta_variable1.get())).place(x=625, y=205)
    Entry(textvariable=kofta_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=209)

    roti_variable1 = IntVar()
    roti_variable = StringVar()
    Checkbutton(text="Roti                       5", font="Cappuccino 18 bold ", bg="orange", var=roti_variable1,
                command=lambda: dishes(roti_variable1.get())).place(x=625, y=245)
    Entry(textvariable=roti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=249)

    nanroti_variable1 = IntVar()
    nanroti_variable = StringVar()
    Checkbutton(text="Nan Roti              10", font="Cappuccino 18 bold ", bg="orange", var=nanroti_variable1,
                command=lambda: dishes(nanroti_variable1.get())).place(x=625, y=285)
    Entry(textvariable=nanroti_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=290)

    rice_variable1 = IntVar()
    rice_variable = StringVar()
    Checkbutton(text="Special Rice        50", font="Cappuccino 18 bold ", bg="orange", var=rice_variable1,
                command=lambda: dishes(rice_variable1.get())).place(x=625, y=325)
    Entry(textvariable=rice_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=332)

    salad_variable1 = IntVar()
    salad_variable = StringVar()
    Checkbutton(text="Salad                   15", font="Cappuccino 18 bold ", bg="orange", var=salad_variable1,
                command=lambda: dishes(salad_variable1.get())).place(x=625, y=365)
    Entry(textvariable=salad_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=373)

    desert_variable1 = IntVar()
    desert_variable = StringVar()
    Checkbutton(text="Desert                  30", font="Cappuccino 18 bold ", bg="orange", var=desert_variable1,
                command=lambda: dishes(desert_variable1.get())).place(x=625, y=405)
    Entry(textvariable=desert_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=414)

    icecream_variable1 = IntVar()
    icecream_variable = StringVar()
    Checkbutton(text="Ice Cream            60", font="Cappuccino 18 bold ", bg="orange", var=icecream_variable1,
                command=lambda: dishes(icecream_variable1.get())).place(x=626, y=445)
    Entry(textvariable=icecream_variable, width=5, font="lucida 15 bold ", state=DISABLED).place(x=900, y=455)

   #creating the calculator
    canwidget.create_rectangle(1015,6,1350,289,fill="orange") # 5 ka decrement hua hai
    expression=StringVar()
    ecalculator= Entry(text=expression,width=26,font=('arial',15, ' bold'),borderwidth=5)
    ecalculator.place(x=1040,y=46)  #114
    ecalculator.bind('<Key>',lambda i:PressAnyKey(i))
    Label(text="CALCULATOR",font="lucida 15 bold ",borderwidth=5,bg="orange").place(x=1100,y=8)
    
    Button(text="0", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(0)).place(x=1040,y=91)  #61
    Button(text="1", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(1)).place(x=1100,y=91)
    Button(text="2", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(2)).place(x=1160,y=91)
    Button(text="3", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(3)).place(x=1220,y=91)
    Button(text="+", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press("+")).place(x=1280, y=91)
    
    Button(text="4", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(4)).place(x=1040, y=142)  #112
    Button(text="5", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(5)).place(x=1100, y=142)
    Button(text="6", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(6)).place(x=1160, y=142)
    Button(text="7", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(7)).place(x=1220, y=142)
    Button(text="-", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press("-")).place(x=1280, y=142)
    
    Button(text="8", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(8)).place(x=1040, y=193)   #163
    Button(text="9", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(9)).place(x=1100, y=193)
    Button(text=".", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press(".")).place(x=1160, y=193)
    Button(text="/", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press("/")).place(x=1220, y=193)
    Button(text="*", bg="red", pady=5, padx=16, borderwidth=5,command=lambda:press("*")).place(x=1280, y=193)
    
    Button(text="=", bg="red", pady=5, padx=16, borderwidth=5,command=equ).place(x=1120, y=240)  #244
    Button(text="C", bg="red", pady=5, padx=16, borderwidth=5,command=c).place(x=1200, y=240)

    ###############################################generating the recipt#######################################
    canwidget.create_rectangle(1015,300,1350,700,fill="red")
    tex = Text(root)
    tex.place(x=1018,y=350)
    tex.config( font=('Arial', 10, 'bold', 'italic'),width=46,height=20) #8

    #********************************************generating the total and subtotal**************************************
    canwidget.create_rectangle(6,510,1000,700,fill="orange")

    CostofDrink=StringVar()
    Label(text="Cost Of Drinks :",font="Cappuccino 15 bold ",bg="pink").place(x=9,y=518)
    Entry(textvariable=CostofDrink,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=182,y=518)

    CostofFood=StringVar()
    Label(text="Cost Of Foods :",font="Cappuccino 15 bold ",bg="pink").place(x=9,y=580)
    Entry(textvariable=CostofFood,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=182,y=578)

    CostofSnacks=StringVar()
    Label(text="Cost Of Snacks :",font="Cappuccino 15 bold ",bg="pink").place(x=9,y=642)
    Entry(textvariable=CostofSnacks,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=182,y=642)

    Total=StringVar()
    Label(text="Total  :",font="Cappuccino 15 bold ",bg="pink").place(x=350,y=518)
    Entry(textvariable=Total,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=435,y=518)

    Taxes=StringVar()
    Label(text="Taxes :",font="Cappuccino 15 bold ",bg="pink").place(x=350,y=578)
    Entry(textvariable=Taxes,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=435,y=578)

    Gtotal=StringVar()
    Label(text="GTotal :",font="Cappuccino 15 bold ",bg="pink").place(x=345,y=642)
    Entry(textvariable=Gtotal,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=435,y=642)

    Paid=StringVar()
    Label(text="Paid :",font="Cappuccino 15 bold ",bg="pink").place(x=620,y=518)
    Entry(textvariable=Paid,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=690,y=518)

    Return=StringVar()
    Label(text="Returned :",font="Cappuccino 15 bold ",bg="pink").place(x=575,y=578)
    Entry(textvariable=Return,font="Cappuccino 14 bold ",borderwidth=5,width=9).place(x=690,y=578)

    Button(text="Get Recipt", font="Cappuccino 14 bold ", borderwidth=5, padx=2,command=recipt).place(x=660, y=642)
    Label(text="YOUR BILL" , font="LUCIDA 18 bold", bg="yellow").place(x=1100, y=310)
    Button(text="Total",font="Cappuccino 14 bold ",borderwidth=5,padx=20,command=total).place(x=860,y=518)
    Button(text="Return", font="Cappuccino 14 bold ", borderwidth=5, padx=13,command=pay1).place(x=860, y=578)
    Button(text="Reset", font="Cappuccino 14 bold ", borderwidth=5, padx=20,command=reset).place(x=860, y=642)

    Label(text="Please Visit Again !",padx=570,bg="red",font="Cappuccino 18 bold ").place(x=0,y=705)

root.bind('<Key>',lambda i:PressAnyKey(i))
root.mainloop()