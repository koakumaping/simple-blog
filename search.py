#coding=utf-8
import web

import model
from settings import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


########################################################################
class search_by_tag:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    #----------------------------------------------------------------------
    def GET(self, tag):
        """"""

        scraps = db.select('scrap', where = 'tag=$tag and is_deleted = 0', vars = locals())
        return model.render_template('search/show_search_by_tag.html', scraps = scraps)


########################################################################
class search_by_archive:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    #----------------------------------------------------------------------
    def GET(self, archive):
        """"""

        scraps = db.select('scrap', where = 'archive=$archive and is_deleted = 0', vars = locals())
        return model.render_template('search/show_search_by_archive.html', scraps = scraps)
