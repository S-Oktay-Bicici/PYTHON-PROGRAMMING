
def sabah(isim):
	print("günaydın",isim)
sabah("oktay")

###################################################################

def sabah(isim):
	print("günaydın",isim)
sabah("oktay")
gündüz = sabah
gündüz("sadık")

####################################################################

def sabah(isim):
	def akşam(isim):
		print("İyi akşamlar",isim)
	print("Günaydın",isim)
	akşam("sadık")
sabah("oktay")

###################################################################

def sabah(isim):
	def akşam(isim):
		print("İyi akşamlar",isim)
	print("Günaydın",isim)
akşam("sadık")
sabah("oktay")
