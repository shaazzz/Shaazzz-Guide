def markdown_href(title, url):
    return "[" + title + "](" + url + ")"

def tag_spoiler(tags):
    return "<details> <summary>Spoiler</summary> <ul>" + \
        ' '.join(list(map(lambda x : "<li>" + x + "</li>", tags))) + \
             "</ul> </details>"

def create_problem_row(problem):
    return "|" + markdown_href(problem["name"], problem["url"]) + "|" + problem["difficulty"] + \
        "|" + tag_spoiler(problem["tags"]) + "|" + problem["judge"] + "|"

def generate_markdown(blog_name, problems):
    file_name = blog_name + ".md"
    file_path = "./Blog/docs/" + file_name
    with open(file_path, "w") as markdown_file:
        markdown_file.write("--- \n")
        markdown_file.write("hide:\n")
        markdown_file.write("  - footer\n")
        markdown_file.write("---\n")

        markdown_file.write("# " + blog_name + "\n\n")
        
        markdown_file.write("| Problem | Difficulty | Tags | Judge | \n")
        markdown_file.write("| :-----: | :----: | :----: | :----: | \n")
        for problem in problems:
            markdown_file.write(create_problem_row(problem) + "\n")
