# EAD Listy

Aplicação desktop em Python para organização de compras por perfil, com controle de quantidade, preço unitário, categoria de produtos e confirmação final do pedido.

## Visão geral

O EAD Listy foi desenvolvido para facilitar a gestão de listas de compras em cenários de uso pessoal ou familiar. A aplicação permite selecionar o perfil ativo, adicionar itens, ajustar valores e concluir a compra com confirmação de pagamento.

Os perfis disponíveis são:

- Solo
- Duo
- Familia

## Funcionalidades implementadas

- Cadastro de produtos com nome, quantidade, preço e categoria
- Suporte a múltiplos perfis de compra
- Atualização da tabela em tempo real
- Ajuste de quantidade e preço dos itens já cadastrados
- Remoção de itens ou de quantidade específica
- Cálculo automático de subtotal e total da categoria
- Confirmação de pedido com escolha de forma de pagamento
- Parcelamento em cartão de crédito de 1 a 12 vezes
- Reinicialização da base padrão ao fechar a aplicação
- Persistência local em arquivo JSON

## Tecnologias

- Python 3
- Tkinter
- ttk
- JSON

## Requisitos

- Python 3.9 ou superior
- Tkinter instalado no ambiente Python

Verificação rápida no Windows:

```bash
python -m tkinter
```

## Como executar

1. Acesse a pasta do projeto:

```bash
cd "c:\Workspace\VScode\shopping-list"
```

2. Execute a aplicação:

```bash
py .\shopping_list_app.py
```

Ou:

```bash
python .\shopping_list_app.py
```

## Estrutura do projeto

```text
shopping-list/
├── shopping_list_app.py          # Aplicação principal
├── listas_personalizadas.json    # Dados persistidos por perfil
├── README.md                     # Documentação pública do projeto
├── ROADMAP.md                    # Plano de desenvolvimento e evolução
├── MEMORY.md                     # Contexto técnico e decisões do projeto
├── .gitignore                    # Arquivos ignorados pelo Git
├── .venv/                        # Ambiente virtual local
└── ia/
    └── Prompt Python.md
```

## Fluxo de uso

1. Escolha o perfil desejado: Solo, Duo ou Familia.
2. Cadastre o produto com nome, quantidade, preço e tipo.
3. Ajuste valores conforme necessário.
4. Remova itens ou quantidades quando desejado.
5. Confirme o pedido.
6. Escolha a forma de pagamento.
7. Se for cartão de crédito, informe o número de parcelas.
8. Confirme o valor final da compra.

## Observações importantes

- A aplicação reseta os itens para a base padrão ao fechar.
- A persistência é local, em arquivo JSON.
- A lógica atual foi construída em estrutura procedural, com foco em funcionalidade e uso prático.

## Licença

Este projeto está disponível para fins educacionais e pessoais.

## Autores

- Aoliabe Santiago
- Diego Danilo
- Erick Lima Moraes

Projeto desenvolvido em colaboração para gestão de lista de compras com foco em perfis, categoria de produtos e confirmação de pedido.
