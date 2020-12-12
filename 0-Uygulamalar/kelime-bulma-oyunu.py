# ## Kelime Bulma Oyunu
# ### Kullanıcı, n harften oluşan ve ******** şeklinde gösterilen bir kelimeden bazı harfler tahmin etmeye çalışacak. 
# ### Doğru tahmin ettiği harf açılacak ve örneğin, *e***e** şeklinde görünecek. 
# ### Toplamda 10 tane yanlış tahmin etme hakkı olacak. 
# ### Yanlış tahmin ettiği her harf için hakları birer birer azalacak. 
# ### Kelimeyi direkt tahmin etmek isterse kelimenin tamamını yazacak. 
# ### Doğru tahmin ettiği zaman, kalan hak * 10 puan alacaktır.


def list_to_dict():
    
    kelime_listesi = ["armut", "avize", "baraj", "banka", "bıçak", "ceviz", "çorap",
                  "kalem", "silgi", "kitap", "makas", "perde", "çiçek", "saksı", 
                  "toprak", "arslan", "mendil", "defter", "klavye", "mantar", 
                  "adaptör", "agresif", "biberon", "çingene", "eğitmen", 
                  "harmoni", "belgesel", "çikolata", "diyagram", "istanbul", 
                  "kimyasal", "lacivert", "maksimum", "pankreas", "telaffuz"]
    
    word_dict = {}
    for word in kelime_listesi:
        l = len(word)
        if l in word_dict:
            word_dict[l].append(word)
        else:
            word_dict[l] = [word]
            
    return word_dict


def find_in_word(char, word, starred):
    flag = False
    temp = ""
    for i in range(len(word)):
        if char == word[i]:
            temp += char
            flag = True
        else:
            temp += starred[i]
            
    return (temp, flag)


import random

word_dict = list_to_dict()
        
answer = int(input("Kaç harfli kelime tahmin etmek istersiniz? (5-6-7-8)"))
words_guessed = word_dict[answer]
idx = random.randint(0, len(words_guessed)-1)
word = words_guessed[idx]
starred = "*"*len(word)

kalan_hak = 10
old_chars = []

while kalan_hak > 0:
    print(starred, "Kalan hakkınız:", kalan_hak)
    char = input("Bir harf veya kelimenin tamamı: ")
    if char not in old_chars:
        if len(char) == 1:
            starred, flag = find_in_word(char, word, starred)
            if not flag:
                kalan_hak -= 1
                print("Yanlış tahmin") 
            else:
                if starred == word:
                    print("Tebrikler kazandınız!")
                    print(word, word)
                    break

        else:
            if char == word:
                print("Tebrikler kazandınız!")
                print(word, word)
                print("Puanınız", kalan_hak*10)
                break
            else:
                kalan_hak -= 1
                print("Yanlış tahmin")
    
        old_chars.append(char)
    
    else:
        print(char, "daha önce tahmin edildi")

