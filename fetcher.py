import requests
url = f"https://api.github.com/repos/sukantahirock/commit_fetcher/commits"
response = requests.get(url)
if response.status_code == 200:
    latest_commit = response.json()[0]
    sha = latest_commit['sha']
    message = latest_commit['commit']['message']
    print(f"Latest Commit Hash: {sha}")
    print(f"Message: {message}")
else:
    print("Failed to fetch commit data:", response.status_code)