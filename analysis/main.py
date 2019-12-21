import psycopg2
import re
connection = psycopg2.connect(user = "admin",
                              password = "pass123!",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "media_comments")

print("Connected")
cursor = connection.cursor()
cursor.execute("SELECT * from Media_Comments;")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")

file = open("/home/andrii/Downloads/zeit_nordstream.txt", 'r')
# file = open("/home/andrii/Downloads/test", 'r')
# file = open("/home/ashara/projects/head_first_programming/german_project/zeit_nordstream.txt"", 'r')

text = file.readlines()
size = len(text)

regex_comment = r"\*\*\s*(\S*\s*\S*\s*\S*)\s+\>\>\s*(\w+)\s*\>\>\s+(.*)"
regex_name = r"\s*\=*\>*\s*\s*\=*\>*\s*\s*\=*\>*\s*[NAME:]*\s+(.*)"

counter_comment_good = 0
counter_comment_bad = 0
counter_name_good = 0
counter_name_bad = 0
file_for_matching = open("/home/andrii/Downloads/zeit_nordstream.txt", 'r')
# file_for_matching = open("/home/andrii/Downloads/test", 'r')
# file_for_matching = open("/home/ashara/projects/head_first_programming/german_project/zeit_nordstream.txt", 'r')
i = 0
username, sentiment, body_of_comment = '', '', ''
article_name = 'Nord Stream 2: Wolfgang Schäuble kritisiert Ostsee-Pipeline'
for line in file_for_matching:
    print("Line = " + line)
    i += 1
    media = 'zeit'
    if re.findall(regex_comment, line):
        counter_comment_good += 1
        print("Group 1 = " + re.search(regex_comment, line).group(1))
        print("Group 2 = " + re.search(regex_comment, line).group(2))
        print("Group 3 = " + re.search(regex_comment, line).group(3))
        username = re.search(regex_comment, line).group(1)
        sentiment = re.search(regex_comment, line).group(2)
        body_of_comment = re.search(regex_comment, line).group(3)
        print( username, sentiment, article_name, media)
        sql_insert = "insert into Media_Comments(media, article_name, username, sentiment, body_of_comment) values (%s, %s, %s, %s, %s);"
        val = (media, article_name, username, sentiment, body_of_comment)
        cursor.execute(sql_insert, val)
        connection.commit()
    elif re.findall(regex_name, line):
        counter_name_good += 1
        article_name = re.search(regex_name, line).group(1)
    else:
        print(line)
        counter_name_bad += 1
        counter_comment_bad += 1


print("All = " + str(size))
print("Matched comments = " + str(counter_comment_good))
print("Not Matched comments = " + str(counter_comment_bad))
print("Matched names = " + str(counter_name_good))
print("Not Matched names = " + str(counter_name_bad))
