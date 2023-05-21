tovari = int(input())

do_3_tona = 0
do_11_tona = 0
nad_12_tona = 0

for i in range(tovari):
    car_type = int(input())
    if 0 <= car_type <= 3:
        do_3_tona += car_type
    elif 4 <= car_type <= 11:
        do_11_tona += car_type
    elif 12 <= car_type:
        nad_12_tona += car_type

total_tovar = do_3_tona + do_11_tona + nad_12_tona
total_tovar_in_tons = ((do_3_tona * 200) + (do_11_tona * 175) + (nad_12_tona * 120)) / total_tovar

mikrobus_in_procent = do_3_tona / total_tovar * 100
kamion_in_procent = do_11_tona / total_tovar * 100
vlak_in_procent = nad_12_tona / total_tovar * 100

print(f'{total_tovar_in_tons:.2f}')
print(f'{mikrobus_in_procent:.2f}%')
print(f'{kamion_in_procent:.2f}%')
print(f'{vlak_in_procent:.2f}%')