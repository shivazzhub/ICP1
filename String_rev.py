String = input()
Str_List = list(String)
del Str_List[3]
del Str_List[-2]
Str_List.reverse()
print(''.join(Str_List))
