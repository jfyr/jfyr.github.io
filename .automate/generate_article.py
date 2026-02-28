#
# # read all topics from /topics dir
# # append topics to topic list in index.html
#
# this_month_topics_count = 0
# categories_count = 0
# last_update = 0
#
# categories
#
#      _
#     | |
#   __| | _____   _____  _ __  ___
#  / _` |/ _ \ \ / / _ \| '_ \/ __|
# | (_| |  __/\ V / (_) | |_) \__ \
#  \__,_|\___| \_/ \___/| .__/|___/
#                       | |
#                       |_|
#
import datetime

from art import *
from jinja2 import Environment, FileSystemLoader

# read user inputs
#  topic
#  category
#  initial description
# read article template
# combine user's input with template and generate initial article html page

template_file = "index.j2"
save_location = "topics"

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("article_sample.j2")
date = datetime.date.today()

if __name__ == '__main__':
    title = input("Provide article title:")
    categories = input("Provide comma separated categories:").split(",")
    description = input("Provide article description:")

    generate_article = template.render(
        {"ascii_title": text2art(title), "title": title, "categories": categories,
         "description": description, "date": date})

    file_name = f"{title}-{date}.html"
    with open(f"{file_name}", "x") as f:
        f.write(generate_article)
        print(f"file [{file_name}] generated")
