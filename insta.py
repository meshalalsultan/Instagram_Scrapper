import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'aman.kharwal')

print(type(profile))

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)

'''
#Need Login
# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieve the usernames of all followees
followees = [followee.username for followee in profile.get_followees()]
print(followers)
'''
'''
Downloading Posts from Another Profile
Getting posts from any profile is easy in python.
We just need to use get_posts().
I will this method on the profile of someone else.
To download each post, we need to loop over the generator object using .
download_post() method. Now let’s go through this:

'''
# Load a new profile
profile = instaloader.Profile.from_username(bot.context, 'wwe')

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")