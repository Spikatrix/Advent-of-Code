import sys

input_lines = [line.strip() for line in sys.stdin.readlines()]

searched_bags = []
my_bag = 'shiny gold'
contain_bags = dict()

for bag_rule in input_lines:
    split_words = bag_rule.split(' ')
    bag = ' '.join(split_words[:2])

    contain_bags[bag] = {}
    if split_words[4] == 'no':
        continue

    bag_index = 4
    loop = True
    while loop:
        contain_bags[bag][' '.join(split_words[bag_index + 1:bag_index + 3])] = int(split_words[bag_index])
        loop = split_words[bag_index + 3].endswith(',');
        bag_index += 4

def find_inner_bag_count(bag):
    inner_bags = contain_bags[bag]
    count = 1

    for key, value in inner_bags.items():
        count += (value * find_inner_bag_count(key))

    return count

print(find_inner_bag_count(my_bag) - 1)
