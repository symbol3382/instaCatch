import instaloader
  
class Followers:

    def __init__(self, username, password):
        self.username = 'aadeezgauravatif'
        self.password = 'aAdeEz@1234' 
        self.obj = instaloader.Instaloader()
        self.obj.login(self.username, self.password)
 
    def get_followers_list(self):
        self.profile = instaloader.Profile.from_username(self.obj.context, self.username)
        followers = set(self.profile.get_followers())
        return followers