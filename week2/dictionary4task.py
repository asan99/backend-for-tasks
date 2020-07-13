cities = {'Bishkek':'Kyrgyzstan','Almata':'Kazakstan','Brussel':'Belgium'}


cities['Russia'] = 'Moscow'
cities['Ukraine'] = 'Kiev'
cities['USA'] = 'Washington'
print(cities)


print('В каком городе вы живете?')
country = input()


if country in cities:

    print('этот город страны', cities[country])