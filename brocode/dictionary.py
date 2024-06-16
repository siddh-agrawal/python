# dictionary = a changeable unordered collection of  unique  key value pairs fast
#              because the y use hashing, allows us to access value  quickly  


capitals = {'USA':'Washington DC',
            'INDIA': 'New Delhi',
            'CHINA': 'Beijing'
}

print(capitals['USA'])
capitals.update({'germany': 'berlin'})
capitals.update({'USA': 'las vegas'})
capitals.pop('CHINA')
capitals.clear()
# print(capitals.keys())
# print(capitals.values())
print(capitals.items())

