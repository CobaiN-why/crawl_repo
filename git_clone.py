import shutil
import git
import os
from datetime import datetime

from nbformat import write


class Progress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print('update(%s/%s), Message:%s' % (cur_count, max_count, message))
        if cur_count == max_count:
            print("OK")


global PYTHON_REPO_LIST
global JAVA_REPO_LIST
global PYTHON_DIR
global JAVA_DIR
PYTHON_LIST_PATH = "./top_1000_python_list.txt"
JAVA_LIST_PATH = "./top_1000_java_list.txt"
PYTHON_LOG_PATH = "F:\\top_1000_repo\\top_1000_python\\top_1000_python_list_log.txt"
JAVA_LOG_PATH = "F:\\top_1000_repo\\top_1000_java\\top_1000_java_list_log.txt"

with open(PYTHON_LIST_PATH) as f:
    python_list = list(f.readlines())

with open(JAVA_LIST_PATH) as f:
    java_list = list(f.readlines())

PYTHON_REPO_LIST = [url.strip() for url in python_list]
JAVA_REPO_LIST = [url.strip() for url in java_list]

PYTHON_DIR = "F:\\top_1000_repo\\top_1000_python\\projects"
JAVA_DIR = "F:\\top_1000_repo\\top_1000_java\\projects"
REPO_DIR = os.path.join(JAVA_DIR, "projects")

# check global variable PYTHON_REPO_LIST
assert len(PYTHON_REPO_LIST) == len(list(set(PYTHON_REPO_LIST)))
assert len(PYTHON_REPO_LIST) >= 1020

# check global variable JAVA_REPO_LIST
assert len(JAVA_REPO_LIST) == len(list(set(JAVA_REPO_LIST)))
assert len(JAVA_REPO_LIST) >= 1020


def test_clone_one():
    # clone_one(JAVA_REPO_LIST[0], JAVA_DIR)
    clone_one(PYTHON_REPO_LIST[0], PYTHON_DIR)


def clone_one(git_url, to_dir, rank=None):
    assert not git_url.endswith("\n")

    repo_name = git_url.split("/")[-1]
    repo_name = repo_name.replace(".git", "")
    if rank:
        repo_name = rank + repo_name
    to_path = os.path.join(to_dir, repo_name)
    assert not os.path.exists(to_path), to_path

    repo = git.Repo.clone_from(git_url, to_path, progress=Progress())

    assert os.path.exists(to_path)
    pull_info = repo.git.pull()

    assert pull_info == "Already up to date."
    print(to_path + "ok")
    return git_url, pull_info


def read_file(path):
    """load lines from a file"""
    sents = []
    with open(path, 'r') as f:
        for line in f:
            sents.append(str(line.strip()))
    return sents


def write_file(filename, data):
    with open(filename, 'w') as f:
        for i in data:
            f.write(str(i).strip() + '\n')


def check_already(logs, repo):
    flag = 1
    for line in logs:
        if repo in line:
            flag = 0
    return flag


def clone_list(repo_list, to_dir, log_file):
    with open(log_file, "a") as f:
        start = datetime.now().strftime("Time: %Y-%m-%d %H:%M\n")
        f.write(start)
    logs = read_file(log_file)
    failed_list = []
    for index, repo in enumerate(repo_list):
        # e.g., top0001, top0002, top0003 etc.
        rank = "top%s_" % str(index+1).rjust(4, "0")
        
        if check_already(logs, repo) and index < 1000:
            try:
                git_url, pull_info = clone_one(repo, to_dir, rank)
                message = "%s || %s\n" % (git_url, pull_info)
                now = datetime.now().strftime("Time: %Y-%m-%d %H:%M\n")
                with open(log_file, "a+") as f:
                    f.write(message)
                    f.write(now)
            except Exception as e:
                failed_list.append(repo)
                with open(log_file, "a+") as f:
                    f.write("%s failed!!!!!!" % (index+1))
                    f.write(now)
        else:
            continue
    
    failed_file = log_file[:-7] + "failed.txt"
    write_file(failed_file, failed_list)


def main():
    # test_clone_one()

    # check global variable PYTHON_DIR
    print("REPO directory:" + PYTHON_DIR)
    # for _, dir, file in os.walk(PYTHON_DIR):
    #     assert dir == [], "repo dir should be empty"
    #     assert file == [], "repo dir should be empty"
    clone_list(PYTHON_REPO_LIST, PYTHON_DIR, PYTHON_LOG_PATH)

    # check global variable JAVA_DIR
    # print("REPO directory:" + JAVA_DIR)
    # for _, dir, file in os.walk(JAVA_DIR):
    #     assert dir == [], "repo dir should be empty"
    #     assert file == [], "repo dir should be empty"
    # clone_list(JAVA_REPO_LIST, JAVA_DIR, JAVA_LOG_PATH)


if __name__ == "__main__":
    main()
