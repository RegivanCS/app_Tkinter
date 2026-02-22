# 🚀 Guia para Subir o Projeto no GitHub

## Arquivos Criados ✅

- ✅ `.gitignore` - Ignora arquivos desnecessários (cache, venv, etc)
- ✅ `README.md` - Documentação completa do projeto
- ✅ `LICENSE` - Licença MIT
- ✅ `requirements.txt` - Dependências do projeto
- ✅ `notes.py` - Código principal do editor

## 📝 Instruções de Commit e Push

### 1. Fazer o Commit Inicial

```bash
git commit -m "feat: Adiciona Editor de Notas completo com interface Tkinter

- Interface moderna com barra de ferramentas
- Menu completo com atalhos de teclado
- Controle de modificações e avisos de salvamento
- Barra de status com informações em tempo real
- Suporte a desfazer/refazer
- Documentação completa"
```

### 2. Criar Repositório no GitHub

1. Acesse https://github.com/new
2. Nome do repositório: `editor-de-notas` (ou outro nome de sua escolha)
3. Descrição: `Editor de texto simples e prático desenvolvido em Python com Tkinter`
4. **NÃO** inicialize com README (já temos um)
5. Clique em "Create repository"

### 3. Conectar ao Repositório Remoto

Após criar o repositório no GitHub, execute:

```bash
# Substitua SEU-USUARIO pelo seu nome de usuário do GitHub
git remote add origin https://github.com/SEU-USUARIO/editor-de-notas.git

# Ou se preferir SSH:
git remote add origin git@github.com:SEU-USUARIO/editor-de-notas.git
```

### 4. Fazer o Push

```bash
# Push do primeiro commit
git push -u origin main

# Ou se a branch for master:
git push -u origin master
```

## 🔄 Comandos Git para Uso Futuro

### Verificar Status
```bash
git status
```

### Adicionar Mudanças
```bash
# Adicionar arquivo específico
git add notes.py

# Adicionar todos os arquivos modificados
git add .
```

### Fazer Commit
```bash
git commit -m "Sua mensagem descritiva"
```

### Enviar para o GitHub
```bash
git push
```

### Atualizar do GitHub
```bash
git pull
```

## 📌 Boas Práticas de Commit

Use mensagens claras e descritivas:

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `style:` - Formatação, ponto e vírgula, etc
- `refactor:` - Refatoração de código
- `test:` - Adição de testes
- `chore:` - Tarefas de manutenção

### Exemplos:
```bash
git commit -m "feat: Adiciona função de buscar e substituir"
git commit -m "fix: Corrige erro ao salvar arquivo vazio"
git commit -m "docs: Atualiza README com novos atalhos"
git commit -m "style: Melhora formatação do código"
```

## 🎯 Próximos Passos

1. ✅ Arquivos já estão no staging (`git add` executado)
2. ⏳ Fazer commit inicial (comando acima)
3. ⏳ Criar repositório no GitHub
4. ⏳ Conectar ao repositório remoto
5. ⏳ Fazer push

## 💡 Dicas

- Lembre-se de atualizar o **README.md** com:
  - Seu nome de usuário do GitHub
  - Link do seu portfolio
  - Screenshots da aplicação (opcional)

- Considere adicionar:
  - Badge de status do projeto
  - Seção de contribuidores
  - Link para demo (se disponível)

---

✨ Seu projeto está pronto para o mundo! Boa sorte! 🚀
