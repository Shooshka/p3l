import datetime
import sys

if len(sys.argv) == 1:
    print("Usage: {} new or {} count".format(sys.argv[0], sys.argv[0]))
elif sys.argv[1] == new:
    now = datetime.datetime.now()
    today = str(now.day) + '.' + str(now.month) + '.' + str(now.year)
    client = input('Клиент: ')
    bases = input('Сколько баз? ')
    ticket = input('Номер тикета')
    with open('otchet.txt', 'a') as ouf:
        print(today, client, bases, str(ticket), sep=',', file=ouf)
    print('Успешно внесли в список обнов')

elif sys.argv[1] == count:
    s = []
    with open('otchet.txt', 'r') as inf:
        for line in inf:
            line = line.strip()
            s.append(line.split(','))
    print('А всего на данный момент обновлено ' + str(sum([int(bases) for today, client, bases, ticket in s])) + ' баз')
