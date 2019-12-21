import re
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('')

class Data(Base):

    __tablename__ = 'media_comments'
    id = Column(Integer, primary_key=True)
    media = Column('media', String(150))
    article_name = Column('article_name', String(500))
    username = Column('username', String(150))
    sentiment = Column('sentiment', String(100))
    comments = Column('body_of_comments', String(100000))

    def __init__(self, media, article_name, username, sentiment, body_of_comment):
        self.media = media
        self.article_name = article_name
        self.username = username
        self.sentiment = sentiment
        self.body_of_comment = body_of_comment

file = open("/home/ashara/projects/head_first_programming/german_project/welt_nordstream.txt", 'r')
# file = open("/home/ashara/projects/head_first_programming/german_project/zeit_nordstream.txt"", 'r')

text = file.readlines()
size = len(text)



regex_comment = r"\*\*\s*(\S*\s*\S*\s*\S*)\s+\>\>\s*(\w+)\s*\>\>\s+(.*)"
regex_name = r"\=*\>+\s+\NAME:\s+(.*)"

session = Session()

counter_comment_good = 0
counter_comment_bad = 0
counter_name_good = 0
counter_name_bad = 0
file_for_matching = open("/home/ashara/projects/head_first_programming/german_project/welt_nordstream.txt", 'r')
# file_for_matching = open("/home/ashara/projects/head_first_programming/german_project/zeit_nordstream.txt", 'r')
for line in file_for_matching:
    media = 'welt'
    comment_object = Data(media, None, None, None, None)
    if re.findall(regex_comment, line):
        counter_comment_good += 1
        comment_object.username = re.match(regex_comment, line).group(0)
        comment_object.sentiment = re.match(regex_comment, line).group(1)
        comment_object.comments = re.match(regex_comment, line).group(2)
    elif re.findall(regex_name, line):
        counter_name_good += 1
        comment_object.article_name = re.match(regex_name, line).group(0)
    else:
        print(line)
        counter_name_bad += 1
        counter_comment_bad += 1
    session.add(comment_object)
    session.commit()
session.close()

print("All = " + str(size))
print("Matched comments = " + str(counter_comment_good))
print("Not Matched comments = " + str(counter_comment_bad))
print("Matched names = " + str(counter_name_good))
print("Not Matched names = " + str(counter_name_bad))


