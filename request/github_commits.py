import requests

def get_commits(user, repo, limit=20, per_page=100):
    all_commits = []
    page = 1

    while len(all_commits) < limit:
        url = f"https://api.github.com/repos/{user}/{repo}/commits"
        params = {"per_page": per_page, "page": page}
        response = requests.get(url, params=params)
        response.raise_for_status()

        commits = response.json()
        if not commits:
            break

        all_commits.extend(commits)
        page += 1

    return all_commits[:limit]

def merge_sort(commits):
    if len(commits) <= 1:
        return commits

    mid = len(commits) // 2
    left = merge_sort(commits[:mid])
    right = merge_sort(commits[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]['commit']['author']['date'] <= right[j]['commit']['author']['date']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result