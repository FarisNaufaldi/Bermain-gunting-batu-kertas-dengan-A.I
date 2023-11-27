import random
def permainan():
    skor_pemain = 0
    skor_komputer = 0
    Pemain = input("Sebagai Pemain anda harus memiliki sebuah nama = ")
    pilihan_komputer = ["g","b","k"]
    y = random.choice(pilihan_komputer)
    while skor_pemain < 4 and skor_komputer < 4:
        try:
            x = input(f"{Pemain}, Masukkan pilihan anda gunting batu atau kertas dengan hanya menuliskan g/b/k = ").lower()
            y = random.choice(pilihan_komputer)
            if (x == "g" and y == "k") or \
               (x == "k" and y == "b") or \
               (x == "b" and y == "g"):
                skor_pemain += 1
                print(f"Skor sementara, {Pemain} memegang {skor_pemain} point dan Komputer memegang {skor_komputer} point")
            elif (x == "k" and y == "g") or \
                 (x == "b" and y == "k") or \
                 (x == "g" and y == "b"):
                skor_komputer += 1
                print(f"Skor sementara, {Pemain} memegang {skor_pemain} point dan Komputer memegang {skor_komputer} point")
            elif (x == "k" and y == "k") or \
                 (x == "b" and y == "b") or \
                 (x == "g" and y == "g"):
                skor_komputer += 1
                skor_pemain += 1
                print(f"Skor sementara, {Pemain} memegang {skor_pemain} point dan Komputer memegang {skor_komputer} point")    
            else:
                print("anda salah memasukkan pilihan, pilihan anda gunting batu atau kertas dengan hanya menuliskan g/b/k = ")
        except:
            x = input(f"{Pemain}, Masukkan pilihan anda gunting batu atau kertas dengan hanya menuliskan g/b/k = ").lower()
    if skor_pemain == 4 and skor_komputer < 4:
        print(f"Pemenang dari permainan ini adalah {Pemain}")
    elif skor_komputer == 4 and skor_pemain < 4:
        print(f"Pemenang dari permainan ini adalah komputer")
    else:
        print("Permainan berakhir seri")
permainan()
            
        


