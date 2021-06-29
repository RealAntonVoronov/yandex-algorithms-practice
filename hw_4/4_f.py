database = {}
with open('input.txt', 'r') as inp:
    text = inp.readlines()
    for line in text:
        customer, good, quantity = line.strip().split()
        if customer not in database:
            database[customer] = {}
        if good not in database[customer]:
            database[customer][good] = int(quantity)
        else:
            database[customer][good] += int(quantity)

for customer in sorted(database.keys()):
    print(f'{customer}:')
    for good in sorted(database[customer].keys()):
        print(good, database[customer][good])