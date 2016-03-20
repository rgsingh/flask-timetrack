'''
Created on Mar 19, 2016

@author: rsingh
@summary: Demonstrates the use of basic routes, templates 
          and context processors.
'''

from app import app
from flask.templating import render_template

title = 'Some Title'

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Carl Poppa'} #fake user
    return render_template('index.tmpl',
                           user=user)
@app.context_processor    
def utility_processor():
    def format_price(amount, currency=u'$'):
        return u'{1}{0:.2f}'.format(amount, currency)
    def get_title():
        return title if title != '' else 'No title here' 
    return dict(format_price=format_price,
                get_title=get_title)
