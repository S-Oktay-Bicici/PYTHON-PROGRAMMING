# ### Saniyeyi, saat-dakika-saniye formatına dönüştüren kodu yazın

def time_formatter(seconds):
    
    mod = seconds % 3600
    hours = (seconds - mod)/3600
    mod2 = mod % 60
    mins = (mod-mod2)/60
    print(int(hours), "saat, ", int(mins), "dakika, ", mod2, "saniye")

time_formatter(7300)

def time_formatter_2(seconds):
    
    hours, rem = divmod(seconds, 3600)
    minute, rem2 = divmod(rem, 60)
    print(hours, "saat, ", minute, "dakika, ", rem2, "saniye")

time_formatter_2(7300)

