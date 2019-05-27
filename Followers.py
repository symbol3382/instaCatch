from instaloader import Instaloader, exceptions, Profile


class Followers:

    def login(self, username, password):
        self.username = username
        self.password = password
        self.obj = Instaloader()
        self.profile = ''

        try:
            self.obj.login(self.username, self.password)
        except exceptions.InvalidArgumentException:
            message = "Username does not exist"
        except exceptions.BadCredentialsException:
            message = "Invalid Password"
        except exceptions.ConnectionException:
            message = "Error in connecting with instagram"
        except exceptions.TwoFactorAuthRequiredException:
            message = "Two Factor Login is not yet supported <br> either wait for a weeks or disable it from account"
        else:
            # if login successfull and prepare profile for further methods
            self.profile = Profile.from_username(
                self.obj.context, self.username)
            print(self.profile.full_name)
            return True
        return message

    def get_followers_list(self):
        followers = set(self.profile.get_followers())
        return followers

    def get_user(self, username):
        profile = Profile.from_username(Instaloader().context, username)
        
        user = {'full_name': profile.full_name,'pic_url': profile.profile_pic_url}
        return user
