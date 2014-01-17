import random
import datetime


def my_view(request):
    return {'project':'newproject'}
    
def home_view( request ):
    return {"project":"gapp1",
			"missatge": "Hem dic Sergi",
			"nombres": [1,2,3,4,5,6,7,8,9]}
			
def zodiac_view( request ):
	return {"fotos_tots":"zodiac_signes.jpg",
			"missatge": "Llista de tots els signes:"}
			
def consulta_view( request ):
	if request.method=="POST":
	
		dia = int(request.POST.get("select1"))
		mes = int(request.POST.get("select2"))
		an = int(request.POST.get("any"))
		
		missatge = ["Te estara rigiendo y con la que podras ser todo lo que deseas. Escribelo en un papel y no dejes de repetirla en todo momento.", 
		"La sugerencia del Prodigio es que no te quejes de nada, al contrario, haz enfasis en todas las cosas que te rodean.", 
		"La sugerencia del Prodigio es que no te quejes de nada, al contrario, haz enfasis en todas las cosas que te rodean.", 
		"La sugerencia del Prodigio es que no te quejes de nada, al contrario, haz enfasis en todas las cosas que te rodean.", 
		"No pongas limites ni barreras en tus proyectos y acciones, al contrario, siempre trata de luchar por ellos.", 
		"Debes hacerlo con todas las cosas que puedes lograr en tu vida, con cada uno de los aspectos que te rodean y siempre tratando de atraer todo lo bueno.", 
		"Usala en todos los aspectos que tengan que ver con el hogar y el amor.", 
		"Pide que haya paz, abundancia, felicidad, amor, que la suerte te rodee y toda la buena vibra este siempre contigo y con los que te rodean.", 
		"Una manera de encontrar soluciones a tus problemas y mejorar las condiciones que te rodean.", 
		"Aprovecha todas tus habilidades y capacidades, y trata de sacarles el mejor provecho posible.", 
		"Debes aprender a perdonar y olvidar situaciones dolorosas.", 
		"Enfocala a todas esas cosas que dejaste inconclusas y quieres volver a retomar, recuerda que nunca es tarde para empezar."]
		
		aleatori = random.randint(0,11)
		
		


		z = datetime.date(an,mes,dia)

		Aries_p = datetime.date(z.year,3,21)
		Aries_f = datetime.date(z.year,4,20)
		Taure_p = datetime.date(z.year,4,21)
		Taure_f = datetime.date(z.year,5,21)
		Geminis_p = datetime.date(z.year,5,22)
		Geminis_f = datetime.date(z.year,6,21)
		Cancer_p = datetime.date(z.year,6,22)
		Cancer_f = datetime.date(z.year,7,22)
		Lleo_p = datetime.date(z.year,7,23)
		Lleo_f = datetime.date(z.year,8,22)
		Verge_p = datetime.date(z.year,8,23)
		Verge_f = datetime.date(z.year,9,22)
		Libra_p = datetime.date(z.year,8,23)
		Libra_f = datetime.date(z.year,9,22)
		Escorpi_p = datetime.date(z.year,10,23)
		Escorpi_f = datetime.date(z.year,11,22)
		Sagitari_p = datetime.date(z.year,11,23)
		Sagitari_f = datetime.date(z.year,12,21)
		Capricorni_p = datetime.date(z.year,12,22)
		Capricorni_f = datetime.date(z.year,1,20)
		Acuari_p = datetime.date(z.year,1,21)
		Acuari_f = datetime.date(z.year,2,19)
		Picis_p = datetime.date(z.year,2,20)
		Picis_f = datetime.date(z.year,3,20)

		if z >= Aries_p and z <= Aries_f:
			zodiac = "ARIES"

		elif z >= Taure_p and z <= Taure_f:
			zodiac = "TAURE"

		elif z >= Geminis_p and z <= Geminis_f:
			zodiac = "GEMINIS"

		elif z >= Cancer_p and z <= Cancer_f:
			zodiac = "CANCER"

		elif z >= Lleo_p and z <= Lleo_f:
			zodiac = "LLEO"

		elif z >= Verge_p and z <= Verge_f:
			zodiac = "VERGE"

		elif z >= Libra_p and z <= Libra_f:
			zodiac = "LIBRA"

		elif z >= Escorpi_p and z <= Escorpi_f:
			zodiac = "ESCORPI"

		elif z >= Sagitari_p and z <= Sagitari_f:
			zodiac = "SAGITARI"

		elif z >= Acuari_p and z <= Acuari_f:
			zodiac = "ACUARI"

		elif z >= Picis_p and z <= Picis_f:
			zodiac = "PICIS"

		else:
			zodiac = "CAPRICORNI"
	
	#Em falta aconseguir que surtin les fotos i el nom del signe en relacio del mes 
		
	#	fotos = ["","","","","",""]
	#	mes = []
	#	signe = ["","","","","",""]
		
		
		return {"dia":dia,
				"mes":mes,
				"zodiac":zodiac,
				"missatge":missatge[aleatori]}
			
	return {"dia":"",
			"mes":"",
			"zodiac":"",
			"missatge":""}
				
	

