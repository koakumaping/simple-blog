#coding=utf-8
import os
import codecs
import markdown
#import markdown2 as markdown
import jinja2

from jinja2 import Environment,FileSystemLoader

#----------------------------------------------------------------------
def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
        extensions=extensions,
    )
    jinja_env.globals.update(globals)

    #jinja_env.update_template_context(context)
    return jinja_env.get_template(template_name).render(context)


#----------------------------------------------------------------------
def md2html(md_file):

    '''从文件读取出md格式文件流'''
    input_file = codecs.open(md_file, mode='r', encoding='utf8')
    md = input_file.read()

    html = markdown.markdown(md) #对应普通语法解析
    #html = markdown.markdown(md, extensions=['markdown.extensions.extra']) #对应扩展语法解析

    return html


#----------------------------------------------------------------------
def evernote_html2html(html_file):

    '''从文件读取出md格式文件流'''
    html = ''

    with open(html_file, mode='r') as input_file:
        i = 0
        for text in input_file:
            i += 1
            if i > 17:
                if 'body' not in text:
                    html = html + text
                else:
                    pass
            else:
                pass

    return html