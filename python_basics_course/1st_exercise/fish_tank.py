daljina = int(input())
shirina = int(input())
visochina = int(input())
procent = float(input()) / 100

obem_na_akvarium = daljina * visochina * shirina
obem_v_litri = obem_na_akvarium * 0.001
needed_liters = obem_v_litri - (obem_v_litri * procent)
print(procent)
print(needed_liters)