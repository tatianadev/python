from os.path import isfile
import sqlite3

if not isfile('test.db'):
    db = sqlite3.connect('test.db')
    db.execute('CREATE TABLE persons (name TEXT PRIMARY KEY, age INT, profession TEXT)')
    db.commit()
else:
    db = sqlite3.connect('test.db')


def load_persons(database):
    cursor = database.execute('SELECT name, age, profession FROM persons')
    return {name: {'age': age, 'profession': profession} for name, age, profession in cursor}


persons = load_persons(db)


class Descriptor(object):
    def __set_name__(self, owner, name):
        self.name = name
        self.owner = owner

    def __get__(self, instance, owner):
        if instance is None:
            return self
        queries = {'age': 'select age from persons where name = ?',
                   'profession': 'select profession from persons where name = ?'}
        cursor = db.execute(queries[self.name], (instance.name,))

        self.value = [value for value in cursor][0][0]

        return self.value

    def __set__(self, instance, value):
        updates = {'age': 'update persons set age = ? where name = ?',
                   'profession': 'update persons set profession = ? where name = ?'}

        db.execute(updates[self.name], (value, instance.name))
        db.commit()


class Person(object):
    def __init__(self, name):
        self.name = name
        if self.name not in persons:
            db.execute('insert into persons values(?,?,?)', (self.name, None, None))
        db.commit()

    age = Descriptor()
    profession = Descriptor()


while True:
    try:
        user_name = input('Enter name: ')
        age = int(input('Enter age: '))
        profession = input('Enter profession: ')
    except:
        print('Invalid input')
    else:
        break

new_user = Person(user_name)
new_user.age = age
new_user.profession = profession
print(new_user.age)
print(Person.age)
print(new_user.name, new_user.age, new_user.profession)
