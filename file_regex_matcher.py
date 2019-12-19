import re

file = open("/media/andrii/73f436aa-9d74-4bcb-87e5-1fc06140dd6c/home/andrii/Downloads/welt_nordstream.txt", 'r')
# file = open("/media/andrii/73f436aa-9d74-4bcb-87e5-1fc06140dd6c/home/andrii/Downloads/zeit_nordstream.txt", 'r')

text = file.readlines()
size = len(text)



regex_comment = r"\*\*\s*(\S*\s*\S*\s*\S*)\s+\>\>\s*(\w+)\s*\>\>\s+(.*)"
regex_name = r"\=*\>+\s+\NAME:\s+(.*)"

counter_comment_good = 0
counter_comment_bad = 0
counter_name_good = 0
counter_name_bad = 0
file_for_matching = open("/media/andrii/73f436aa-9d74-4bcb-87e5-1fc06140dd6c/home/andrii/Downloads/welt_nordstream.txt", 'r')
# file_for_matching = open("/media/andrii/73f436aa-9d74-4bcb-87e5-1fc06140dd6c/home/andrii/Downloads/zeit_nordstream.txt", 'r')
for line in file_for_matching:
    if re.findall(regex_comment, line):
        counter_comment_good += 1
    elif re.findall(regex_name, line):
        counter_name_good += 1
    else:
        print(line)
        counter_name_bad += 1
        counter_comment_bad += 1

print("All = " + str(size))
print("Matched comments = " + str(counter_comment_good))
print("Not Matched comments = " + str(counter_comment_bad))
print("Matched names = " + str(counter_name_good))
print("Not Matched names = " + str(counter_name_bad))


