from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from variables_constantes import*
import pygame
import random
from mutagen.mp3 import MP3
import os


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
#controlador de pausa binario
binario = 0

#funcion de prueba

playlist =[]
posicion = 0

def abrir_musica():
	global playlist
	
	carpeta = filedialog.askdirectory(title= "busca canciones", )

	if carpeta :
		canciones = []

		for nombre_cancion in os.listdir(carpeta):
			ruta_music = os.path.join(carpeta, nombre_cancion)
			if os.path.isfile(ruta_music):
				canciones.append(ruta_music)
		
	playlist = canciones

	return playlist


def pasar_music():
	global posicion
	posicion +=1
	return posicion

def play_music():
	global playlist, posicion
	pygame.mixer.music.load(playlist[posicion])
	pygame.mixer.music.play()
	pygame.mixer.music.play()





	




imagen_play=PhotoImage(file="play.png")
imagen_pausa= PhotoImage(file="pause.png")
imagen_cargar= PhotoImage(file="carga.png")


boton_cargar=Button(ventana,image=imagen_cargar, width=56, height=56,highlightbackground ="black", padx=0,pady=1,bg="black",relief="flat",command=lambda:abrir_musica()).place(x=10,y=20)
boton_play=Button(ventana,image= imagen_play,width=60, height=60,highlightbackground ="black", padx=0,pady=1,bg="black",relief="flat",command=lambda:play_music()).place(x=115,y=300)
boton_pause=Button(ventana,image= imagen_pausa,width=60, height=60,highlightbackground ="black", padx=0,pady=1,bg="black",relief="flat",command=lambda:pasar_music()).place(x=50,y=300)





#colocamos el nombre que tendra la ventana 
ventana.title("Amusic")
ventana.mainloop()
