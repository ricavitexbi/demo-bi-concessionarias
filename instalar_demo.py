"""
Script de instalação para a Demo do Sistema BI Concessionárias
Instala todas as dependências necessárias
"""

import subprocess
import sys

def instalar_dependencias():
    """Instala todas as bibliotecas necessárias"""
    
    print("="*80)
    print("   INSTALAÇÃO - DEMO SISTEMA BI CONCESSIONÁRIAS")
    print("="*80)
    print()
    
    pacotes = [
        'streamlit',
        'pandas',
        'numpy',
        'plotly',
        'openpyxl',
        'scikit-learn'
    ]
    
    print("📦 Instalando dependências...\n")
    
    for pacote in pacotes:
        print(f"Instalando {pacote}...")
        try:
            subprocess.check_call([
                sys.executable, 
                '-m', 
                'pip', 
                'install', 
                pacote,
                '--break-system-packages'
            ])
            print(f"✅ {pacote} instalado com sucesso!\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar {pacote}: {e}\n")
    
    print("="*80)
    print("✅ INSTALAÇÃO CONCLUÍDA!")
    print("="*80)
    print()
    print("Para iniciar a demo, execute:")
    print("   streamlit run demo_concessionaria.py")
    print()

if __name__ == "__main__":
    instalar_dependencias()
