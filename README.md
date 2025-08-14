# 🍽️ Sabor Express

## Descrição
Sabor Express é uma aplicação de linha de comando desenvolvida em Python para gerenciamento de restaurantes. Este foi meu primeiro projeto em Python, desenvolvido durante o curso da Alura, onde aprendi os conceitos fundamentais da linguagem.

## ✨ Funcionalidades

- **Cadastrar restaurante**: Adicione novos restaurantes com nome e categoria
- **Listar restaurantes**: Visualize todos os restaurantes cadastrados com suas informações
- **Alternar estado**: Ative ou desative restaurantes conforme necessário
- **Interface amigável**: Menu interativo com navegação simples

## 🚀 Como executar

### Pré-requisitos
- Python 3.x instalado no sistema

### Executando o projeto
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/sabor-express.git
```

2. Navegue até o diretório do projeto:
```bash
cd sabor-express
```

3. Execute a aplicação:
```bash
python sabor_express.py
```

## 📋 Como usar

1. **Ao iniciar**, você verá o menu principal com 4 opções
2. **Digite o número** da opção desejada e pressione Enter
3. **Siga as instruções** na tela para cada funcionalidade

### Menu de opções:
- `1` - Cadastrar um novo restaurante
- `2` - Listar todos os restaurantes
- `3` - Alternar estado (ativar/desativar) de um restaurante
- `4` - Sair da aplicação

## 🛠️ Tecnologias utilizadas

- **Python 3.x**
- Biblioteca `os` para limpeza de terminal

## 📊 Estrutura do projeto

```
sabor-express/
│
├── sabor_express.py    # Arquivo principal da aplicação
└── README.md          # Documentação do projeto
```

## 🎯 Funcionalidades detalhadas

### Cadastrar restaurante
- Solicita nome do restaurante
- Solicita categoria do restaurante
- Adiciona o restaurante com status "Desativado" por padrão

### Listar restaurantes
- Exibe uma tabela formatada com:
  - Nome do restaurante
  - Categoria
  - Status (Ativado/Desativado)

### Alternar estado
- Permite ativar ou desativar um restaurante pelo nome
- Confirma a alteração com mensagem de sucesso
- Informa se o restaurante não foi encontrado

## 🧪 Dados de exemplo

O projeto já vem com alguns restaurantes pré-cadastrados para demonstração:
- Praça (Japonesa) - Desativado
- Pizza Superma (Pizza) - Ativado  
- Cantina (Italiano) - Desativado

## 🔄 Possíveis melhorias futuras

- [ ] Persistência de dados em arquivo
- [ ] Validação mais robusta de inputs
- [ ] Busca de restaurantes por categoria
- [ ] Sistema de avaliações
- [ ] Interface gráfica

## 📚 Aprendizados

Este projeto me permitiu praticar:
- Estruturas de dados (listas e dicionários)
- Funções em Python
- Estruturas condicionais e loops
- Tratamento de exceções
- Manipulação de strings
- Organização de código

## 👨‍💻 Autor

Desenvolvido durante meus estudos na Alura - Primeiro projeto em Python!

---

⭐ Se este projeto te ajudou de alguma forma, considere dar uma estrela no repositório!
