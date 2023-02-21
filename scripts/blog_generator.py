#!/bin/python3

import json
import markdown_generator
import tags
from pathlib import Path

with open("./problems.json", "r") as file:
    problems = json.load(file)["problems"]

problems_map = {}
for problem in problems:
    for tag in problem["tags"]:
        if not (tag in problems_map.keys()):
            problems_map[tag] = []

        problems_map[tag].append(problem)

tags = tags.tags_dict()

for tag in tags.keys():
    blog_path = "./Blog/docs/" + tags[tag]["site_path"]
    description_path = "./Posts/" + tag + ".md"
    Path(blog_path).parent.mkdir(parents=True, exist_ok=True)

    description = None
    if Path.exists(Path(description_path)):
        with open(description_path, "r") as file:
            description = file.read()
 
    tag_problems = []
    if tag in problems_map.keys():
        tag_problems = problems_map[tag]

    print("Generating " + blog_path + "...")
    markdown_generator.generate_markdown(blog_path, tags[tag]["blog_title"], description, tag_problems)

blog_path = "./Blog/docs/" + "problemset.md"
Path(blog_path).parent.mkdir(parents=True, exist_ok=True)
markdown_generator.generate_markdown(blog_path, "همه سوالات", None, problems)