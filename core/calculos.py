import math
def vida_base_por_componente(nome):
    n = nome.strip().lower()
    if n in ['capacitor eletrolítico','capacitor','electrolytic capacitor']:
        return 20000
    if n in ['transistor','bjt','transistor bjt']:
        return 40000
    if n in ['mosfet','fet']:
        return 45000
    if n in ['microcontrolador','microcontroller','mcu']:
        return 60000
    if n in ['ic','circuito integrado','integrated circuit']:
        return 50000
    if n in ['resistor','resistor (ohm)']:
        return 70000
    if n in ['diodo','diode']:
        return 70000
    if n in ['indutor','inductor']:
        return 65000
    if n in ['regulador de tensão','regulador','voltage regulator']:
        return 40000
    return 35000

def calcular_vida_estimada(componentes_list, tolerancia_pct, ambiente_score,
                           horas_dia, acidentes_semana, parasitas, model='linear'):
    """Return (vida_hours, fatores_dict). Model parameter only changes nothing here;
    it's used later by simulators (core.modelos)."""
    vidas = [vida_base_por_componente(c) for c in componentes_list if c.strip()!='']
    if not vidas:
        vidas = [35000]
    vida_base = sum(vidas)/len(vidas)
    fator_tolerancia = max(0.5, 1 - (tolerancia_pct/100))
    fator_ambiente = 1 - (min(max(ambiente_score,0),10) * 0.05)
    if horas_dia <= 0:
        horas_dia = 8.0
    hours_excess = max(0, horas_dia - 8)
    if hours_excess:
        fator_tempo = 1 - (hours_excess * 0.02)
    else:
        fator_tempo = 1 + (min(8 - horas_dia, 8) * 0.01)
    fator_humano = max(0.5, 1 - (acidentes_semana * 0.03))
    pesos = { 'emi':0.25, 'cap_parasita':0.18, 'umidade':0.20, 'vibracao':0.12, 'poeira':0.08, 'esd':0.10, 'gases':0.15 }
    fator_parasitas = 1.0
    for key,peso in pesos.items():
        sever = parasitas.get(key,0)
        sever = min(max(sever,0),100)
        effect = 1 - (0.6 * (sever/100))
        fator_parasitas *= (effect ** peso)
    vida_final = vida_base * fator_tolerancia * fator_ambiente * fator_tempo * fator_humano * fator_parasitas
    vida_final = max(100.0, vida_final)
    fatores = { 'vida_base':vida_base, 'fator_tolerancia':fator_tolerancia, 'fator_ambiente':fator_ambiente,
               'fator_tempo':fator_tempo, 'fator_humano':fator_humano, 'fator_parasitas':fator_parasitas, 'model':model }
    return vida_final, fatores
