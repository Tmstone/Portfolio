from config import app
from controllers import *

app.add_url_rule('/', view_func=index)
app.add_url_rule('/nav', view_func=nav)

app.add_url_rule('/about', view_func=about)
app.add_url_rule('/projects', view_func=projects)
app.add_url_rule('/contact',view_func=contact)
app.add_url_rule('/jackfruit', view_func=login)
