import sys

input_lines = sys.stdin.read()
passports = [passport.replace('\n', ' ') for passport in input_lines.replace('\r', '').split('\n\n')]

fields = {
            'byr': False,
            'iyr': False,
            'eyr': False,
            'hgt': False,
            'hcl': False,
            'ecl': False,
            'pid': False,
            'cid': False,
         }

valid_count = 0

for passport in passports:
    for field in passport.split(' '):
        fields[field[:3]] = True

    count = len(list(filter(lambda x: x, fields.values())))

    if (not fields['cid'] and count == 7) or (count == 8):
        valid_count += 1

    fields = {key: False for key in fields.keys()}

print(valid_count)
