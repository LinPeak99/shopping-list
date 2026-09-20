# MEMORY - EAD Listy

## Visão geral

Este arquivo registra a memória de trabalho do projeto EAD Listy para preservar o contexto do desenvolvimento e facilitar continuidade por parte de outros agentes de IA ou desenvolvedores.

O objetivo é documentar decisões importantes, regras de negócio, arquitetura escolhida, padrões adotados e histórico de mudanças para que o projeto possa evoluir sem perder contexto.

---

## 1. Contexto do projeto

- Nome do software: EAD Listy
- Tipo: aplicação desktop em Python
- Framework principal: Tkinter
- Objetivo: gerenciar listas de compras por perfil com organização, cálculo de valores e confirmação de pedido
- Público-alvo: uso pessoal e acadêmico, especialmente em cenário de listas por perfil familiar ou compartilhada

---

## 2. Regras de negócio implementadas

### Perfil de compra
- O sistema aceita 3 perfis:
  - Solo
  - Duo
  - Familia
- A seleção do perfil define a lista ativa e o comportamento da compra.
- A lista deve ser atualizada dinamicamente conforme o perfil selecionado.

### Produtos
- Cada item possui:
  - nome
  - quantidade
  - preço unitário
  - tipo do alimento
- O usuário pode adicionar, remover e ajustar valores.
- O processo de remoção deve respeitar a regra de quantidade e item selecionado.

### Tipos de alimento
- Tipos existentes incluem, principalmente:
  - Bebida
  - Frutas
  - Legumes
  - Outros alimentos relevantes ao contexto do projeto
- A categoria deve estar disponível no cadastro do produto.

### Cálculo financeiro
- O subtotal de cada item deve ser calculado como:
  quantidade x preço unitário
- O total da categoria deve refletir a soma dos subtotais daquele tipo.
- O total geral da compra deve ser atualizado em tempo real.

### Confirmação de pedido
- O usuário pode confirmar a compra após revisar os itens.
- A confirmação exige escolha da forma de pagamento.
- Se a forma for cartão de crédito, deve haver escolha de parcelamento.

### Reinicialização do sistema
- Ao fechar a aplicação, o sistema deve retornar aos produtos padrão para reiniciar a experiência com a base inicial.
- Isso garante que o software permaneça consistente e previsível em cada nova execução.

---

## 3. Decisões de implementação

### Estrutura do código
- A aplicação foi desenvolvida em um único arquivo principal: shopping_list_app.py
- O código foi mantido de forma procedural, sem uso de classes, para facilitar leitura e manutenção no contexto do projeto atual
- As variáveis globais controlam estado da interface, perfil ativo, itens e valores calculados

### Persistência
- Os dados são salvos em arquivo JSON local
- O armazenamento local é suficiente para o estado atual do projeto
- O arquivo listas_personalizadas.json foi utilizado como base para persistência

### UI / interação
- A interface foi construída com Tkinter e ttk
- Os botões e campos foram organizados em blocos visuais
- O status da operação e o total da compra precisam ser atualizados em tempo real
- O sistema deve ser simples e direto, priorizando uso prático

### Nome da marca
- O nome do software foi definido como EAD Listy
- Esse nome deve ser mantido na documentação, janela principal e apresentação do projeto

---

## 4. Convenções de desenvolvimento

### Nomenclatura
- Variáveis em Python devem seguir padrão snake_case
- Funções devem ter nomes descritivos, como:
  - adicionar_item
  - remover_item_selecionado
  - alterar_quantidade_item
  - alterar_preco_item
  - confirmar_pedido
  - principal

### Organização de lógica
- Lógica de negócios e interface estão juntas no mesmo arquivo no momento atual
- Prefere-se manter a lógica do fluxo da compra e UI em um único ponto para reduzir complexidade em versão inicial

### Tratamento de valores
- Preços devem aceitar valores em decimal, inclusive com vírgula e ponto
- O cálculo final deve ser convertido para moeda com duas casas decimais
- O sistema deve evitar erros de entrada sem quebrar a aplicação

---

## 5. Problemas resolvidos e aprendizados

### 1. Erro de criação de variáveis antes da janela principal
- O problema ocorreu porque algumas variáveis Tk foram criadas antes da instância principal do Tk.
- Solução: criar a janela antes de inicializar certas variáveis e manter um único controle para perfil selecionado.

### 2. Conflitos de lógica de perfil
- Houve duplicidade de seleção de perfil e inconsistência no estado atual.
- Solução: usar uma única StringVar para sincronizar a seleção visual e a lógica interna.

### 3. Ajuste de categorias e tipos
- A categoria extra e a estrutura de tipos inicialmente geraram ruído na UX.
- Solução: manter a seleção clara do tipo do alimento e simplificar a entrada para evitar excesso de campos.

### 4. Reset do sistema
- Foi necessário garantir que o software voltasse aos valores iniciais quando reiniciado.
- Solução: usar regra de reset ao fechar para restaurar base padrão.

### 5. Personalização dos valores e ordem dos itens
- A lista precisava refletir itens novos no topo e manter a ordem mais útil para o usuário.
- Solução: inserir novos itens no início da lista e manter ordenação funcional.

---

## 6. Diretrizes para continuidade

Ao continuar o desenvolvimento, o agente deve respeitar estas premissas:

- manter o nome EAD Listy consistente em todos os pontos do projeto
- preservar a lógica de perfis Solo/Duo/Familia
- respeitar a regra de cálculo financeiro e parcelamento
- manter a aplicação simples, prática e previsível
- priorizar funcionalidade antes de estética avançada
- documentar qualquer mudança de regra de negócio neste arquivo

---

## 7. Checklist de manutenção de memória

Sempre que houver mudança relevante no projeto, registrar:

- nova funcionalidade
- ajuste de regra de negócio
- alteração de nome, marca ou identidade visual
- mudança de arquitetura
- alteração em persistência ou dados
- correções de bugs relevantes
- decisões futuras de evolução

---

## 8. Registro de evolução do projeto

### Etapa inicial
- Criação da aplicação desktop
- Estrutura básica de compra por perfil
- Funcionalidade de adicionar itens

### Etapa intermediatória
- Implementação de alteração de quantidade e preço
- Ajuste de subtotal e total
- Adição de categoria de tipo de alimento
- Confirmação de pedido e pagamento

### Etapa atual
- Nome do software definido como EAD Listy
- Ajustes finais na UX e comportamento
- Criação da documentação de apresentação
- Preparação para uso e evolução futura

---

## 9. Recomendação para agentes futuros

Agentes que forem trabalhar no projeto devem ler primeiro:

1. README.md
2. ROADMAP.md
3. MEMORY.md
4. shopping_list_app.py

Isso ajuda a preservar contexto, evitar regressões e manter coerência com as escolhas já feitas.

---

## 10. Resumo executivo

O EAD Listy foi concebido como uma ferramenta prática de listagem de compras por perfil, com foco em simplicidade, usabilidade e lógica financeira clara. A aplicação já conseguiu consolidar um conjunto funcional de operações e regras de negócio. O principal valor desta memória é garantir que futuras alterações mantenham a coesão do projeto e sigam as escolhas já validadas.
