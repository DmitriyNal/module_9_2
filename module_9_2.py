first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
print(first_result)

second_result = [(string, string_2) for string in second_strings for string_2 in first_strings
                 if len(string_2) == len(string)]
print(second_result)

all_strings = first_strings + second_strings
third_result = {s: len(s) for s in all_strings if len(s) % 2 == 0}
print(third_result)