from config import app
from controllers import index, nav, about, projects, contact, new_contact, login, footer

app.add_url_rule('/', view_func=index)
app.add_url_rule('/nav', view_func=nav)
app.add_url_rule('/footer', view_func=footer)
#refactor /about to /experience
app.add_url_rule('/about', view_func=about)
app.add_url_rule('/projects', view_func=projects)
app.add_url_rule('/contact',view_func=contact)
app.add_url_rule('/jackfruit', view_func=login)

app.add_url_rule('/new/contact', view_func=new_contact, methods=['POST'])
