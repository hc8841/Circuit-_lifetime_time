# Simulador de Vida Útil de Circuito (Modular)
Projeto modular do simulador de vida útil de circuito em Python (PyQt5).
- GUI: `ui/main_window.py` (PyQt5)
- Núcleo de cálculos: `core/calculos.py`
- Modelos de degradação: `core/modelos.py` (linear, exponencial, weibull)
- Modo CLI disponível (`python -m simulador_vida_util_circuito --cli`)
- Exportação CSV a partir do GUI

## Instalação (sugestão)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Executar (GUI)
```bash
python -m simulador_vida_util_circuito
```
## Executar (CLI)
```bash
python -m simulador_vida_util_circuito --cli --components capacitor resistor --export-csv out.csv
```
