# ### Girdi olarak kullanıcıdan bir karakter dizisi alan, ve frekansına göre sıkıştırma işlemi uygulayan Python kodunu yazınız.
# ### Örnek: 
# ###### Input: aaaabbcccccdefffghhhhii
# ###### Output: 4a2b5c1d1e3f1g4h2i

def zipping(st):
    result = ""
    rep = 1
    for i in range(len(st)):
        char = st[i]
        try:
            char2 = st[i+1P]
        except:
            result = result + str(rep) + char
            rep = 1
            return result
        
        if char == char2:
            rep += 1
        else:
            result = result + str(rep) + char
            rep = 1

zipping("aaaabbcccccdefffghhhhii")

