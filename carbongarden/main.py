import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Profile(ndb.Model):
    name = ndb.StringProperty()
    hometown = ndb.StringProperty()
    email = ndb.StringProperty()
    score = ndb.IntegerProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        profile=""
        current_user = users.get_current_user()
        login_url = users.create_login_url('/')
        logout_url = users.create_logout_url('/')
        if current_user:
            profile = Profile.query().filter(Profile.email == current_user.email()).get()

         # Force the user to log in if they haven't already.
        if not current_user:
            login_url = users.create_login_url('/profile')

        template_vars = {
        "current_user": current_user,
        "login_url": login_url,
        "logout_url": logout_url,
        'profile':profile,
        }

        template = jinja_environment.get_template('templates/welcome.html')
        self.response.out.write(template.render(template_vars))

    def post(self):
        email = users.get_current_user().email()
        self.redirect('/')

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        profiles = Profile.query().fetch()
        current_user = users.get_current_user()
        email = current_user.email()
        profile_query = Profile.query().filter(Profile.email == email)
        profile_exists = profile_query.get()

        if not profile_exists:
            template_vars = {
                'profiles': profiles,
                'current_user': current_user,
            }

            template = jinja_environment.get_template('templates/profile.html')
            self.response.write(template.render(template_vars))
        else:
            self.redirect('/')

    def post(self):
        user = users.get_current_user()
        email= user.email()
        name = self.request.get('name')
        hometown = self.request.get('hometown')
        score = 0
        profile = Profile(name=name,hometown=hometown,email=email, score=score)
        profile.put()
        self.redirect('/')

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        my_vars = {"name": "User"}
        template = jinja_environment.get_template('templates/welcome.html')
        self.response.out.write(template.render(my_vars))

class QuestionHandler(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        #p2 = k.get()
        current_user.score = 9 #SOSOSOSOOSOS
        score = current_user.score
        #current_user.put()

        template_vars = {
        'score' : score,
        }
        template = jinja_environment.get_template('templates/questions.html')
        self.response.out.write(template.render())

class MyProfileHandler(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        profile = Profile.query().filter(Profile.email == current_user.email()).get()

        template_vars = {
            'profile': profile,
            'logout_url':logout_url,
        }

        template = jinja_environment.get_template('templates/myprofile.html')
        self.response.write(template.render(template_vars))

class GardenHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/garden.html')
        self.response.out.write(template.render())

class LeaderboardHandler(webapp2.RequestHandler):
    def get(self):
        profiles = Profile.query().fetch()

        template_vars = {
            'profiles': profiles,
        }

        template = jinja_environment.get_template('templates/leaderboard.html')
        self.response.out.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler),
    ('/profile', ProfileHandler),
    ('/questions', QuestionHandler),
    ('/myprofile', MyProfileHandler),
    ('/mygarden', GardenHandler),
    ('/leaderboard', LeaderboardHandler),

], debug=True)
