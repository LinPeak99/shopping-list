# EAD Listy - Estoque, Alimentação e Domicílio

Aplicação desktop em Python com interface gráfica usando Tkinter para gerenciar listas de compras por perfil, com categorias, valores, alteração de itens e confirmação de pedido.

## Visão geral

Este projeto foi desenvolvido para facilitar a organização de compras por perfil:

- Solo
- Duo
- Familia

A aplicação permite:

- adicionar produtos à lista
- remover itens ou quantidades
- alterar quantidade e preço unitário
- selecionar o tipo do alimento
- visualizar subtotal e total da categoria
- confirmar pedido e escolher a forma de pagamento
- configurar parcelamento em cartão de crédito
- reiniciar o sistema com os produtos padrão

## Funcionalidades principais

- Gestão de listas por perfil
- Produtos com categoria por tipo de alimento
- Cálculo automático de subtotal e total
- Atualização em tempo real da tabela
- Persistência local em arquivo JSON
- Confirmação de pedido com forma de pagamento
- Parcelamento de 1 a 12 vezes em cartão de crédito
- Interface simples e prática para uso diário

## Tecnologias

- Python 3
- Tkinter
- JSON para armazenamento local

## Requisitos

- Python 3.9 ou superior
- Tkinter instalado no ambiente Python

No Windows, normalmente o Tkinter já vem com a instalação do Python. Caso necessário, confirme com:

```bash
python -m tkinter
```

## Como executar

1. Abra o terminal
2. Acesse a pasta do projeto:

```bash
cd "c:\Workspace\VScode\shopping-list"
```

3. Execute a aplicação:

```bash
py .\shopping_list_app.py
```

Ou diretamente com o Python:

```bash
python .\shopping_list_app.py
```

## Estrutura do projeto

```text
shopping-list/
├── shopping_list_app.py   # Aplicação principal
├── listas_personalizadas.json  # Arquivo de persistência local
├── README.md              # Documentação do projeto
└── .gitignore             # Configuração Git (se existir)
```

## Fluxo de uso

1. Selecione o perfil desejado: Solo, Duo ou Familia
2. Cadastre um novo produto com:
   - nome
   - quantidade
   - preço unitário
   - tipo do alimento
3. Ajuste quantidade ou preço caso necessário
4. Remova itens ou unidades conforme a necessidade
5. Confirme o pedido
6. Escolha a forma de pagamento
7. Se for cartão de crédito, escolha o número de parcelas
8. Veja o valor total final da compra

## Observações

- Ao fechar o aplicativo, o sistema volta aos produtos padrão para reiniciar a experiência com a base inicial.
- Os dados são salvos localmente em JSON para facilitar o uso contínuo da aplicação.

## Licença

Este projeto está disponível para fins educacionais e pessoais.

## Autores

- Aoliabe Santiago
- Diego Danilo
- Erick Lima Moraes

Projeto desenvolvido em colaboração como aplicação de lista de compras com foco em perfil, categoria e confirmação de pedido.
