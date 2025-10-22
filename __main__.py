from ui.main_window import run_gui
from core.calculos import calcular_vida_estimada
import argparse, sys
def main():
    parser = argparse.ArgumentParser(description='Simulador de Vida Útil de Circuito')
    parser.add_argument('--cli', action='store_true', help='Rodar em modo CLI (headless)')
    parser.add_argument('--components', nargs='*', default=['capacitor'], help='Lista de componentes')
    parser.add_argument('--tolerancia', type=float, default=5.0)
    parser.add_argument('--ambiente', type=int, default=4)
    parser.add_argument('--horas', type=float, default=8.0)
    parser.add_argument('--acidentes', type=float, default=1.0)
    parser.add_argument('--model', choices=['linear','exponencial','weibull'], default='linear', help='Modelo de degradação')
    parser.add_argument('--simdays', type=int, default=2000)
    parser.add_argument('--manut-interval', type=int, default=365)
    parser.add_argument('--manut-rec', type=float, default=20.0)
    parser.add_argument('--export-csv', type=str, default=None, help='Salvar CSV com confiabilidade por dia')
    args = parser.parse_args()
    if args.cli:
        paras = { 'emi':0,'cap_parasita':0,'umidade':0,'vibracao':0,'poeira':0,'esd':0,'gases':0 }
        vida, fatores = calcular_vida_estimada(args.components, args.tolerancia, args.ambiente, args.horas, args.acidentes, paras, model=args.model)
        print('Vida estimada (horas):', round(vida))
        print('Fatores:', fatores)
        from core.modelos import simular_degradacao_generic
        dias, confi_list, manut_days, dias_sem = simular_degradacao_generic(vida, args.horas, args.simdays, args.manut_interval, args.manut_rec)
        print(f'Simulação: {len(dias)} dias, manutenções: {len(manut_days)}')
        if args.export_csv:
            import csv
            with open(args.export_csv, 'w', newline='') as f:
                w = csv.writer(f)
                w.writerow(['dia','confiabilidade'])
                for d,c in zip(dias, confi_list):
                    w.writerow([d, f'{c:.3f}'])
            print('CSV salvo em', args.export_csv)
        return
    run_gui()

if __name__ == '__main__':
    main()
