import json
import markdown_generator

with open("./problems.json", "r") as file:
    problems = json.load(file)["problems"]

tag_map = {}
for problem in problems:
    for tag in problem["tags"]:
        if not (tag in tag_map.keys()):
            tag_map[tag] = []

        tag_map[tag].append(problem)

for tag in tag_map.keys():
    # tag_map[tag] = sorted(tag_map[tag], key=lambda x : int(x["difficulty"]))
    markdown_generator.generate_markdown(tag, tag_map[tag])