osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje sorumlusu"

print("osman : ",osman)
print("mehmet : ",mehmet,end = "\n\n")

osman, mehmet = mehmet, osman

print("osman : ",osman)
print("mehmet : ",mehmet,end = "\n\n")

##############################################
osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje sorumlusu"
geçici = "Proje Sorumlusu"

print("osman : ",osman)
print("mehmet : ",mehmet,end = "\n\n")

mehmet = osman 

print("osman : ",osman)
print("mehmet : ",mehmet,end = "\n\n")


osman = geçici

print("osman : ",osman)
print("mehmet : ",mehmet)
