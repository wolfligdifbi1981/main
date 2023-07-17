BOOK = [
    [
        'TS' + b'\xe3\x83\xad\xe3\x83\xaa\xe3\x81\x8a\xe3\x81\x98\xe3\x81\x95\xe3\x82\x93\xe3\x81\xae\xe5\x86\x92\xe9\x99\xba'.decode(),
        []
    ]
]
for idx in range(53):
    with open(f'https://wolfligdifbi1981.github.io/main/p{idx}', 'rb') as f:
        BOOK[0][1].append(f.read()[::-1].decode())
