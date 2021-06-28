favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['john', 'gianna', 'girby', 'phil']

for persons in people:
    if persons in favorite_languages:
        print('Thank you for taking the poll!')
    else:
        print('Dafuq bro. Take the poll already.')