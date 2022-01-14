def list(pay):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} |'.format(
            "Счет плательщика",
            "Счет получателя",
            "Снятая сумма"
        )
    )
    print(line)

    # Вывести данные о всех учениках
    for idx, pay in enumerate(pay, 1):
        print(
            '| {:<4} | {:<30} | {:<20} |'.format(
                idx,
                pay.get('name_g', ''),
                pay.get('name_o', '')
            ), end=' ')
        for i in pay.get('sum'):
            print(i, end=' ')
        print('|')
    print(line)