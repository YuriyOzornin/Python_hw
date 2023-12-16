"""Функция для поиска дубликатов в списке."""
duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)

#def list_of_duplicates(_list_integer: List[int]) -> List[int]:
#    """Функция для поиска дубликатов в списке."""
#    duplicates = set()
#    for item in _list_integer:
#        if _list_integer.count(item) > 1:
#            duplicates.add(item)
#    return list(duplicates)