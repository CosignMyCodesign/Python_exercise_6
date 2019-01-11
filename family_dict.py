# 1. Define a dictionary that contains information about several members of your family.

mi_familia = {
  'mother': {
    'name': 'Kimberly',
    'age': 52
  },
  'father': {
    'name': 'Travis',
    'age': 54
  },
  'brother': {
    'name': 'Dallas',
    'age': 30
  },
  'sister': {
    'name': 'Kati',
    'age': 34
  }
}

# 2. Using a dictionary comprehension, produce output that looks like the following example.
  # Krista is my sister and is 42 years old 


family_comprehension = {f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' for (family_member, member_values) in mi_familia.items()}

print(family_comprehension)