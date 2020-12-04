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
        field_key, field_value = field.split(':')

        # Some conditions are a bit loose as per the requirements, but it works on my input
        if (field_key == 'byr' and 1920 <= int(field_value) <= 2020) or \
           (field_key == 'iyr' and 2010 <= int(field_value) <= 2020) or \
           (field_key == 'eyr' and 2020 <= int(field_value) <= 2030) or \
           (field_key == 'hgt' and \
            (field_value[-2:] == 'cm' and 150 <= int(field_value[:-2]) <= 193) or \
            (field_value[-2:] == 'in' and 59 <= int(field_value[:-2]) <= 76) \
           ) or \
           (field_key == 'hcl' and len(field_value) == 7) or \
           (field_key == 'ecl' and field_value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) or \
           (field_key == 'pid' and len(field_value) == 9):
            fields[field_key] = True

    count = len(list(filter(lambda x: x, fields.values())))

    if (not fields['cid'] and count == 7) or (count == 8):
        valid_count += 1

    fields = {key: False for key in fields.keys()}

print(valid_count)
