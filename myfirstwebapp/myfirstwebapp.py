from flask import Flask, render_template, request, session
import vsearch
from checker import check_logged_in
from DBcm import UseDataBase


app = Flask(__name__)


app.config['dbconfig'] = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password':'vsearchpasswd',
                'database':'vsearchlogDB'}


def log_request(req:'flask_request', res:str) -> None:
    with UseDataBase(app.config['dbconfig']) as cursor:
        sql = """insert into log (phrase, letters, ip, browser_string, results)
                 values
                 (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (req.form['phrase'],
                             req.form['letters'],
                             req.remote_addr,
                             req.user_agent.browser,
                             res,))


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    title = 'Welcome to search4letters on the web!'
    return render_template('entry.html',
                           the_title=title)


@app.route('/search4', methods = ['GET', 'POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'This is you(R)e results'
    results = str(vsearch.search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print('Something wrong: ', str(err))
    return render_template('results.html',
                             the_title = title,
                             the_phrase = phrase,
                             the_letters = letters,
                             the_results = results,)


@app.route('/viewlog')
@check_logged_in
def viewlog() -> 'html':
    title = 'View Log'
    with UseDataBase(app.config['dbconfig']) as cursor:
        sql = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(sql)
        contents = cursor.fetchall()


    titles = ('phrase', 'letters', 'Remote_addr', 'User_agent', 'Results')


    return render_template('viewlog.html',
                           the_title = title,
                           the_row_titles = titles,
                           the_data = contents,)



@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are logged in.'


@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are not loggid in'


app.secret_key = '23451969as'

if __name__ == '__main__':
    app.run(debug=True)