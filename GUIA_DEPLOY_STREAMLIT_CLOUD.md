# 🚀 GUIA COMPLETO: Deploy da Demo no Streamlit Cloud

## 📋 Visão Geral

Este guia vai te ensinar a fazer o deploy da sua demo no **Streamlit Cloud** (gratuito e fácil!).

**Por que Streamlit Cloud e não Vercel?**
- ❌ Vercel não suporta Streamlit (é serverless)
- ✅ Streamlit Cloud é gratuito e feito especificamente para Streamlit
- ✅ Deploy automático via GitHub
- ✅ URL personalizada
- ✅ SSL/HTTPS grátis

**Tempo estimado:** 15-20 minutos

---

## 📝 Pré-requisitos

Antes de começar, você precisa:

1. ✅ Conta no GitHub (gratuita)
2. ✅ Conta no Streamlit Cloud (gratuita)
3. ✅ Git instalado no seu computador

---

## 🎯 PASSO 1: Preparar Arquivos para Deploy

### 1.1 Criar arquivo requirements.txt

Este arquivo lista todas as bibliotecas Python que a demo precisa.

```bash
cd /mnt/user-data/outputs
```

Crie o arquivo `requirements.txt` com o seguinte conteúdo:

```txt
streamlit==1.51.0
pandas==2.3.3
numpy==2.3.5
plotly==6.5.0
openpyxl==3.1.5
scikit-learn==1.7.2
```

### 1.2 Criar arquivo .gitignore

Para não subir arquivos desnecessários pro GitHub:

```txt
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.env
.venv
.DS_Store
*.log
```

### 1.3 Criar configuração do Streamlit

Crie a pasta `.streamlit` e o arquivo `config.toml`:

```bash
mkdir -p .streamlit
```

Conteúdo do arquivo `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
```

---

## 🎯 PASSO 2: Criar Repositório no GitHub

### 2.1 Criar Repositório

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name:** `demo-bi-concessionarias`
   - **Description:** "Demo interativa de Sistema BI para Concessionárias"
   - **Public** ou **Private** (sua escolha)
   - ✅ **Add a README file** (marque esta opção)
3. Clique em **"Create repository"**

### 2.2 Configurar Git Local

No terminal:

```bash
# Configurar Git (se primeira vez)
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"

# Ir para o diretório da demo
cd /mnt/user-data/outputs

# Inicializar Git
git init

# Adicionar remote (substitua SEU_USUARIO pelo seu usuário GitHub)
git remote add origin https://github.com/SEU_USUARIO/demo-bi-concessionarias.git
```

### 2.3 Commit e Push

```bash
# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit: Demo BI Concessionárias"

# Enviar para GitHub
git push -u origin main
```

**Nota:** Se der erro de autenticação, você precisará criar um **Personal Access Token** no GitHub:
1. GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Generate new token
3. Marque: `repo` (full control)
4. Copie o token gerado
5. Use como senha ao fazer push

---

## 🎯 PASSO 3: Deploy no Streamlit Cloud

### 3.1 Criar Conta no Streamlit Cloud

1. Acesse: https://share.streamlit.io/
2. Clique em **"Sign up"**
3. Escolha **"Continue with GitHub"**
4. Autorize o Streamlit Cloud a acessar seu GitHub

### 3.2 Criar Nova App

1. No dashboard do Streamlit Cloud, clique em **"New app"**
2. Preencha:
   - **Repository:** Selecione `demo-bi-concessionarias`
   - **Branch:** `main`
   - **Main file path:** `demo_concessionaria.py`
3. Clique em **"Deploy!"**

### 3.3 Aguardar Deploy

- O Streamlit Cloud vai:
  1. Instalar as dependências do `requirements.txt`
  2. Executar sua aplicação
  3. Gerar uma URL pública

- Tempo estimado: 2-5 minutos
- Você verá os logs em tempo real

### 3.4 Sua App Está Online! 🎉

Você receberá uma URL tipo:
```
https://seu-usuario-demo-bi-concessionarias-xyz.streamlit.app
```

---

## 🎯 PASSO 4: Configurações Avançadas (Opcional)

### 4.1 URL Personalizada

1. No dashboard do Streamlit Cloud
2. Vá em Settings → General
3. Em "App URL", você pode personalizar o slug

### 4.2 Variáveis de Ambiente

Se precisar de secrets/variáveis:
1. Settings → Secrets
2. Adicione no formato TOML

### 4.3 Atualizar a App

Sempre que você fizer alterações:

```bash
git add .
git commit -m "Descrição das alterações"
git push
```

O Streamlit Cloud detecta automaticamente e faz redeploy!

---

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError"

**Causa:** Falta biblioteca no requirements.txt

**Solução:**
1. Adicione a biblioteca em `requirements.txt`
2. Commit e push
3. Streamlit Cloud fará redeploy automático

### Erro: "File not found: dados_concessionaria.xlsx"

**Causa:** Arquivo Excel não está no repositório

**Solução:**
```bash
# Copiar arquivo para o diretório
cp /mnt/project/dados_concessionaria.xlsx /mnt/user-data/outputs/

# Adicionar ao Git
git add dados_concessionaria.xlsx
git commit -m "Adicionar arquivo de dados"
git push
```

### App está lenta

**Causa:** Dados muito grandes ou processamento pesado

**Soluções:**
1. Use `@st.cache_data` em funções pesadas
2. Otimize carregamento de dados
3. Considere plano pago do Streamlit Cloud (mais recursos)

### Erro de autenticação GitHub

**Solução:** Use Personal Access Token como senha:
1. GitHub → Settings → Developer Settings → Personal Access Tokens
2. Generate new token (classic)
3. Marque `repo`
4. Use token como senha ao fazer push

---

## 📊 Comparação: Streamlit Cloud vs Outras Plataformas

| Plataforma       | Suporta Streamlit? | Gratuito? | Facilidade |
|------------------|-------------------|-----------|------------|
| Streamlit Cloud  | ✅ Nativo         | ✅ Sim    | ⭐⭐⭐⭐⭐ |
| Vercel           | ❌ Não            | ✅ Sim    | ❌         |
| Heroku           | ✅ Com config     | ⚠️ Limited| ⭐⭐⭐     |
| AWS EC2          | ✅ Com setup      | ⚠️ Complex| ⭐⭐       |
| Google Cloud Run | ✅ Com Docker     | ⚠️ Pago   | ⭐⭐       |

**Recomendação:** Use Streamlit Cloud! É a solução mais fácil e gratuita.

---

## 🎯 Checklist Completo

### Preparação
- [ ] Criar `requirements.txt`
- [ ] Criar `.gitignore`
- [ ] Criar `.streamlit/config.toml`
- [ ] Copiar `dados_concessionaria.xlsx` para o diretório

### GitHub
- [ ] Criar repositório no GitHub
- [ ] Configurar Git local
- [ ] Fazer primeiro commit
- [ ] Push para GitHub

### Streamlit Cloud
- [ ] Criar conta no Streamlit Cloud
- [ ] Conectar com GitHub
- [ ] Criar nova app
- [ ] Aguardar deploy
- [ ] Testar URL pública

### Finalização
- [ ] Compartilhar URL com clientes
- [ ] Documentar URL para referência
- [ ] Configurar analytics (opcional)

---

## 🌟 Dicas Profissionais

### 1. Analytics

Adicione Google Analytics à sua demo:

```python
# No início do demo_concessionaria.py
import streamlit as st

# Google Analytics
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=SEU_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'SEU_ID');
</script>
""", unsafe_allow_html=True)
```

### 2. Senha de Acesso

Proteja a demo com senha:

```python
import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == "sua_senha_aqui":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Senha", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Senha", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Senha incorreta")
        return False
    else:
        return True

if check_password():
    # Seu código da demo aqui
    pass
```

### 3. Domínio Personalizado

Para URL profissional (ex: demo.suaempresa.com.br):
1. Configure CNAME no seu domínio apontando para Streamlit
2. No Streamlit Cloud: Settings → Custom domain
3. Adicione seu domínio

**Nota:** Requer plano pago do Streamlit Cloud

---

## 📞 Links Úteis

- **Streamlit Cloud:** https://share.streamlit.io/
- **Documentação Streamlit:** https://docs.streamlit.io/
- **GitHub Help:** https://docs.github.com/
- **Streamlit Community:** https://discuss.streamlit.io/

---

## 🎉 Pronto!

Agora sua demo está online e acessível por qualquer pessoa com a URL!

Compartilhe com seus clientes e comece a fechar negócios! 💰

---

## 📧 Próximos Passos

1. ✅ Teste a URL pública
2. ✅ Compartilhe com stakeholders
3. ✅ Colete feedback
4. ✅ Itere e melhore
5. ✅ Feche negócios!

---

*Desenvolvido com ❤️ para revolucionar a gestão de concessionárias no Brasil*
