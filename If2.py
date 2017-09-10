def str_compare(str1,str2):
    if str1 == str2:
        result = '1'
    elif str2 == 'learn':
        result = '3'
    elif len(str2) > len(str1):
        result = '2'
    return result

res=str_compare(str(input('Введите строку1: ')), str(input('Введите строку2: ')))
print(res)
