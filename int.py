from customtkinter import CTk, CTkButton, CTkLabel, CTkToplevel, set_appearance_mode
from customtkinter import filedialog

def ouvrir_repertoire():
    filedialog.askdirectory()

def nouvelle_fenetre():
    nouvelle = CTkToplevel(app)
    nouvelle.geometry("1080x1080")
    nouvelle.title("Séparation")
    imp = CTkButton(master=nouvelle, text="Importer", corner_radius=32, width=300, height=60, text_color="white")
    imp.place(relx=0.4, rely=0.4, anchor="center")

app = CTk()
app.geometry("1080x1080")
app.title("Zarafeo")
set_appearance_mode("white")

btn = CTkButton(master=app, text="Karaoke", corner_radius=32, fg_color="#059C02", hover_color="#C850C0", command=ouvrir_repertoire, width=250, height=50, text_color="white", font=("courier", 20))
btn1 = CTkButton(master=app, text="Séparation", corner_radius=32, fg_color="#059C02", width=250, height=50, text_color="white", command=nouvelle_fenetre, font=("courier", 20))
btn.place(relx=0.66, rely=0.4, anchor="center")
btn1.place(relx=0.33, rely=0.4, anchor="center")

titre = CTkLabel(master=app, text="Bienvenue sur Zarafeo", font=("Poppins", 70))
titre.place(relx=0.5, rely=0.1, anchor="center")

soratra = CTkLabel(master=app, text="Séparation Vocal & Instrumental + Karaoke", font=("poppins", 12), text_color="#8C53FF")
soratra.place(relx=0.36, rely=0.7)

app.mainloop()
