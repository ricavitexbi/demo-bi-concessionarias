# 🍕 GIT EXPLICADO COM PIZZA (Sim, Pizza!)

## 🤔 Por Que Pizza?

Porque todo mundo entende pizza! Vou explicar Git usando coisas que você já conhece.

---

## 📖 Capítulo 1: O Que É Git? (Usando Caderno)

### Imagine um caderno de receitas:

**Caderno Normal:**
- Você escreve uma receita
- Se errar, tem que apagar ou riscar
- Não dá pra voltar atrás facilmente
- Se perder o caderno, perdeu tudo

**Caderno MÁGICO (Git):**
- Você escreve uma receita
- Pode tirar "fotos" de cada versão
- Se errar, volta para a foto anterior
- Tem cópia automática na nuvem
- Várias pessoas podem colaborar

**Git = Caderno Mágico para Código**

---

## 🏠 Capítulo 2: O Que É "cd"? (Entrar em Casa)

### Seu computador é como um prédio:

```
🏢 Prédio (Computador)
│
├─ 🚪 Apartamento 101 (Pasta Documentos)
├─ 🚪 Apartamento 102 (Pasta Downloads)
└─ 🚪 Apartamento 103 (Pasta outputs) ← Queremos entrar aqui!
```

**"cd" = Change Door (Mudar de Porta)**

Quando você digita:
```bash
cd /mnt/user-data/outputs
```

É como dizer: "Quero entrar no apartamento 103"

---

### Como Saber Se Entrou?

Digite:
```bash
pwd
```

**pwd = "Onde eu estou agora?"**

É como perguntar: "Em qual apartamento eu estou?"

---

## 👤 Capítulo 3: Configurar Nome e Email (Assinar Documento)

### Sabe quando você assina um documento?

Você coloca:
- ✍️ Seu nome
- 📧 Seu email ou telefone

**É exatamente isso que esses comandos fazem:**

```bash
git config --global user.name "João Silva"
```
↑ Isso é como escrever seu nome numa etiqueta

```bash
git config --global user.email "joao@email.com"
```
↑ Isso é como escrever seu email numa etiqueta

**Por quê?** Para o Git saber quem fez cada mudança!

---

## 📸 Capítulo 4: Os Comandos Explicados com Fotos

### Imagine que você está organizando fotos de família:

**1. git init (Criar álbum)**
```bash
git init
```
= "Vou criar um álbum de fotos novo!"

Cria a estrutura para guardar as "fotos" do seu código.

---

**2. git add . (Selecionar fotos)**
```bash
git add .
```
= "Vou selecionar TODAS as fotos para colocar no álbum"

O ponto (.) significa "todas as fotos" (todos os arquivos).

---

**3. git commit (Colar no álbum)**
```bash
git commit -m "Minhas primeiras fotos"
```
= "Vou colar as fotos no álbum com a legenda: 'Minhas primeiras fotos'"

A parte entre aspas é a legenda/descrição.

---

**4. git push (Enviar para nuvem)**
```bash
git push
```
= "Vou fazer backup do álbum no Google Fotos"

Envia tudo para o GitHub (nuvem).

---

## 🍕 Capítulo 5: Git Explicado com Pizzaria

### Você vai abrir uma pizzaria e quer anotar as receitas:

**Situação 1: Sem Git (Caderno Normal)**
```
Segunda: Escrevo receita de pizza margherita
Terça: Apago tudo e escrevo receita de calabresa
Quarta: Quero voltar pra margherita... 😰 NÃO DÁ!
```

**Situação 2: Com Git (Caderno Mágico)**
```
Segunda: Escrevo margherita → git commit "Margherita pronta"
Terça: Escrevo calabresa → git commit "Calabresa pronta"
Quarta: Quero voltar pra margherita? → git checkout [volta]
```

**Viu a diferença?** Com Git você pode:
- Guardar todas as versões
- Voltar pra qualquer versão
- Comparar o que mudou
- Trabalhar em equipe sem conflito

---

## 🎯 Capítulo 6: Passo a Passo COM ANALOGIAS

### Passo 1: Abrir o Terminal

**Analogia:** É como abrir o bloco de notas, mas para dar comandos.

**Como fazer:**
- Windows: Tecla Windows → digite `cmd` → Enter
- Mac: Command + Espaço → digite `terminal` → Enter

---

### Passo 2: Ir Para a Pasta (cd)

**Analogia:** Você está na sala, precisa ir pro quarto.

**Digite:**
```bash
cd /mnt/user-data/outputs
```

**Tradução:** "Vá para a pasta onde estão os arquivos da demo"

---

### Passo 3: Confirmar Que Está no Lugar Certo (ls)

**Analogia:** Olhar ao redor pra ver se está no lugar certo.

**Digite:**
```bash
ls
```

**Tradução:** "Mostre o que tem nesta pasta"

**Deve aparecer:** demo_concessionaria.py, dados_concessionaria.xlsx, etc.

---

### Passo 4: Criar "Álbum de Fotos" (git init)

**Analogia:** Pegar um álbum vazio e colocar o título.

**Digite:**
```bash
git init
```

**Tradução:** "Crie um sistema de controle de versão aqui"

**Vai aparecer:** "Initialized empty Git repository..."

---

### Passo 5: Colocar Seu Nome (git config)

**Analogia:** Escrever seu nome na capa do álbum.

**Digite (COM SEU NOME REAL):**
```bash
git config --global user.name "Maria Santos"
```

**Digite (COM SEU EMAIL REAL):**
```bash
git config --global user.email "maria@email.com"
```

---

### Passo 6: Selecionar Todos os Arquivos (git add)

**Analogia:** Selecionar todas as fotos pra colocar no álbum.

**Digite:**
```bash
git add .
```

**IMPORTANTE:** O ponto (.) no final significa "TUDO"

---

### Passo 7: "Tirar a Foto" (git commit)

**Analogia:** Bater a foto do momento atual.

**Digite:**
```bash
git commit -m "Minha primeira versão da demo"
```

**A frase entre aspas** é uma legenda. Pode mudar se quiser!

---

## 🌐 Capítulo 7: Enviar Para o GitHub

### Analogia: Google Drive/Dropbox

O GitHub é tipo Google Drive, mas para código!

---

### Passo 1: Criar Conta no GitHub

**Como fazer:**

1. Vá em: https://github.com
2. Clique: "Sign up"
3. Preencha:
   - Nome de usuário (sem espaços)
   - Email
   - Senha
4. Clique: "Create account"
5. Verifique seu email

**É grátis!** ✅

---

### Passo 2: Criar "Pasta na Nuvem" (Repositório)

**Analogia:** Criar uma pasta nova no Google Drive.

1. No GitHub, clique no **"+"** (canto superior direito)
2. Clique: "New repository"
3. Nome: `demo-bi-concessionarias`
4. Deixe público (ou privado se preferir)
5. **NÃO MARQUE** nenhuma caixinha
6. Clique: "Create repository"

---

### Passo 3: Conectar Seu Computador com a Nuvem

**Analogia:** Configurar o Google Drive no seu PC.

**Copie a URL** que aparece na tela (algo tipo):
```
https://github.com/seu-usuario/demo-bi-concessionarias.git
```

**No terminal, digite (substitua pela SUA URL):**
```bash
git remote add origin https://github.com/seu-usuario/demo-bi-concessionarias.git
```

**Tradução:** "Conecte com minha pasta na nuvem"

---

### Passo 4: Fazer Upload (git push)

**Analogia:** Enviar arquivos pro Google Drive.

**Digite:**
```bash
git branch -M main
```

**Depois:**
```bash
git push -u origin main
```

**Vai pedir:**
- Username: seu-usuario-github
- Password: **USE UM TOKEN!** (não sua senha)

---

## 🔑 O QUE É TOKEN?

### Analogia: Senha de App

Sabe quando você usa Gmail em outro app e ele pede uma "senha de app"?  
Token é a mesma coisa!

É uma senha especial só pra aplicações.

---

### Como Criar Token:

1. GitHub → Sua foto → Settings
2. Developer settings (fim da página)
3. Personal access tokens → Tokens (classic)
4. Generate new token (classic)
5. Descrição: "Token da demo"
6. Validade: 90 dias
7. Marque: **repo** ✅
8. Generate token
9. **COPIE!** Você não verá ele novamente!

Parece: `ghp_xxxxxxxxxxxx`

---

### Como Usar:

Quando pedir senha, **cole o token** (Ctrl+V)

**NÃO VAI APARECER NA TELA!** É normal por segurança.

---

## ✅ LISTA DE COMPRAS (Checklist)

Marque conforme for fazendo:

### Preparação:
- [ ] Terminal aberto
- [ ] Git instalado (teste: `git --version`)
- [ ] Sei em qual pasta estou

### Git Local:
- [ ] `cd /mnt/user-data/outputs`
- [ ] `git init`
- [ ] `git config` (nome e email)
- [ ] `git add .`
- [ ] `git commit -m "..."`

### GitHub:
- [ ] Conta criada
- [ ] Repositório criado
- [ ] Token criado e copiado
- [ ] `git remote add origin ...`
- [ ] `git push`

### Pronto!
- [ ] Código no GitHub ✅
- [ ] Pronto pro Streamlit Cloud ✅

---

## 🎓 VOCÊ APRENDEU!

Hoje você aprendeu:
- ✅ O que é terminal (bloco de notas de comandos)
- ✅ O que é Git (caderno mágico)
- ✅ O que é GitHub (Google Drive pra código)
- ✅ Como fazer commit (tirar foto)
- ✅ Como fazer push (enviar pra nuvem)
- ✅ O que é token (senha de app)

**Isso é MUITO!** Parabéns! 🎉

---

## 🆘 ERROS COMUNS

### "git: command not found"
**Solução:** Instale o Git
- Windows: https://git-scm.com/download/win
- Mac: https://git-scm.com/download/mac
- Linux: `sudo apt-get install git`

---

### "Permission denied"
**Solução:** Use token, não senha normal!

---

### "Already exists"
**Solução:** Já foi feito! Está tudo certo!

---

### "Not a git repository"
**Solução:** Você não está na pasta certa. Use `cd` para ir lá.

---

## 🎯 PRÓXIMO PASSO

Seu código está no GitHub! 🎊

Agora vamos pro **Streamlit Cloud**:

1. https://share.streamlit.io/
2. Login com GitHub
3. New app
4. Selecione seu repositório
5. Deploy!

**Sua demo estará online em 5 minutos!**

---

## 💭 ANALOGIA FINAL

```
GIT = Máquina do Tempo
GITHUB = Netflix das versões
STREAMLIT CLOUD = TV que mostra pro mundo

Você criou → Salvou → Enviou pro mundo! 🚀
```

---

Espero que tenha ficado mais claro! 😊

Qualquer dúvida, pergunte! Estou aqui pra ajudar! 💪

---

*Criado com ❤️ (e muita pizza 🍕) para quem está começando!*
