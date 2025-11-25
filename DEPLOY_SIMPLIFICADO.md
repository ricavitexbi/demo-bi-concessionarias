# 🎯 DEPLOY SIMPLIFICADO - Para Iniciantes

## 📋 O Que Você Vai Fazer

Vamos colocar sua demo na internet em 3 passos simples:

1. **GitHub** - Guardar o código online
2. **Streamlit Cloud** - Hospedar a demo
3. **Compartilhar** - Mandar o link para clientes

**Tempo total:** 15-20 minutos  
**Custo:** R$ 0,00 (tudo gratuito!)

---

## 🚀 OPÇÃO 1: Modo Automático (Recomendado!)

### Use o script que já preparamos para você:

```bash
cd /mnt/user-data/outputs
./setup_deploy.sh
```

O script vai:
- ✅ Configurar o Git
- ✅ Conectar com GitHub
- ✅ Enviar o código
- ✅ Te guiar no deploy

**É só seguir as perguntas na tela!**

---

## 🎓 OPÇÃO 2: Modo Manual (Passo a Passo)

### Passo 1: Criar Conta no GitHub

1. Acesse: https://github.com/
2. Clique em "Sign up"
3. Preencha:
   - Username (exemplo: seunome)
   - Email
   - Senha
4. Verifique seu email
5. ✅ Pronto!

### Passo 2: Criar Repositório

1. Faça login no GitHub
2. Clique no "+" no canto superior direito
3. Selecione "New repository"
4. Preencha:
   ```
   Nome: demo-bi-concessionarias
   Descrição: Demo Sistema BI para Concessionárias
   Visibilidade: Public (ou Private se preferir)
   ```
5. **NÃO** marque "Add a README file"
6. Clique em "Create repository"
7. ✅ Repositório criado!

### Passo 3: Configurar Git Local

Abra o terminal e execute:

```bash
# Ir para o diretório
cd /mnt/user-data/outputs

# Configurar Git (primeira vez)
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"

# Inicializar repositório
git init

# Adicionar arquivos
git add .

# Fazer commit
git commit -m "Initial commit: Demo BI Concessionárias"
```

### Passo 4: Conectar com GitHub

```bash
# Substituir SEU_USUARIO pelo seu usuário do GitHub
git remote add origin https://github.com/SEU_USUARIO/demo-bi-concessionarias.git

# Enviar código
git branch -M main
git push -u origin main
```

**Atenção:** Na primeira vez, vai pedir usuário e senha:
- Usuário: seu_usuario_github
- Senha: Use um **Personal Access Token** (não sua senha normal)

#### Como criar Personal Access Token:

1. GitHub → Clique na sua foto (canto superior direito)
2. Settings → Developer Settings
3. Personal Access Tokens → Tokens (classic)
4. Generate new token (classic)
5. Marque: `repo` (full control of private repositories)
6. Generate token
7. **COPIE O TOKEN** (você não verá ele novamente!)
8. Use esse token como senha ao fazer push

### Passo 5: Deploy no Streamlit Cloud

1. Acesse: https://share.streamlit.io/
2. Clique em "Sign up" (ou "Log in" se já tem conta)
3. Escolha "Continue with GitHub"
4. Autorize o Streamlit Cloud
5. Clique em "New app"
6. Preencha:
   ```
   Repository: SEU_USUARIO/demo-bi-concessionarias
   Branch: main
   Main file path: demo_concessionaria.py
   ```
7. Clique em "Deploy!"
8. Aguarde 2-5 minutos ⏳

### Passo 6: Sua Demo Está Online! 🎉

Você receberá uma URL tipo:
```
https://seu-usuario-demo-bi-concessionarias-xyz.streamlit.app
```

**Compartilhe essa URL com seus clientes!**

---

## 🎨 Diagrama Visual do Processo

```
📁 Seu Computador                 ☁️ GitHub                    ☁️ Streamlit Cloud
  (Código local)              (Armazena código)            (Roda a aplicação)
       │                              │                            │
       │  git push                    │  Conecta automaticamente   │
       └──────────────────────────────┘                            │
                                      │                            │
                                      └────────────────────────────┘
                                                                   │
                                                                   │
                                                                   ▼
                                                           🌐 URL Pública
                                                     (Qualquer pessoa acessa)
```

---

## 💡 Dicas Importantes

### ✅ Fazer Atualizações

Sempre que mudar o código:

```bash
cd /mnt/user-data/outputs
git add .
git commit -m "Descrição da mudança"
git push
```

O Streamlit Cloud detecta automaticamente e atualiza!

### ✅ Ver Logs de Deploy

No Streamlit Cloud:
- Clique na sua app
- Veja os logs em tempo real
- Se der erro, os logs mostram o problema

### ✅ Gerenciar Apps

No Streamlit Cloud você pode:
- Pausar/Reativar apps
- Ver estatísticas de uso
- Configurar domínio personalizado (plano pago)

---

## ❓ Perguntas Frequentes

### "Git não está instalado"

**Solução:**
- Windows: https://git-scm.com/download/win
- Mac: `brew install git`
- Linux: `sudo apt-get install git`

### "Permission denied ao fazer push"

**Solução:**
- Use Personal Access Token como senha
- Não use sua senha normal do GitHub

### "ModuleNotFoundError no Streamlit Cloud"

**Solução:**
- Verifique se a biblioteca está em `requirements.txt`
- Push as alterações

### "File not found: dados_concessionaria.xlsx"

**Solução:**
```bash
cp /mnt/project/dados_concessionaria.xlsx /mnt/user-data/outputs/
git add dados_concessionaria.xlsx
git commit -m "Adicionar arquivo de dados"
git push
```

### "Como mudar a URL?"

**Solução:**
- Streamlit Cloud → Settings → App URL
- Você pode personalizar o slug

---

## 🎯 Checklist Rápido

Marque conforme for completando:

**Preparação:**
- [ ] Conta criada no GitHub
- [ ] Git instalado no computador
- [ ] Terminal aberto no diretório correto

**GitHub:**
- [ ] Repositório criado
- [ ] Git configurado localmente
- [ ] Código enviado (push)

**Streamlit Cloud:**
- [ ] Conta criada/conectada
- [ ] App criada e configurada
- [ ] Deploy concluído com sucesso
- [ ] URL funcionando

**Finalização:**
- [ ] Testei a URL
- [ ] Compartilhei com alguém
- [ ] Salvei a URL para referência

---

## 🎉 Pronto!

Agora você tem:
- ✅ Código no GitHub
- ✅ Demo online no Streamlit Cloud
- ✅ URL para compartilhar

**Próximos passos:**
1. Teste a URL em diferentes dispositivos
2. Compartilhe com clientes
3. Colete feedback
4. Faça ajustes e push novamente

---

## 📚 Recursos Adicionais

### Tutoriais em Vídeo:
- Git para iniciantes: https://www.youtube.com/watch?v=2alg7MQ6_sI
- GitHub basics: https://docs.github.com/pt/get-started

### Documentação:
- [GUIA_DEPLOY_STREAMLIT_CLOUD.md](GUIA_DEPLOY_STREAMLIT_CLOUD.md) - Guia completo
- [README.md](README.md) - Documentação do projeto

### Suporte:
- Streamlit Community: https://discuss.streamlit.io/
- GitHub Docs: https://docs.github.com/pt

---

## 💪 Você Consegue!

Parece complicado mas é mais simples do que parece. Milhões de pessoas fazem isso todo dia!

**Dica:** Use o script automático `setup_deploy.sh` - ele facilita muito!

```bash
cd /mnt/user-data/outputs
./setup_deploy.sh
```

Boa sorte! 🚀

---

*Criado para iniciantes com ❤️*
