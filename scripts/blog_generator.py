import json
import markdown_generator
from pathlib import Path

with open("./problems.json", "r") as file:
    problems = json.load(file)["problems"]

problems_map = {}
for problem in problems:
    for tag in problem["tags"]:
        if not (tag in problems_map.keys()):
            problems_map[tag] = []

        problems_map[tag].append(problem)

for tag in problems_map.keys():
    problems_map[tag] = sorted(problems_map[tag], key=lambda x : int(x["difficulty"]))

with open("./tags.json") as file:
    tags = json.load(file)["tags"]

for tag in tags:
    blog_path = "./Blog/docs/" + tag["path"]
    Path(blog_path).parent.mkdir(parents=True, exist_ok=True)

    problems = []
    if tag["tag"] in problems_map.keys():
        problems = problems_map[tag["tag"]]

    print("Generating " + blog_path + "...")
    markdown_generator.generate_markdown(blog_path, tag["blog_title"], problems)