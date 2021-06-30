import numpy as np
from flask import *
from flask import Flask, request, jsonify, render_template,session,redirect,url_for
import pickle
import os
from werkzeug.utils import secure_filename
import pymongo
from datetime import date

client = pymongo.MongoClient("mongodb+srv://nandhu12:nandhu@cluster0.dfmct.mongodb.net/covid_19?retryWrites=true&w=majority")
db = client['covid_19']


app = Flask(__name__)
app.secret_key="hello123"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =="POST":
        credentials=request.form.to_dict()
        user_name=credentials["user_name"]
        user_password=credentials["user_password"]
        user_email=credentials["user_email"]
        login=db['login']
        #check_for_duplicate
        existing_user = login.find_one(({"_id":credentials['user_email']}))
        if existing_user is not  None:
            return render_template('index.html',exist=1)
        #data_entry
        past = {"_id":user_email,"name":user_name,"password":user_password}
        login.insert_one(past)
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        credentials = request.form.to_dict()
        #checking
        login=db['login']
        existing_user = login.find_one(({"_id": credentials["user_email"]}))
        #
        if existing_user is None:
            return render_template("index.html")
        
        if credentials['user_password'] == existing_user['password']:
            session['user_email']=existing_user["_id"]
            session['user_name']=existing_user["name"]
            return render_template('contribution/Contribution_index.html')
        else:
            return render_template('index.html',invalid=1)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    return render_template('contribution/Contribution_survey.html')

@app.route('/record', methods=['GET', 'POST'])
def record():
    if request.method =="POST":
        #credentials = request.form.to_dict()
        req = request.form
        #user_name=credentials["user_name"]
        
        user_name = req.get("user_name")

        user_age=req.get("user_age")
        user_sex=req.get("user_sex")
        user_country=req.get("user_country")
        user_state=req.get("user_state")
        user_district=req.get('user_district')
        asthma=req.get('asthma')
        Cystic_fibrosis=req.get('Cystic_fibrosis')
        COPD_Emphysema=req.get('COPD/Emphysema')
        Pulmonary_fibrosis=req.get('Pulmonary_fibrosis')
        Pnuemonia=req.get('Pnuemonia')
        other_lung_disease=req.get('other_lung_disease')
        high_blood_pressure=req.get('high_blood_pressure')
        Angina=req.get('Angina')
        ischaemic_attack=req.get('Previous_stroke/ischaemic_attack')
        heart_attack=req.get('previous_heart_attack')
        valvular_heart_disease=req.get('valvular_heart_disease')
        other_heart_disease=req.get('other_heart_disease')
        cancer=req.get('Cancer')
        Diabetes=req.get('Diabetes')
        previous_organ_transplant=req.get('previous_organ_transplant')
        hiv_impaired_immune=req.get('hiv/impaired_immune')
        othr_user_long_term_condition=req.get('othr_long_term_condition')
        user_smoking=req.get('user_smoking')
        user_vaccine_status=req.get('user_vaccine_status')
        user_cold=req.get('user_cold')
        user_cough=req.get('user_cough')
        user_fever=req.get('user_fever')
        user_diarrhoea=req.get('user_diarrhoea')
        sore_throat=req.get('sore_throat')
        difficulty_breathing=req.get('difficulty_breathing')
        dizziness_confusion=req.get('dizziness/confusion')
        headache=req.get('headache')
        running_blocked_nose=req.get('running/blocked_nose')
        loss_taste=req.get('loss_taste')
        muscle_pain=req.get('muscle_pain')
        fatique=req.get('fatique')


    return render_template('contribution/Contribution_record.html')


@app.route("/breath_shallow", methods=['POST', 'GET'])
def breath_shallow():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_breathe_shallow.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")

@app.route("/breath_deep", methods=['POST', 'GET'])
def breath_deep():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_breathe_deep.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")

@app.route("/cough_shallow", methods=['POST', 'GET'])
def cough_shallow():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_cough_shallow.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")
    
@app.route("/cough_heavy", methods=['POST', 'GET'])
def cough_heavy():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_cough_heavy.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")
    
@app.route("/vowel_a", methods=['POST', 'GET'])
def vowel_a():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_vowel_a.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")

@app.route("/vowel_e", methods=['POST', 'GET'])
def vowel_e():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_vowel_e.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")
    
@app.route("/vowel_o", methods=['POST', 'GET'])
def vowel_o():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_vowel_o.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")

@app.route("/counting_normal", methods=['POST', 'GET'])
def counting_normal():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_counting_normal.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")

@app.route("/counting_fast", methods=['POST', 'GET'])
def counting_fast():
    if request.method == "POST":
        k = request.files['audio_data']
        interm='audios/'+session['user_email']+'_counting_fast.wav'
        with open(interm, 'wb') as audio:
            k.save(audio)
        print('file uploaded successfully')

        return render_template('contribution/Contribution_survey.html', request="POST")   
    else:
        return render_template("contribution/Contribution_survey.html")

@app.route('/processing', methods=['GET', 'POST'])
def processing():
    return render_template('contribution/Contribution_feedback.html')










































if __name__ == '__main__':
    app.run(debug=True)