names = ['nico', 'zule', 'santi']
ages = [12, 46, 98]

print(list(zip(names, ages)))

new_dic = {name: age for (name, age) in zip(names, ages)}

print(new_dic)