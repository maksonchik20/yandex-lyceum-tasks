def lucky(ticket: int) -> str:
    global lastTicket
    ticket, lastTicket = str(ticket), str(lastTicket)
    while len(ticket) < 6:
        ticket = '0' + ticket
    while len(lastTicket) < 6:
        lastTicket = '0' + lastTicket
    print(lastTicket, ticket)
    if sum(list(map(int, ticket[:3]))) == sum(list(map(int, ticket[-3:]))):
        if sum(list(map(int, str(lastTicket)[:3]))) == sum(list(map(int, str(lastTicket)[-3:]))):
            return "Счастливый"
    return "Несчастливый"

lastTicket = 111111
print(lucky(2020))

