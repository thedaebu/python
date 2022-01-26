## creating dictionaries
emails = { 
    'caleb': 'caleb@email.com',
    'gal': 'gale@gmail.com',
    (5, 5): 'test'
}

## retrieving data from dictionaries
emails = { 
    'caleb': 'caleb@email.com',
    'gal': 'gale@gmail.com',
    (5, 5): 'test'
}
emails['caleb']
emails.get('caleb', 'no user found') # first argument is key, second argument is return if key in dictionary does not exist

## adding data to dictionary
emails = { 
    'caleb': 'caleb@email.com',
    'gal': 'gale@gmail.com',
    (5, 5): 'test'
}
emails['eddie'] = 'eddie@gmail.com' # javascript way
emails.update({
    'eddie': 'eddie@gmail.com',
    'thedaebu': 'thedaebu@gmail.com'
}) # add multiple data to hash using a hash data
emails.update(eddie = 'eddie@gmail.com') # prolly not go this way

## iterate through data of a dictionary
emails = { 
    'caleb': 'caleb@email.com',
    'gal': 'gale@gmail.com',
    (5, 5): 'test'
}
for k in emails:
    k # returns key of dictionary

for k, v in emails.items():
    v # returns value of dictionary