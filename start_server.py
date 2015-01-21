import web
import model

from mysite import *
from admin import *
from search import * 
from settings import * 

def session_hook():
    """"""
    web.ctx.session = session
    

if __name__ == '__main__':
    app = web.application(urls, globals())
    session = web.session.Session(app, web.session.DBStore(db, 'sessions'), initializer={'email': None, 'passwd': None,})
    app.add_processor(web.loadhook(session_hook))
    app.run()