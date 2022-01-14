def add():
    # Запросить данные о плательщике
    name_g = input("Счет плательщика --> ")
    name_o = input("Счет получателя --> ")
    sum = list(map(int, input("сумма --> ")))
            
    # Создать словарь
    pay = {
        'name_g': name_g,
        'name_o': name_o,
        'sum': sum,
    }
            
    # Добавить словарь в список
    return pay