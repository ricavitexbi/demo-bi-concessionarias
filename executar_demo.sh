#!/bin/bash

# Script de Execução Rápida - Demo BI Concessionárias
# Execute: ./executar_demo.sh

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║              🚗 DEMO - SISTEMA DE BI PARA CONCESSIONÁRIAS                  ║"
echo "║                    Powered by Viv.IA Intelligence                          ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar se Streamlit está instalado
if ! command -v streamlit &> /dev/null
then
    echo "❌ Streamlit não encontrado. Instalando dependências..."
    python3 instalar_demo.py
    echo ""
fi

# Verificar arquivo de dados
if [ ! -f "/mnt/project/dados_concessionaria.xlsx" ]; then
    echo "❌ Arquivo de dados não encontrado em /mnt/project/"
    echo "   Verifique se dados_concessionaria.xlsx existe"
    exit 1
fi

echo "✅ Tudo pronto!"
echo ""
echo "🚀 Iniciando demo..."
echo ""
echo "📌 A demo abrirá automaticamente no navegador"
echo "📌 URL: http://localhost:8501"
echo ""
echo "Para parar a demo, pressione Ctrl+C"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

# Executar Streamlit
streamlit run demo_concessionaria.py
