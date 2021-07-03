import argparse
import re
import os
import requests

urls = {"EU": "https://uvapythonexams.eu.pythonanywhere.com/test_requests",
        "US": "https://asepythonexams.pythonanywhere.com/test_requests"}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Test an exam question for correctness")
    parser.add_argument(
        "question", type=str,
        help="Question to test (1, 2, ...)")
    return parser.parse_args()


def strip_solution_text(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = remove_block_comments(lines)
    lines = remove_empty_lines(lines)
    lines = remove_single_comment_lines(lines)
    return "".join(lines)


def remove_block_comments(lines, temp_line_sep="||"):
    text = "".join(lines).replace("\n", temp_line_sep)
    while m := re.search(r"'''.*?'''", text):
        text = text.replace(m.group(0), "")
    while m := re.search(r'""".*?"""', text):
        text = text.replace(m.group(0), "")
    return [line + "\n" for line in text.split(temp_line_sep)]


def remove_empty_lines(lines):
    return [line for line in lines if line.strip()]


def remove_single_comment_lines(lines):
    return [line for line in lines if not line.lstrip().startswith("#")]


def get_api_urls():
    eu = os.environ.get("PYTHONANYWHERE_SITE") == "eu.pythonanywhere.com"
    alt_locs = [_ for _ in urls.keys() if _ not in ["EU", "US"]]
    locs = ["EU"] + alt_locs + ["US"] if eu else ["US"] + alt_locs + ["EU"]
    return [urls[_] for _ in locs]


if __name__ == "__main__":
    args = parse_args()
    api_urls = get_api_urls()

    test_request = {
        "submitter": "11968850",
        "exam": "problem_set_w8",
        "question_no": int(args.question),
        "solution": strip_solution_text(f"{args.question}.py"),
    }

    resp_status = None

    while api_urls and resp_status != 201:
        resp = requests.post(api_urls.pop(0), data=test_request,
                             auth=("788f1303455041d0e07ee99b",
                                   "zP!Fz47)phi@EmO3V34(gBi0ZXrH"))
        resp_status = resp.status_code

    if resp_status != 201:
        print("Something went wrong with the test request, sorry!")
        print(f"Response status code: {resp_status}")
    else:
        print(f"\nSOLUTION BEING TESTED")
        print(f"=====================")
        print(f"\n{resp.json()['solution']}")
        print(f"\nTEST RESULT")
        print(f"===========")
        print(f"\n{resp.json()['test_result']}\n")