import shutil
import git
import os
from datetime import datetime


class Progress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print('update(%s/%s), Message:%s' % (cur_count, max_count, message))
        if cur_count == max_count:
            print("OK")


global CSHARP_REPO_LIST
global JAVA_REPO_LIST
global CSHARP_DIR
global JAVA_DIR
CSHARP_LIST_PATH = "/mnt/qiuyuan/Data/top_1000_csharp/top_1000_csharp_list 202012231701.txt"
JAVA_LIST_PATH = "/mnt/qiuyuan/Data/top_1000_java/top_1000_java_list 202012231653.txt"
CSHARP_LOG_PATH = "/mnt/qiuyuan/Data/top_1000_csharp/top_1000_charp_list_log.txt"
JAVA_LOG_PATH = "/mnt/qiuyuan/Data/top_1000_java/top_1000_java_list_log.txt"

with open(CSHARP_LIST_PATH) as f:
    csharp_list = list(f.readlines())

with open(JAVA_LIST_PATH) as f:
    java_list = list(f.readlines())

CSHARP_REPO_LIST = [url.replace("https:", "git:").strip()
                    for url in csharp_list]
JAVA_REPO_LIST = [url.replace("https:", "git:").strip() for url in java_list]

CSHARP_DIR = "/mnt/qiuyuan/Data/top_1000_csharp/projects"
JAVA_DIR = "/mnt/qiuyuan/Data/top_1000_java/projects"
REPO_DIR = os.path.join(JAVA_DIR, "projects")

# check global variable CSHARP_REPO_LIST
assert len(CSHARP_REPO_LIST) == len(list(set(CSHARP_REPO_LIST)))
assert len(CSHARP_REPO_LIST) >= 1020

# check global variable JAVA_REPO_LIST
assert len(JAVA_REPO_LIST) == len(list(set(JAVA_REPO_LIST)))
assert len(JAVA_REPO_LIST) >= 1020


def test_clone_one():
    # clone_one(JAVA_REPO_LIST[0], JAVA_DIR)
    clone_one(CSHARP_REPO_LIST[0], CSHARP_DIR)


def clone_one(git_url, to_dir, rank=None):
    assert git_url.startswith("git://"), git_url
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


def clone_list(repo_list, to_dir, log_file):
    with open(log_file, "w") as f:
        start = datetime.now().strftime("Time: %Y-%m-%d %H:%M\n")
        f.write(start)
    for index, repo in enumerate(repo_list):
        # e.g., top0001, top0002, top0003 etc.
        rank = "top%s_" % str(index+1).rjust(4, "0")
        git_url, pull_info = clone_one(repo, to_dir, rank)
        message = "%s || %s\n" % (git_url, pull_info)
        now = datetime.now().strftime("Time: %Y-%m-%d %H:%M\n")
        with open(log_file, "a+") as f:
            f.write(message)
            f.write(now)


def main():
    # test_clone_one()

    # check global variable CSHARP_DIR
    print("REPO directory:" + CSHARP_DIR)
    for _, dir, file in os.walk(CSHARP_DIR):
        assert dir == [], "repo dir should be empty"
        assert file == [], "repo dir should be empty"
    clone_list(CSHARP_REPO_LIST, CSHARP_DIR, CSHARP_LOG_PATH)

    # check global variable JAVA_DIR
    # print("REPO directory:" + JAVA_DIR)
    # for _, dir, file in os.walk(JAVA_DIR):
    #     assert dir == [], "repo dir should be empty"
    #     assert file == [], "repo dir should be empty"
    # clone_list(JAVA_REPO_LIST, JAVA_DIR, JAVA_LOG_PATH)


if __name__ == "__main__":
    main()
