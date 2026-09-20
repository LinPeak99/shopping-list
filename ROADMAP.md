# ROADMAP - EAD Listy

## Visão geral

Este documento documenta o desenvolvimento realizado até o momento no projeto EAD Listy e serve como base para futuras melhorias, refinamentos e novas entregas.

O projeto está em uma fase funcional, com interface gráfica em Tkinter, gestão de listas por perfil, cálculo de valores, confirmação de pedido e persistência local.

---

## Status atual

### ✅ Concluído

#### 1. Estrutura inicial da aplicação
- Criação da interface principal com Tkinter
- Organização visual em área de perfis, formulário e tabela
- Configuração do estilo da aplicação com ttk

#### 2. Gestão de perfis
- Perfis implementados: Solo, Duo e Familia
- Troca dinâmica de lista conforme o perfil selecionado
- Reinício para a base inicial quando necessário

#### 3. Cadastro e edição de produtos
- Adição de produtos com nome, quantidade, preço e categoria
- Validação de quantidade e preço
- Edição de quantidade do item selecionado
- Edição do preço unitário do item selecionado
- Remoção de item ou remoção por quantidade
- Atualização da tabela em tempo real

#### 4. Organização por categoria de produto
- Tipos disponíveis: Frutas, Frios, Fresco, Legumes, Processados, Limpeza e Bebida
- Cálculo do subtotal por item
- Soma do total da categoria

#### 5. Lógica de compra e confirmação
- Cálculo total da compra
- Validação antes da confirmação do pedido
- Janela de pagamento
- Opções de pagamento: Dinheiro, Cartão de crédito, Cartão de débito e Pix
- Parcelamento para cartão de crédito de 1 a 12 vezes
- Tela final de confirmação do pedido

#### 6. Persistência local
- Armazenamento em JSON
- Base de dados local para uso contínuo
- Reinicialização automática para estado padrão ao abrir o app

#### 7. Documentação e apresentação
- README concluído para apresentação no GitHub
- ROADMAP documentando evolução
- MEMORY para preservação do contexto do projeto

---

## Funcionalidades implementadas na versão atual

1. Usuário seleciona o perfil ativo.
2. A aplicação carrega a base padrão dos produtos.
3. O usuário inclui itens na lista.
4. O sistema calcula o subtotal e o total da categoria.
5. O usuário pode alterar ou remover itens.
6. O pedido é confirmado.
7. A forma de pagamento é definida.
8. Se for cartão de crédito, o número de parcelas é escolhido.
9. A confirmação final é exibida.
10. Ao fechar o sistema, o estado volta para a base inicial.

---

## Arquitetura atual

```text
shopping-list/
├── shopping_list_app.py          # Aplicação principal e lógica do sistema
├── listas_personalizadas.json    # Persistência local dos dados
├── README.md                     # Documentação pública do projeto
├── ROADMAP.md                    # Registro de evolução e planejamento
├── MEMORY.md                     # Memória técnica do desenvolvimento
├── .gitignore                    # Arquivos ignorados pelo Git
├── .venv/                        # Ambiente virtual local
├── ia/
│   └── Prompt Python.md
└── __pycache__/
```

---

## Melhorias planejadas

### Prioridade alta
- Refinar a identidade visual da marca EAD Listy
- Adicionar logo ou ícone do sistema
- Melhorar a experiência de uso com tela inicial mais profissional
- Aumentar validações de entrada e feedback visual
- Melhorar mensagens de erro e atenção do usuário

### Prioridade média
- Adicionar filtro por categoria
- Permitir busca por nome de produto
- Ordenação mais inteligente da lista
- Exportação da lista para PDF ou TXT
- Histórico de compras realizadas

### Prioridade baixa
- Modo administrativo para gestão de produtos padrão
- Versionamento de listas personalizadas
- Integração com banco de dados
- Cadastro de usuários ou autenticação simples
- Gestão de estoque e reposição automática

---

## Fases sugeridas de evolução

### Fase 1 - Polimento visual e UX
- ajustes visuais
- identidade visual da marca
- melhoria de organização da interface
- refinamento de botões e mensagens

### Fase 2 - Funcionalidades avançadas
- filtro e busca
- histórico de compra
- categorias personalizadas
- gestão de estoque

### Fase 3 - Evolução profissional
- modularização do código
- testes automatizados
- persistência mais robusta
- migração para arquitetura web ou híbrida

---

## Observações finais

O projeto já alcançou uma versão funcional completa para o uso de lista de compras por perfil. Ele inclui lógica de negócio, cálculo financeiro, confirmação de pedido e fluxo de pagamento. A partir deste ponto, o foco principal pode ser em refinamento de UX, organização estrutural e expansão das funcionalidades para uma versão mais robusta e profissional.

---

## Histórico resumido

- Criação da interface principal em Tkinter
- Implementação dos perfis Solo, Duo e Familia
- Desenvolvimento do cadastro e edição de itens
- Ajuste de cálculo de subtotal e total
- Implementação de pagamento e parcelamento
- Inclusão do tipo Bebida
- Criação de documentação e memória de contexto
- Preparação do projeto para evolução e apresentação
