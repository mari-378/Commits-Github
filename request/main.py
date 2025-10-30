from github_commits import get_commits, merge_sort

if __name__ == "__main__":
    print("Executando o main.py...")
    
    user = ""
    repo = ""

    commits = get_commits(user, repo, limit=20)
    sorted_commits = merge_sort(commits)


    for i, c in enumerate(sorted_commits, start=1):
        date = c['commit']['author']['date']
        message = c['commit']['message'].split("\n")[0]
        print(f"{i:02d}. {date} — {message}")

