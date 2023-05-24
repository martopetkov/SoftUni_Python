first_words = input().split(", ")
second_words = input().split(", ")

result = []

for substring in first_words:
    for word in second_words:
        found_subst = substring in word  #ще върне true or false
        if found_subst:
            result.append(substring)
            break # слага се брейк, защото иначе ще принтира повече от веднъж даден събстринг

print(result)
