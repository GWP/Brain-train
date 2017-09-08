# #!../virtual/bin/python3.6
#
# from flask import Flask, render_template, request, redirect, session, make_response, url_for
# from flask_sqlalchemy import SQLAlchemy
# from problem_generator import generate_problem, Add_Problem
# from util import is_valid_problem_input
# import logging
# import signal
# from datetime import datetime
# import sys
# import json
#
#
# # import subprocess
# # from models import db
#
# def sig_term_handler(signal, frame):
#     print("ta for now!")
#     db.drop_all()
#     sys.exit(0)
#
#
# signal.signal(signal.SIGINT, sig_term_handler)
#
#
# class MyFlask(Flask):
#     def get_send_file_max_age(self, name):
#         if name.lower().endswith('.css') or name.lower().endswith('.html') or name.lower().endswith('.js'):
#             return 5
#         return Flask.get_send_file_max_age(self, name)
#
#
# app = MyFlask(__name__)
# app.config.from_object('config')
# app.secret_key = 'a secret key'
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger('whetlog')
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     date_created = db.Column(db.DateTime)
#     date_modified = db.Column(db.DateTime)
#     nickname = db.Column(db.String(64), index=True, unique=True)
#     password = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=False)
#     problems = db.relationship('Problem', backref='author', lazy='dynamic')
#
#     @property
#     def is_authenticated(self):
#         return True
#
#     @property
#     def is_active(self):
#         return True
#
#     @property
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         try:
#             return unicode(self.id)  # python 2
#         except NameError:
#             return str(self.id)  # python 3
#
#     def __repr__(self):
#         return '<User {}>'.format(self.nickname)
#
#
# class Problem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.String(140))
#     # difficulty = db.Column(db.String(64))
#     answer = db.Column(db.String(140))
#     problem_type = db.Column(db.String(64))
#     timestamp = db.Column(db.DateTime)
#     time_to_complete = db.Column(db.String(120))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.question)
#
#
# @app.route('/hello')
# def hello():
#     if 'user' in session:
#         return render_template('hello.html', welcome='Welcome, {}'.format(session['user']))
#     else:
#         return render_template('hello.html')
#
#
# @app.route('/question_and_answer', methods=['GET', 'POST'])
# def processProblem():
#     logging.info("The request is: {} and {}".format(request.form['question'], request.form['answer']))
#     logging.info("Time elapsed: {}".format(request.form['time']))
#     logging.info("Problem type is: {}".format(request.form['ptype']))
#     if 'user' in session:
#         logging.info("The user is: {}".format(session['user']))
#         user = User.query.filter_by(nickname=session['user']).first()
#         post = Problem(question=request.form['question'], answer=request.form['answer'],
#                        problem_type=request.form['ptype'], time_to_complete=request.form['time'],
#                        timestamp=datetime.utcnow(), author=user)
#         db.session.add(post)
#         db.session.commit()
#     return "Correct!"
#
#
# @app.route('/', methods=['GET', 'POST'])
# def ask_user():
#     print("we're here")
#     if request.method == 'POST':
#         print("now here with info: ", request.form['problem_type'])
#         problem_type = request.form['problem_type']
#         difficulty = request.form['difficulty']
#         if is_valid_problem_input(problem_type, difficulty) is True:
#             return redirect('/problem/{}/{}'.format(problem_type, difficulty))
#         else:
#             print("It's an error")
#             return render_template('main.html', error='There is a problem with your inputs! Please try again')
#     if request.method == 'GET':
#         session['solved'] = True
#         return render_template('main.html')
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def do_login():
#     # from models import User
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         username, password, email = request.form['username'], request.form['password'], request.form['email']
#         does_user_exist = User.query.filter_by(nickname=username).first()
#         if not does_user_exist:
#             new_user = User(nickname=username, password=password, email=email)
#             db.session.add(new_user)
#             db.session.commit()
#             session['user'] = username
#             return render_template('hello.html', welcome='Welcome, {}'.format(session['user']))
#         else:
#             user_pw = User.query.filter_by(nickname=username).first().password
#             if user_pw == password:
#                 session['user'] = username
#                 logging.info("setting session user")
#                 logging.info("user is {}".format(session['user']))
#                 return redirect(url_for('hello'))
#             else:
#                 return render_template('login.html', message="Invalid password, please try again")
#
#
# @app.route('/logout', methods=['GET'])
# def do_logout():
#     session.pop('user')
#     return redirect(url_for('hello'))
#
#
# @app.route('/problem', methods=['GET', 'POST'])
# @app.route('/problem/<ptype>/<difficulty>', methods=['GET', 'POST'])
# def do_problem(ptype, difficulty):
#     logger.info("do_problem called with ptype={} and difficulty={}".format(ptype, difficulty))
#
#     if 'solved' not in session:
#         session['solved'] = False
#     if 'question' not in session or session['solved'] is True:
#         problem = generate_problem(ptype, difficulty)
#         session['question'] = problem.question
#         session['answer'] = problem.answer
#         session['solved'] = False
#
#     if request.method == 'GET':
#         return render_template('problem.html', user_problem=session['question'], type=ptype, difficulty=difficulty)
#     if request.method == 'POST':
#         user_answer = request.form['user_answer']
#         print("User answer: ", user_answer, "type is: ", type(user_answer))
#         print("Real answer: ", session['answer'], "type is: ", type(session['answer']))
#         logging.info("User's answer is {} with type {}, and the real answer is {} with type {}"
#                      .format(user_answer, type(user_answer), session['answer'], type(session['answer'])))
#         if float(user_answer) == session['answer']:
#             session['solved'] = True
#             resp = make_response(render_template('problem.html', status='Correct!'))
#             resp.headers.set('Cache-Control', 'public, max-age=0')
#             return resp
#         else:
#             resp = make_response(render_template('problem.html', user_problem=session['question'],
#                                                  status='Incorrect! Try again', type=ptype, difficulty=difficulty))
#             resp.headers.set('Cache-Control', 'public, max-age=0')
#             return resp
#
#
# @app.route('/userstats', methods=['GET', 'POST'])
# def get_stats():
#     if request.method == 'GET':
#         logging.info("Doing a GET")
#         if 'user' not in session:
#             return redirect(url_for('do_login'))
#         else:
#             return render_template('stats.html')
#     elif request.method == 'POST':
#         if 'user' not in session:
#             logging.info("No user!")
#             return redirect(url_for('do_login'))
#         logging.info("Getting stats for {}".format(session['user']))
#         try:
#             user = User.query.filter_by(nickname=session['user']).first()
#             logging.info("we got this far with {}".format(user))
#             problems = Problem.query.filter_by(author=user).all()
#             logging.info("now we got the problems {}".format(problems))
#             session['num_of_problems'] = len(problems)
#             additions = [n for n in problems if n.problem_type == 'add']
#             times = [int(n.time_to_complete) for n in additions]
#             average = sum(times) / len(times)
#             logging.info("Your average was {} milliseconds".format(average))
#             return "Your {} for {} was {}".format("average time", "Addition", average)
#         except Exception as e:
#             logging.error("There is a problem finding the stats: {}".format(e))
#         return "We have a problem"
#
#
# def calculate_stat(ptype, query_type):
#     user = User.query.filter_by(nickname=session['user']).first()
#     logging.info("we got this far with {}".format(user))
#     problems = Problem.query.filter_by(author=user).all()
#     logging.info("now we got the problems {}".format(problems))
#
#     prob_map = {
#         'Addition': [int(n.time_to_complete) for n in problems if n.problem_type == 'Addition'],
#         'Subtraction': [int(n.time_to_complete) for n in problems if n.problem_type == 'Subtraction'],
#         'Multiplication': [int(n.time_to_complete) for n in problems if n.problem_type == 'Multiplication'],
#         'Division': [int(n.time_to_complete) for n in problems if n.problem_type == 'Division'],
#         'Hexadecimal': [int(n.time_to_complete) for n in problems if n.problem_type == 'Hexadecimal']
#     }
#
#     def statify(x): return {'Average': sum(x) / len(x), 'Quickest': min(x)}
#
#     stats = {prob_type: statify(prob_map[prob_type]) for prob_type in prob_map}
#
#     return stats[ptype][query_type]
#
#
# if __name__ == '__main__':
#     try:
#         db.create_all()
#         app.run(debug=True, threaded=True)
#     except KeyboardInterrupt:
#         db.drop_all()
#         sys.exit(0)
