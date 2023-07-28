import re
from rich import print
import sys
from urllib.parse import urlparse
import validators

judges = {
    "www.usaco.org": r".+/index\.php\?page=viewproblem2&cpid=\d+",
    "codeforces.com": r".+/problemset/problem/\d+/.+",
    "open.kattis.com": r".+/problems/.+",
}

valid_judges = judges.keys()


def throw_error(name: str, msg: str):
    print(f"[red][bold]{name}:[/bold] {msg}[/red]")
    sys.exit(1)


def is_problem(url: str):
    rexp = judges[urlparse(url).netloc]
    return bool(re.fullmatch(rexp, url))


def is_valid_judge(url: str):
    if not validators.url(url):
        return False

    return urlparse(url).netloc in valid_judges
