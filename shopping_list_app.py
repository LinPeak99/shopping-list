import copy
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Variáveis globais que representam o estado do sistema.
PERFIS = ["Solo", "Duo", "Familia"]
TIPOS_ALIMENTO = ["Frutas", "Frios", "Fresco", "Legumes", "Processados", "Limpeza", "Bebida"]
PERFIL_ATUAL = "Solo"
ARQUIVO_PERSISTENCIA = os.path.join(os.path.dirname(__file__), "listas_personalizadas.json")

# Estrutura base do vetor de produtos por perfil. Cada item representa uma posição do vetor.
BASE_VETOR_PRODUTOS = {
    "Solo": [
        {"nome": "Café", "quantidade": 1, "preco_unitario": 28.00, "tipo": "Bebida"},
        {"nome": "Leite", "quantidade": 1, "preco_unitario": 8.00, "tipo": "Bebida"},
        {"nome": "Chá", "quantidade": 1, "preco_unitario": 10.00, "tipo": "Bebida"},
        {"nome": "Bananas", "quantidade": 4, "preco_unitario": 1.50, "tipo": "Frutas"},
        {"nome": "Maçãs", "quantidade": 2, "preco_unitario": 3.00, "tipo": "Frutas"},
        {"nome": "Limões", "quantidade": 2, "preco_unitario": 2.00, "tipo": "Frutas"},
        {"nome": "Ovos (dúzia)", "quantidade": 1, "preco_unitario": 16.00, "tipo": "Fresco"},
        {"nome": "Queijo fatiado", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Fresco"},
        {"nome": "Peito de frango (1 kg)", "quantidade": 1, "preco_unitario": 35.00, "tipo": "Fresco"},
        {"nome": "Cebola (1 kg)", "quantidade": 1, "preco_unitario": 7.00, "tipo": "Legumes"},
        {"nome": "Alho", "quantidade": 1, "preco_unitario": 2.00, "tipo": "Legumes"},
        {"nome": "Batata (1 kg)", "quantidade": 1, "preco_unitario": 8.00, "tipo": "Legumes"},
        {"nome": "Cenoura (1 kg)", "quantidade": 1, "preco_unitario": 7.00, "tipo": "Legumes"},
        {"nome": "Tomate (1 kg)", "quantidade": 1, "preco_unitario": 10.00, "tipo": "Legumes"},
        {"nome": "Arroz (pacote 5 kg)", "quantidade": 1, "preco_unitario": 38.00, "tipo": "Processados"},
        {"nome": "Feijão (pacote 1 kg)", "quantidade": 1, "preco_unitario": 11.00, "tipo": "Processados"},
        {"nome": "Azeite (500 ml)", "quantidade": 1, "preco_unitario": 45.00, "tipo": "Processados"},
        {"nome": "Pão de forma", "quantidade": 1, "preco_unitario": 12.00, "tipo": "Processados"},
        {"nome": "Aveia (500 g)", "quantidade": 1, "preco_unitario": 10.00, "tipo": "Processados"},
        {"nome": "Molho de tomate", "quantidade": 2, "preco_unitario": 4.00, "tipo": "Processados"},
        {"nome": "Detergente neutro", "quantidade": 1, "preco_unitario": 4.00, "tipo": "Limpeza"},
        {"nome": "Sabão em pó (1 kg)", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Limpeza"},
        {"nome": "Amaciante (1 L)", "quantidade": 1, "preco_unitario": 14.00, "tipo": "Limpeza"},
        {"nome": "Papel higiênico (4 rolos)", "quantidade": 1, "preco_unitario": 10.00, "tipo": "Limpeza"},
        {"nome": "Sabonete", "quantidade": 2, "preco_unitario": 3.00, "tipo": "Limpeza"},
        {"nome": "Creme dental", "quantidade": 1, "preco_unitario": 9.00, "tipo": "Limpeza"},
    ],
    "Duo": [
        {"nome": "Café", "quantidade": 1, "preco_unitario": 30.00, "tipo": "Bebida"},
        {"nome": "Leite", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Bebida"},
        {"nome": "Suco concentrado", "quantidade": 2, "preco_unitario": 15.00, "tipo": "Bebida"},
        {"nome": "Água com gás", "quantidade": 2, "preco_unitario": 5.00, "tipo": "Bebida"},
        {"nome": "Bananas", "quantidade": 8, "preco_unitario": 1.50, "tipo": "Frutas"},
        {"nome": "Maçãs", "quantidade": 4, "preco_unitario": 2.50, "tipo": "Frutas"},
        {"nome": "Laranjas", "quantidade": 4, "preco_unitario": 2.00, "tipo": "Frutas"},
        {"nome": "Mamão", "quantidade": 1, "preco_unitario": 10.00, "tipo": "Frutas"},
        {"nome": "Uva (1 kg)", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Frutas"},
        {"nome": "Ovos (2 dúzias)", "quantidade": 1, "preco_unitario": 28.00, "tipo": "Fresco"},
        {"nome": "Queijo mussarela (500 g)", "quantidade": 1, "preco_unitario": 28.00, "tipo": "Fresco"},
        {"nome": "Peito de peru (300 g)", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Fresco"},
        {"nome": "Carne moída (kg)", "quantidade": 2, "preco_unitario": 42.00, "tipo": "Fresco"},
        {"nome": "Filé de frango (kg)", "quantidade": 2, "preco_unitario": 34.00, "tipo": "Fresco"},
        {"nome": "Cebola (2 kg)", "quantidade": 2, "preco_unitario": 7.00, "tipo": "Legumes"},
        {"nome": "Alho", "quantidade": 2, "preco_unitario": 2.00, "tipo": "Legumes"},
        {"nome": "Batata (2 kg)", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Legumes"},
        {"nome": "Cenoura (1 kg)", "quantidade": 1, "preco_unitario": 7.00, "tipo": "Legumes"},
        {"nome": "Abobrinha", "quantidade": 2, "preco_unitario": 4.00, "tipo": "Legumes"},
        {"nome": "Pimentão", "quantidade": 2, "preco_unitario": 5.00, "tipo": "Legumes"},
        {"nome": "Tomate (2 kg)", "quantidade": 2, "preco_unitario": 9.00, "tipo": "Legumes"},
        {"nome": "Arroz (pacote 5 kg)", "quantidade": 1, "preco_unitario": 35.00, "tipo": "Processados"},
        {"nome": "Feijão (1 kg)", "quantidade": 1, "preco_unitario": 12.00, "tipo": "Processados"},
        {"nome": "Macarrão", "quantidade": 2, "preco_unitario": 7.00, "tipo": "Processados"},
        {"nome": "Azeite (500 ml)", "quantidade": 1, "preco_unitario": 60.00, "tipo": "Processados"},
        {"nome": "Molho de tomate", "quantidade": 2, "preco_unitario": 5.00, "tipo": "Processados"},
        {"nome": "Pão integral", "quantidade": 1, "preco_unitario": 14.00, "tipo": "Processados"},
        {"nome": "Biscoitos", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Processados"},
        {"nome": "Detergente neutro", "quantidade": 3, "preco_unitario": 4.00, "tipo": "Limpeza"},
        {"nome": "Desinfetante (2 L)", "quantidade": 1, "preco_unitario": 16.00, "tipo": "Limpeza"},
        {"nome": "Sabão em pó (2 kg)", "quantidade": 1, "preco_unitario": 33.00, "tipo": "Limpeza"},
        {"nome": "Amaciante (2 L)", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Limpeza"},
        {"nome": "Papel higiênico (12 rolos)", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Limpeza"},
        {"nome": "Papel toalha", "quantidade": 2, "preco_unitario": 4.50, "tipo": "Limpeza"},
        {"nome": "Esponja de pia", "quantidade": 2, "preco_unitario": 3.00, "tipo": "Limpeza"},
    ],
    "Familia": [
        {"nome": "Café", "quantidade": 2, "preco_unitario": 29.00, "tipo": "Bebida"},
        {"nome": "Leite (caixa com 12 unidades)", "quantidade": 1, "preco_unitario": 78.00, "tipo": "Bebida"},
        {"nome": "Sucos variados", "quantidade": 3, "preco_unitario": 12.00, "tipo": "Bebida"},
        {"nome": "Achocolatado", "quantidade": 1, "preco_unitario": 20.00, "tipo": "Bebida"},
        {"nome": "Água mineral (galão 5 L)", "quantidade": 2, "preco_unitario": 15.00, "tipo": "Bebida"},
        {"nome": "Bananas", "quantidade": 12, "preco_unitario": 1.50, "tipo": "Frutas"},
        {"nome": "Maçãs", "quantidade": 8, "preco_unitario": 2.50, "tipo": "Frutas"},
        {"nome": "Laranjas", "quantidade": 8, "preco_unitario": 2.00, "tipo": "Frutas"},
        {"nome": "Melancia", "quantidade": 1, "preco_unitario": 22.00, "tipo": "Frutas"},
        {"nome": "Morango", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Frutas"},
        {"nome": "Limões", "quantidade": 4, "preco_unitario": 1.50, "tipo": "Frutas"},
        {"nome": "Ovos (cartela com 30 unidades)", "quantidade": 1, "preco_unitario": 25.00, "tipo": "Fresco"},
        {"nome": "Queijo (1 kg)", "quantidade": 1, "preco_unitario": 40.00, "tipo": "Fresco"},
        {"nome": "Presunto (1 kg)", "quantidade": 1, "preco_unitario": 30.00, "tipo": "Fresco"},
        {"nome": "Carne bovina (kg)", "quantidade": 2, "preco_unitario": 42.00, "tipo": "Fresco"},
        {"nome": "Frango (kg)", "quantidade": 2, "preco_unitario": 26.00, "tipo": "Fresco"},
        {"nome": "Peixe (1 kg)", "quantidade": 1, "preco_unitario": 40.00, "tipo": "Fresco"},
        {"nome": "Iogurtes", "quantidade": 8, "preco_unitario": 3.00, "tipo": "Fresco"},
        {"nome": "Cebola (2 kg)", "quantidade": 2, "preco_unitario": 7.00, "tipo": "Legumes"},
        {"nome": "Alho", "quantidade": 2, "preco_unitario": 2.00, "tipo": "Legumes"},
        {"nome": "Batata (pacote 2 kg)", "quantidade": 1, "preco_unitario": 15.00, "tipo": "Legumes"},
        {"nome": "Cenoura (1 kg)", "quantidade": 1, "preco_unitario": 8.00, "tipo": "Legumes"},
        {"nome": "Tomate (2 kg)", "quantidade": 2, "preco_unitario": 9.00, "tipo": "Legumes"},
        {"nome": "Abóbora (2 kg)", "quantidade": 2, "preco_unitario": 7.00, "tipo": "Legumes"},
        {"nome": "Brócolis", "quantidade": 1, "preco_unitario": 10.00, "tipo": "Legumes"},
        {"nome": "Alface", "quantidade": 2, "preco_unitario": 5.00, "tipo": "Legumes"},
        {"nome": "Arroz (pacote 5 kg)", "quantidade": 1, "preco_unitario": 32.00, "tipo": "Processados"},
        {"nome": "Feijão", "quantidade": 3, "preco_unitario": 9.00, "tipo": "Processados"},
        {"nome": "Macarrão variado", "quantidade": 3, "preco_unitario": 7.00, "tipo": "Processados"},
        {"nome": "Azeite (500 ml)", "quantidade": 1, "preco_unitario": 40.00, "tipo": "Processados"},
        {"nome": "Óleo de soja (2 L)", "quantidade": 1, "preco_unitario": 15.00, "tipo": "Processados"},
        {"nome": "Extrato de tomate", "quantidade": 3, "preco_unitario": 4.00, "tipo": "Processados"},
        {"nome": "Cereais matinais", "quantidade": 1, "preco_unitario": 18.00, "tipo": "Processados"},
        {"nome": "Pães variados", "quantidade": 2, "preco_unitario": 13.00, "tipo": "Processados"},
        {"nome": "Biscoitos doces", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Processados"},
        {"nome": "Biscoitos salgados", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Processados"},
        {"nome": "Detergente (fardo com 12 unidades)", "quantidade": 1, "preco_unitario": 36.00, "tipo": "Limpeza"},
        {"nome": "Sabão em pó (3 kg)", "quantidade": 1, "preco_unitario": 36.00, "tipo": "Limpeza"},
        {"nome": "Amaciante (2 unidades)", "quantidade": 2, "preco_unitario": 14.00, "tipo": "Limpeza"},
        {"nome": "Desinfetante", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Limpeza"},
        {"nome": "Água sanitária", "quantidade": 2, "preco_unitario": 6.00, "tipo": "Limpeza"},
        {"nome": "Papel higiênico (fardo)", "quantidade": 1, "preco_unitario": 43.00, "tipo": "Limpeza"},
        {"nome": "Papel toalha", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Limpeza"},
        {"nome": "Saco de lixo", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Limpeza"},
        {"nome": "Sabonetes", "quantidade": 6, "preco_unitario": 3.00, "tipo": "Limpeza"},
        {"nome": "Xampus", "quantidade": 2, "preco_unitario": 15.00, "tipo": "Limpeza"},
        {"nome": "Creme dental", "quantidade": 2, "preco_unitario": 8.00, "tipo": "Limpeza"},
    ],
}
VETOR_PRODUTOS = copy.deepcopy(BASE_VETOR_PRODUTOS)


def configurar_estilo():
    """Configura a aparência nativa usando ttk.Style."""
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("TFrame", background="#f5f5f5")
    estilo.configure("Titulo.TLabel", font=("Segoe UI", 18, "bold"), background="#f5f5f5", foreground="#1f2937")
    estilo.configure("Slogan.TLabel", font=("Georgia", 11, "italic"), background="#f5f5f5", foreground="#4b5563")
    estilo.configure("Campo.TLabel", font=("Segoe UI", 10, "bold"), background="#f5f5f5", foreground="#374151")
    estilo.configure("Sair.TButton", font=("Segoe UI", 10, "bold"), foreground="#c62828")
    estilo.configure("BotaoPrincipal.TButton", font=("Segoe UI", 10, "bold"))
    estilo.configure("BotaoSecundario.TButton", font=("Segoe UI", 10))
    estilo.configure("BotaoTipo.TButton", font=("Segoe UI", 9, "bold"))
    estilo.configure("Treeview", rowheight=28, font=("Segoe UI", 10))
    estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))


def carregar_dados_iniciais():
    """Carrega sempre os produtos padrão ao abrir o programa."""
    global VETOR_PRODUTOS
    VETOR_PRODUTOS = copy.deepcopy(BASE_VETOR_PRODUTOS)
    salvar_dados()


def salvar_dados():
    """Persiste a lista atual do sistema em arquivo JSON."""
    with open(ARQUIVO_PERSISTENCIA, "w", encoding="utf-8") as arquivo:
        json.dump(VETOR_PRODUTOS, arquivo, ensure_ascii=False, indent=2)


def calcular_subtotal(item):
    """Calcula o subtotal de um item usando quantidade × preço unitário."""
    return item["quantidade"] * item["preco_unitario"]


def atualizar_status(texto):
    """Atualiza a mensagem visível no rodapé da interface."""
    status_var.set(texto)


def obter_total_compra():
    """Calcula o total do perfil atual usando soma dos subtotais."""
    # Usa sum() para somar os subtotais de cada item, substituindo um loop de acumulação manual.
    subtotais = [calcular_subtotal(item) for item in VETOR_PRODUTOS[PERFIL_ATUAL]]
    return sum(subtotais)


def obter_total_itens():
    """Retorna a quantidade de itens do perfil atual."""
    # Usa len() para contar elementos do vetor, substituindo um contador manual em laço.
    return len(VETOR_PRODUTOS[PERFIL_ATUAL])


def limpar_campos():
    """Limpa os campos de entrada para inserir um novo produto."""
    campo_nome.delete(0, tk.END)
    campo_quantidade.delete(0, tk.END)
    campo_preco.delete(0, tk.END)
    campo_tipo.set(TIPOS_ALIMENTO[0])
    campo_nome.focus()


def validar_produto(nome, quantidade_texto, preco_texto):
    """Valida nome, quantidade e preço antes de adicionar o item."""
    nome = nome.strip()
    if nome == "":
        raise ValueError("Informe o nome do produto.")

    try:
        quantidade = int(quantidade_texto)
    except ValueError as erro:
        raise ValueError("A quantidade deve ser um número inteiro válido.") from erro

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    valor = str(preco_texto).strip()
    if valor == "":
        raise ValueError("Informe o preço unitário.")

    valor = valor.replace(" ", "")
    if "," in valor and "." in valor:
        valor = valor.replace(".", "").replace(",", ".")
    elif "," in valor:
        valor = valor.replace(",", ".")

    try:
        preco = float(valor)
    except ValueError as erro:
        raise ValueError("O preço unitário deve ser um número válido.") from erro

    if preco <= 0:
        raise ValueError("O preço unitário deve ser maior que zero.")

    return nome, quantidade, preco


def atualizar_tabela():
    """Atualiza a tabela com os itens do perfil atual."""
    for linha in arvore.get_children():
        arvore.delete(linha)

    lista_ordenada = list(VETOR_PRODUTOS[PERFIL_ATUAL])
    lista_ordenada.reverse()

    for item in lista_ordenada:
        arvore.insert(
            "",
            tk.END,
            values=(
                item["nome"],
                item["tipo"],
                item["quantidade"],
                f"R$ {item['preco_unitario']:.2f}",
                f"R$ {calcular_subtotal(item):.2f}",
            ),
        )

    total_itens = obter_total_itens()
    total_compra = obter_total_compra()
    label_total_itens.config(text=f"Itens: {total_itens}")
    label_total_compra.config(text=f"Total da categoria: R$ {total_compra:.2f}")
    atualizar_status(f"Perfil {PERFIL_ATUAL} carregado com sucesso.")


def selecionar_perfil(perfil):
    """Carrega a lista correspondente ao perfil escolhido."""
    global PERFIL_ATUAL
    PERFIL_ATUAL = perfil
    if 'perfil_selecionado' in globals():
        perfil_selecionado.set(perfil)
    atualizar_tabela()


def adicionar_item():
    """Adiciona um produto novo ou atualiza um já existente no perfil atual."""
    try:
        nome, quantidade, preco = validar_produto(
            campo_nome.get(),
            campo_quantidade.get(),
            campo_preco.get(),
        )

        tipo = campo_tipo.get()
        produto_encontrado = False

        for item in VETOR_PRODUTOS[PERFIL_ATUAL]:
            if item["nome"].lower() == nome.lower():
                item["quantidade"] += quantidade
                item["preco_unitario"] = preco
                item["tipo"] = tipo
                produto_encontrado = True
                break

        if not produto_encontrado:
            VETOR_PRODUTOS[PERFIL_ATUAL].append({
                "nome": nome,
                "quantidade": quantidade,
                "preco_unitario": preco,
                "tipo": tipo,
            })

        limpar_campos()
        atualizar_tabela()
        salvar_dados()
    except ValueError as erro:
        messagebox.showerror("Dados inválidos", str(erro))
    except Exception as erro:
        messagebox.showerror("Erro inesperado", f"Não foi possível incluir o item: {erro}")


def remover_item_selecionado():
    """Remove uma quantidade do item selecionado ou apaga o produto quando a quantidade chegar a zero."""
    item_selecionado = arvore.selection()
    if not item_selecionado:
        messagebox.showwarning("Nada selecionado", "Selecione um produto para remover.")
        return

    nome = arvore.item(item_selecionado[0], "values")[0]
    quantidade_para_remover = simpledialog.askinteger("Remover quantidade", f"Informe quantas unidades de '{nome}' deseja remover:")

    if quantidade_para_remover is None:
        return

    if quantidade_para_remover <= 0:
        messagebox.showerror("Quantidade inválida", "A quantidade para remover deve ser maior que zero.")
        return

    for item in VETOR_PRODUTOS[PERFIL_ATUAL]:
        if item["nome"].lower() == nome.lower():
            if quantidade_para_remover >= item["quantidade"]:
                VETOR_PRODUTOS[PERFIL_ATUAL] = [produto for produto in VETOR_PRODUTOS[PERFIL_ATUAL] if produto["nome"].lower() != nome.lower()]
                atualizar_tabela()
                salvar_dados()
                messagebox.showinfo("Remoção", f"Produto '{nome}' removido com sucesso.")
            else:
                item["quantidade"] -= quantidade_para_remover
                atualizar_tabela()
                salvar_dados()
                messagebox.showinfo("Remoção", f"Quantidade removida com sucesso: {quantidade_para_remover} unidade(s) de '{nome}'.")
            return

    messagebox.showwarning("Produto não encontrado", f"Produto '{nome}' não foi encontrado na lista.")


def alterar_quantidade_item():
    """Permite alterar a quantidade do item selecionado."""
    item_selecionado = arvore.selection()
    if not item_selecionado:
        messagebox.showwarning("Seleção obrigatória", "Escolha um produto antes de alterar a quantidade.")
        return

    nome = arvore.item(item_selecionado[0], "values")[0]
    nova_quantidade = simpledialog.askinteger("Nova quantidade", f"Informe a nova quantidade para '{nome}':")

    if nova_quantidade is None:
        return

    if nova_quantidade <= 0:
        messagebox.showerror("Quantidade inválida", "A quantidade deve ser maior que zero.")
        return

    for item in VETOR_PRODUTOS[PERFIL_ATUAL]:
        if item["nome"].lower() == nome.lower():
            item["quantidade"] = nova_quantidade
            break

    atualizar_tabela()
    salvar_dados()
    messagebox.showinfo("Atualização", f"Quantidade de '{nome}' alterada com sucesso.")


def alterar_preco_item():
    """Permite alterar o preço unitário do item selecionado."""
    item_selecionado = arvore.selection()
    if not item_selecionado:
        messagebox.showwarning("Seleção obrigatória", "Escolha um produto antes de alterar o preço.")
        return

    nome = arvore.item(item_selecionado[0], "values")[0]
    novo_preco = simpledialog.askfloat("Novo preço", f"Informe o novo preço unitário para '{nome}':")

    if novo_preco is None:
        return

    if novo_preco <= 0:
        messagebox.showerror("Preço inválido", "O preço unitário deve ser maior que zero.")
        return

    for item in VETOR_PRODUTOS[PERFIL_ATUAL]:
        if item["nome"].lower() == nome.lower():
            item["preco_unitario"] = novo_preco
            break

    atualizar_tabela()
    salvar_dados()
    messagebox.showinfo("Atualização", f"Preço de '{nome}' alterado com sucesso.")


def limpar_lista_perfil():
    """Remove todos os itens do perfil atual após confirmação."""
    if not VETOR_PRODUTOS[PERFIL_ATUAL]:
        messagebox.showinfo("Lista vazia", f"O perfil {PERFIL_ATUAL} já está vazio.")
        return

    confirmacao = messagebox.askyesno("Confirmação", f"Deseja limpar todos os itens de {PERFIL_ATUAL}?")
    if confirmacao:
        VETOR_PRODUTOS[PERFIL_ATUAL] = []
        atualizar_tabela()
        salvar_dados()
        messagebox.showinfo("Lista limpa", f"O perfil {PERFIL_ATUAL} foi esvaziado.")


def resetar_para_inicio():
    """Restaura os valores iniciais e retorna ao perfil padrão."""
    global PERFIL_ATUAL
    VETOR_PRODUTOS.clear()
    VETOR_PRODUTOS.update(copy.deepcopy(BASE_VETOR_PRODUTOS))
    PERFIL_ATUAL = "Solo"
    if 'perfil_selecionado' in globals():
        perfil_selecionado.set(PERFIL_ATUAL)
    if 'atualizar_tabela' in globals():
        atualizar_tabela()
    salvar_dados()


def fechar_app_com_reset():
    """Reseta os dados antes de fechar o app para reabrir com os valores padrão."""
    resetar_para_inicio()
    janela.destroy()


def confirmar_pedido():
    """Encaminha a lista para preparação e solicita a forma de pagamento escolhida."""
    if not VETOR_PRODUTOS[PERFIL_ATUAL]:
        messagebox.showwarning("Lista vazia", "O perfil atual não possui itens para confirmar o pedido.")
        return

    janela_pagamento = tk.Toplevel(janela)
    janela_pagamento.title("Forma de pagamento")
    janela_pagamento.geometry("420x220")
    janela_pagamento.transient(janela)
    janela_pagamento.grab_set()

    ttk.Label(janela_pagamento, text="Selecione a forma de pagamento:", style="Campo.TLabel").pack(padx=18, pady=(18, 10), anchor="w")
    formas_pagamento = ["Dinheiro", "Cartão de crédito", "Cartão de débito", "Pix"]
    variavel_pagamento = tk.StringVar(value=formas_pagamento[0])
    combobox_pagamento = ttk.Combobox(janela_pagamento, textvariable=variavel_pagamento, values=formas_pagamento, state="readonly", width=28)
    combobox_pagamento.pack(padx=18, pady=(0, 12), fill=tk.X)

    variavel_parcelas = tk.StringVar(value="1")
    label_parcelas = ttk.Label(janela_pagamento, text="Parcelas:", style="Campo.TLabel")
    opcoes_parcelas = [str(numero) for numero in range(1, 13)]
    combobox_parcelas = ttk.Combobox(janela_pagamento, textvariable=variavel_parcelas, values=opcoes_parcelas, state="readonly", width=10)

    def atualizar_parcelas(evento=None):
        if variavel_pagamento.get() == "Cartão de crédito":
            label_parcelas.pack(padx=18, pady=(0, 6), anchor="w")
            combobox_parcelas.pack(padx=18, pady=(0, 12), anchor="w")
        else:
            label_parcelas.pack_forget()
            combobox_parcelas.pack_forget()

    combobox_pagamento.bind("<<ComboboxSelected>>", atualizar_parcelas)
    atualizar_parcelas()

    def fechar_app():
        resetar_para_inicio()
        janela.destroy()

    def voltar_inicial():
        janela_pagamento.destroy()
        resetar_para_inicio()
        messagebox.showinfo("Início", "O sistema foi reiniciado para uma nova compra.")

    def finalizar_confirmacao():
        forma = variavel_pagamento.get()
        parcelas = variavel_parcelas.get()
        valor_total = obter_total_compra()
        janela_pagamento.destroy()

        tela_final = tk.Toplevel(janela)
        tela_final.title("Pedido confirmado")
        tela_final.geometry("420x220")
        tela_final.transient(janela)
        tela_final.grab_set()

        ttk.Label(tela_final, text=f"Pedido do perfil {PERFIL_ATUAL} confirmado!", style="Campo.TLabel").pack(pady=(20, 10))
        ttk.Label(tela_final, text=f"Forma de pagamento: {forma}", style="Campo.TLabel").pack(pady=(0, 6))
        if forma == "Cartão de crédito":
            ttk.Label(tela_final, text=f"Parcelas: {parcelas}x", style="Campo.TLabel").pack(pady=(0, 6))
        ttk.Label(tela_final, text=f"Valor total da compra: R$ {valor_total:.2f}", style="Campo.TLabel").pack(pady=(0, 10))

        ttk.Button(tela_final, text="Fechar app", command=fechar_app, style="BotaoPrincipal.TButton").pack(side=tk.LEFT, padx=(45, 10), pady=(10, 0))
        ttk.Button(tela_final, text="Voltar ao início", command=voltar_inicial, style="BotaoSecundario.TButton").pack(side=tk.RIGHT, padx=(10, 45), pady=(10, 0))

    ttk.Button(janela_pagamento, text="Confirmar", command=finalizar_confirmacao, style="BotaoPrincipal.TButton").pack(pady=(0, 12))


def principal():
    """Função principal que monta a interface da aplicação."""
    global janela, arvore, campo_nome, campo_quantidade, campo_preco, campo_tipo, status_var, label_total_itens, label_total_compra, perfil_selecionado

    carregar_dados_iniciais()

    janela = tk.Tk()
    perfil_selecionado = tk.StringVar(value=PERFIL_ATUAL)
    campo_tipo = tk.StringVar(value=TIPOS_ALIMENTO[0])
    janela.title("EAD List")
    janela.geometry("1150x720")
    janela.minsize(900, 620)
    janela.configure(bg="#f5f5f5")
    janela.protocol("WM_DELETE_WINDOW", fechar_app_com_reset)

    configurar_estilo()

    frame_principal = ttk.Frame(janela, padding=18)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    cabecalho = ttk.Frame(frame_principal)
    cabecalho.grid(row=0, column=0, columnspan=12, sticky="ew", pady=(0, 12))
    titulo = ttk.Label(cabecalho, text="EAD List", style="Titulo.TLabel")
    titulo.pack(side=tk.LEFT, anchor="s", padx=(0, 14))
    slogan = ttk.Label(
        cabecalho,
        text="Essencial para a sua rotina, Acessível ao seu bolso, Direto no mercado.",
        style="Slogan.TLabel",
    )
    slogan.pack(side=tk.LEFT, anchor="s", pady=(0, 3))
    ttk.Button(cabecalho, text="SAIR", command=fechar_app_com_reset, style="Sair.TButton").pack(side=tk.RIGHT, anchor="n")

    frame_perfis = ttk.LabelFrame(frame_principal, text="Perfis", padding=(12, 10))
    frame_perfis.grid(row=1, column=0, columnspan=12, sticky="ew", pady=(0, 12))

    for indice, perfil in enumerate(PERFIS):
        ttk.Radiobutton(
            frame_perfis,
            text=perfil,
            value=perfil,
            variable=perfil_selecionado,
            command=lambda perfil=perfil: selecionar_perfil(perfil),
        ).grid(row=0, column=indice, padx=(0, 20), sticky="w")

    frame_entrada = ttk.LabelFrame(frame_principal, text="Personalizar lista", padding=12)
    frame_entrada.grid(row=2, column=0, columnspan=12, sticky="ew", pady=(0, 12))

    ttk.Label(frame_entrada, text="Produto:", style="Campo.TLabel").grid(row=0, column=0, padx=(0, 8), pady=6, sticky="w")
    campo_nome = ttk.Entry(frame_entrada, width=22)
    campo_nome.grid(row=0, column=1, padx=(0, 10), pady=6, sticky="ew")

    ttk.Label(frame_entrada, text="Quantidade:", style="Campo.TLabel").grid(row=0, column=2, padx=(0, 4), pady=6, sticky="w")
    campo_quantidade = ttk.Entry(frame_entrada, width=10)
    campo_quantidade.grid(row=0, column=3, padx=(0, 10), pady=6, sticky="ew")

    ttk.Label(frame_entrada, text="Preço unitário:", style="Campo.TLabel").grid(row=0, column=4, padx=(0, 8), pady=6, sticky="w")
    campo_preco = ttk.Entry(frame_entrada, width=12)
    campo_preco.grid(row=0, column=5, padx=(0, 12), pady=6, sticky="ew")

    ttk.Label(frame_entrada, text="Tipo do alimento:", style="Campo.TLabel").grid(row=1, column=0, padx=(0, 8), pady=(8, 6), sticky="w")
    combo_tipo = ttk.Combobox(frame_entrada, textvariable=campo_tipo, values=TIPOS_ALIMENTO, state="readonly", width=18)
    combo_tipo.grid(row=1, column=1, padx=(0, 12), pady=(8, 6), sticky="w")

    ttk.Button(frame_entrada, text="Adicionar item", command=adicionar_item, style="BotaoPrincipal.TButton").grid(row=2, column=0, padx=(0, 8), pady=10, sticky="w")
    ttk.Button(frame_entrada, text="Remover item", command=remover_item_selecionado, style="BotaoPrincipal.TButton").grid(row=2, column=1, padx=(0, 8), pady=10, sticky="w")
    ttk.Button(frame_entrada, text="Alterar quantidade", command=alterar_quantidade_item, style="BotaoPrincipal.TButton").grid(row=2, column=2, padx=(0, 8), pady=10, sticky="w")
    ttk.Button(frame_entrada, text="Alterar preço", command=alterar_preco_item, style="BotaoPrincipal.TButton").grid(row=2, column=3, padx=(0, 8), pady=10, sticky="w")

    status_var = tk.StringVar(value="Sistema iniciado. Escolha um perfil para carregar a lista.")
    status_label = ttk.Label(frame_principal, textvariable=status_var, foreground="#1d4ed8")
    status_label.grid(row=5, column=0, columnspan=12, sticky="w", pady=(0, 8))

    tabela_frame = ttk.Frame(frame_principal)
    tabela_frame.grid(row=6, column=0, columnspan=12, sticky="nsew")
    frame_principal.grid_columnconfigure(0, weight=1)
    frame_principal.grid_rowconfigure(6, weight=1)

    colunas = ("Produto", "Tipo", "Quantidade", "Preço Unit.", "Subtotal")
    arvore = ttk.Treeview(tabela_frame, columns=colunas, show="headings")

    for coluna in colunas:
        arvore.heading(coluna, text=coluna)
        arvore.column(coluna, anchor="center", width=150)

    arvore.column("Produto", width=220, anchor="w")
    arvore.column("Tipo", width=140)
    arvore.column("Quantidade", width=100)
    arvore.column("Preço Unit.", width=140)
    arvore.column("Subtotal", width=140)

    barra_rolagem = ttk.Scrollbar(tabela_frame, orient="vertical", command=arvore.yview)
    arvore.configure(yscrollcommand=barra_rolagem.set)

    arvore.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    barra_rolagem.pack(side=tk.RIGHT, fill=tk.Y)

    botoes_rodape = ttk.Frame(frame_principal)
    botoes_rodape.grid(row=7, column=0, columnspan=12, sticky="ew", pady=(12, 0))
    ttk.Button(botoes_rodape, text="Limpar perfil", command=limpar_lista_perfil, style="BotaoSecundario.TButton").pack(side=tk.LEFT, padx=(0, 8))
    ttk.Button(botoes_rodape, text="Salvar alterações", command=salvar_dados, style="BotaoPrincipal.TButton").pack(side=tk.LEFT, padx=(0, 8))
    ttk.Button(botoes_rodape, text="Confirmar pedido", command=confirmar_pedido, style="BotaoPrincipal.TButton").pack(side=tk.LEFT)

    frame_resumo = ttk.Frame(frame_principal)
    frame_resumo.grid(row=7, column=0, columnspan=12, sticky="e", pady=(0, 0))
    label_total_itens = ttk.Label(frame_resumo, text="Itens: 0", style="Campo.TLabel")
    label_total_itens.grid(row=0, column=0, padx=(0, 18), sticky="e")
    label_total_compra = ttk.Label(frame_resumo, text="Total da categoria: R$ 0.00", style="Campo.TLabel")
    label_total_compra.grid(row=0, column=1, sticky="e")

    # Repetição: a tabela é atualizada sempre que o perfil ou os dados forem alterados.
    atualizar_tabela()

    # Seleção: a escolha do perfil define qual vetor será exibido ao usuário.
    janela.mainloop()


if __name__ == "__main__":
    principal()
