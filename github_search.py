from github import Github
from time import sleep
import os

COLLECTION_DIR = "./"

ACCESS_USERNAME = '7178986756@qq.com'
ACCESS_PWD = "Wang717898675"

with open(os.path.join(COLLECTION_DIR, "github_token.txt")) as f:
    token = f.read()

g = Github(token)
# g = Github(ACCESS_USERNAME, ACCESS_PWD)


def search_top1000_type(lang_type):
    repository_path = os.path.join(COLLECTION_DIR, "top_1000_"+lang_type+"_list.txt")
    star_path = os.path.join(COLLECTION_DIR, "top_1000_stars_"+lang_type+".txt")
    repo_dict = {}
    
    # 因为网络问题，连续跑四次，查漏补缺
    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(1)
        if len(repo_dict) % 100 == 0:
            print("===========================")
        if len(repo_dict) > 1500:
            break

    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(1)
        if len(repo_dict) % 100 == 0:
            print("===========================")
        if len(repo_dict) > 1500:
            break

    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(1)
        if len(repo_dict) % 100 == 0:
            print("===========================")
        if len(repo_dict) > 1500:
            break

    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(1)
        if len(repo_dict) % 100 == 0:
            print("===========================")
        if len(repo_dict) > 1500:
            break

    sorted_repo = sorted(repo_dict.items(), key=lambda x: x[1], reverse=True)
    print(len(sorted_repo))

    with open(repository_path, "w") as f:
        with open(star_path, "w") as star:
            for clone_url, stars in sorted_repo:
                print(clone_url)
                f.write(clone_url)
                f.write("\n")

                star.write(str(stars))
                star.write("\n")

    
    assert len(sorted_repo) > 1000, "Not enough dirs, it should be larger than 1000 (sometimes 1020)"


if __name__ == "__main__":
    # search_top1000_csharp()
    # search_top1000_java()
    search_top1000_type("java")
