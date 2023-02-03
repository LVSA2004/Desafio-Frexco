from typing import List

opcao = 0
opcao1 = 0

ValorVendas = [870, 868, 1.189, 742, 317, 685, 1.366, 1.213, 1.055, 1.343, 832, 240, 235, 1.050, 711, 745, 1.009, 18, 40, 67, 821,572, 429, 638, 106,
    54, 144, 814, 679, 712, 1.229, 821, 319, 317, 1.317, 807, 923, 1.265, 892, 289, 566, 1.692, 1.097, 1.302, 1.405,945]
Tamanho = len(ValorVendas)


def Opcoes(opcao):
    return opcao != '0'


def Opcoes1(opcao1):
    return opcao1 != '0'


def EntradaDados():
    return int(input("Insira a opção desejada:"))


def MenuPrincipal():
    return print('''
    ==================={ Menu Principal }===================

        (1) - Calcular Previsão de Demanda
        (0) - Finalizar o Programa

    ========================================================
          ''')


def Calculos():
 MediaGeral = sum(ValorVendas) / Tamanho
 Media1 = (1.265 + 892 + 289 + 566 + 1.692) / 5
 Media2 = (892 + 289 + 566 + 1.692 + 1.097) / 5
 Media3 = (289 + 566 + 1.692 + 1.097 + 1.302) / 5
 Media4 = (566 + 1.692 + 1.097 + 1.302 + 1.405) / 5
 Media5 = (1.692 + 1.097 + 1.302 + 1.405 +945) / 5


 print(f"\n As vendas do dia 21/01/2023, baseadas na média móvel aritmética, seriam de {Media1}, podendo variar em {MediaGeral}")
 print(f"\n As vendas do dia 22/01/2023, baseadas na média móvel aritmética, seriam de {Media2}, podendo variar em {MediaGeral}")
 print(f"\n As vendas do dia 23/01/2023, baseadas na média móvel aritmética, seriam de {Media3}, podendo variar em {MediaGeral}")
 print(f"\n As vendas do dia 24/01/2023, baseadas na média móvel aritmética, seriam de {Media4}, podendo variar em {MediaGeral}")
 print(f"\n As vendas do dia 25/01/2023, baseadas na média móvel aritmética, seriam de {Media5}, podendo variar em {MediaGeral}")



#Programa Principal
while Opcoes(opcao):
        try:
            MenuPrincipal()
            opcao = EntradaDados()
        except ValueError as err:
            print("Dado Inválido. Insira uma opção válida!.")
        if opcao == 1:
            Calculos()
        if opcao == 0:
            break