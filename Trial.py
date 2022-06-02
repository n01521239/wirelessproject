
from github import Github
my_git = Github("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")

for repo in my_git.get_user().get_repos():
        print(repo.name)

wireless_project = my_git.get_repo("n01521239/wirelessproject")
contents = wireless_project.get_contents("")
for content_file in contents:
    print(content_file)

user = my_git.get_user()
repo = user.create_repo('test')
repo.create_file("text.txt","commit","this is test")
