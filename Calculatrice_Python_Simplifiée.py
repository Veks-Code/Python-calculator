from tkinter import *

class Calculatrice(Tk) :
    def __init__(self):
        super().__init__()
        self.ecran_var = StringVar()
        self.ecran_var.set("")  # Texte de départ vide


        #Création une fenêtre 
        self.title("Calculatrice Python", )
        self.minsize(250,300)
        self.resizable(width=False, height=False)
        self.configure(bg="lightcyan")
        self.wm_attributes("-topmost", True)

        #Configuration de la grille
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        #Création des variables
        self.nombre1 = ""
        self.nombre2 = ""
        self.operateur = ""

        #Définition du style des boutons
        default_button_grid = {"padx": 2, "pady": 2, "sticky": NSEW}

        #Première ligne(seulement l'écran)
        screen = Button(self, textvariable=self.ecran_var,relief=RIDGE, bg="whitesmoke")
        screen.grid(row=0, column=0, columnspan=4, **default_button_grid)


        #Deuxième ligne(les touches de AC à -)
        ac = Button(self, text="AC", command=self.touch_AC_push,bg="orange")
        ac.grid(row=1, column=0, **default_button_grid)

        divise = Button(self, text="/", command=self.touch_divise_push)
        divise.grid(row=1, column=1, **default_button_grid)

        multiplie = Button(self, text="*", command=self.touch_multiplie_push)
        multiplie.grid(row=1, column=2, **default_button_grid)

        subtract = Button(self, text="-", command=self.touch_subtract_push)
        subtract.grid(row=1, column=3, **default_button_grid)


        #Troisième ligne(les touches de 7 à +)
        _7 = Button(self, text="7", command=self.touch_7_push)
        _7.grid(row=2, column=0, **default_button_grid)

        _8 = Button(self, text="8", command=self.touch_8_push)
        _8.grid(row=2, column=1, **default_button_grid)

        _9 = Button(self, text="9", command=self.touch_9_push)
        _9.grid(row=2, column=2, **default_button_grid)

        add = Button(self, text="+", command=self.touch_add_push)
        add.grid(row=2, column=3, rowspan=2, **default_button_grid)


        #Quatrième ligne(les touches de 4 à 6)
        _4 = Button(self, text="4", command=self.touch_4_push)
        _4.grid(row=3, column=0, **default_button_grid)

        _5 = Button(self, text="5", command=self.touch_5_push)
        _5.grid(row=3, column=1, **default_button_grid)

        _6 = Button(self, text="6", command=self.touch_6_push)
        _6.grid(row=3, column=2, **default_button_grid)


        #Cinquième ligne(les touches de 1 à Entrée)
        _1 = Button(self, text="1", command=self.touch_1_push)
        _1.grid(row=4, column=0, **default_button_grid)

        _2 = Button(self, text="2", command=self.touch_2_push)
        _2.grid(row=4, column=1, **default_button_grid)

        _3 = Button(self, text="3", command=self.touch_3_push)
        _3.grid(row=4, column=2, **default_button_grid)

        entree = Button(self, text="Entree \n =", command=self.touch_entree_push, bg="royalblue")
        entree.grid(row=4, column=3, rowspan=2, **default_button_grid)


        #Sixième ligne(les touches de 0 à virgule)
        _0 = Button(self, text="0", command=self.touch_0_push)
        _0.grid(row=5, column=0, columnspan=2, **default_button_grid)

        comma = Button(self, text=".", command=self.touch_comma_push)
        comma.grid(row=5, column=2, **default_button_grid)





    #Fonction deuxième ligne(les touches de AC à -)
    def touch_AC_push(self):
        self.operateur = ""
        self.nombre1 = ""
        self.nombre2 = ""
        self.ecran_var.set("")

    def touch_divise_push(self):
        if not self.nombre1 == "":
            self.operateur = "/"

    def touch_multiplie_push(self):
        if not self.nombre1 == "":
            self.operateur = "*"

    def touch_subtract_push(self):
        if not self.nombre1 == "":
            self.operateur = "-"


    #Fonction troisième ligne(les touches de 7 à +)
    def touch_7_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "7"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "7"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "7"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "7"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_8_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "8"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "8"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "8"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "8"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_9_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "9"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "9"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "9"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "9"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_add_push(self):
        if not self.nombre1 == "":
            self.operateur = "+"


    #Quatrième ligne(les touches de 4 à 6)
    def touch_4_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "4"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "4"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "4"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "4"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_5_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "5"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "5"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "5"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "5"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_6_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "6"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "6"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "6"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "6"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)


    #Cinquième ligne(les touches de 1 à Entrée)
    def touch_1_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "1"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "1"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "1"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "1"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_2_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "2"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "2"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "2"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "2"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_3_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "3"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre1 = "3"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre1 == "0":
                self.nombre2 += "3"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
            else:
                self.nombre2 = "3"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_entree_push(self):
        if not self.nombre1 == "" and not self.nombre2 == "" and not self.operateur == "" :
                self.nombre1 = float(self.nombre1)
                self.nombre2 = float(self.nombre2)
                if self.operateur == "+":
                    self.ecran_var.set(self.nombre1 + self.nombre2)
                elif self.operateur == "-":
                    self.ecran_var.set(self.nombre1 - self.nombre2)
                elif self.operateur == "/":
                    if self.nombre2 == 0:
                        self.ecran_var.set("Erreur maths")
                    else:
                        self.ecran_var.set(self.nombre1 / self.nombre2)
                elif self.operateur == "*":
                    self.ecran_var.set(self.nombre1 * self.nombre2)


    #Fonction sixième ligne(les touches de 0 à virgule)
    def touch_0_push(self):
        if self.operateur == "":
            if not self.nombre1 == "0":
                self.nombre1 += "0"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        else:
            if not self.nombre2 == "0":
                self.nombre2 += "0"
                self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)

    def touch_comma_push(self):
        if not self.nombre1.endswith("."):
            if not self.nombre1 == "":
                if self.operateur == "":
                    self.nombre1 += "."
                    self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)
        if not self.nombre2.endswith("."):
            if not self.nombre2 == "":
                if not self.operateur == "":
                    self.nombre2 += "."
                    self.ecran_var.set(self.nombre1 + self.operateur + self.nombre2)


window = Calculatrice()
window.mainloop()
