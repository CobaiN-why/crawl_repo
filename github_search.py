from github import Github
from time import sleep
import os

COLLECTION_DIR = "./"

with open(os.path.join(COLLECTION_DIR, "github_token.txt")) as f:
    token = f.read()

g = Github(token)

def search_top1000_csharp():
    repository_path_csharp = os.path.join(COLLECTION_DIR, "top_1000_csharp_list.txt")
    star_path_csharp = os.path.join(COLLECTION_DIR, "top_1000_stars_csharp.txt")
    repo_dict = {}

    # 因为网络问题，连续跑四次，查漏补缺
    csharp_repositories = g.search_repositories(query='language:c#', sort='stars', order='desc')
    for repo in csharp_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    csharp_repositories = g.search_repositories(query='language:c#', sort='stars', order='desc')
    for repo in csharp_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    csharp_repositories = g.search_repositories(query='language:c#', sort='stars', order='desc')
    for repo in csharp_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)


    csharp_repositories = g.search_repositories(query='language:c#', sort='stars', order='desc')
    for repo in csharp_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    sorted_repo = sorted(repo_dict.items(), key=lambda x: x[1], reverse=True)
    print(len(sorted_repo))

    with open(repository_path_csharp, "w") as f:
        with open(star_path_csharp, "w") as star:
            for clone_url, stars in sorted_repo:
                print(clone_url)
                f.write(clone_url)
                f.write("\n")

                star.write(str(stars))
                star.write("\n")
    
    assert len(sorted_repo) > 1000, "Not enough dirs, it should be larger than 1000 (sometimes 1020)"

def search_top1000_java():
    repository_path_java = os.path.join(COLLECTION_DIR, "top_1000_java_list.txt")
    star_path_java = os.path.join(COLLECTION_DIR, "top_1000_stars_java.txt")
    repo_dict = {}
    
    # 因为网络问题，连续跑四次，查漏补缺
    java_repositories = g.search_repositories(query='language:java', sort='stars', order='desc')
    for repo in java_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    java_repositories = g.search_repositories(query='language:java', sort='stars', order='desc')
    for repo in java_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    java_repositories = g.search_repositories(query='language:java', sort='stars', order='desc')
    for repo in java_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    java_repositories = g.search_repositories(query='language:java', sort='stars', order='desc')
    for repo in java_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    sorted_repo = sorted(repo_dict.items(), key=lambda x: x[1], reverse=True)
    print(len(sorted_repo))

    with open(repository_path_java, "w") as f:
        with open(star_path_java, "w") as star:
            for clone_url, stars in sorted_repo:
                print(clone_url)
                f.write(clone_url)
                f.write("\n")

                star.write(str(stars))
                star.write("\n")

    
    assert len(sorted_repo) > 1000, "Not enough dirs, it should be larger than 1000 (sometimes 1020)"


def search_top1000_type(lang_type):
    repository_path = os.path.join(COLLECTION_DIR, "top_1000_"+lang_type+"_list.txt")
    star_path = os.path.join(COLLECTION_DIR, "top_1000_stars_"+lang_type+".txt")
    repo_dict = {}
    
    # 因为网络问题，连续跑四次，查漏补缺
    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

    lang_repositories = g.search_repositories(query='language:'+lang_type, sort='stars', order='desc')
    for repo in lang_repositories:
        print(repo.clone_url)
        repo_dict[repo.clone_url] = repo.stargazers_count
        sleep(0.03)

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
