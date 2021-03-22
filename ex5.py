from sys import argv

from question_3 import currency_rates

if len(argv) < 2:
    print('Не введён параметр запуска')
else:

    result, cur_rate, date_of_rate = currency_rates(argv[1].upper())
    # собираем результат в строку:
    txt_rate = f'{result[1]} {result[2]} = {result[3]} рублей.\n1 {result[0]} стоит {cur_rate} RUR.' \
               f'\nДата обновления курса {date_of_rate.day:0>2}.{date_of_rate.month:0>2}.{date_of_rate.year}г.'
    print(txt_rate)