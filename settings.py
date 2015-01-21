#coding=utf-8
import web

Scrap_DIR = "static/scraps/"

web.config.debug = False
web.config.session_parameters['timeout'] = 60 * 10
web.config.session_parameters['ignore_change_ip'] = False
#web.config.session_parameters['secret_key'] = '!AvadD03FDS34%%Sdfas035$$asd'

db = web.db.database(
    dbn = 'mysql',
    user = 'twifi',
    pw = 'twifi123$',
    db = 'twifi_dev',
    port = 3306
)

urls = (
    '/', 'index',
    '/blog', 'redirect',
    '/add', 'add',
    '/del', 'delete', 
    '/blog/(\d+)', 'show_scrap_all',
    '/tag/(.*)', 'search_by_tag',
    '/archive/(.*)', 'search_by_archive',
    '/scrap/(.*)', 'show_scrap',
    '/add_scrap', 'add_scrap',
    '/del_scrap', 'del_scrap',
    '/add_tag', 'add_tag', 
    '/login', 'login',
    '/logout', 'logout', 
    '/admin', 'admin', 
)