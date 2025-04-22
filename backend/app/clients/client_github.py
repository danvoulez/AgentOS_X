import os
import httpx
import git

class GitHubClient:
    def __init__(self):
        self.pat = os.getenv("GITHUB_PAT")
        self.repo = os.getenv("GITHUB_REPO")
        self.headers = {"Authorization": f"token {self.pat}"}

    def clone_repo(self, clone_dir):
        git.Repo.clone_from(f"https://github.com/{self.repo}.git", clone_dir)

    def create_issue(self, title, body):
        url = f"https://api.github.com/repos/{self.repo}/issues"
        data = {"title": title, "body": body}
        response = httpx.post(url, json=data, headers=self.headers)
        return response.json()
