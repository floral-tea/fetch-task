from fetch_task.utils import is_valid_judge, is_problem


def test_valid_judges():
    valid_judges = [
        "https://open.kattis.com/problems/birthday",
        "https://open.kattis.com/",
        "http://www.usaco.org/index.php",
    ]

    for j in valid_judges:
        assert is_valid_judge(j) is True


def test_invalid_judges():
    invalid_judges = ["duckduckgo.com", "abc", "github.com"]

    for j in invalid_judges:
        assert is_valid_judge(j) is False


def test_valid_problems():
    valid_problems = [
        "https://open.kattis.com/problems/birthday",
        "https://codeforces.com/problemset/problem/920/E",
        "http://www.usaco.org/index.php?page=viewproblem2&cpid=1282",
    ]

    for p in valid_problems:
        assert is_problem(p) is True


def test_invalid_problems():
    invalid_problems = [
        "https://open.kattis.com/",
        "https://codeforces.com/",
        "http://www.usaco.org/index.php",
    ]

    for p in invalid_problems:
        assert is_problem(p) is False
