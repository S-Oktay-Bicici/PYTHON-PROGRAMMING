
demet = ("ocak","şubat",29,"mart")
print(demet)
print(type(demet))

#################################################################

demet = "ocak"
print(type(demet))

demet = "ocak",
print(type(demet))

####################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet[2])

######################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet[2:9])

#####################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet[1:12:3])

#####################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet[1:])

####################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet[:2])

########################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet[::2])

########################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet[::-1])

######################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet.index("haziran"))

###################################################################

demet = ("ocak","şubat","mart","nisan","mayıs","haziran",
         "temmuz","ağustos","eylül","ekim","kasım","aralık")
print(demet.count("ocak"))

#####################################################################
