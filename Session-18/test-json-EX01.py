import json
import termcolor
from pathlib import Path

jsonstring = Path("people-EX01.json").read_text()
people = json.loads(jsonstring)
people = people['person']
print("Total people in the database:", len(people))
for person in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])
    phoneNumbers = person['phoneNumber']
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])
