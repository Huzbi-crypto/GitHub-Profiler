import getpass
import argparse
from github import Github
from datetime import datetime, timezone

def parse_arguments():
 parser = argparse.ArgumentParser(description='Get GitHub user info')
 parser.add_argument('username', nargs='?', help='GitHub username')
 return parser.parse_args()

def get_user_info(username, github_token):
  if github_token:
     g = Github(github_token)
  else:
     g = Github()
  creation_date = g.get_user(username).created_at
  return creation_date

def calculate_account_age(creation_date):
  now = datetime.now(timezone.utc)
  return now - creation_date

def convert_timedelta_to_years(timedelta):
  age_in_years = timedelta.days / 365
  return round(age_in_years, 2) 

def get_last_commit_date(username, github_token):
  if github_token:
     g = Github(github_token)
  else:
     g = Github()
  user = g.get_user(username)
  repos = user.get_repos()
  last_commit_date = None
  for repo in repos:
      commits = repo.get_commits()
      if commits.totalCount > 0:
          last_commit = commits[0]
          if last_commit_date is None or last_commit.commit.author.date > last_commit_date:
              last_commit_date = last_commit.commit.author.date
  return last_commit_date

def get_last_seen_date(username, github_token):
  if github_token:
     g = Github(github_token)
  else:
     g = Github()
  user = g.get_user(username)
  events = user.get_events()
  last_seen_date = None
  for event in events:
      if last_seen_date is None or event.created_at > last_seen_date:
          last_seen_date = event.created_at
  return last_seen_date

def main():
  args = parse_arguments()
  username = args.username

  if username is None:
     username = input('Enter the GitHub user\'s username: ')

  github_token = getpass.getpass('Enter your GitHub token (optional): ') # used getpass to hide the token

  creation_date = get_user_info(username, github_token)
  print(f'Created at => {creation_date}')

  account_age = calculate_account_age(creation_date)
  print(f'The GitHub account age is => {account_age}')

  account_age_years = convert_timedelta_to_years(account_age)
  print(f'The GitHub account age in years is => {account_age_years}')

  last_commit_date = get_last_commit_date(username, github_token)
  print(f'The GitHub last commit date is => {last_commit_date}')

  last_seen_date = get_last_seen_date(username, github_token)
  print(f'The GitHub last seen date is => {last_seen_date}')

if __name__ == "__main__":
  main()
