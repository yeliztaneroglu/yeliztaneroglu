# -*- coding: utf-8 -*-
def eposta():
    return "size eposta ile ulaşılacak"
def mektup():
    return "size mektup ile ulaşılacak"
def web():
    return "size web yolu ile ulaşılacak"
def cikis():
    return "çıkış yapıldı"
okunan=" "
while okunan <>'C':
    print "size hangi yolla bildirimde bulunulsun?"
    print "[E]posta,[M]ektup,[W]eb,[C]ıkıs"
    okunan=raw_input()
    menu={"E":eposta, "M":mektup,"W":web,"C":cikis}
    print menu[okunan]()
    
