#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
        profile = Profile(name=name,hometown=hometown,email=email)
        profile.put()
        self.redirect('/')

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        my_vars = {"name": "User"}
        template = jinja_environment.get_template('templates/welcome.html')
        self.response.out.write(template.render(my_vars))

class QuestionHandler(webapp2.RequestHandler):
    def get(self):
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


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler),
    ('/profile', ProfileHandler),
    ('/questions', QuestionHandler),
    ('/myprofile', MyProfileHandler),

], debug=True)
