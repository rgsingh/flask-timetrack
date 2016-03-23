'''
Created on Mar 19, 2016

@author: rsingh
@summary: Demonstrates the use of basic routes, templates 
          and context processors.
'''

from app import app
from flask.templating import render_template

title = 'TaskTrack'

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'John Smith'} #fake user
    return render_template('index.tmpl',
                           user=user)
@app.context_processor    
def utility_processor():
    def format_version(version, prefix='v'):
        return prefix+version
    def get_title():
        return title if title != '' else 'No title here' 
    return dict(format_version=format_version,
                get_title=get_title)
