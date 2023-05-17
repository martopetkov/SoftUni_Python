godishna_taksa = int(input())

obuvki = (godishna_taksa - (godishna_taksa * 0.40))
ekip = (obuvki - (obuvki * 0.20))
topka = ekip * 0.25
aksesoari = topka * 0.2
total_price = godishna_taksa + obuvki + ekip + topka +aksesoari
print(total_price)