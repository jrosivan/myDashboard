from flask import render_template
from flask_simplelogin import SimpleLogin, login_required
from app import app, views

@app.route('/')
@app.route('/dashboard')
@login_required(basic=True)
def index():
    from collections import Counter

    hospitais = views.get_lista_hospitais()
    nutricao = views.get_eventos_estatisticas_nutricao()
    enfermagem = views.get_eventos_estatisticas_enfermagem()
    estadonutricional = views.get_eventos_estadonutricional()
    

    #  sumarios.... por hospital
    sum_nutricao          = Counter([(x.hospitais_id, 'ERROS') for x in nutricao if x.hospitais_id == x.hospitais_id ])
    sum_enfermagem        = Counter([(x.hospitais_id, 'ERROS') for x in enfermagem if x.hospitais_id == x.hospitais_id ])
    sum_estadonutricional = Counter([(x.hospitais_id, x.erro) for x in estadonutricional if x.erro == x.erro and x.hospitais_id == x.hospitais_id ])

    
    return render_template('dashboard.html', title='Dashboard', **locals())



@app.route('/tutoriais')
@login_required(basic=True)
def videos():
    return render_template('tutoriais.html', title='Tutoriais')
