#coding=utf-8
import web
import markdown

import model
from settings import *
from admin import check_login

########################################################################
class redirect:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

    #----------------------------------------------------------------------
    def GET(self):
        """"""
        web.seeother('/blog/1')      


########################################################################
class index:
    """SHow Home Page"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    #----------------------------------------------------------------------
    def GET(self):
        """"""
        active = 1
        context = "Welcom to my Blog."
        return model.render_template('main.html', context = context, active = active)


########################################################################
class show_scrap_all:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""


    #----------------------------------------------------------------------
    def GET(self, id):
        """"""

        active = 2
        NavNum = 7
        id = int(id)

        if id is None:
            id = 1

        results = db.query("SELECT COUNT(*) AS numbers FROM scrap WHERE is_deleted = 0")
        pages_all = results[0].numbers

        if pages_all % NavNum == 0:
            pages = pages_all / NavNum

        else:
            pages = pages_all / NavNum + 1

        offset = (id - 1) * NavNum
        scrap = db.select('scrap', where = 'is_deleted = 0', limit=NavNum, offset = offset, order = 'id desc')

        if len(scrap) == 0:
            return 'No scrap!'

        return model.render_template('blog/index.html', scrap = scrap, pages = pages, active = active, id = id)            


########################################################################
class show_scrap:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    #----------------------------------------------------------------------
    def GET(self, title):
        """"""
        active = 2
        #if web.ctx.ip != '127.0.0.1':
        try:
            results = db.select('scrap', what = 'file_type,counter,content', where = 'title = $title and is_deleted = 0', vars = locals())
            results = results[0]
            path = results.file_type
            counter = results.counter
            content = results.content

            if 'md' in path:

                scrap = markdown.markdown(content, extensions=['markdown.extensions.extra'])

                #scrap = model.md2html(path)

            else:
                scrap = content

            db.query('UPDATE scrap SET scrap.counter=scrap.counter+1 WHERE title=$title', vars = locals())

        except Exception as e:
            print str(e)
            return "Markdown file not found!"


        return model.render_template('blog/show_scrap.html', scrap = scrap, active = active, counter = counter)