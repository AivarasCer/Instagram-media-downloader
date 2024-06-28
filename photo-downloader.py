import instaloader


def download_photos(username, login_user, login_pass):
    loader = instaloader.Instaloader()

    try:
        loader.login(login_user, login_pass)
        print(f'Logged in as {login_user}')

        loader.download_profile(username, profile_pic_only=False)
        print(f'Photos from {username} have been downloaded successfully.')
    except instaloader.exceptions.ProfileNotExistsException:
        print(f'The profile {username} does not exist.')
    except instaloader.exceptions.LoginRequiredException:
        print(f'You need to be logged in to download photos from this profile.')
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f'The profile {username} is private. You need to follow the profile to download photos.')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    user_name = input("Enter the Instagram username: ")
    user_login = input("Enter your Instagram username: ")
    pass_login = input("Enter your Instagram password: ")
    download_photos(user_name, user_login, pass_login)
