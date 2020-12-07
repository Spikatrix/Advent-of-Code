import sys

input_lines = [line.strip() for line in sys.stdin.readlines()]

searched_bags = []
to_search_bags = ['shiny gold']
final_bags = set()
contain_bags = dict()

for bag_rule in input_lines:
    split_words = bag_rule.split(' ')
    bag = ' '.join(split_words[:2])

    contain_bags[bag] = []
    if split_words[4] == 'no':
        continue

    bag_index = 5
    loop = True
    while loop:
        contain_bags[bag].append(' '.join(split_words[bag_index:bag_index + 2]))
        loop = split_words[bag_index + 2].endswith(',');
        bag_index += 4

while to_search_bags != []:
    search_bag = to_search_bags.pop()
    to_search_bags.extend([bag_key for bag_key, bag_value in contain_bags.items() if search_bag in bag_value])

    for to_search_bag in to_search_bags:
        final_bags.add(to_search_bag)

print(len(final_bags))
