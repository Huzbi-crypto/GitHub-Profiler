from urllib.parse import urlparse
from github import Github
from datetime import datetime, timezone

def get_username_from_url(url):
    parsed_url = urlparse(url)
    return parsed_url.path.split('/')[-1]

def get_user_info(username):
    g = Github()
    creation_date = g.get_user(username).created_at
    return creation_date

def calculate_account_age(creation_date):
    now = datetime.now(timezone.utc)
    return now - creation_date

def convert_timedelta_to_years(timedelta):
    age_in_years = timedelta.days / 365
    return round(age_in_years, 2) 

def get_last_commit_date(username):
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


# get the user's URL
url = input('Enter the GitHub user\'s URL: ')
username = get_username_from_url(url) # get the username from the URL
print(f'The GitHub username is => {username}')

# get the user's creation date
creation_date = get_user_info(username)
print(f'Created at => {creation_date}')

# calculate the account age
account_age = calculate_account_age(creation_date)
print(f'The GitHub account age is => {account_age}')

# convert the account age to years
account_age_years = convert_timedelta_to_years(account_age)
print(f'The GitHub account age in years is => {account_age_years}')

# get the last commit date
last_commit_date = get_last_commit_date(username)
print(f'The GitHub last commit date is => {last_commit_date}')

input('Press ENTER to exit...')