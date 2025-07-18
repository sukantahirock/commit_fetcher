import requests
url = f"https://api.github.com/repos/sukantahirock/commit_fetcher/commits"
response = requests.get(url)
if response.status_code == 200:
    all_commits = response.json()

    for commit in all_commits:
        sha = commit['sha']
        message = commit['commit']['message']
        print(f"Commit Hash: {sha}")
        print(f"Message: {message}")
        print("-" * 50)
else:
    print("Failed to fetch commits. Status code:", response.status_code)

