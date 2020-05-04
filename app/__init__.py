from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_simplelogin import SimpleLogin, login_required

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models, views

# ----------------inicializar database....
models.db.create_all()
#--- criar hospitais:
db.session.add(models.Hospitais(nomehospital='SANTA BARBARA', sigla='HSB', sistema='MV'))
db.session.add(models.Hospitais(nomehospital='SAO VICENTE', sigla='HSV', sistema='TASY'))
db.session.add(models.Hospitais(nomehospital='REGIONAL', sigla='HREG', sistema='MV-SOUL'))
db.session.add(models.Hospitais(nomehospital='IRMA DULCE', sigla='HID', sistema='MV'))
db.session.add(models.Hospitais(nomehospital='SAMARITANO', sigla='HSMT', sistema='TASY'))
db.session.commit()
# 
# criar usuário: "teste"   senha:  "teste"
u = models.User(hospitais_id=1, nome='Usuário Teste', login='teste')
u.set_password('teste')
db.session.add(u)
db.session.commit()

#--- inserir valores nas tabelas dos erros:
from random import randint
for k in [1,2,3,4,5]:
    for i in range (1, randint(2,30)):
        db.session.add(models.Dashboard_EstadoNutricional(hospitais_id=k, atendimento=str(i*100), erro='REAVALIACAO' ))
    for i in range (1, randint(2,30)):
        db.session.add(models.Dashboard_EstadoNutricional(hospitais_id=k, atendimento=str(i*100), erro='NOTIFICACAO' ))
    for i in range (1, randint(2,30)):
        db.session.add(models.Dashboard_EstatisticasEnfermagem(hospitais_id=k, usuarios_id=1, ano=2020, mes=1, erro='erro preenchimento-' + str(i*100)))
    for i in range (1, randint(2,30)):
        db.session.add(models.DashBoard_EstatisticasNutricao(hospitais_id=k, usuarios_id=1, ano=2020, mes=1, erro='erro preenchimento-' + str(i*100)))

db.session.commit()



# ---------------- Efetuar Login:
SimpleLogin(app, login_checker=views.check_my_users)

