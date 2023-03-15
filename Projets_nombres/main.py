from Fonctions import *
import tkinter as tkt


class fenetres:
    #Opérations
    def __init__(self) -> None:
        pass
    def ShowAddit(self):
        Mainwin.withdraw()
        self.Additwin= tkt.Toplevel(Mainwin)
        self.Additwin.geometry("400x400")
        self.Additwin.title("Additions")
        #Bouton Retour
        tkt.Button(self.Additwin,text="Retour",command =lambda:self.showmain(self.Additwin)).pack()

        #Sauf specifié tout fonctionne avec du Binaire
        #Bouton additions 
        #sans precision
        tkt.Button(self.Additwin,text="Addition sans choix precision").pack()
        #avec precision
        tkt.Button(self.Additwin,text="Addition avec choix précision",command=mainfun.addition_avec_choix).pack()

        #Soustractions 
        #sans precision
        tkt.Button(self.Additwin,text="Soustraction sans choix precision").pack()
        #avec precision
        tkt.Button(self.Additwin,text="Soustraction avec choix precision").pack()

        #Multiplications
        #sans precision
        tkt.Button(self.Additwin,text="Multiplication sans choix precision").pack()
        #avec precision
        tkt.Button(self.Additwin,text="Multiplication avec choix precision").pack()

        #Comparaison
        tkt.Button(self.Additwin,text="Compare deux binaires").pack()

        #Addition en IEEE754
        tkt.Button(self.Additwin,text="Addition en norme 'IEEE754', double précision").pack()

                #Bouton Quitter
        tkt.Button(self.Additwin,text="Quitter",command =Mainwin.quit).pack()

    def addition_avec_choix(self):
        Additionavec = tkt.Toplevel(self.Additwin)
        Additionavec.geometry("300x190")
        Additionavec.title("Addition binaire avec Precision")
        num1 =""
        num2=""
        tkt.Entry(Additionavec,text="nombre 1",textvariable=num1).pack()
        tkt.Entry(Additionavec,text="nombre 2",textvariable=num2).pack()
        tkt.Button(Additionavec,text="Commencer",command=lambda:print(num1,num2)).pack()
    #Conversions
    def showConv(self):
        Mainwin.withdraw()
        Convwin = tkt.Toplevel(Mainwin)
        Convwin.geometry("400x700")
        Convwin.title("Additions")
        #Boutons Systeme

        #Bouton Retour
        tkt.Button(Convwin,text="Retour",command =lambda:mainfun.showmain(Convwin)).pack()

        #Conversions vers binaire
        #Decimal
        tkt.Button(Convwin,text="Conversion de décimal vers binaire").pack()
        #Hexadécimal
        tkt.Button(Convwin,text="Conversion Hexa vers Binaire").pack()
        
        #Conversions vers décimal
        #binaire
        tkt.Button(Convwin,text="Conversion binaire vers decimal").pack()
        #Hexadécimal
        tkt.Button(Convwin,text="conversion Hexa vers décimal").pack()
        #Complément à 2
            #Sans précision
        tkt.Button(Convwin,text="Conversion Comp2 vers Décimal sans précision").pack()
            #Avec précision
        tkt.Button(Convwin,text="Conversion Comp2 vers Décimal avec précision").pack()
        #Flottant
            #Sans précision
        tkt.Button(Convwin,text="Conversion flottant vers décimal sans precision").pack()
            #avec précision
        tkt.Button(Convwin,text="Conversion flottant decimal avec precision").pack()

        #Conversions depuis le Decimal
        #Hexadécimal
        tkt.Button(Convwin,text="Conversion décimal vers Hexa").pack()
        #Comp2
            #Sans précision
        tkt.Button(Convwin,text="Conversion décimal vers Conversion à 2 sans précision").pack()
            #avec précision
        tkt.Button(Convwin,text="Covnersion décimal vers Complément à 2 avec précision").pack()
        #Flottant
            #avec précision
        tkt.Button(Convwin,text="Conversion Decimal vers Flottant sans précision").pack()
            #Sans précision
        tkt.Button(Convwin,text="Conversion Décimal vers Flottant avec précision").pack()
        #IEEE
        tkt.Button(Convwin,text="Conversion décimal vers IEEE754").pack()

        #Bouton Quitter
        tkt.Button(Convwin,text="Quitter",command =Mainwin.quit).pack()


    #Retour au principal
    def showmain(self,previous:tkt.Toplevel):
        previous.destroy()
        Mainwin.deiconify()
        Mainwin.mainloop()

def begin():
    Mainwin.title("Ecritures nombres")
    Mainwin.geometry("300x100")
    tkt.Button(Mainwin,text="Conversions",command=mainfun.showConv).pack()
    tkt.Button(Mainwin,text="Opérations",command=mainfun.ShowAddit).pack()
    tkt.Button(Mainwin,text="Quitter",command=Mainwin.quit).pack()
    Mainwin.mainloop()
    
Mainwin = tkt.Tk()
mainfun = fenetres()
begin()


