from Fonctions import *
import tkinter as tkt


class fenetres:
    #Opérations


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
        tkt.Button(self.Additwin,text="Addition sans choix precision",command=lambda:self.callfunction(2,addany)).pack()
        #avec precision
        tkt.Button(self.Additwin,text="Addition avec choix précision",command=lambda:self.callfunction(3,addfix)).pack()

        #Soustractions 
        #sans precision
        tkt.Button(self.Additwin,text="Soustraction sans choix precision",command=lambda:self.callfunction(2,subany)).pack()
        #avec precision
        tkt.Button(self.Additwin,text="Soustraction avec choix precision",command=lambda:self.callfunction(3,subfix)).pack()

        #Multiplications
        #sans precision
        tkt.Button(self.Additwin,text="Multiplication sans choix precision",command=lambda:self.callfunction(2,multipleany)).pack()
        #avec precision
        tkt.Button(self.Additwin,text="Multiplication avec choix precision",command=lambda:self.callfunction(3,multiplefix)).pack()

        #Comparaison
        tkt.Button(self.Additwin,text="Compare deux binaires",command=lambda:self.callfunction(2,comparebin)).pack()

        #Addition en IEEE754
        tkt.Button(self.Additwin,text="Addition en norme 'IEEE754', double précision",command=lambda:self.callfunction(2,addieee754doublepre)).pack()

        #Soustraction en IEEE754
        tkt.Button(self.Additwin,text="Soustraction en norme 'IEEE754",command = lambda:self.callfunction(2,subieedoublepré)).pack()

                #Bouton Quitter
        tkt.Button(self.Additwin,text="Quitter",command =Mainwin.quit).pack()

    #fonction pour créer les fenêtres 
    def callfunction(self,argnum,functionname):
        Currentwin = tkt.Toplevel(Mainwin)
        Currentwin.geometry("300x200")
        Currentwin.title("Function")
        num1 = tkt.Entry(Currentwin)
        num1.pack()
        if argnum==2:
            num2=tkt.Entry(Currentwin)
            num2.pack()
            tkt.Button(Currentwin,text="Commencer",command=lambda:tkt.Label(Currentwin,text=functionname(num1.get(),num2.get())).pack()).pack()
        elif argnum==3:
            num2=tkt.Entry(Currentwin)
            num2.pack()
            precision=tkt.Entry(Currentwin)
            precision.pack()
            tkt.Button(Currentwin,text="Commencer",command=lambda:tkt.Label(Currentwin,text=functionname(num1.get(),num2.get(),precision.get())).pack()).pack()
        elif argnum ==1:
            tkt.Button(Currentwin,text="Commencer",command=lambda:tkt.Label(Currentwin,text=functionname(num1.get())).pack()).pack()

    #Conversions
    def showConv(self):
        Mainwin.withdraw()
        Convwin = tkt.Toplevel(Mainwin)
        Convwin.geometry("400x700")
        Convwin.title("Additions")
        #Boutons Systeme
        #Bouton Retour
        tkt.Button(Convwin,text="Retour",command =lambda:mainfun.showmain(Convwin)).pack()

        tkt.Button(Convwin,text="Conversion binaire vers hexadécimale",command=lambda:self.callfunction(1,bintohex)).pack()
        tkt.Button(Convwin,text="Conversion de base B1 vers base b2",command=lambda:self.callfunction(3,b1b2)).pack()
        #Conversions vers binaire
        #Decimal
        tkt.Button(Convwin,text="Conversion de décimal vers binaire",command=lambda:self.callfunction(1,dectobin)).pack()
        #Hexadécimal
        tkt.Button(Convwin,text="Conversion Hexa vers Binaire",command=lambda:self.callfunction(1,hextobin)).pack()
        
        #Conversions vers décimal
        #binaire
        tkt.Button(Convwin,text="Conversion binaire vers decimal",command=lambda:self.callfunction(1,bintodec)).pack()
        #Hexadécimal
        tkt.Button(Convwin,text="conversion Hexa vers décimal",command=lambda:self.callfunction(1,hextodec)).pack()
        #Complément à 2
            #Sans précision
        tkt.Button(Convwin,text="Conversion Comp2 vers Décimal sans précision",command=lambda:self.callfunction(1,comp2decany)).pack()
            #Avec précision
        tkt.Button(Convwin,text="Conversion Comp2 vers Décimal avec précision",command=lambda:self.callfunction(2,comp2decfix)).pack()
        #Flottant
            #Sans précision
        tkt.Button(Convwin,text="Conversion flottant vers décimal sans precision",command=lambda:self.callfunction(1,floattodecany)).pack()
            #avec précision
        tkt.Button(Convwin,text="Conversion flottant decimal avec precision",command=lambda:self.callfunction(2,floattodecfix)).pack()

        #Conversions depuis le Decimal
        #Hexadécimal
        tkt.Button(Convwin,text="Conversion décimal vers Hexa",command=lambda:self.callfunction(1,dectohex)).pack()
        #Comp2
            #Sans précision
        tkt.Button(Convwin,text="Conversion décimal vers Conversion à 2 sans précision",command=lambda:self.callfunction(1,deccomp2any)).pack()
            #avec précision
        tkt.Button(Convwin,text="Covnersion décimal vers Complément à 2 avec précision",command=lambda:self.callfunction(2,deccomp2fix)).pack()
        #Flottant
            #avec précision
        tkt.Button(Convwin,text="Conversion Decimal vers Flottant sans précision",command=lambda:self.callfunction(2,dectofloatfix)).pack()
            #Sans précision
        tkt.Button(Convwin,text="Conversion Décimal vers Flottant avec précision",command=lambda:self.callfunction(1,dectofloatany)).pack()
        #IEEE
        tkt.Button(Convwin,text="Conversion décimal vers IEEE754",command=lambda:self.callfunction(2,dectoieee754)).pack()

        tkt.Button(Convwin,text="Conversion IEEE754 vers décimal",command=lambda:self.callfunction(2,ieeetodec)).pack()
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