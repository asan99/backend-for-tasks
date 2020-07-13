def metod2():
    dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
    for x in dict_.keys():
        try:
            x + 'abc'
        except TypeError:
            str(x)+'abc'
    print(dict_)
metod2()