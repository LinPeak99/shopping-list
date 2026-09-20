# ROADMAP - EAD Listy

## Visão geral

O EAD Listy é uma aplicação desktop desenvolvida em Python com interface gráfica em Tkinter para organizar listas de compras por perfil, com controle de quantidade, preço, tipo de alimento e confirmação do pedido.

Este documento registra o desenvolvimento concluído até o momento e serve como base para futuras melhorias e entregas.

---

## Status atual

### ✅ Concluído

#### 1. Estrutura inicial da aplicação
- Criação da interface principal com Tkinter
- Organização da tela em seções e blocos lógicos
- Configuração de estilos visuais para melhor experiência do usuário

#### 2. Gestão de perfis
- Suporte aos perfis:
  - Solo
  - Duo
  - Familia
- Seleção de perfil com atualização da lista correspondente
- Reset do sistema para a base padrão quando necessário

#### 3. Cadastro e edição de produtos
- Adição de itens com:
  - nome
  - quantidade
  - preço unitário
  - tipo do alimento
- Edição de quantidade do produto
- Edição de preço unitário
- Remoção de itens da lista
- Ajuste de produtos com atualização em tempo real

#### 4. Organização por categoria
- Controle de produtos por tipo de alimento
- Inclusão do tipo de categoria "Bebida"
- Exibição de subtotal por categoria
- Total da compra calculado automaticamente

#### 5. Lógica de negócio da compra
- Cálculo de subtotal e total geral
- Validação de valores e quantidade
- Exibição de informações em tempo real
- Confirmação final do pedido

#### 6. Sistema de pagamento
- Opções de pagamento
- Suporte a cartão de crédito
- Escolha de parcelas de 1 a 12 vezes
- Tela de confirmação do pedido final

#### 7. Persistência local
- Armazenamento em arquivo JSON
- Reuso de dados entre execuções
- Sistema com base inicial para reinicialização do uso

#### 8. Documentação do projeto
- Criação do README principal para apresentação
- Organização das instruções de execução
- Preparo para apresentação em repositório GitHub

---

## Funcionalidades implementadas no fluxo atual

1. Usuário escolhe o perfil.
2. A aplicação carrega os produtos padrão ou os dados já existentes.
3. O usuário pode adicionar ou editar itens.
4. A lista atualiza automaticamente com subtotal e total.
5. O usuário confirma o pedido.
6. O sistema solicita a forma de pagamento.
7. Caso seja cartão, o usuário escolhe o número de parcelas.
8. O pedido é finalizado e o app retorna ao início ou oferece nova execução.

---

## Arquitetura e estrutura atual

```text
shopping-list/
├── shopping_list_app.py      # Aplicação principal
├── listas_personalizadas.json # Persistência local dos dados
├── README.md                 # Documentação inicial do projeto
├── ROADMAP.md                # Plano de desenvolvimento e evolução
├── .gitignore                # Arquivos ignorados pelo Git
└── .venv/                    # Ambiente virtual local
```

---

## Melhorias planejadas para futuras versões

### Prioridade alta
- Melhorar a interface visual com identidade visual da marca EAD Listy
- Adicionar ícone ou logotipo do sistema
- Criar tela de apresentação inicial com nome do produto e slogan
- Implementar validações mais robustas de entrada de dados
- Melhorar mensagens de erro e feedback visual

### Prioridade média
- Adicionar filtro por categoria
- Permitir pesquisa de produtos por nome
- Ordenação manual ou automática da lista
- Exportação da lista para PDF ou TXT
- Histórico de pedidos realizados

### Prioridade baixa
- Versionamento de listas personalizadas
- Modo administrativo para gerenciar produtos base
- Cadastro de usuários ou autenticação simples
- Exportação/importação de dados em outros formatos
- Reposição automática de estoque

---

## Evolução sugerida

### Fase 1 - Polimento da aplicação
- Ajustes visuais
- Melhor organização da tela
- Iconografia e branding
- Melhor UX para inserção e remoção

### Fase 2 - Funcionalidades avançadas
- Persistência mais sofisticada
- Histórico de compras
- Categorias personalizadas
- Gestão de estoque

### Fase 3 - Escala e profissionalização
- Estrutura modular em arquivos
- Testes automatizados
- Possível migração para web ou versão híbrida
- Integração com banco de dados

---

## Observações finais

O projeto já está funcional e com lógica de negócio completa para o uso de lista de compras por perfil, incluindo categoria, valores, pagamento e confirmação de pedido. A partir daqui, o foco principal pode ser em refinamento visual, organização do código e expansão de funcionalidades para uma versão mais robusta e profissional.

---

## Histórico resumido

- Criação da aplicação principal em Python/Tkinter
- Implementação de perfis e listas personalizadas
- Desenvolvimento de cálculo de totais e subtotais
- Suporte a pagamento e parcelamento
- Inclusão do tipo "Bebida"
- Documentação inicial em README
- Criação deste ROADMAP para acompanhamento do projeto
