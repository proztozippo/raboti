import webbrowser

#как я понял, практика 1 - это то, что некоторые генерили, а некоторые написали
#я его для себя создавал, когда экспеементировал с вебсайтами

#открытие вебсайта с книгами

print("выбор книги: ")
print("1 - пуля квант", "2 - выбор оружия", "3 - слепое пятно", "4 - череп мутанта", "5 - сердце зоны", "6 - мгла", "7 - тропами мутантов", "8 - трое против зоны", sep = "\n")
while True:
       a = int(input())
       brow =("",
              "https://royallib.com/read/bobl_aleksey/pulya_kvant.html#NaN",
              "https://royallib.com/read/levitskiy_andrey/vibor_orugiya.html#0",
              "https://royallib.com/read/nochkin_viktor/slepoe_pyatno.html#0"
              "https://royallib.com/read/nochkin_viktor/cherep_mutanta.html#0"
              "https://royallib.com/read/levitskiy_andrey/serdtse_zoni.html#0"
              "https://royallib.com/read/levitskiy_andrey/saga_smerti_mgla.html#0"
              "https://royallib.com/read/levitskiy_andrey/ya__stalker_tropami_mutantov.html#0"
              "https://royallib.com/read/levitskiy_andrey/troe_protiv_zoni.html#0"
              )
       webbrowser.open_new_tab(brow[a])