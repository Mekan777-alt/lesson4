from datetime import date
from requests import get, utils
from decimal import Decimal

def currency_rates(code):
    resp = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encode = utils.get_encoding_from_headers(resp.headers)
    valute_string = resp.content.decode(encoding=encode)
    resp.close()
    val_curs_date = valute_string[valute_string.find('Date="') + 6:valute_string.find('Date="') + 16].split('.')
    val_curs_date = date(year=int(val_curs_date[2]), month=int(val_curs_date[1]), day=int(val_curs_date[0]))
    find_charcode = valute_string.find(f'<CharCode>{code}')
    if find_charcode == -1:
        return ['ВАЛЮТА НЕ НАЙДЕНА', None, code, None], None, val_curs_date
    find_ending = find_charcode + valute_string[find_charcode:].find('</Valute>')
    valute_string = valute_string[find_charcode:find_ending]
    data_list = []
    for num in range(4):
        data_start = valute_string.find('>') + 1
        data_end = valute_string.find('</')
        data_list.append(valute_string[data_start:data_end])
        valute_string = valute_string[data_end + 12:]
    data_list[1] = int(data_list[1])
    rate = Decimal(data_list[3].replace(',', '.')) / data_list[1]
    data_list[3] = round(Decimal(data_list[3].replace(',', '.')), 2)
    return data_list, rate, val_curs_date


if __name__ == '__main__':
    result, cur_rate, date_of_rate = currency_rates(input('Введите код валюты: ').upper())
    txt_rate = f'{result[1]} {result[2]} = {result[3]} рублей.\n1 {result[0]} стоит {cur_rate} RUR.' \
               f'\nДата обновления курса {date_of_rate.day:0>2}.{date_of_rate.month:0>2}.{date_of_rate.year}г.'
    print(txt_rate)