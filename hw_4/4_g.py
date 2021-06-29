database = dict()

with open('input.txt', 'r') as inp:
    for line in inp.readlines():
        query = line.strip().split()
        if query[0] == 'DEPOSIT':
            client, sum = query[1], int(query[2])
            if client not in database:
                database[client] = sum
            else:
                database[client] += sum
        elif query[0] == 'WITHDRAW':
            client, sum = query[1], int(query[2])
            if client not in database:
                database[client] = -sum
            else:
                database[client] -= sum
        elif query[0] == 'BALANCE':
            client = query[1]
            if client not in database:
                print('ERROR')
            else:
                print(int(database[query[1]]))
        elif query[0] == 'TRANSFER':
            client_one, client_two, sum = query[1], query[2], int(query[3])
            if client_one not in database:
                database[client_one] = 0
            if client_two not in database:
                database[client_two] = 0
            database[client_one] -= sum
            database[client_two] += sum
        elif query[0] == 'INCOME':
            p = float(query[1])
            for client in database.keys():
                if database[client] > 0:
                    profit = (p/100 * database[client])//1
                    database[client] += profit