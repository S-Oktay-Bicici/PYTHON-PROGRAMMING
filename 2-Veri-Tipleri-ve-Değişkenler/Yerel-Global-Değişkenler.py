
def yerel():
	a = 5
	print(a)
yerel()

########################################################################

def yerel():
	a = 5
	print(a)
yerel()
print(a)

#########################################################################

a = 10
def yerel():
	a = 5
	print(a)
yerel()
print(a)

#########################################################################

def fonksiyon():
	global c
	c = 5
	print(c)
fonksiyon()
print(c)

########################################################################

c = 10
def fonksiyon():
	global c
	c = 5
	print(c)
fonksiyon()
print(c)

#######################################################################

c = 10
def fonksiyon():
	global c
	c = 5
	print(c)
fonksiyon()
c = 15
print(c)

#######################################################################

if True:
	a = 10
	print(a)
print(a)

while True:
	b = 10
	print(b)
	break
print(b)

#if ve while bloklarında değerler global olur
