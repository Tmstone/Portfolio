from config import app
from controllers import *

add_url_rule('/', view_func=index)
add_url_rule('/nav', view_func=nav)
