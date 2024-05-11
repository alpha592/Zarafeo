from customtkinter import *
from customtkinter import filedialog
import customtkinter as ctk
def ouvrir_repertoire():
    filedialog.askdirectory()
def nouvelle_fenetre():
    nouv=CTk()
    nouvelle=ctk.CTkToplevel(app)
    nouvelle.geometry("1080x1080")
    nouvelle.title("separation")
    nouvelle._raise_(app)
    imp=CTkButton(text="importer",corner_radius=32,width=300,height=60,text_color="white")
    imp.place(relx=0.4,rely=0.4,anchor="center")
app.close
app= CTk()

app.geometry("1080x1080")

set_appearance_mode("dark")
app.title("Zarafeo")
btn=CTkButton(master=app,text="karaoke",corner_radius=32,fg_color="#059C02",hover_color="#C850C0",command=ouvrir_repertoire,width=250,height=50,text_color="white",font=("courrier",20))
btn1=CTkButton(master=app,text="Separation",corner_radius=32,fg_color="#059C02",width=250,height=50,text_color="white",command=nouvelle_fenetre,font=("courrier",20))
btn.place(relx=0.66,rely=0.4,anchor="center")
btn1.place(relx=0.33,rely=0.4,anchor="center")
titre=CTkLabel(master=app,text="Bienvenue sur Zarafeo",font=("Poppins",70),)
titre.place(relx=0.5,rely=0.1,anchor="center")
soratra=CTkLabel(master=app,text="SEPARATION   VOCAL &  INSTRUMENTAL +  KARAOKE",font=("poppins",12),text_color="#8C53FF")
soratra.place(relx=0.36,rely=0.7)

#059C02
app.mainloop()