# MEMORY - EAD Listy

## Visão geral

Este arquivo registra a memória de trabalho do projeto EAD Listy com base no estado real do código atual. Ele foi criado para preservar o contexto do desenvolvimento, manter a consistência das decisões técnicas e facilitar a continuidade por outros agentes de IA ou desenvolvedores.

A aplicação atual já está funcional e implementa a lógica principal de listagem de compras por perfil, cálculo financeiro, persistência em JSON e confirmação de pedido.

---

## 1. Contexto do projeto

- Nome do software: EAD Listy
- Tipo: aplicação desktop em Python
- Interface: Tkinter + ttk
- Persistência: JSON local
- Objetivo: gerenciar listas de compras por perfil, controlar quantidade e preço, calcular totais e finalizar a compra
- Público-alvo: uso pessoal, acadêmico e doméstico

Arquivos principais:

- shopping_list_app.py
- listas_personalizadas.json
- README.md
- ROADMAP.md
- MEMORY.md

---

## 2. Estado real da aplicação

### Funcionalidades implementadas

#### Perfis
- Solo
- Duo
- Familia

A aplicação alterna automaticamente entre listas por perfil e atualiza a tabela correspondente ao perfil ativo.

#### Cadastro de itens
- Nome do produto
- Quantidade
- Preço unitário
- Tipo do alimento

A lógica valida entradas e evita valores inválidos antes de gravar os dados.

#### Tipos de alimento disponíveis
- Frutas
- Frios
- Fresco
- Legumes
- Processados
- Limpeza
- Bebida

#### Cálculo financeiro
- Subtotal por item: quantidade × preço unitário
- Total da categoria: soma dos subtotais do perfil atual
- Total da compra: calculado em tempo real

#### Remoção e ajuste
- Remoção de item selecionado
- Remoção por quantidade específica
- Alteração de quantidade
- Alteração de preço
- Limpeza da lista do perfil atual

#### Confirmação de pedido
- Seleção de forma de pagamento
- Opções: Dinheiro, Cartão de crédito, Cartão de débito, Pix
- Parcelamento de 1 a 12 vezes quando o pagamento é cartão de crédito
- Tela final de confirmação do pedido

#### Reinicialização
- Ao fechar a aplicação, o sistema reseta para a base padrão
- A aplicação volta ao estado inicial ao abrir novamente

---

## 3. Regras de negócio confirmadas no código

### Regra 1: base padrão sempre retorna ao abrir o programa
- A função carregar_dados_iniciais() sobrescreve os dados atuais com BASE_VETOR_PRODUTOS.
- Isso garante que cada execução inicie em um estado previsível.

### Regra 2: cada perfil tem sua própria lista
- O dicionário BASE_VETOR_PRODUTOS armazena lista separada para Solo, Duo e Familia.
- O perfil atual define qual lista é exibida na interface.

### Regra 3: produtos duplicados aumentam a quantidade
- Se o usuário adiciona um produto que já existe, o sistema soma a nova quantidade ao item existente.
- O tipo e o preço também são atualizados.

### Regra 4: remoção parcial é permitida
- Se a quantidade informada para remoção for menor que a atual, apenas reduz a quantidade.
- Se for maior ou igual, remove o item total do perfil.

### Regra 5: valores monetários são normalizados
- O sistema aceita valores com vírgula e ponto.
- O valor é normalizado antes do cálculo para evitar erros de precisão.

### Regra 6: lista recente aparece primeiro
- A função atualizar_tabela() inverte a ordem da lista antes de mostrar na Treeview.
- Isso faz com que itens recém-adicionados apareçam no topo da tabela.

### Regra 7: reset ao fechar é uma decisão deliberada
- A função fechar_app_com_reset() chama resetar_para_inicio() antes de destruir a janela.
- Isso foi implementado para manter a experiência consistente e evitar estados persistentes ocupando a base do projeto.

---

## 4. Decisões de implementação reais

### Estrutura do código
- O projeto foi construído em um único arquivo principal: shopping_list_app.py.
- A lógica de interface e regra de negócio foi organizada proceduralmente, sem uso de classes.
- O código usa variáveis globais para controlar o estado da aplicação.

### Persistência
- Os dados de compra são salvos em JSON local.
- O caminho é definido por ARQUIVO_PERSISTENCIA.
- O arquivo usado no projeto é:
  - listas_personalizadas.json

### Interface gráfica
- O app usa Tkinter e ttk.
- Componentes principais:
  - Frame
  - LabelFrame
  - Entry
  - Combobox
  - Button
  - RadioButton
  - Treeview
  - Scrollbar

### Estilo visual
- O tema é configurado com ttk.Style().
- Tema atual: "clam".
- A janela principal mostra o título EAD Listy.

### Nome da marca
- O nome do software foi definido como EAD Listy.
- Esse nome deve ser mantido em documentos, interface e comunicação do projeto.

---

## 5. Variáveis e funções centrais

### Variáveis globais
- PERFIS
- TIPOS_ALIMENTO
- PERFIL_ATUAL
- BASE_VETOR_PRODUTOS
- VETOR_PRODUTOS
- ARQUIVO_PERSISTENCIA

### Funções centrais do sistema
- configurar_estilo()
- carregar_dados_iniciais()
- salvar_dados()
- calcular_subtotal(item)
- atualizar_status(texto)
- obter_total_compra()
- obter_total_itens()
- limpar_campos()
- validar_produto(nome, quantidade_texto, preco_texto)
- atualizar_tabela()
- selecionar_perfil(perfil)
- adicionar_item()
- remover_item_selecionado()
- alterar_quantidade_item()
- alterar_preco_item()
- limpar_lista_perfil()
- resetar_para_inicio()
- fechar_app_com_reset()
- confirmar_pedido()
- principal()

---

## 6. Fluxo real da aplicação

1. O programa inicia em principal().
2. A base padrão é carregada via carregar_dados_iniciais().
3. A janela principal do EAD Listy abre.
4. O usuário escolhe um perfil: Solo, Duo ou Familia.
5. A tabela lista os itens daquele perfil.
6. O usuário preenche os campos de produto, quantidade e preço.
7. O sistema valida os dados e inclui o item.
8. O subtotal e o total são recalculados automaticamente.
9. O usuário pode editar ou remover itens selecionados.
10. O pedido é confirmado.
11. A aplicação abre a janela de pagamento.
12. Caso a escolha seja cartão de crédito, solicita parcelas.
13. A confirmação final é exibida na tela.
14. O app pode ser reiniciado para uma nova compra.

---

## 7. Aprendizados importantes do projeto

### 1. Ordem de criação de widgets e variáveis Tk
- Houve erro de runtime quando variáveis Tk eram criadas antes da janela principal existir.
- Solução: criar a instância do Tk antes de inicializar componentes dependentes da interface.

### 2. Perfil ativo deve ser sincronizado em um único ponto
- Foi necessário centralizar a seleção do perfil em uma única StringVar para manter o estado consistente.

### 3. UX da listagem precisa ser simples e objetiva
- O projeto foi ajustado para evitar excesso de campos e manter a interação direta.
- O formulário foi otimizado para coletar apenas o necessário para o uso diário.

### 4. Ordenação visual é funcional
- Os itens novos devem aparecer no topo para reforçar a sensação de compra atual.
- Esse comportamento foi preservado em atualizar_tabela().

### 5. Reset foi uma decisão arquitetural
- A base padrão foi configurada para sobrescrever o estado ao fechar para não acumular lixo de dados e melhorar a previsibilidade do software.

---

## 8. Diretrizes para continuidade

Ao continuar o desenvolvimento, o agente deve respeitar as regras abaixo:

- manter o nome EAD Listy em todos os pontos do projeto
- preservar a lógica de perfis Solo/Duo/Familia
- manter a lógica de base padrão e reset ao fechar
- respeitar o cálculo de subtotal e total
- manter a validação de dados monetários e quantitativos
- preservar o fluxo de pagamento e parcelas
- documentar mudanças relevantes neste arquivo

---

## 9. Checklist de manutenção de memória

Sempre que houver alteração relevante, registrar:

- nova funcionalidade
- regra de negócio alterada
- ajuste visual ou de identidade
- mudança na arquitetura
- alteração de persistência
- correção de bug relevante
- planejamento de evolução futura

---

## 10. Resumo executivo

O EAD Listy evoluiu para uma aplicação funcional de listagem de compra por perfil, com interface em Tkinter, persistência em JSON, cálculo de valores e confirmação de pedido. O sistema já consolidou sua lógica principal e esta memória serve como referência para garantir consistência em futuras evoluções, preservando a base do trabalho realizado até o momento.
