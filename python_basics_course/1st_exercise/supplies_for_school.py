broi_himikalki = int(input()) * 5.80
broi_markeri = int(input()) * 7.20
litri_preparat = int(input()) * 1.20
procent_namalenie = int(input())
price_for_all_materials = broi_himikalki + broi_markeri + litri_preparat
price_with_discount = price_for_all_materials - (price_for_all_materials * (procent_namalenie / 100))
print(price_with_discount)