import re

file = open("/media/andrii/73f436aa-9d74-4bcb-87e5-1fc06140dd6c/home/andrii/Downloads/welt_nordstream.txt", 'r')

text = file.readlines()
size = len(text)



regex = r"\*\*\s*(\S*\s*\S*\s*\S*)\s+\>\>\s*(\w+)\s*\>\>\s+(.*)"

counter_good = 0
counter_bad = 0
file_for_matching = open("/media/andrii/73f436aa-9d74-4bcb-87e5-1fc06140dd6c/home/andrii/Downloads/welt_nordstream.txt", 'r')
for line in file_for_matching:
    if re.findall(regex, line):
        counter_good += 1
    else:
        print(line)
        counter_bad += 1

print("All = " + str(size))
print("Matched = " + str(counter_good))
print("Not Matched = " + str(counter_bad))


