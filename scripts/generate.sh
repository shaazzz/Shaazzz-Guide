#!/bin/bash

git pull

URL="https://docs.google.com/spreadsheets/d/e/2PACX-1vT4u9dg9TRV_VjxMhv4TuXOTRcKUGQz2_vt2eh2-PUn6sC6wEi9_djsKzVLMpK2R63XvIKO94TVjmmZ/pub?gid=1911820389&single=true&output=csv"
curl -Ls $URL -o "problems.csv"
python3 ./scripts/csv_to_json.py
python3 ./scripts/blog_generator.py

git add -A && git commit -m "problems update"
git push