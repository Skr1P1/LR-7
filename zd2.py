from packet import add, show


if __name__ == '__main__':
    # Список учеников
    pay = []
    
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала
        command = input(">>> ").lower()
        
        # Выполнить действие в соответствие с командой
        if command == 'exit':
            break
        
        elif command == 'add':
            pay.append(add.add())
            
        elif command == 'list':    
            show.list(pay)

        else:
            print(f"Неизвестная команда {command}")