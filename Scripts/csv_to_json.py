import csv
import json

def problems_json():
    problems_dict = { "problems": [] }

    with open("./problems.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            problem = {}
            problem["judge"] = row[0]
            problem["name"] = row[1] 
            problem["url"] = row[2]
            problem["tags"] = list(map(lambda tag: tag.strip().lower(), row[3].split("|")))
            problem["difficulty"] = row[4]         

            problems_dict["problems"].append(problem)

    with open("problems.json", 'w', encoding="utf8") as jsonfile:
        json.dump(problems_dict, jsonfile, indent=4, ensure_ascii=False)
problems_json()