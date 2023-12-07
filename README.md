# GitHub User Info Finder

## Overview

I just had an impulse to create a program/script that can calculate the age of a GitHub user's account based on their creation date. I know that GitHub has a feature that shows the age of an account, but I wanted to create my own program/script that can do the same thing.

Now, I want to add more features to this program/script, such as showing the last commit date of the user and the last seen date of the user. This impulse of mine has just started, so I will add more features to this program/script in the future.

## How to use

1. Clone this repository
2. Install the required packages using `pip install -r requirements.txt`.
3. Enter the name of the GitHub user as an argument when running the program/script:

```bash
python GitHub-User_Info.py <GITHUB_USER_NAME>
```

4. You can also enter the name as input when running the program/script:

```bash
python GitHub-User_Info.py
```

5. It will ask for GitHub API token as an optional input. If you don't have one, you can just press enter and it will use the default token. If you want to use your own token, you can enter it and it will use your token instead of the default token. That way, you can avoid getting rate limit.

### Prerequisites

 You will have to create a `.env` file with the following content:

```env
GITHUB_PERSONAL_ACCESS_TOKEN = <YOUR_PERSONAL_GITHUB_TOKEN>   
```

You can create a personal access token by following the instructions [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). Make sure to select the `user` scope when creating the token.

Or, you can edit the code and replace the `os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")` with your personal access token. If you are okay with getting rate limit, you can remove the first three lines after importing libraries and removing the variable from all `Github` objects.

## Future plans

- [x] Add a feature of showing the last commit date of the user.
- [x] Add a feature of showing the last seen date of the user.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.