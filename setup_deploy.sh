#!/bin/bash

# Script de Setup Automático para Deploy no Streamlit Cloud
# Para iniciantes no Git e GitHub

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║              🚀 SETUP AUTOMÁTICO - DEPLOY STREAMLIT CLOUD                 ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para perguntas sim/não
ask_yes_no() {
    while true; do
        read -p "$1 (s/n): " yn
        case $yn in
            [Ss]* ) return 0;;
            [Nn]* ) return 1;;
            * ) echo "Por favor, responda s (sim) ou n (não).";;
        esac
    done
}

# Verificar se está no diretório correto
if [ ! -f "demo_concessionaria.py" ]; then
    echo -e "${RED}❌ Erro: Arquivo demo_concessionaria.py não encontrado!${NC}"
    echo "Execute este script no diretório /mnt/user-data/outputs/"
    exit 1
fi

echo "✅ Verificação inicial: OK"
echo ""

# ============================================================================
# PASSO 1: Configurar Git
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 PASSO 1: Configurar Git"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Verificar se Git está instalado
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git não está instalado!${NC}"
    echo "Instale o Git: https://git-scm.com/downloads"
    exit 1
fi

echo "✅ Git instalado: $(git --version)"
echo ""

# Verificar configuração do Git
GIT_USER=$(git config --global user.name 2>/dev/null)
GIT_EMAIL=$(git config --global user.email 2>/dev/null)

if [ -z "$GIT_USER" ] || [ -z "$GIT_EMAIL" ]; then
    echo "⚠️  Git não está configurado. Vamos configurar agora!"
    echo ""
    
    read -p "Digite seu nome: " USER_NAME
    read -p "Digite seu email: " USER_EMAIL
    
    git config --global user.name "$USER_NAME"
    git config --global user.email "$USER_EMAIL"
    
    echo ""
    echo -e "${GREEN}✅ Git configurado com sucesso!${NC}"
else
    echo "✅ Git já configurado:"
    echo "   Nome: $GIT_USER"
    echo "   Email: $GIT_EMAIL"
fi

echo ""

# ============================================================================
# PASSO 2: Inicializar Repositório
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 PASSO 2: Inicializar Repositório Local"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ -d ".git" ]; then
    echo "⚠️  Repositório Git já existe neste diretório."
    
    if ask_yes_no "Deseja reinicializar?"; then
        rm -rf .git
        git init
        echo -e "${GREEN}✅ Repositório reinicializado${NC}"
    else
        echo "Mantendo repositório existente."
    fi
else
    git init
    echo -e "${GREEN}✅ Repositório Git inicializado${NC}"
fi

echo ""

# ============================================================================
# PASSO 3: Verificar Arquivos
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📂 PASSO 3: Verificar Arquivos Necessários"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

REQUIRED_FILES=(
    "demo_concessionaria.py"
    "dados_concessionaria.xlsx"
    "requirements.txt"
    ".gitignore"
    ".streamlit/config.toml"
    "README.md"
)

ALL_FILES_OK=true

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ] || [ -d "$(dirname "$file")" ]; then
        echo -e "${GREEN}✅${NC} $file"
    else
        echo -e "${RED}❌${NC} $file (FALTANDO!)"
        ALL_FILES_OK=false
    fi
done

echo ""

if [ "$ALL_FILES_OK" = false ]; then
    echo -e "${RED}❌ Alguns arquivos necessários estão faltando!${NC}"
    echo "Execute o script de preparação antes de continuar."
    exit 1
fi

echo -e "${GREEN}✅ Todos os arquivos necessários estão presentes!${NC}"
echo ""

# ============================================================================
# PASSO 4: Conectar com GitHub
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔗 PASSO 4: Conectar com GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "📌 IMPORTANTE: Antes de continuar, você precisa:"
echo ""
echo "   1. Criar um repositório no GitHub:"
echo "      https://github.com/new"
echo ""
echo "   2. Nome sugerido: demo-bi-concessionarias"
echo "   3. Pode ser público ou privado"
echo "   4. NÃO marque 'Add a README file'"
echo ""

if ! ask_yes_no "Você já criou o repositório no GitHub?"; then
    echo ""
    echo -e "${YELLOW}⚠️  Por favor, crie o repositório primeiro e execute este script novamente.${NC}"
    echo ""
    echo "Tutorial: https://docs.github.com/pt/get-started/quickstart/create-a-repo"
    exit 0
fi

echo ""
read -p "Digite seu usuário do GitHub: " GITHUB_USER
read -p "Digite o nome do repositório (padrão: demo-bi-concessionarias): " REPO_NAME

# Usar nome padrão se não fornecido
REPO_NAME=${REPO_NAME:-demo-bi-concessionarias}

GITHUB_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo ""
echo "URL do repositório: $GITHUB_URL"
echo ""

# Verificar se remote já existe
if git remote | grep -q "^origin$"; then
    echo "⚠️  Remote 'origin' já existe."
    
    if ask_yes_no "Deseja atualizar para o novo repositório?"; then
        git remote remove origin
        git remote add origin "$GITHUB_URL"
        echo -e "${GREEN}✅ Remote atualizado${NC}"
    fi
else
    git remote add origin "$GITHUB_URL"
    echo -e "${GREEN}✅ Remote adicionado${NC}"
fi

echo ""

# ============================================================================
# PASSO 5: Commit e Push
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📤 PASSO 5: Commit e Push para GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "Adicionando arquivos..."
git add .

echo "Criando commit..."
git commit -m "Initial commit: Demo BI Concessionárias com Streamlit"

echo ""
echo "Enviando para GitHub..."
echo ""
echo -e "${YELLOW}⚠️  ATENÇÃO:${NC}"
echo "   Se for a primeira vez, você precisará autenticar."
echo "   Use um Personal Access Token como senha."
echo ""
echo "   Como criar token:"
echo "   GitHub → Settings → Developer Settings → Personal Access Tokens"
echo "   → Tokens (classic) → Generate new token"
echo "   Marque: 'repo' (full control)"
echo ""

if ask_yes_no "Pronto para fazer push?"; then
    git branch -M main
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✅ Push realizado com sucesso!${NC}"
    else
        echo ""
        echo -e "${RED}❌ Erro ao fazer push${NC}"
        echo ""
        echo "Possíveis soluções:"
        echo "1. Verifique suas credenciais GitHub"
        echo "2. Use Personal Access Token como senha"
        echo "3. Tente novamente com: git push -u origin main"
        exit 1
    fi
else
    echo ""
    echo "Push cancelado. Você pode fazer manualmente depois com:"
    echo "   git push -u origin main"
    exit 0
fi

echo ""

# ============================================================================
# PASSO 6: Instruções Streamlit Cloud
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "☁️  PASSO 6: Deploy no Streamlit Cloud"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo -e "${GREEN}🎉 Código enviado para GitHub com sucesso!${NC}"
echo ""
echo "Agora faça o deploy no Streamlit Cloud:"
echo ""
echo "1. Acesse: https://share.streamlit.io/"
echo "2. Clique em 'Sign up' ou 'Log in'"
echo "3. Escolha 'Continue with GitHub'"
echo "4. Autorize o Streamlit Cloud"
echo "5. Clique em 'New app'"
echo "6. Preencha:"
echo "   - Repository: $GITHUB_USER/$REPO_NAME"
echo "   - Branch: main"
echo "   - Main file: demo_concessionaria.py"
echo "7. Clique em 'Deploy!'"
echo "8. Aguarde 2-5 minutos"
echo ""
echo "Sua URL será algo como:"
echo "https://$GITHUB_USER-$REPO_NAME-xyz.streamlit.app"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📚 Documentação Adicional"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Para mais detalhes, consulte:"
echo "   - GUIA_DEPLOY_STREAMLIT_CLOUD.md"
echo "   - README.md"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Setup concluído com sucesso!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Próximos passos:"
echo "1. ✅ Código no GitHub"
echo "2. ⏳ Deploy no Streamlit Cloud (siga instruções acima)"
echo "3. 🎉 Compartilhe a URL com clientes!"
echo ""
