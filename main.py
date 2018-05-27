#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        params = {"sporocilo": "Home message"}
        return self.render_template("home.html", params=params)

class LotoHandler(BaseHandler):

    def is_unique(self, num, loto_numbers):
        for key in loto_numbers:
            if num == loto_numbers[key]:
                return False
        return True

    def sort(self, loto_numbers):
        sorted = False
        while not sorted:
            sorted = True
            for n in range(7):
                key1 = "num" + str(n+1)
                key2 = "num" + str(n+2)
                num1 = loto_numbers[key1]
                num2 = loto_numbers[key2]
                if num1 > num2:
                    loto_numbers[key1] = num2
                    loto_numbers[key2] = num1
                    sorted = False
        return loto_numbers

    def get(self):
        loto_numbers = {}
        for n in range(8):
            while True:
                num = random.randint(1, 39)
                if self.is_unique(num, loto_numbers):
                    break
            key = "num" + str(n+1)
            loto_numbers.update({key: num})

        loto_numbers = self.sort(loto_numbers)
        return self.render_template("loto.html", params=loto_numbers)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto', LotoHandler),
], debug=True)
