from pathlib import Path
import json

with open("./judges.json", "r") as json_file:
    judges = json.load(json_file)


def markdown_href(title, url, open_in_new_tab = True):
    url = str(url)
    result = "[" + title + "](" + url + ")"
    if open_in_new_tab:
        result = result + "{:target=\"_blank\"}"

        return result

def judge_div(judge):
    if not judge in judges:
        return judge
    
    return ":" + judges[judge]["icon"] + ": " + markdown_href(judges[judge]["name"], judges[judge]["url"]) 

def tag_link(tag, tags_list):
    tag_object = [x for x in tags_list if x["tag"] == tag]
    if not tag_object:
        return tag
    
    return markdown_href(tag_object[0]["blog_title"], Path("/Shaazzz-Guide/" + tag_object[0]["path"]).with_suffix(""))

def tag_spoiler(tags, tags_list):
    return "<details> <summary>Spoiler</summary> <ul>" + \
        ' '.join(list(map(lambda tag : "<li>" + tag_link(tag, tags_list) + "</li>", tags))) + \
             "</ul> </details>"

def create_problem_row(problem, tags_list):
    return "|" + markdown_href(problem["name"], problem["url"]) + "|" + problem["difficulty"] + \
        "|" + tag_spoiler(problem["tags"], tags_list) + "|" + judge_div(problem["judge"]) + "|"

def generate_markdown(blog_path, blog_name, description, problems, tags_list):
    file_name = blog_name + ".md"
    with open(blog_path, "w") as markdown_file:
        markdown_file.write("--- \n")
        markdown_file.write("hide:\n")
        markdown_file.write("  - footer\n")
        markdown_file.write("---\n")

        markdown_file.write("# " + blog_name + "\n\n")
        
        if description:
            markdown_file.write("## توضیحات: \n")
            markdown_file.write(description)
            markdown_file.write("\n")

        if problems:
            markdown_file.write("## سوال ها \n")
            markdown_file.write("| سوال | سختی | تگ ها | جاج | \n")
            markdown_file.write("| :-----: | :----: | :----: | :----: | \n")
            for problem in problems:
                markdown_file.write(create_problem_row(problem, tags_list) + "\n")
