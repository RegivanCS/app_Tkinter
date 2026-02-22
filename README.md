# 📝 Editor de Notas

Um editor de texto simples e prático desenvolvido em Python com Tkinter.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Funcionalidades

- ✨ **Interface moderna** com barra de ferramentas e ícones
- 📄 **Criar novo arquivo** (Ctrl+N)
- 📁 **Abrir arquivos** de texto (Ctrl+O)
- 💾 **Salvar arquivos** (Ctrl+S)
- 💾 **Salvar Como** para criar cópias
- ↩️ **Desfazer/Refazer** alterações (Ctrl+Z / Ctrl+Y)
- 🔍 **Selecionar tudo** (Ctrl+A)
- 📊 **Barra de status** com contador de linhas e caracteres
- ⚠️ **Controle de modificações** - indica documentos não salvos com asterisco (*)
- 🔔 **Avisos inteligentes** - pergunta se deseja salvar antes de fechar/abrir
- 🎯 **Janela centralizada** automaticamente

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Tkinter (geralmente incluído na instalação padrão do Python)

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/editor-de-notas.git
cd editor-de-notas
```

2. Verifique se o Tkinter está instalado:
```bash
python -m tkinter
```

Se uma janela aparecer, o Tkinter está instalado corretamente!

## 💻 Como Usar

Execute o script principal:

```bash
python notes.py
```

### Atalhos de Teclado

| Atalho | Função |
|--------|--------|
| `Ctrl+N` | Novo arquivo |
| `Ctrl+O` | Abrir arquivo |
| `Ctrl+S` | Salvar arquivo |
| `Ctrl+Q` | Sair do editor |
| `Ctrl+Z` | Desfazer |
| `Ctrl+Y` | Refazer |
| `Ctrl+A` | Selecionar tudo |

## 📸 Screenshots

### Interface Principal
- Barra de ferramentas com botões visuais
- Área de texto com fonte legível
- Barra de status informativa

### Menus Disponíveis
- **Arquivo**: Novo, Abrir, Salvar, Salvar Como, Sair
- **Editar**: Desfazer, Refazer, Selecionar tudo
- **Ajuda**: Sobre

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem de programação
- **Tkinter** - Biblioteca para interface gráfica
- **filedialog** - Diálogos de arquivo
- **messagebox** - Caixas de mensagem

## 📝 Estrutura do Projeto

```
app_Tkinter/
│
├── notes.py          # Arquivo principal do editor
├── README.md         # Documentação
├── .gitignore        # Arquivos ignorados pelo Git
└── requirements.txt  # Dependências (opcional)
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**Seu Nome**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Portfolio: [Meu Portfolio](https://seu-portfolio.com)

## 🎯 Melhorias Futuras

- [ ] Suporte para múltiplas abas
- [ ] Buscar e substituir texto
- [ ] Temas personalizáveis (escuro/claro)
- [ ] Numeração de linhas
- [ ] Destacar sintaxe para código
- [ ] Exportar para PDF
- [ ] Configurações personalizáveis

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões, por favor abra uma [issue](https://github.com/seu-usuario/editor-de-notas/issues).

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
