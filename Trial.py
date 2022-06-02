
from github import Github
my_git = Github("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")

for repo in my_git.get_user().get_repos():
        print(repo.name)

wireless_project = my_git.get_repo("n01521239/wirelessproject")
contents = wireless_project.get_contents("")
for content_file in contents:
    print(content_file)