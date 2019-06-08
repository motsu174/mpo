from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from optimization import main

app = Flask(__name__)

class HelloForm(Form):
    name1 = TextAreaField('', [validators.DataRequired()])
    name2 = TextAreaField('', [validators.DataRequired()])
    name3 = TextAreaField('', [validators.DataRequired()])
    sta1 = TextAreaField('', [validators.DataRequired()])
    sta2 = TextAreaField('', [validators.DataRequired()])
    sta3 = TextAreaField('', [validators.DataRequired()])
    des1 = TextAreaField('', [validators.DataRequired()])
    des2 = TextAreaField('', [validators.DataRequired()])
    des3 = TextAreaField('', [validators.DataRequired()])
    des4 = TextAreaField('', [validators.DataRequired()])
    des5 = TextAreaField('', [validators.DataRequired()])


@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('app.html', form=form)

@app.route('/hello',methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name1 = request.form['name1']
        name2 = request.form['name2']
        name3 = request.form['name3']
        sta1 = request.form['sta1']
        sta2 = request.form['sta2']
        sta3 = request.form['sta3']
        des1 = request.form['des1']
        des2 = request.form['des2']
        des3 = request.form['des3']
        des4 = request.form['des4']
        des5 = request.form['des5']

        names = [name1, name2, name3]
        stations = [sta1, sta2, sta3]
        destinations = [des1, des2, des3, des4, des5]
        try:
            destination_opt,P_vars = main.optimization(names, stations,destinations)
        except:
            return render_template('app_error.html', form=form)
        return render_template('hello.html', destination_opt=destination_opt,P_vars=P_vars)
    return render_template('app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

