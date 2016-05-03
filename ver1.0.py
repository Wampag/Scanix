#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import subprocess

app = Tk()
app.title("Scanix")

def hacer_click():
	try:
		pass
	except Exception, e:
		raise e

#Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

boton1 = Button(vp, text="Direccion Eth")
boton1.grid(column=1, row=1, sticky=(W,E))
valor1 = ""
entrada_texto1 = Entry(vp, width=10, textvariable=valor1)
entrada_texto1.grid(column=2, row=1)

valor2 = ""
boton2 = Button(vp, text="Direccion Wlan")
boton2.grid(column=1, row=2, sticky=(W,E))
entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
entrada_texto2.grid(column=2, row=2)

app.mainloop()

#CURRENT_IP=''
#for INTERFACE in wlan0 eth0; do
#    if [ -z $CURRENT_IP ]; then
#        CURRENT_IP=$(ip addr show dev $INTERFACE | grep "inet " | head -1 | awk '{ print $2 }')
#    fi
#done
