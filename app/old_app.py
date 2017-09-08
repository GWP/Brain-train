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
# # import subprocess
# from models import db
#
# def sig_term_handler(signal, frame):
#     print("ta for now!")
#     db.drop_all(app=app)
#     sys.exit(0)
#
# signal.signal(signal.SIGINT, sig_term_handler)
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
# db.init_app(app)
# db.create_all(app=app)
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger('whetlog')
# # db = SQLAlchemy(app)
# # app.run(debug=True, threaded=True)
#
# # @app.route('/hello')
# # def hello():
# #     if 'user' in session:
# #         return render_template('hello.html', welcome='Welcome, {}'.format(session['user']))
# #     else:
# #         return render_template('hello.html')
#
#
#
# if __name__ == '__main__':
#     try:
#         # setup_app()
#         # db.create_all()
#         app.run(debug=True, threaded=True)
#     except KeyboardInterrupt:
#         db.drop_all()
#         sys.exit(0)
