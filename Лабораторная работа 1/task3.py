# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
onesymbol = 4
onebook = pages*lines*symbols*onesymbol
diskette = 1.44*1024*1024
amount = (round(diskette // onebook))
print("Количество книг, помещающихся на дискету:", amount)