from flask import Flask, render_template, request, session, url_for, redirect,g
import os
from user import User
from tp import TP
from hashlib import md5
from time import time


def get_md5(tar):
    return md5(bytes(str(tar), encoding='utf-8')).hexdigest()

def get_time_tip():
    return str(int(time()*1000))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(10)
app.config['DATABASE'] = 'data.db'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if session.get('email'):
            return '''<script>alert('you have been login');window.location.href='/manager'</script>'''
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        u = User(email, password, app.config['DATABASE'])
        check_id = u.check_user()
        if check_id == 0:
            session['email'] = email
            session['password'] = password
            return redirect(url_for('manager'))
        elif check_id == 1:
            return '''<script>alert("user doesn't exist");window.location.href='/register'</script>'''
        elif check_id == 2:
            return '''<script>alert("wrong password");window.location.href='/login'</script>'''
        else:
            return redirect(url_for('index'))


@app.route('/logout')
def logout():
    if session.get('email'):
        session.pop('email')
        return redirect(url_for('index'))
    else:
        return '''<script>alert("hasn't login");window.location.href='/login'</script>'''


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        u = User(email, password, app.config['DATABASE'])
        check_id = u.check_user()
        if check_id == 0:
            return '''<script>alert("user has been existed");window.location.href='/login'</script>'''
        elif check_id == 1:
            u.add_user()
            return redirect(url_for('login'))
        else:
            return redirect(url_for('index'))


@app.route('/manager', methods=['GET', 'POST'])
def manager():
    if not session.get('email'):
        return '''<script>alert("hasn't login");window.location.href='/login'</script>'''
    else:
        tp_hash = User(session['email'], session['password'], app.config['DATABASE']).get_tp_hash()
        t = TP(app.config['DATABASE'], tp_hash)
        if request.method == 'GET':
            info = t.get_info()
            li = {'email': session['email'], 'info': info, 'num': len(info)}
            return render_template('manager.html', li=li)
        elif request.method == 'POST':
            ssid = request.form.get('ssid')
            if ssid == '1':
                title = request.form.get('title')
                content = request.form.get('content')
                category = request.form.get('category')
                title_hash = get_md5(session['email'] + title + get_time_tip())
                t.add(title, title_hash, category, content, session['email'])
                return redirect(url_for('manager'))
            elif ssid == '0':
                title_hash = request.form.get('title_hash')
                t.delete(title_hash)
                return redirect(url_for('manager'))


@app.route('/user/<title_hash>')
def resolve_title_hash(title_hash):
    if not session.get('email'):
        return '''<script>alert("hasn't login");window.location.href='/login'</script>'''
    else:
        tp_hash = User(session['email'], session['password'], app.config['DATABASE']).get_tp_hash()
        t = TP(app.config['DATABASE'], tp_hash)
        li = t.get_single_info(title_hash)
        li['email'] = session['email']
        return render_template('manageBase.html', li=li)


@app.route('/tp/<title_hash>', methods=['GET', 'POST'])
def share_link_tp(title_hash):
    t = TP(app.config['DATABASE'])
    li = t.get_share_info(title_hash)
    if request.method == 'GET':
        if li is not None:
            return render_template('shareBase.html', li=li)
        else:
            return render_template('404.html'), 404
    else:
        l = t.get_result_info(title_hash)
        if session.get(title_hash) is None:
            session[title_hash] = 'guest'
            id = request.form.get('id')
            t.tp(id)
            return render_template('resultBase.html', li=l)
        elif session.get(title_hash) == 'guest':
            return render_template('resultBase.html', li=l)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def server_error(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
