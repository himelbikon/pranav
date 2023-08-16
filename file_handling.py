import json

database = ['Pranav', 'Diba', 'Shuvo']

# not dumps
json.dump(
    {'db': database},
    open('test.json', 'w')
)

# not loads
content = json.load(open('test.json', 'r'))

database_2 = content.get('db')

print(database_2)
print(type(database_2))
