num_paper = int(input())
num_cloth = int(input())
lit_glue = float(input())
percent_discount = int(input())

all_materials = (num_paper * 5.8) + (num_cloth * 7.2) + (lit_glue * 1.2)
price_after_discount = all_materials - (all_materials * percent_discount) / 100

print(f'{price_after_discount:.3f}')

