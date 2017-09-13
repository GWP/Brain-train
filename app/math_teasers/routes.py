from flask import Blueprint, render_template, flash, redirect, request, redirect, session, make_response, url_for
from datetime import datetime
from app import db
from app.math_teasers.models import User, Problem
from app import logging

math_teasers = Blueprint('math_teasers', __name__)


@math_teasers.route('/')
def main_page():
    if 'user' in session:
        return render_template('main_page.html', welcome='Welcome, {}'.format(session['user']))
    else:
        return render_template('main_page.html')


@math_teasers.route('/question_and_answer', methods=['GET', 'POST'])
def processProblem():
    logging.info("The request is: {} and {}".format(request.form['question'], request.form['answer']))
    logging.info("Time elapsed: {}".format(request.form['time']))
    logging.info("Problem type is: {}".format(request.form['ptype']))
    if 'user' in session:
        logging.info("The user is: {}".format(session['user']))
        user = User.query.filter_by(nickname=session['user']).first()
        post = Problem(question=request.form['question'], answer=request.form['answer'], problem_type=request.form['ptype'], time_to_complete=request.form['time'], author=user)
        db.session.add(post)
        db.session.commit()
    return "Correct!"


@math_teasers.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username, password, email = request.form['username'], request.form['password'], request.form['email']
        does_user_exist = User.query.filter_by(nickname=username).first()
        if not does_user_exist:
            new_user = User(nickname=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            session['user'] = username
            return render_template('main_page.html', welcome='Welcome, {}'.format(session['user']))
        else:
            user_pw = User.query.filter_by(nickname=username).first().password
            if user_pw == password:
                session['user'] = username
                logging.info("setting session user")
                logging.info("user is {}".format(session['user']))
                return redirect(url_for('math_teasers.main_page'))
            else:
                return render_template('login.html', message="Invalid password, please try again")


@math_teasers.route('/logout', methods=['GET'])
def do_logout():
    session.pop('user')
    return redirect(url_for('math_teasers.main_page'))


@math_teasers.route('/userstats', methods=['GET', 'POST'])
def get_stats():
    if request.method == 'GET':
        logging.info("Doing a GET")
        if 'user' not in session:
            return redirect(url_for('do_login'))
        else:
            return render_template('stats.html')
    elif request.method == 'POST':
        if 'user' not in session:
            logging.info("No user!")
            return redirect(url_for('do_login'))
        logging.info("Getting stats for {}".format(session['user']))
        try:
            user = User.query.filter_by(nickname=session['user']).first()
            logging.info("we got this far with {}".format(user))
            problems = Problem.query.filter_by(author=user).all()
            logging.info("now we got the problems {}".format(problems))
            session['num_of_problems'] = len(problems)
            additions = [n for n in problems if n.problem_type == 'Addition']
            times = [int(n.time_to_complete) for n in additions]
            average = sum(times)/len(times)
            logging.info("Your average was {} milliseconds".format(average))
            return "Your {} for {} was {}".format("average time", "Addition", average)
        except Exception as e:
            logging.error("There is a problem finding the stats: {}".format(e))
        return "We have a problem"


def calculate_stat(ptype, query_type):
    user = User.query.filter_by(nickname=session['user']).first()
    logging.info("we got this far with {}".format(user))
    problems = Problem.query.filter_by(author=user).all()
    logging.info("now we got the problems {}".format(problems))

    prob_map = {
        'Addition': [int(n.time_to_complete) for n in problems if n.problem_type == 'Addition'],
        'Subtraction': [int(n.time_to_complete) for n in problems if n.problem_type == 'Subtraction'],
        'Multiplication': [int(n.time_to_complete) for n in problems if n.problem_type == 'Multiplication'],
        'Division': [int(n.time_to_complete) for n in problems if n.problem_type == 'Division'],
        'Hexadecimal': [int(n.time_to_complete) for n in problems if n.problem_type == 'Hexadecimal']
    }

    def statify(x): return {'Average': sum(x)/len(x), 'Quickest': min(x)}

    stats = {prob_type: statify(prob_map[prob_type]) for prob_type in prob_map}

    return stats[ptype][query_type]
