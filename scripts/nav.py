import json
persian_digits = "۰۱۲۳۴۵۶۷۸۹"

def indent(x, a):
    return (x * "  ") + a + "\n"

def create_nav():
    with open("./tags.json", "r") as json_file:
        tags = json.load(json_file)

    nav_yml = indent(0, "nav:")
    nav_yml += indent(1, "- شازززگاید: index.md")

    ind = 1
    for level, level_tags in tags.items():
        nav_yml += indent(1, "- سطح " + persian_digits[ind] + ":")
        if len(level_tags.keys()) == 0:
            nav_yml += indent(2, "- Coming soon...: coming_soon.md")
        else:
            for tag in level_tags.values():
                nav_yml += indent(2, "- " + tag["blog_title"] + ": " + level + "/" + tag["path"])

        ind = ind + 1

    nav_yml += indent(1, "- همه سوالات: problemset.md")
    return nav_yml

def generate_mkdocs_nav():
    nav_yml = create_nav()

    with open("./Blog/mkdocs.yml", "r+") as mkdocs_yml:
        lines = mkdocs_yml.readlines()
        while len(lines) > 0 and lines.pop().strip() != "nav:":
            continue

        mkdocs_yml.seek(0)
        mkdocs_yml.truncate(0)
        mkdocs_yml.writelines(lines)
        mkdocs_yml.write(nav_yml)

generate_mkdocs_nav()