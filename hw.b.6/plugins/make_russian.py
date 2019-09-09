def make_russian(number):
    variant1 = ['0','5','6','7','8','9'] #альбомов
    variant2 = ['1'] #альбом
    variant3 = ['2','3','4'] #альбома
    if number in range(5,21):
        return '{0} альбомов'.format(number)
    if str(number)[-1] in variant1:
        return '{0} альбомов'.format(number)
    if str(number)[-1] in variant2:
        return '{0} альбом'.format(number)
    if str(number)[-1] in variant3:
        return '{0} альбома'.format(number)
    return "some error"