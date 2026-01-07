from tkinter import messagebox
import requests
import tkinter as tk
from PIL import Image,ImageTk,ImageFilter
key_api="264df1f720ee238622dcc4899c5854b2"
target_url="https://api.openweathermap.org/data/2.5/weather"
ekran=tk.Tk()
title=ekran.title("hava durumu")
ekran.geometry("300x400")
havadurumu=tk.Label(ekran,text="")
bg_label=tk.Label(ekran)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
bg_label.lower()
panel=tk.Frame(ekran,bg="white")
panel.place(x=15,y=15,width=270,height=130)
panel.place(x=15,y=15,width=270,height=130)
panel.lift()
#hava_resimleri={"01":"acık.jpg","02":"azbulutlu.jpg","03":"bulutlu.jpg","09":"yağmur.jpg","13":"kar.jpg"}
def arkaplan_resimleri(icon):
    kod=icon[0:2]
    if kod=="01":
        dosya="acık.jpg"
    elif kod=="02":
        dosya="azbulutlu.jpg"
    elif kod=="04":
        dosya="bulutlu.jpg"
    elif kod=="09":
        dosya="yagmur.jpg"
    elif kod=="13":
        dosya="kar.jpg"
    else:
        dosya="acık.jpg"
    ekran.update_idletasks()
    w,h=ekran.winfo_width(),ekran.winfo_height()
    resim=ImageTk.PhotoImage(Image.open(dosya).resize((w,h)).filter(ImageFilter.GaussianBlur(7)))
    bg_label.config(image=resim)
    bg_label.image=resim
    ekran.update()

panel=tk.Frame(ekran,bg="white")
panel.place(x=15,y=15,width=270,height=130)
etiket=tk.Label(ekran,text="LÜTFEN ŞEHİR ADI GİRİNİZ :",bg="white",font="Arial 12 bold")
etiket.place(x=20,y=20)
entry1=tk.Entry(panel,font="Arial 12 bold")
entry1.place(x=10,y=45,width=160,height=28)
def wheather():
    sehir = entry1.get().strip()
    if not sehir:
        messagebox.showerror("HATA","lütfen şehir giriniz")
        return
    params = {"q": sehir, "appid": key_api, "units": "metric", "lang": "tr"}
    response = requests.get(target_url, params=params)
    x = response.json()
    if str(x.get("cod"))!="200":
        messagebox.showerror("HATA","Şehir bulunamadı!!")
        return
    description = x["weather"][0]["description"]
    sıcaklik = x["main"]["temp"]
    icon = x["weather"][0]["icon"]
    arkaplan_resimleri(icon)
    havadurumu.config(text=f'sıcaklık : {sıcaklik} \u00B0C\nhava : {description}',font="Arial 12 bold",bg="white")
    havadurumu.place(x=70,y=150)
    entry1.delete(0, tk.END)

buton=tk.Button(ekran,text="göster",command=wheather,width=10,height=1)
buton.place(x=200,y=56)
arkaplan_resimleri("01d")
ekran.mainloop()
