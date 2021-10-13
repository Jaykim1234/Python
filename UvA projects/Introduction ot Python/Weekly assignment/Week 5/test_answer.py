import argparse
import re
import requests

url = "https://uvapythonexams.eu.pythonanywhere.com/test_requests"


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


if __name__ == "__main__":
    args = parse_args()

    test_request = {
        "submitter": "11968850",
        "exam": "problem_set_w5",
        "question_no": int(args.question),
        "solution": strip_solution_text(f"{args.question}.py"),
    }
    resp = requests.post(url, data=test_request,
                         auth=("3aba5e23836689100580254a",
                               "M3yA%8xB1uZyc2J@TcaGneiWF9ih"))

    if resp.status_code != 201:
        print("Something went wrong with the test request, sorry!")
        print(f"Response status code: {resp.status_code}")
    else:
        print(f"\nSOLUTION BEING TESTED")
        print(f"=====================")
        print(f"\n{resp.json()['solution']}")
        print(f"\nTEST RESULT")
        print(f"===========")
        print(f"\n{resp.json()['test_result']}\n")
