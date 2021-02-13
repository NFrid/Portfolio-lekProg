import main


dummy = {
    'id': 42,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john@example.com',
    'gender': 'male',
    'ip_address': '1.0.0.0'
}

assert type(main.jsonToTable([dummy])) == type([])
assert type(main.jsonToTable([dummy])[0]) == type(str())
assert len(main.jsonToTable([dummy, dummy, dummy])
           ) == 7  # +4 for lines and headers
