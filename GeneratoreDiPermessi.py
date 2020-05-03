
import tkinter as tk
from tkinter import ttk
from random import randint
import pymsgbox

root = tk.Tk()

combotext = tk.StringVar()
combotext.set('Scegli la regione')

box = ttk.Combobox(root, textvariable=combotext, state='readonly')
box.pack()
box['values'] = (
    ' Abruzzo '
    ' Basilicata '
    ' Calabria '
    ' Campania '
    ' Emilia Romagna '
    ' Friuli-Venezia-Giulia '
    ' Lazio '
    ' Liguria '
    ' Lombardia '
    ' Marche '
    ' Molise '
    ' Piemonte '
    ' Puglia '
    ' Sardegna '
    ' Sicilia '
    ' Toscana '
    ' Trentino-Alto-Adige '
    ' Umbria '
    ' Val-d-Aosta '
    ' Veneto '
) 

def callback_function(event):
	regionescelta=combotext.get()
	print(regionescelta)
	return regionescelta
#regione=combotext.get()
regione=root.bind('<<ComboboxSelected>>', callback_function)
root.mainloop()

def visita():
	root = tk.Tk()

	combotext = tk.StringVar()
	combotext.set('Scegli il parente')

	box = ttk.Combobox(root, textvariable=combotext, state='readonly')
	box.pack()
	box['values'] = (
		' Genitore '
		' Figlio '
		' Cugino_della_suocera_da_parte_di_madre '
		' Nipote '
		' Figlio_del_genitore_separato '
		' Cugino_di_3_grado_da_parte_della_madre_acquisita ')
	root.mainloop()

def callback_function(event):
	ragionescelta=combotext.get()
	if ragionescelta=='Visita-parenti':
		possibile=visita()


root = tk.Tk()

combotext = tk.StringVar()
combotext.set('Scegli la motivazione')

box = ttk.Combobox(root, textvariable=combotext, state='readonly')
box.pack()
box['values'] = (
    ' Lavoro '
    ' Grigliata '
    ' Visita-parenti '
    ' Visita-amici '
    ' Ritorno-alla-residenza '
    ' Visita-cimiteri '
    ' Acquisti-al-supermercato '
) 


#regione=combotext.get()
ragione=root.bind('<<ComboboxSelected>>', callback_function)
root.mainloop()


rand=randint(0,7)
if rand==0:
	testo=" Stai a casa!"
elif rand==1:
	testo=" Certo!"
elif rand==2:
	testo="Solo se accompagnato da De Luca col lanciafiamme"
elif rand==3:
	testo="Solo per mezz'ora, il terzo mercoledì dei mesi dispari"
elif rand==4:
	testo="Nel caso in cui tu possa tornare camminando su un piede solo"
elif rand==5:	
	testo="Tarapìa tapiòco! Prematurata la supercazzola, o scherziamo?"
elif rand==6:	
	testo="	Ma allora io le potrei dire, anche con il rispetto per l'autorità, che anche soltanto le due cose come vicesindaco"
elif rand==7:	
	testo="	Pàstene soppaltate secondo l'articolo 12, abbia pazienza, sennò posterdati, per due, anche un pochino antani in prefettura"

pymsgbox.alert(testo)






