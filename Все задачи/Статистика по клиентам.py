payments = {}


def get_transactions(query):
    global payments
    if query == "print_it":
        for el in payments.items():
            print(el[1][0], el[0], el[1][1])
    else:
        query = query.split('-')[1].split(':')
        name, pay = query[0], int(query[1])
        if payments.get(name) is None:
            payments[name] = [1, pay]
        else:
            payments[name][0] += 1
            payments[name][1] += pay
