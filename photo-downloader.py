import instaloader


def download_photos(username):
    loader = instaloader.Instaloader()

    try:
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
    download_photos(user_name)
