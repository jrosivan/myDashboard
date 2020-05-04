from app import db
from werkzeug.security import generate_password_hash, check_password_hash

#---------------------------------------
class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    hospitais_id = db.Column(db.Integer())
    nome = db.Column(db.String(50))
    login = db.Column(db.String(50))
    senha = db.Column(db.String(128))

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)


class Hospitais(db.Model):
    __tablename__ = 'hospitais'
    id = db.Column(db.Integer, primary_key=True)
    nomehospital = db.Column(db.String(30))
    sigla = db.Column(db.String(10))
    sistema = db.Column(db.String(10))


class Dashboard_EstadoNutricional(db.Model):
    __tablename__ = 'dashboard_estadonutricional'
    id = db.Column(db.Integer, primary_key=True)
    hospitais_id = db.Column(db.Integer)
    atendimento = db.Column(db.String(10))
    erro = db.Column(db.String(15))


class Dashboard_EstatisticasEnfermagem(db.Model):
    __tablename__ = 'dashboard_estatisticas_enfermagem'
    id = db.Column(db.Integer, primary_key=True)
    hospitais_id = db.Column(db.Integer)
    usuarios_id = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    mes = db.Column(db.Integer)
    erro = db.Column(db.String(255))


class DashBoard_EstatisticasNutricao(db.Model):
    __tablename__ = 'dashboard_estatisticas_nutricao'
    id = db.Column(db.Integer, primary_key=True)
    hospitais_id = db.Column(db.Integer)
    usuarios_id = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    mes = db.Column(db.Integer)
    erro = db.Column(db.String(255))
