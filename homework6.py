# работа со словврями
my_dict={"Ефремов":"Час Быка","Снегов":"Люди как боги","Толстой":"Аэлита"}
print(my_dict)
print(my_dict["Снегов"])
my_dict["Булычёв"]="Посёлок"
print(my_dict)
my_dict.update({"Носов":"Незнайка на Луне","Мартынов":"Гость из бездны"})
print(my_dict)
print(my_dict.pop("Ефремов"))


# работа с множествами
my_set={10, 56,"snack", 10,  2, 45, 4, 56, 2, 4, 45, "snack"}
print(my_set)
my_set.add(98)
my_set.add(6)
print(my_set)
