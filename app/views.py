'''
Created on Mar 19, 2016

@author: rsingh
@summary: Demonstrates the use of basic routes, templates 
          and context processors.
'''

from app import app
from flask.templating import render_template
from flask import request
import json 

title = 'TaskTrack'
user = {'nickname': 'John Smith'} #fake user

@app.route('/')
@app.route('/index')
def index():
    with open('app/templates/tasks.json') as tasks_file:
        tasks = json.load(tasks_file)
        
    return render_template('index.html',
                           user=user,
                           tasks=tasks)

@app.route('/edittask')
def editpost():
    taskid = request.args.get('id')
    with open('app/templates/tasks.json') as tasks_file:
        # Filter python objects with list comprehensions
#         filtered_task = [x for x in tasks_file if x['taskid'] == taskid]
        filtered_task = [x for x in tasks_file if get_by_taskid(x,taskid)]
        task = json.dumps(filtered_task)
    return render_template('edittask.html', 
                           id=id, 
                           task=task)    
    
@app.context_processor    
def utility_processor():
    def format_version(version, prefix='v'):
        return prefix+version
    def get_title():
        return title if title != '' else 'No title here' 
    return dict(format_version=format_version,
                get_title=get_title,
                user=user)
    
    
def get_by_taskid(tasks, taskid):
    try:
        return tasks['taskid'] == taskid
    except (KeyError, TypeError):
        return False    
