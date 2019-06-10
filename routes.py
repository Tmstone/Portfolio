from config import app
from controllers import *

app.add_url_rule('/', view_func=index)
app.add_url_rule('/nav', view_func=nav)
