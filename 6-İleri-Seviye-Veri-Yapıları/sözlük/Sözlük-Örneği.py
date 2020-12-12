
sözlük = {"home" : "ev",
          "pen"  : "kalem",
          "book" : "kitap"}

print(sözlük)
print(sözlük["book"])

########################################################################

karakter = {"ad" : "oktay",
            "güç" : 80,
            "silah": "kılıç",
            "can" : 100}

karakter2 = {"ad" : "karakter2",
             "güç": "40",
             "silah": "kılıç",
             "can" : 100}            
            
print("Karakterin adı : {}".format(karakter["ad"]))
print("Karakterin gücü : {}".format(karakter["güç"]))
print("Karakterin silahı : {}".format(karakter["silah"]))
print("Karakterin canı : {}".format(karakter["can"]))

def vur(vuran:dict,vurulan:dict):
		eksilen = vuran["güç"]
		vurulan["can"] = vurulan["can"] - eksilen

vur(karakter,karakter2)
vur(karakter2,karakter)

print("Karakter 1 canı : ",karakter["can"])
print("Karakter 2 canı : ",karakter2["can"])

#####################################################################3

sözlük = {"pazartesi":1,
			 "salı":2,
			 "çarşamba":3,
			 "perşembe":4,
			 "cuma":5,}
print(sözlük)

#########################################################################

sözlük = {"pazartesi":1,
			 "salı":2,
			 "çarşamba":3,
			 "perşembe":4,
			 "cuma":5,}
print(sözlük["çarşamba"])

######################################################################

sözlük = {"pazartesi":1,
			 "salı":2,
			 "çarşamba":3,
			 "perşembe":4,
			 "cuma":5,}
print(sözlük[2])

#######################################################################

sözlük = {"pazartesi":1,
			 "salı":2,
			 "aylar":["ocak","şubat","mart","nisan"],
			 "çarşamba":3
			 "perşembe":4,
			 "cuma":5,}
print(sözlük)

#########################################################################

sözlük = {"pazartesi":1,
			 "salı":2,
			 "aylar":["ocak","şubat","mart","nisan"],
			 "çarşamba":3
			 "perşembe":4,
			 "cuma":5,}
print(sözlük["aylar"])

##########################################################################

sözlük = {"pazartesi":1,
			 "salı":2,
			 "aylar":["ocak","şubat","mart","nisan"],
			 "çarşamba":3
			 "perşembe":4,
			 "cuma":5,}
print(sözlük["aylar"][2])

##########################################################################

sözlük = {"pazartesi":1,
			 "salı":2,
			 "aylar":["ocak","şubat","mart","nisan"],
			 "çarşamba":3
			 "perşembe":4,
			 "cuma":5,}
print(sözlük["aylar"][2][2])

##########################################################################
