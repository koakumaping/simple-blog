#coding=utf-8
import os
import web
import markdown
import time

import model
from settings import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#----------------------------------------------------------------------
def check_login(pre_page):
    """"""
    session = web.ctx.session
    if session.email == None or session.passwd == None:
        web.seeother('/login')

    else:
        pass

#----------------------------------------------------------------------
def check_scrap(title):
    """"""
    scrap = db.select('scrap', where = 'title = $title and is_deleted = 0', order = 'id desc', vars = locals())
    
    if len(scrap) != 0:
        return True
    else:
        return False
    
########################################################################
class admin:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        
    #----------------------------------------------------------------------
    def GET(self):
        """"""
        check_login('/admin')
        active = 1
        time_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return model.render_template('admin/index.html', active = active, time_date = time_date)
        
    
########################################################################
class login:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    #----------------------------------------------------------------------
    def GET(self):
        """"""
        session = web.ctx.session
        #session.username = 'login get'
        return model.render_template('admin/login.html')

    #----------------------------------------------------------------------
    def POST(self):
        """"""
        session = web.ctx.session
        i = web.input()
        
        checkbox = web.input(checkbox = [])
        cks = checkbox.get('checkbox')
        
        if i.email == 'test@163.com' and i.password == '123':
            
            if cks != []:
                web.config.session_parameters['timeout'] = 60 * 24
                print web.config.session_parameters['timeout']
            else:
                pass
            
            session.email = i.email
            session.passwd = i.password
            web.seeother('/admin')
            
        else:
            return "login faild."


########################################################################
class logout:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass


    #----------------------------------------------------------------------
    def GET(self):
        """"""
        session = web.ctx.session
        session.email = None
        session.passwd = None
        web.seeother('/login')


########################################################################
class add_scrap:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    #----------------------------------------------------------------------
    def POST(self):
        """"""
        check_login('/add_scrap')
        i = web.input()
        markdown_file = web.input(myfile={})
        file_name = markdown_file['myfile'].filename
        file_value = markdown_file['myfile'].value
        name, ext = os.path.splitext(file_name)

        if check_scrap(i.title):
            return 'Scrap alredy exists.'

        if i.title != "" and ext == ".md":

            try:
                markdown_value = file_value
                db.insert('scrap', title = i.title, file_type = ext.split('.')[1], \
                          content = markdown_value, archive = i.archive, tag = i.tag)

            except Exception as e:
                print str(e)
                return "Upload Markdown file faild!"

        if i.tag != "":
            pass

        else:
            return "not Markdown file!"

        raise web.seeother('/blog')


    #----------------------------------------------------------------------
    def GET(self):
        """"""
        check_login('/add_scrap')
        active = 2
        tags = db.select('scrap_tags', what = 'tag')
        return model.render_template('admin/show_add_scrap.html', tags = tags, active = active)


########################################################################
class del_scrap:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        pass

    #----------------------------------------------------------------------
    def POST(self):
        """"""
        i = web.input()
        title = i.title
        if title != "":
            #db.update('scrap', where = 'title=$i.title', vars = locals())
            db.query('UPDATE scrap SET is_deleted = 1 WHERE title=$title and is_deleted = 0', \
                     vars = locals())
        raise web.seeother('/blog')


    #----------------------------------------------------------------------
    def GET(self):
        """"""

        check_login('/del_scrap')
        active = 3
        return model.render_template('admin/show_del_scrap.html', active = active)


########################################################################
class add_tag:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    
    #----------------------------------------------------------------------
    def POST(self):
        """"""
        i = web.input()
        
        if i.tag != "":
            db.insert('scrap_tags', tag = i.tag)
    
        web.seeother('/admin')
        
    
    #----------------------------------------------------------------------
    def GET(self):
        """"""
        check_login('/add_tag')
        active = 4
        
        return model.render_template('admin/show_add_tag.html', active = active)