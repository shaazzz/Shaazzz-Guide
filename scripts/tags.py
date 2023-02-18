import json

def tags_dict():
    tags = {}
    with open("./tags.json") as file:
        tags_json = json.load(file)
        for level in tags_json.items():
            level_tags = level[1]
            for tag in level_tags.items():
                tag[1]["level"] = level[0]
                tag[1]["site_path"] = tag[1]["level"] + "/" + tag[1]["path"]
                tags[tag[0]] = tag[1]

    return tags
