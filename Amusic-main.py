from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from variables_constantes import*
import pygame
import random
from mutagen.mp3 import MP3


pygame.mixer.init()
pygame.mixer.init(frequency=44100)
# variables de la ventana
ancho_W,alto_W = 500,1000
#creamos la ventana
ventana = Tk()
#le damos un forma predeterminada a la ventana
ventana.geometry("300x400")
ventana.config(bg="black")
ventana.resizable(0,0)

#funcion de prueba
cancion_actual=""
dire =""

def abrir_musica():
	global cancion_actual,posicion,x,dire,nombre
	posicion = 0
	x = 0
	dire = filedialog.askopenfilenames(initialdir="/home",
											title="Escoger cancion",
										filetypes=(('mp3 files', '*.mp3*'),('All files', '*.*')))
	x = len(dire)
	cancion_actual=dire[posicion]

	nombre=cancion_actual.split("/")
	nombre = cancion_actual[-1]

def play_music():
	global cancion_actual,posicion
	pygame.mixer.music.load(cancion_actual)
	pygame.mixer.music.play()
	posicion+=1
def para_musica():
	global cancion_actual,posicion
	pygame.mixer.music.pause()
def despausar():
	global cancion_actual,posicion
	pygame.mixer.music.unpause()
def seguir():
	global cancion_actual
	pygame.mixer.music.play(-1)




imagen_play=PhotoImage(file="play.png")
imagen_pausa= PhotoImage(file="pause.png")
imagen_cargar= PhotoImage(file="carga.png")
imagen_unpause=PhotoImage(file="imagen_unpause.png")
imagen= PhotoImage(file="monika.chr")

boton_cargar=Button(ventana,image=imagen_cargar, width=56, height=56,highlightbackground ="black", padx=0,pady=1,bg="black",relief="flat",command=lambda:abrir_musica()).place(x=10,y=20)
boton_play=Button(ventana,image= imagen_play,width=60, height=60,highlightbackground ="black", padx=0,pady=1,bg="black",relief="flat",command=lambda:play_music()).place(x=115,y=300)
boton_pause=Button(ventana,image= imagen_pausa,width=60, height=60,highlightbackground ="black", padx=0,pady=1,bg="black",relief="flat",command=lambda:para_musica()).place(x=50,y=300)
boton_despausar=Button(ventana,image= imagen_unpause,width=60, height=60,highlightbackground ="black", padx=0,pady=1,bg="black",relief="flat",command=lambda:despausar()).place(x=180,y=300)

foto= Label(ventana,image=imagen).place(x=150,y=150)











#colocamos el nombre que tendra la ventana 
ventana.title("Amusic")
ventana.mainloop()
