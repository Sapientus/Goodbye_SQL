from mongoengine import *
import json
#from pathlib import Path
# Wanted to use Pathlib for making Path to a file universal.

def define_amount(file_path): #This defines the amount of dicts in files, so it will automatically create objects
    with open(file_path, 'r', encoding='utf-8') as f:
        data=json.load(f)
    return len(data)

class Author(Document):
    fullname = StringField(max_length=100, required=True)
    born_date = StringField(max_length=100, required=True)
    born_location = StringField(max_length=200)
    description = StringField()


class Quote(Document):
    tags = ListField()
    author = ReferenceField('Author', reverse_delete_rule=CASCADE)
    quote = StringField(required=True)


class Loader:
# I know, Document has 'from_json' method but I decided to make my own.    

    def load_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data=json.load(f)
        return data

    def count_objects(self, datas):
        return len(datas)

    def make_author(self, file_path, number):
        data=self.load_data(file_path)
        try:
            author=Author(
                fullname=data[number].get('fullname'), 
                born_date=data[number].get('born_date'), 
                born_location=data[number].get('born_location'), 
                description=data[number].get('description'))
            author.save()
        except IndexError:
            print('This number isn`t correct')

    def make_quote(self, file_path, num):
        data=self.load_data(file_path)
        try:
            certain_author=Author.objects(fullname=data[num].get('author')).first()
            if not certain_author:
                certain_author=Author(fullname=data[num].get('author'))
            quote=Quote(tags=data[num].get('tags'), author=certain_author, quote=data[num].get('quote'))
            quote.save()
        except IndexError:
            print('This number isn`t correct')

