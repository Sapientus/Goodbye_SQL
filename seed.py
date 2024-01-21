from models import *
import connection

authors=[]
for amount in range(define_amount('authors.json')):
    author=Loader()
    authors.append(author.make_author('authors.json', amount))

quotes=[]
for amount in range(define_amount('quotes.json')):
    quote=Loader()
    quotes.append(quote.make_quote('quotes.json', amount))
