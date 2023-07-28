import fire
from rich import print
from utils import is_valid_judge, is_problem, throw_error


def download_problem(url: str):
    if not is_valid_judge(url):
        throw_error("Input Error", "Invalid url, judge is not supported")

    if not is_problem(url):
        throw_error("Input Error", "Invalid url, page does not contain a task")

    print("Fetching...")


def cli():
    fire.Fire(download_problem)


if __name__ == "__main__":
    cli()
