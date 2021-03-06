import webapp2
import jinja2
import os
#import PyV8


from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Profile(ndb.Model):
    name = ndb.StringProperty()
    hometown = ndb.StringProperty()
    email = ndb.StringProperty()
    score = ndb.IntegerProperty()
    #image = ndb.StringProperty()

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
        my_vars = {
        "name": profile.name
        }
        template = jinja_environment.get_template('templates/welcome.html')
        self.response.out.write(template.render(my_vars))

class QuestionHandler(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        profile = Profile.query().filter(Profile.email == current_user.email()).get()
        current_email = current_user.email()
        logout_url = users.create_logout_url('/')

        template_vars = {
        "logout_url": logout_url,
        'profile': profile,
        'current_email':current_email,
        }


        template = jinja_environment.get_template('templates/questions.html')
        self.response.out.write(template.render(template_vars))

    def post(self):
        current_user = users.get_current_user()
        current_email = current_user.email()
        profile = Profile.query().filter(Profile.email == current_user.email()).get()
         #js.check()
        profile.score = 5
        profile.put()

        template_vars = {
            'profile': profile,
            'current_email':current_email,
        }


        template = jinja_environment.get_template('templates/questions.html')
        self.response.out.write(template.render(template_vars))

        self.redirect('/')


#class Global(PyV8.JSClass):
#    pass

#with PyV8.JSContext(Global()) as ctxt:
#    totalpts = ctxt.eval("var totalpts = localStorage.getItem("score")");

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


        #current_user = users.get_current_user()
        #profile = Profile.query().filter(Profile.email == current_user.email()).get()
         #js.check()
        #profile.score += 1
        #profile.put()

        template = jinja_environment.get_template('templates/garden.html')
        self.response.out.write(template.render())


class LeaderboardHandler(webapp2.RequestHandler):
    def get(self):
        profiles = Profile.query().order(-Profile.score).fetch(5)
        logout_url = users.create_logout_url('/')
        template_vars = {
            'logout_url':logout_url,
            'profiles': profiles,
        }
        template = jinja_environment.get_template('templates/leaderboard.html')
        self.response.out.write(template.render(template_vars))

class CustomizeHandler(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        profile = Profile.query().filter(Profile.email == current_user.email()).get()


        template_vars = {
            'profile': profile,
        }

        template = jinja_environment.get_template('templates/customize.html')
        self.response.out.write(template.render(template_vars))

    def post(self):
        current_user = users.get_current_user()
        profile = Profile.query().filter(Profile.email == current_user.email()).get()
        name = self.request.get('name')
        profile.name = name
        hometown = self.request.get('hometown')
        profile.hometown = hometown
        profile.put()
        self.redirect('/myprofile')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler),
    ('/profile', ProfileHandler),
    ('/questions', QuestionHandler),
    ('/myprofile', MyProfileHandler),
    ('/mygarden', GardenHandler),
    ('/leaderboard', LeaderboardHandler),
    ('/customize', CustomizeHandler)

], debug=True)
