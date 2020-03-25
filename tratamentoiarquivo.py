def tratamento(book):

    b = '{""}'

    for i in range(0, len(b)):
        book = book.replace(b[i], "")

    book = book.split(':')
    book = book[1]
    b = "''"

    for i in range(0, len(b)):
        book = book.replace(b[i], "")

    tam = len(book)
    book = book[1:tam]
    return book


msg = tratamento('{"ip": "127.0.0.1"}')
print(msg)

