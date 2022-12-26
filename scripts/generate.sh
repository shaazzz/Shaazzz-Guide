#!/bin/bash

git pull
curl -O -J -L "https://docs.google.com/spreadsheets/d/e/2PACX-1vT4u9dg9TRV_VjxMhv4TuXOTRcKUGQz2_vt2eh2-PUn6sC6wEi9_djsKzVLMpK2R63XvIKO94TVjmmZ/pub\?gid\=1911820389\&single\=true\&output\=csv" -o "../problems.csv"
python3 csv_to_json.py
python3 blog_generator.py

git add -A && git commit -m "problems update"
git push