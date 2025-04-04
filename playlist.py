#!/bin/bash/python3

from bs4 import BeautifulSoup

version = 0.5

title = "Playlist v"+str(version)


print (title)

print ("-"*len(title))


#xml_ejemplo = '<personaje><nombre>Jacinto</nombre><edad valor="33"/></personaje>'

#personaje = BeautifulSoup(xml_ejemplo, 'xml')

#print (personaje.prettify())

#nombre = (personaje.nombre)


#print(nombre.text)

songs_xml_file = open("songs/song.xml", "r")

song_xml = songs_xml_file.read()

#print (song_xml)

song = BeautifulSoup(song_xml, 'xml')

print (song.title.text)
print (int(song.duration["seconds"])/60)
for artists in song.artists.find("artista"):
	print (artists.text)
