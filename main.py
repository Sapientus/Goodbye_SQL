from models import Author, Quote
import connection

stop_list=['exit', 'end']
command_list=['name', 'tag', 'tags']
word=True

#I'll modify it for SOLID as soon as I have strength for this  but now engoy this sh*t
while word:
    print('Available commands: "name", "tag", "tags". To finish type "exit" or "end".')
    user_input=input('Type like this "command: word": ')
    parsed_input=user_input.split(':')
    if parsed_input[0]=='name':
        auth=Author.objects(fullname=parsed_input[1].removeprefix(' ')).first()
        quotes=Quote.objects(author=auth)
        for q in quotes:
            print(q.quote)
    elif parsed_input[0]=='tag':
        quotes=Quote.objects(tags=parsed_input[1].removeprefix(' '))
        for q in quotes:
            print(q.quote)
    elif parsed_input[0]=='tags':
        tags_list=[t for t in parsed_input[1].replace(' ', '').split(',')]
        quotes=Quote.objects(tags__in=tags_list)
        for q in quotes:
            print(q.quote)
    elif parsed_input[0] in stop_list:
        word=False
        print('Bye!')
    else:
        print('There is no such command!')
        continue