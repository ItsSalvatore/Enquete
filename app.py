
from flask import Flask, render_template, url_for, redirect, app, config, flash
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)



from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

import os


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://helmerc:6h7#e61CfWEFl#@oege.ie.hva.nl/zhelmerc"
app.config['SQLAlchemy TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sdjhdjhsnkdnkdsnkshuhuhnn'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'ssl':{'fake_flag_to_enable_tls':True}}}
db = SQLAlchemy(app)



@app.route("/")
def index():
    return render_template("index.html")

    

class Question_dotshop(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     question_1 = db.Column(db.String(100), nullable=False)
     question_2 = db.Column(db.String(100), nullable=False)
     question_3 = db.Column(db.String(100), nullable=False)
     question_4 = db.Column(db.String(100), nullable=False)
     question_5 = db.Column(db.String(100), nullable=False)
     question_6 = db.Column(db.String(100), nullable=False)
     question_7 = db.Column(db.String(100), nullable=False)
     question_8 = db.Column(db.String(100), nullable=False)
     question_9 = db.Column(db.String(100), nullable=False)
     question_10 = db.Column(db.String(100), nullable=False)
     question_11 = db.Column(db.String(100), nullable=False)

     def __repr__(self):
          return f'Response {self.name}'
     
@app.route("/submit_question", methods=["POST"]) 
def submit_question():
       
        question_1 = request.form['question_1']
        question_2 = request.form['question_2']
        question_3 = request.form['question_3']
        question_4 = request.form['question_4']
        question_5 = request.form['question_5']
        question_6 = request.form['question_6']
        question_7 = request.form['question_7']
        question_8 = request.form['question_8']
        question_9 = request.form['question_9']
        question_10 = request.form['question_10']
        question_11 = request.form['question_11'] 
    
      

        question_dotshop = Question_dotshop(question_1=question_1, question_2=question_2, question_3=question_3, question_4=question_4, question_5=question_5, 
                                        question_6=question_6, question_7=question_7, question_8=question_8, question_9=question_9, question_10=question_10, question_11=question_11)

        db.session.add(question_dotshop)
        db.session.commit()

        flash('Bedankt voor uw medewerking')

        return redirect(url_for('question_dotshop')) 
   
@app.route("/question_dotshop")
def question_dotshop():
    return render_template("question.html")
    
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


# hieronder bevinden zich de gebruikte bronnen (al deze bronnen bevatten uitleg)

# https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/