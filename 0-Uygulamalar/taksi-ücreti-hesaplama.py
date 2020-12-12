# ### Taksi ücretini 4 TL başlangıç ve KM başına 0.3 TL olacak şekilde hesaplayan fonksiyonu yazın

def trip_cost(km):
    start = 4
    total = start + km*0.3
    return total

cst = trip_cost(26)
print(cst)

