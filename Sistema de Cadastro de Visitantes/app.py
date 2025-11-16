# =========================
# Sistema de Cadastro de Visitantes
# Autor: Luiz Fernando Martins dos Santos
# Turma: TMS0226 3015
# Data: 25/10/2025
# =========================

# bibliotecas
from datetime import datetime  # Biblioteca para data(horario)
import json  # Para salvar arquivos em json
from time import sleep
import os

# Lista vazia de visitantes
visitantes = []

# -------------------------
# Funções auxiliares
# -------------------------

# Função de identificador unico
id = 0
def proximo_id():
    """Retorna o próximo ID auto-incremental para um visitante."""
    global id
    id += 1
    return id


# Função para formatar e validar CPF
def formatar_e_validar_cpf(cpf: str) -> str | None:
    """Remove formatação e valida CPF. Retorna o CPF limpo se for válido, senão None."""
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove tudo que não for número

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return None

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    if cpf[-2:] != f"{digito1}{digito2}":
        return None

    return cpf


# -------------------------
# Funções principais
# -------------------------

# Função para registar entrada do visitante
def registrar_entrada():
    """Registra a entrada de um visitante."""

    print("\n=== Registrar Entrada ===")
    print("Digite '0' ou 'sair' a qualquer momento para voltar ao menu.\n")
    try:

        # Criação das entradas das colunas

        nome = input("\nNome (*obrigatorio): \n").strip()
        if nome.lower() in ["0", "sair"] or not nome:
            print("\nVoltando ao menu...\n")
            return

        documento = input("\nCPF (*obrigatorio): \n").strip()
        if documento.lower() in ["0", "sair"] or not documento:
            print("Voltando ao menu...\n")
            return

        # Verificando se o cpf é verdadeiro
        documento = formatar_e_validar_cpf(documento)
        if not documento:
            print("\nCPF inválido! Digite um CPF válido (com ou sem traços).\n")
            return

        '''Se o visitante com um documento igual de alguem que esta dentro do local, impessa o registro
           desse visitante'''

        for v in visitantes:
            if v['documento'] == documento and v['saida'] is None:
                print("\nEste visitante já está registrado e ainda não saiu.\n")
                return

        visitado = input("\nQuem a pessoa veio visitar (*obrigatorio): \n").strip()
        if visitado.lower() in ["0", "sair"] or not visitado:
            print("\nVoltando ao menu...\n")
            return

        motivo = input("\nQual o motivo da visita (opcional): \n").strip()
        if motivo.lower() in ["0", "sair"]:
            print("\nVoltando ao menu...\n")
            return

        # Pegando a data e o horario em tempo real
        entrada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Criação das colunas em um dicionario(json)
        visitante = {
            "id": proximo_id(),
            "nome": nome,
            "documento": documento,
            "visitado": visitado,
            "motivo": motivo,
            "entrada": entrada,
            "saida": None
        }

        # Adicionando meu dicionanrio(visitante) a minha lista(visitantes)
        visitantes.append(visitante)
        print(f"\nEntrada registrada para {nome} às {entrada}.\n")

    # Para erros inesperados
    except Exception as e:
        print(f"\nErro ao registrar entrada: {e}\n")


# Função para registrar a saída do visitante
def registrar_saida():
    """Registra a saída de um visitante."""

    print("\n=== Registrar Saída ===")
    print("Digite '0' ou 'sair' a qualquer momento para voltar ao menu.\n")

    # Registrando a saída atraves do CPF
    documento = input("\nDocumento do visitante: \n").strip()
    if documento.lower() in ["0", "sair"]:
        print("\nVoltando ao menu...\n")
        return

    '''Se o CPF digitado for igual o cpf que esta dentro de documento'''

    for v in visitantes:
        if v["documento"] == documento:

            '''Execute Se minha saida for None: coloque o horario que o visitante saiu'''

            if v["saida"] is None:
                # Pegando a data e o horario em tempo real
                v["saida"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"\nSaída registrada para {v['nome']} às {v['saida']}\n")
                return

            # Se o CPF ja tiver registrado uma saida
            else:
                print("\nSaída já registrada.\n")
                return

    # Se o documento digitado não estiver registrado
    print("\nVisitante não encontrado.\n")


# Função para listar todos os registros
def listar_visitante():
    """Lista todos os visitantes cadastrados."""

    # Se não tiver visitantes
    if not visitantes:
        print("\nNenhum visitante encontrado.\n")
        return

    # Se tiver visitantes
    print("\n=== Lista de Visitantes ===\n")

    # Ordenando todos os visitantes por nome
    for v in sorted(visitantes, key=lambda x: x["nome"].lower()):
        # Exiba todos os visitantes
        print(f"ID: {v['id']} \nNome: {v['nome']} \nDocumento: {v['documento']}"
              f"\nVisitado: {v['visitado']} \nMotivo: {v['motivo']}"
              f"\nEntrada: {v['entrada']} \nSaída: {v['saida']}\n")


# Função para buscar um visitante especifico
def buscar_visitante():
    """Busca visitante pelo nome ou CPF."""

    print("\n=== Buscar Visitante ===")
    print("Digite '0' ou 'sair' a qualquer momento para voltar ao menu.\n")

    # Buscando atraves do CPF ou Nome do visitante
    termo = input("\nDigite o documento ou nome do visitante: \n").strip()
    if termo.lower() in ["0", "sair"]:
        print("\nVoltando ao menu...\n")
        return

    '''Se o meu documento for igual a o documento do registro ou meu nome for
    igual ao nome do registro, me entregue esse registro especifico'''

    encontrados = [v for v in visitantes if termo.lower() in v["nome"].lower() or termo == v["documento"]]
    # Se não existir o registro especifico ou visitantes
    if not encontrados:
        print("\nNenhum visitante encontrado.\n")
        return

    # Exiba meu registro especifico
    for v in encontrados:
        print(f"\nID: {v['id']} \nNome: {v['nome']} \nDocumento: {v['documento']}"
              f"\nVisitado: {v['visitado']} \nMotivo: {v['motivo']}"
              f"\nEntrada: {v['entrada']} \nSaída: {v['saida']}\n")


def atualizar_registro():
    """Atualiza dados de um visitante."""

    print("\n=== Atualizar Registro ===")
    print("Digite '0' ou 'sair' a qualquer momento para voltar ao menu.\n")

    documento = input("CPF: \n").strip()
    if documento.lower() in ["0", "sair"]:
        print("\nVoltando ao menu principal...\n")
        return

    visitante_encontrado = None
    for v in visitantes:
        if v["documento"] == documento:
            visitante_encontrado = v
            break

    if not visitante_encontrado:
        print("\nVisitante não encontrado.\n")
        return

    print("\n>Pressione ENTER para manter o valor atual.\n")

    nome = input(f"Nome atual: {visitante_encontrado['nome']}\nNovo nome: ").strip()
    if nome:
        visitante_encontrado["nome"] = nome

    novo_doc = input(f"CPF atual: {visitante_encontrado['documento']}\nNovo CPF: ").strip()
    if novo_doc:
        novo_doc = formatar_e_validar_cpf(novo_doc)
        if not novo_doc:
            print("Novo CPF inválido! Mantendo o anterior.\n")
        else:
            visitante_encontrado["documento"] = novo_doc

    visitado = input(f"Visitado atual: {visitante_encontrado['visitado']}\nNovo visitado: ").strip()
    if visitado:
        visitante_encontrado["visitado"] = visitado

    motivo = input(f"Motivo atual: {visitante_encontrado['motivo']}\nNovo motivo: ").strip()
    if motivo:
        visitante_encontrado["motivo"] = motivo

    entrada = input(f"Entrada atual: {visitante_encontrado['entrada']}\nNova entrada: ").strip()
    if entrada:
        visitante_encontrado["entrada"] = entrada

    saida = input(f"Saída atual: {visitante_encontrado['saida']}\nNova saída: ").strip()
    if saida:
        visitante_encontrado["saida"] = saida

    print("\nRegistro atualizado com sucesso!\n")


# Função para remover um registro
def remove_registro():
    """Remove um visitante pelo CPF."""

    print("\n=== Remover Registro ===")
    print("Digite '0' ou 'sair' a qualquer momento para voltar ao menu.\n")

    # Removendo atraves do CPF do visitante
    documento = input("CPF do visitante: \n").strip()
    if documento.lower() in ["0", "sair"]:
        print("Voltando ao menu...\n")
        return

    '''Se o CPF digitado for igual ao CPF do registro, remova o registro desse CPF especifico'''

    for v in visitantes:
        if v["documento"] == documento:
            visitantes.remove(v)
            print(f"Visitante {v['nome']} com CPF {documento} removido com sucesso!\n")
            return
    # Se tiver digitado o CPF errado ou não tiver esse CPF no registro
    print("Visitante não encontrado.\n")


# Função para salvar o registro
def salvar_registros():
    """Salva registros em arquivo JSON com verificação de sobrescrita."""

    global visitantes, id
    caminho = "visitantes.json"
    dados = {"ultimo_id": id, "visitantes": visitantes}

    if os.path.exists(caminho):
        print("\nUm arquivo existente foi detectado!")

        print("""
        \n        Dica: Vá no arquivo com o nome 'visitantes.json' e altere o nome para não perde o conteúdo
        desse arquivo, mas caso esse arquivo não tenha registros, ou os registros não seja importante
        ou os registros ja foram carregados e você so esta salvando novos registros em cima do existenten então
        sobreescreva.\n

        Dica bônus: Caso você já tenha um arquivo salvo sempre carregue ele primeiro antes de adicionar novos registros.
        """)

        confirmar = input("Deseja sobrescrever o arquivo existente? (s/n): ").strip().lower()
        if confirmar != "s":
            print("Operação cancelada. Nenhum dado foi alterado.\n")
            return

    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print("Registros salvos com sucesso!\n")
    except Exception as e:
        print(f"Erro ao salvar registros: {e}\n")


def carregar_registro():
    """Carrega registros de arquivo JSON."""

    global visitantes, id
    caminho = "visitantes.json"
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
            visitantes = dados.get("visitantes", [])
            id = dados.get("ultimo_id", 0)
        print("Registros carregados com sucesso!\n")
    except FileNotFoundError:
        visitantes = []
        id = 0
        print("Arquivo não encontrado. Lista vazia.\n")


def estatistica():
    """Exibe estatísticas do sistema."""

    print("\n=== Estatísticas ===")
    total = len(visitantes)
    dentro = [v for v in visitantes if v['saida'] is None]
    fora = [v for v in visitantes if v['saida'] is not None]
    print(f"Total de visitantes cadastrados: {total}")
    print(f"Visitantes ainda dentro: {len(dentro)}")
    print(f"Visitantes que já saíram: {len(fora)}")


# -------------------------
# Função principal (menu)
# -------------------------

def main():
    while True:
        print("=" * 40)
        print(f"{'Sistema de cadastro de visitante':^40}")
        print("=" * 40)
        print("\n1 - Registrar entrada"
              "\n2 - Registrar saída"
              "\n3 - Listar visitantes"
              "\n4 - Buscar visitante"
              "\n5 - Remover registro"
              "\n6 - Atualizar registro"
              "\n7 - Estatísticas"
              "\n8 - Salvar registros"
              "\n9 - Carregar registros"
              "\n0 - Sair")
        opcao = input("Escolha uma opção: \n").strip()
        try:
            if opcao == '1':
                registrar_entrada()
            elif opcao == '2':
                registrar_saida()
            elif opcao == '3':
                listar_visitante()
            elif opcao == '4':
                buscar_visitante()
            elif opcao == '5':
                remove_registro()
            elif opcao == '6':
                atualizar_registro()
            elif opcao == '7':
                estatistica()
            elif opcao == '8':
                salvar_registros()
            elif opcao == '9':
                carregar_registro()
            elif opcao == '0':

                # Pergunta antes de sair
                salvar = input("\nDeseja salvar as alterações antes de sair? (s/n): ").strip().lower()
                if salvar in "sim":
                    salvar_registros()

                print("Saindo", end="")
                sleep(0.5)
                print(end='.')
                sleep(1)
                print(end=".")
                sleep(1)
                print(end=".")
                sleep(2)
                print("\n>Sistema finalizado<\n")

                break
            else:
                print("Opção inválida.\n")
        except KeyboardInterrupt:
            print("\nInterrupção detectada. Voltando ao menu...\n")
        except Exception as e:
            print(f"Erro inesperado: {e}\n")


# -------------------------
# Executa o programa
# -------------------------
if __name__ == "__main__":
    main()
