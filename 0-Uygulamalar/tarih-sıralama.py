# ### Girdi olarak, “gün.ay.yıl” şeklinde tarihler olan bir liste alıp, bu tarihleri en yeniden, en eski olana doğru sıralayıp çıktı olarak veren kodu yazınız.
# #### Input: dates = [“20.05.1960”, “11.09.2004”, “02.03.1989”]
# #### Output: dates = [“11.09.2004”, “02.03.1989”, “20.05.1960”]

def date_sorter(dates):
    temp = []
    for date in dates:
        gun, ay, yil = date.split(".")
        new_format_date = ".".join([yil, ay, gun])
        temp.append(new_format_date)
    
    temp.sort(reverse=True)
    result = []
    for date in temp:
        yil, ay, gun = date.split(".")
        new_format = ".".join([gun, ay, yil])
        result.append(new_format)
    
    
    return result

date_sorter(["20.05.1960", "11.09.2004", "02.03.1989", "19.03.1989"])

