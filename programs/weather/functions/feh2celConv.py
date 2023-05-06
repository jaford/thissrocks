def feh2cel(tempDegree):
    try:
        if isinstance(tempDegree, str):
            print('"{}" is not a number!'.format(tempDegree))
        else: 
            fahrenheit = float(tempDegree)
            celConv = ((fahrenheit - 32) * (5 / 9))
            print(u'Fahrenheit: {}\u00b0\nCelsius: {}\u00b0\n'.format(tempDegree, celConv))
    except Exception as err:
        celsiusError = str(tempDegree)
        print('"{}" is not a number!'.format(celsiusError))
        pass

    return celConv