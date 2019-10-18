nama_lengkap = input("Masukkan Nama : ")
nomor_unik = sum([ord(char)
                  for char in nama_lengkap.upper() if char.isalpha()]) % 400

print("Nomor unik untuk " + nama_lengkap + " adalah " + str(nomor_unik))
