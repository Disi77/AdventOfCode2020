with open("day07_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read()

input_data = input_data.strip().split("\n")


def get_all_rules(data):
    """
    Create list of rules from data in format:
    (color1, num, color2)
    '<color1> bags contain <num> <color2> bags'
    """
    rules = []
    for record in data:
        count = record.count(",")
        record = record.split()
        bag_from = record[0] + " " + record[1]
        if "other" in record:
            rule = (bag_from, 0, "no other")
            rules.append(rule)
            continue
        for i in range(count+1):
            bag_to_count = record[4+4*i]
            bag_to = record[5+4*i] + " " + record[6+4*i]
            rule = (bag_from, int(bag_to_count), bag_to)
            rules.append(rule)
    return rules


def get_rules_for_santa(rules, santa_bag):
    """
    Find list of rules connected with Santa's bag in format:
    (color1, num, color2)
    '<color1> bags contain <num> <color2> bags'
    """
    rules_santa = []

    colors = []
    temp_colors = []

    # Start with rules where is "shiny gold" bag on the left side
    for rule in rules:
        if rule[0] == santa_bag:
            temp_colors.append(rule[2])
            rules_santa.append(rule)

    # Then for each of the rule with "shiny gold" bag fint the children rule
    while True:
        temp = []
        for color in temp_colors:
            for rule in rules:
                if color == rule[0]:
                    temp.append(rule[2])
                    rules_santa.append(rule)

        # All used colors saved in the list "colors"
        colors.extend(temp_colors)
        colors = list(set(colors))

        # Set colors for processing in next round
        temp_colors = list(temp)

        if not temp_colors:
            break

    # Return list of Santa's rules
    return list(set(rules_santa))


def get_count_of_bags(pointer):
    """
    Counter of bags
    """
    temp_rules = []
    for rule in rules_santa:
        if rule[0] == pointer:
            temp_rules.append(rule)
    result = 0
    for rule in temp_rules:
        if rule[2] == "no other":
            return 0
        result += rule[1] * (1 + get_count_of_bags(rule[2]))

    return result


rules_all = get_all_rules(input_data)
santa_bag = "shiny gold"
rules_santa = get_rules_for_santa(rules_all, santa_bag)
result = get_count_of_bags(santa_bag)

print("How many individual bags are required inside single shiny gold bag?")
print(result)
