# Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре
# различны. Выведите синоним для последнего слова.
slovar = {"vverh":"up", "vniz":"down", "vlevo":"left", "vpravo":"right"}
poslednii_item = {slovar.popitem()}

newdict = {}

newdict.update(poslednii_item)

print(newdict.values())
print(newdict.get("vpravo"))