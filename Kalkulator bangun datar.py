print("KALKULATOR BANGUN DATAR")
print("="*25)
print("Silahkan Pilih Bangun Datar yang ingin di hitung : ")


while True:
    a = "Persegi"
    print("A.", a)

    b = "Persegi Panjang"
    print("B.", b)

    c = "Segitiga"
    print("C.", c)

    d = "Lingkaran"
    print("D.", d)
    bangun_datar = input("Silahkan Pilih huruf mewakili bangun datar : " )


    #SISTEM PERSEGI
    if bangun_datar == "a" or bangun_datar == "A" :
        print()
        print("="*25)
        print()
        print("Anda memilih PERSEGI")
        
        #Input data oleh user 
        sisi_Persegi = int(input("Masukan panjang sisi : "))
        #Hitungan Luas
        Luas_Persegi = sisi_Persegi**2
        #Hitungan Keliling
        Keliling_Persegi = sisi_Persegi*4
        
        #Output hitungan 
        print("Persegi tersebut memiliki LUAS sebesar", Luas_Persegi )
        print("Persegi tersebut memiliki KELILING sebesar", Keliling_Persegi )
        print("Terima kasih sudah menggunakan kalkulator 😊")
        
        
    #SISTEM PERSEGI PANJANG
    elif bangun_datar == "b" or bangun_datar == "B" :
        print()
        print("="*25)
        print()
        print("Anda memilih PERSEGI PANJANG")
        
            #Input data oleh user 
        Panjang_PP = int(input("Masukan panjang sisi : "))
        Lebar_PP = int(input("Masukan lebar sisi : "))
        #Hitungan Luas
        Luas_PP = Panjang_PP * Lebar_PP
        #Hitungan Keliling
        Keliling_PP = 2*(Panjang_PP+Lebar_PP)
        
        #Output hitungan 
        print("Persegi Panjang tersebut memiliki LUAS sebesar", Luas_PP )
        print("Persegi Panjang tersebut memiliki KELILING sebesar",Keliling_PP )
        print("Terima kasih sudah menggunakan kalkulator 😊")
        
    #SISTEM SEGITIGA
    elif bangun_datar == "c" or bangun_datar == "C" :
        print()
        print("="*25)
        print()
        print("Anda memilih SEGITIGA")
        
        #Input data oleh user 
        Alas_st = int(input("Masukan panjang Alas : "))
        Tinggi_st = int(input("Masukan panjang Tinggi : "))
        sisi1_st = int(input("Masukan panjang sisi 1 : "))
        sisi2_st = int(input("Masukan panjang sisi 2 : "))
        sisi3_st = int(input("Masukan panjang sisi 3 : "))
        #Hitungan Luas
        Luas_st = (Alas_st*Tinggi_st)/2
        #Hitungan Keliling
        Keliling_st = sisi1_st+sisi2_st+sisi3_st
        
        #Output hitungan 
        print("Segitiga tersebut memiliki LUAS sebesar", Luas_st )
        print("Segitiga tersebut memiliki KELILING sebesar",Keliling_st )
        print("Terima kasih sudah menggunakan kalkulator 😊")
        
    #SISTEM LINGKARAN
    elif bangun_datar == "d" or bangun_datar == "D" :
        print()
        print("="*25)
        print()
        print("Anda memilih LINGKARAN")
        
        #Input data oleh user 
        r = float(input("Masukan panjang jari-jari : "))
        phi = (22/7)
        if r % 7 == 0 :
            phi= (22/7)
        else:
            phi =3.14
        d= 2*r    

        #Hitungan Luas
        Luas_C = r**2*phi
        
        #Hitungan Keliling
        Keliling_C = d*phi
        
        #Output hitungan 
        print("Lingkaran tersebut memiliki LUAS sebesar", Luas_C )
        print("Lingkaran tersebut memiliki KELILING sebesar",Keliling_C )
        print("Terima kasih sudah menggunakan kalkulator 😊")
        
        
    else :
        print("😊 Harap pilih a, b, c atau d")
        ulang = input("Apakah Anda ingin menghitung lagi? (y/n): ")
    if ulang.lower() != "y":
        break
        
    ulang = input("Apakah Anda ingin menghitung lagi? (y/n): ")
    if ulang.lower() != "y":
        print("Terima kasih sudah menggunakan kalkulator 😊")
        break
    
        
