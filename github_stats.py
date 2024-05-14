from github import Github
import markdown
import os

# Replace 'YOUR_GITHUB_TOKEN' with your actual personal access token
ACCESS_TOKEN = os.environ.get('GITHUB_TOKEN')

# Create a GitHub instance using your access token
g = Github(ACCESS_TOKEN)

# Get the authenticated user
user = g.get_user()

# Fetch user data
username = user.login
public_repos = user.public_repos
followers = user.followers
following = user.following

# Generate the statistics as a Markdown badge
stats_badge = f"![GitHub Stats](https://img.shields.io/badge/Public%20Repos-{public_repos}-brightgreen?style=for-the-badge&logo=github)"

# Write the statistics to a file
with open("README.md", "w") as f:
    f.write(f"# GitHub Statistics for {username}\n\n")
    f.write(stats_badge)
    f.write(f"\n\nFollowers: {followers} | Following: {following}")