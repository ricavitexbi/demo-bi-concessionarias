# 🎓 GIT E GITHUB PARA INICIANTES ABSOLUTOS

## 📌 O Que Vamos Fazer (Em Português Simples)

Imagine que você tem um documento no Word e quer:
1. Guardar ele na nuvem (tipo Google Drive)
2. Deixar outras pessoas verem
3. Controlar as versões (tipo histórico do Google Docs)

É ISSO que vamos fazer com seu código! 

**GitHub** = Google Drive para código  
**Git** = Ferramenta para enviar/baixar do GitHub

---

## 🖥️ PARTE 1: O Que É Terminal/Prompt?

### O terminal é tipo o "MS-DOS antigo"

É uma tela preta onde você digita comandos em vez de clicar.

**Como abrir:**

**Windows:**
1. Aperte a tecla Windows
2. Digite: `cmd` ou `PowerShell`
3. Aperte Enter
4. Vai abrir uma janela preta/azul

**Mac:**
1. Aperte Command + Espaço
2. Digite: `terminal`
3. Aperte Enter

**Linux:**
1. Aperte Ctrl + Alt + T

---

## 📂 PARTE 2: O Que É "cd" (Change Directory)?

### cd = Entrar numa pasta

Sabe quando você clica duas vezes numa pasta para abrir?  
`cd` faz a mesma coisa, mas digitando!

### Exemplo Visual:

```
Você está aqui:
📁 Computador
  └─ 📁 Usuários
      └─ 📁 Você
          └─ 📁 Desktop  ← VOCÊ ESTÁ AQUI

Quer ir para:
📁 Computador
  └─ 📁 mnt
      └─ 📁 user-data
          └─ 📁 outputs  ← QUER IR AQUI
```

### Como fazer:

**Digite no terminal:**
```bash
cd /mnt/user-data/outputs
```

**Aperte Enter**

Pronto! Agora você está "dentro" dessa pasta.

### Como saber se deu certo?

Digite:
```bash
pwd
```

Vai mostrar onde você está. Deve aparecer: `/mnt/user-data/outputs`

---

## 🔧 PARTE 3: Comandos Git Explicados (UM POR UM)

### 🎯 Comando 1: Configurar Seu Nome

```bash
git config --global user.name "Seu Nome"
```

**O que isso faz?**  
Diz pro Git quem você é. Tipo colocar seu nome numa etiqueta.

**Como fazer:**
1. Copie o comando acima
2. Cole no terminal
3. MUDE "Seu Nome" para seu nome real
4. Exemplo: `git config --global user.name "Ricardo Silva"`
5. Aperte Enter

**Você verá:** Nada! O terminal não diz nada quando dá certo. É normal.

---

### 🎯 Comando 2: Configurar Seu Email

```bash
git config --global user.email "seu-email@example.com"
```

**O que isso faz?**  
Diz pro Git seu email. Tipo assinar um documento.

**Como fazer:**
1. Copie o comando acima
2. Cole no terminal
3. MUDE para seu email real
4. Exemplo: `git config --global user.email "ricardo@gmail.com"`
5. Aperte Enter

**Você verá:** Nada novamente! É normal.

---

### 🎯 Comando 3: Inicializar Repositório

```bash
git init
```

**O que isso faz?**  
Cria uma "caixinha mágica" na pasta onde você está.  
Essa caixinha vai guardar o histórico de todas as mudanças.

**Analogia:**  
É como começar um novo documento no Word com "Controlar Alterações" ligado.

**Como fazer:**
1. Digite: `git init`
2. Aperte Enter

**Você verá:**
```
Initialized empty Git repository in /mnt/user-data/outputs/.git/
```

Isso é bom! Significa que deu certo! ✅

---

### 🎯 Comando 4: Adicionar Arquivos

```bash
git add .
```

**O que isso faz?**  
Prepara TODOS os arquivos da pasta para serem "guardados".

**Analogia:**  
É como selecionar arquivos para copiar. Você ainda não copiou, só selecionou.

**Como fazer:**
1. Digite: `git add .`
2. Aperte Enter

**ATENÇÃO:** O ponto (.) no final é importante! Significa "todos os arquivos".

**Você verá:** Nada, ou uma lista de arquivos. Ambos estão certos!

---

### 🎯 Comando 5: Fazer Commit

```bash
git commit -m "Initial commit: Demo BI Concessionárias"
```

**O que isso faz?**  
"Tira uma foto" de todos os arquivos neste momento.

**Analogia:**  
É como salvar o documento no Word. Você cria um ponto de restore.

**Como fazer:**
1. Copie o comando completo
2. Cole no terminal
3. Aperte Enter

**A parte entre aspas** é uma mensagem explicando o que você fez.  
Pode mudar se quiser, mas deixe entre aspas!

**Você verá:**
```
[main 1a2b3c4] Initial commit: Demo BI Concessionárias
 16 files changed, 2500 insertions(+)
 create mode 100644 demo_concessionaria.py
 create mode 100644 requirements.txt
 ...
```

Isso significa sucesso! ✅

---

## 🎬 RESUMO VISUAL DO QUE VOCÊ FEZ

```
ANTES:
📁 outputs/
  📄 demo.py
  📄 dados.xlsx
  (arquivos soltos)

DEPOIS DE: git init
📁 outputs/
  📄 demo.py
  📄 dados.xlsx
  🔮 .git/ (caixinha mágica criada)

DEPOIS DE: git add .
📁 outputs/
  📄 demo.py ✅ (marcado)
  📄 dados.xlsx ✅ (marcado)
  🔮 .git/ (esperando...)

DEPOIS DE: git commit
📁 outputs/
  📄 demo.py 📸 (fotografado)
  📄 dados.xlsx 📸 (fotografado)
  🔮 .git/ (histórico salvo!)
```

---

## 🎯 PASSO A PASSO COMPLETO (COPIE E COLE)

### 1️⃣ Abra o Terminal

**Windows:** Win + R, digite `cmd`, Enter  
**Mac:** Command + Espaço, digite `terminal`, Enter  
**Linux:** Ctrl + Alt + T

---

### 2️⃣ Vá para a Pasta da Demo

**Digite linha por linha, apertando Enter depois de cada:**

```bash
cd /mnt/user-data/outputs
```

**Para confirmar que está no lugar certo:**
```bash
ls
```

Deve aparecer: `demo_concessionaria.py`, `dados_concessionaria.xlsx`, etc.

---

### 3️⃣ Configure o Git (SÓ PRIMEIRA VEZ)

**Substitua "Seu Nome" e "seu@email.com" pelos seus dados reais:**

```bash
git config --global user.name "Ricardo Silva"
```

```bash
git config --global user.email "ricardo@gmail.com"
```

**Para verificar se salvou:**
```bash
git config --global user.name
git config --global user.email
```

Vai mostrar o que você digitou.

---

### 4️⃣ Inicialize o Git

```bash
git init
```

**Deve aparecer:**
```
Initialized empty Git repository...
```

---

### 5️⃣ Adicione os Arquivos

```bash
git add .
```

(Não esqueça o ponto no final!)

---

### 6️⃣ Faça o Commit

```bash
git commit -m "Minha primeira demo"
```

**Deve aparecer:**
```
[main ...] Minha primeira demo
 XX files changed...
```

---

## ✅ PRONTO! PARTE 1 CONCLUÍDA!

Agora você tem:
- ✅ Git configurado com seu nome e email
- ✅ Repositório criado na pasta
- ✅ Todos os arquivos "fotografados" (commit)

**Próximo passo:** Enviar isso para o GitHub!

---

## 🌐 PARTE 4: Enviar para o GitHub

### Antes de Continuar...

Você precisa:
1. Criar uma conta no GitHub (se ainda não tem)
2. Criar um repositório lá

**Vou explicar isso também! Continue lendo...**

---

## 🆕 Criar Conta no GitHub

### Passo a Passo:

1. **Abra o navegador**
2. **Acesse:** https://github.com/
3. **Clique em:** "Sign up" (no canto superior direito)
4. **Preencha:**
   - Username: `seu-nome-aqui` (sem espaços)
   - Email: seu email
   - Password: crie uma senha forte
5. **Resolva o puzzle** (para provar que não é robô)
6. **Clique em:** "Create account"
7. **Verifique seu email** (eles vão mandar um código)
8. **Digite o código** da verificação
9. **Pronto!** ✅

---

## 📦 Criar Repositório no GitHub

### Passo a Passo:

1. **Faça login** no GitHub
2. **Clique no "+"** (canto superior direito)
3. **Selecione:** "New repository"
4. **Preencha:**
   ```
   Repository name: demo-bi-concessionarias
   Description: Demo Sistema BI para Concessionárias
   Visibilidade: Public (ou Private se quiser)
   ```
5. **NÃO MARQUE** nenhuma caixinha (README, .gitignore, etc)
6. **Clique em:** "Create repository"

**Você vai ver uma página com instruções.**  
Não se preocupe com elas agora!

---

## 🔗 Conectar Seu Computador com o GitHub

### Copie a URL do Seu Repositório

Na página do repositório recém-criado, você vai ver uma URL tipo:
```
https://github.com/SEU-USUARIO/demo-bi-concessionarias.git
```

**COPIE ESSA URL!** Vamos usar ela agora.

---

### No Terminal, Digite:

**Substitua SEU-USUARIO pelo seu usuário real:**

```bash
git remote add origin https://github.com/SEU-USUARIO/demo-bi-concessionarias.git
```

**Exemplo real:**
```bash
git remote add origin https://github.com/ricardo-silva/demo-bi-concessionarias.git
```

**Aperte Enter**

**Você verá:** Nada! É normal quando dá certo.

---

### Enviar o Código

```bash
git branch -M main
```

```bash
git push -u origin main
```

**Aqui ele vai pedir:**
- Username: `seu-usuario-github`
- Password: **NÃO use sua senha normal!** Use um "token"

---

## 🔑 IMPORTANTE: Personal Access Token

### Por Que Não Posso Usar Minha Senha?

O GitHub não aceita mais senha normal por segurança.  
Você precisa criar um "token" (senha especial).

### Como Criar o Token:

1. **No GitHub, clique** na sua foto (canto superior direito)
2. **Settings** (Configurações)
3. **Developer settings** (lá embaixo)
4. **Personal access tokens**
5. **Tokens (classic)**
6. **Generate new token (classic)**
7. **Note:** Digite "Token para demo"
8. **Expiration:** 90 days
9. **Marque a caixinha:** `repo` (acesso completo)
10. **Clique:** Generate token
11. **COPIE O TOKEN!** (você não verá ele novamente)

Parece: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

### Use o Token Como Senha

Quando o terminal pedir:
```
Username: seu-usuario
Password: [cole o token aqui]
```

**Cole o token** (Ctrl+V) e aperte Enter.

**Nota:** O terminal não mostra o que você está colando. É normal!

---

## 🎉 SUCESSO!

Se deu tudo certo, você vai ver:
```
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
...
To https://github.com/seu-usuario/demo-bi-concessionarias.git
 * [new branch]      main -> main
```

**PARABÉNS!** Seu código está no GitHub! 🎊

---

## 📊 RESUMO VISUAL COMPLETO

```
SEU COMPUTADOR          GITHUB              STREAMLIT CLOUD
    📂                    ☁️                      🌐
    
1. git init          2. git push         3. Deploy
   ↓                    ↓                    ↓
   
📄 Arquivos        📦 Repositório      🚀 Demo Online
    locais           online              pública
```

---

## 🔄 Para Atualizar Depois

Se você mudar alguma coisa, faça:

```bash
git add .
git commit -m "Descreva o que mudou"
git push
```

É só isso! O Streamlit Cloud atualiza automaticamente.

---

## ❓ PERGUNTAS FREQUENTES

### "Não tenho /mnt/user-data/outputs"

Você está no **Windows**? O caminho é diferente:

```bash
cd C:\Users\SeuNome\Desktop\demo-concessionarias
```

Ou onde quer que você salvou os arquivos.

---

### "git: command not found"

O Git não está instalado. Instale:
- **Windows:** https://git-scm.com/download/win
- **Mac:** `brew install git` ou baixe do site
- **Linux:** `sudo apt-get install git`

---

### "Permission denied"

Use o **token**, não a senha normal!

---

### "Already exists"

O repositório já foi criado. Está tudo certo!

---

## 🎯 PRÓXIMO PASSO: STREAMLIT CLOUD

Agora que seu código está no GitHub:

1. Acesse: https://share.streamlit.io/
2. Faça login com GitHub
3. Clique em "New app"
4. Selecione seu repositório
5. Main file: `demo_concessionaria.py`
6. Deploy!

**Em 5 minutos, sua demo estará online!**

---

## 💪 VOCÊ CONSEGUE!

Sei que parece muita coisa, mas veja o que você já aprendeu:
- ✅ O que é terminal
- ✅ Como navegar em pastas
- ✅ O que é Git e GitHub
- ✅ Como fazer commit
- ✅ Como enviar código para nuvem

**Isso é MUITO para um dia!** 🎉

Respire, siga passo a passo, e vai dar certo!

---

## 📞 PRECISA DE AJUDA?

**Se travar em algum passo:**

1. Anote a mensagem de erro EXATA
2. Google: "git [mensagem de erro]"
3. Provavelmente já aconteceu com milhares de pessoas
4. Tem solução na internet!

**Comunidades úteis:**
- Stack Overflow (em inglês)
- Stack Overflow em Português
- GitHub Community

---

Criado com ❤️ para iniciantes absolutos!

Você consegue! 💪🚀
