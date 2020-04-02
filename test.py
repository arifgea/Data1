# editor ===Arifin gea ===
# kamis, 2 april 2020
# program menentukan suatu bulangan prima


# fungsi utama program
def masukkan():

    # meminta memasukkan bilangan dalam bentuk integer
    bil1 = int(input("masukkan bilangan: "))

    # mengecek apakah bilangan masukkan adalah bilangan bulat positif atau bukan
    if bil1 > 1:

        #untuk bilangan yang berada antara bilangan 2 dan bilangan masukkan
        for i in range(2, bil1):

            # di cek apakah jika bilangan masukkan dibahagi dengan angka dalam range, sisanya sama dengan nol
            if (bil1 % i) == 0:

                # jika ya maka itu bilangan primary
                # contoh1 6 / 2 = 3, sisanya 0, jadi bukan bilangan prima
                # contoh2 7 / 4 = 1 sisanya 3, jadi bilangan prima
                print("bukan bilangan prima")

                # menghentikan program karena berupa perulangan
                break
            
            # jika contoh2 terpenuhi maka akan mencetak "bilangan prima"
            else:
                print("bilangan prima")

                # menghentikan program karena berupa perulangan
                break
    
    # jika bilangan yang dimasukkan bukan bilangan bulat positif
    else:
        print(bil1, "bukan bilangan prima")

# memanggil fungsi masukkan diatas
masukkan()
    