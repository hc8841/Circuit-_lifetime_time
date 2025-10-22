import math
from core.calculos import calcular_vida_estimada

def simular_degradacao_linear(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct):
    if horas_dia <= 0:
        horas_dia = 8.0
    dias_ate_falha = vida_hours / horas_dia
    degradacao_diaria_pct = 100.0 / dias_ate_falha
    confiabilidade = 100.0
    dias = []; confi_list = []; manut_days = []
    for dia in range(1, int(dias_simulacao)+1):
        confiabilidade -= degradacao_diaria_pct
        if manut_intervalo_dias > 0 and dia % manut_intervalo_dias == 0:
            recupera = (100.0 - confiabilidade) * (manut_recupera_pct / 100.0)
            confiabilidade += recupera
            manut_days.append(dia)
        confiabilidade = max(0.0, min(100.0, confiabilidade))
        dias.append(dia); confi_list.append(confiabilidade)
        if confiabilidade <= 0.0:
            break
    return dias, confi_list, manut_days, dias_ate_falha

def simular_degradacao_exponencial(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct):
    if horas_dia <= 0:
        horas_dia = 8.0
    dias_ate_falha = vida_hours / horas_dia
    tau = max(1.0, dias_ate_falha / 5.0)
    dias = []; confi_list = []; manut_days = []
    for dia in range(1, int(dias_simulacao)+1):
        t = dia
        new_conf = 100.0 * math.exp(-t / tau)
        if manut_intervalo_dias > 0 and dia % manut_intervalo_dias == 0:
            lost = 100.0 - new_conf
            recupera = lost * (manut_recupera_pct / 100.0)
            new_conf += recupera
            manut_days.append(dia)
        new_conf = max(0.0, min(100.0, new_conf))
        dias.append(dia); confi_list.append(new_conf)
        if new_conf <= 0.0:
            break
    return dias, confi_list, manut_days, dias_ate_falha

def simular_degradacao_weibull(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct):
    if horas_dia <= 0:
        horas_dia = 8.0
    dias_ate_falha = vida_hours / horas_dia
    k = 1.5
    lam = max(1.0, dias_ate_falha / 1.5)
    dias = []; confi_list = []; manut_days = []
    for dia in range(1, int(dias_simulacao)+1):
        F = 1.0 - math.exp(- (dia / lam) ** k)
        new_conf = max(0.0, 100.0 * (1.0 - F))
        if manut_intervalo_dias > 0 and dia % manut_intervalo_dias == 0:
            lost = 100.0 - new_conf
            recupera = lost * (manut_recupera_pct / 100.0)
            new_conf += recupera
            manut_days.append(dia)
        new_conf = max(0.0, min(100.0, new_conf))
        dias.append(dia); confi_list.append(new_conf)
        if new_conf <= 0.0:
            break
    return dias, confi_list, manut_days, dias_ate_falha

def simular_degradacao_generic(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct, model='linear'):
    model = model.lower() if model else 'linear'
    if model == 'linear':
        return simular_degradacao_linear(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct)
    if model == 'exponencial' or model == 'exponential':
        return simular_degradacao_exponencial(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct)
    if model == 'weibull':
        return simular_degradacao_weibull(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct)
    return simular_degradacao_linear(vida_hours, horas_dia, dias_simulacao, manut_intervalo_dias, manut_recupera_pct)
