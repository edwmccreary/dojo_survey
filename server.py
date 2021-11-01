from flask import Flask, render_template,session,redirect,request

app = Flask(__name__)
app.secret_key = 'my secret key'

@app.route('/')
def default():
    if not 'survey' in session:
        session['survey'] = {}

    return render_template("index.html")

@app.route('/add_survey', methods=['POST'])
def add_survey():
    print(request.form)
    new_survey = {}
    new_survey['your_name'] = request.form['your_name']
    new_survey['dojo_location'] = request.form['dojo_location']
    new_survey['fave_language'] = request.form['fave_language']
    new_survey['comments'] = request.form['comments']
    session['survey'] = new_survey
    return redirect("/results")

@app.route('/results')
def results():
    return render_template("results.html",survey=session['survey'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)