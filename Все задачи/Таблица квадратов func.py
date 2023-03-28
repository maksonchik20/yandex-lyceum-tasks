def squared(a, b, k):
    for h in range(a, b + 1, 10):
        result = []
        for w in range(h, h + 10):
            kv = w ** 2
            if kv % k != 0 and w <= b:
                result.append(f"{kv:<4}")
        print(*result)
squared(22, 64, 5)