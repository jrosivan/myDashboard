from app import models


#---------------------------------------------------
# Funções de acesso ao banco de dados....
#---------------------------------------------------
def check_my_users(user):
    usuario = models.User.query.filter_by(login=user.get('username')).first()
    return not usuario is None and usuario.check_password(user.get('password'))

#-----------------------------
def get_lista_hospitais():
    return models.Hospitais.query.order_by(models.Hospitais.nomehospital).all()

#-----------------------------
def get_eventos_estatisticas_nutricao():
    return models.DashBoard_EstatisticasNutricao.query.order_by(
        models.DashBoard_EstatisticasNutricao.usuarios_id,
        models.DashBoard_EstatisticasNutricao.ano,
        models.DashBoard_EstatisticasNutricao.mes).all()

#-----------------------------
def get_eventos_estatisticas_enfermagem():
    return models.Dashboard_EstatisticasEnfermagem.query.order_by(
        models.Dashboard_EstatisticasEnfermagem.usuarios_id,
        models.Dashboard_EstatisticasEnfermagem.ano,
        models.Dashboard_EstatisticasEnfermagem.mes).all()

#-----------------------------
def get_eventos_estadonutricional():
    return models.Dashboard_EstadoNutricional.query.all()

