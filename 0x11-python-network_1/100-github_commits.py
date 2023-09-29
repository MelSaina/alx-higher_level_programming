#!/usr/bin/python3
"""
Script that fetches the 10 most recent commits from a GitHub repository using the GitHub API.
Usage: ./100-github_commits.py <repository name> <owner name>
"""

import requests
import sys

def fetch_commits(repo_name, owner_name):
    """
    Fetch the 10 most recent commits from a GitHub repository using the GitHub API.

    Args:
        repo_name (str): The name of the GitHub repository.
        owner_name (str): The name of the repository owner.

    Returns:
        None

    """
    # GitHub API endpoint for fetching commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check the status code to ensure a successful request
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the first 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(f'Error: Unable to fetch commits. Status code: {response.status_code}')

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_commits(repo_name, owner_name)
