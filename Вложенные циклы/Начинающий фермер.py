balance = int(input())
head = int(input())

BIK_PRICE = 20
KOROVA_PRICE = 10
TELENOR_PRICE = 5

for bik in range(1, head + 1):
    for korova in range(head - bik + 1):
        for telenok in range(head - korova + 1):
            if bik * BIK_PRICE + korova * KOROVA_PRICE + telenok * TELENOR_PRICE == balance:
                if bik + korova + telenok == head:
                    print(bik, korova, telenok)