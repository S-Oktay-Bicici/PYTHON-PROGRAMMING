#####################################################################

a = "sadık oktay biçici"

#string içerisinde aranan karakterin kaçıncı sırada olduğunu bulmamıza yarar
#soldan sağa arama yapar
print(a.find("ı"))

#istedğimiz aralıkda aramak istersek
print(a.find("t",2,14))

#####################################################################

a = "sadık oktay biçici"

#find methodunun tersi olarak sağdan sola doğru okur
print(a.rfind("t"))

#####################################################################
