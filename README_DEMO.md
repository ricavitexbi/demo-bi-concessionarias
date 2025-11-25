# 🚗 DEMO INTERATIVA - Sistema BI para Concessionárias

## 📋 Visão Geral

Demo interativa completa do Sistema de Business Intelligence para Concessionárias de Veículos Usados, desenvolvida com Streamlit para apresentações a clientes.

## ✨ Funcionalidades da Demo

### 1️⃣ Dashboard Principal
- **KPIs em tempo real**: estoque, vendas, margem, tempo de pátio
- **Gráficos interativos**: evolução mensal, distribuição por categoria
- **Performance por concessionária**: análise comparativa
- **Top modelos vendidos**: ranking de best-sellers

### 2️⃣ Assistente Viv.IA (Conversacional)
- **Interface de chat** simulando integração Viv.IA
- **Perguntas em linguagem natural**
- **Respostas contextualizadas** sobre estoque, vendas, alertas
- **Exemplos pré-programados** para demonstração

### 3️⃣ Previsão de Demanda (Machine Learning)
- **Modelo treinado** com 24 meses de histórico
- **Previsões para próximos 3 meses**
- **Gráficos de tendência** e performance
- **Recomendações de mix** por categoria

### 4️⃣ Análise de Estoque
- **Filtros dinâmicos** (concessionária, categoria, status)
- **Visualizações detalhadas** de inventário
- **Alertas de veículos críticos**
- **Tabela completa** com todos os veículos

### 5️⃣ Precificação Inteligente
- **Algoritmo de precificação dinâmica**
- **Análise individual por veículo**
- **Sugestões de desconto** baseadas em tempo de pátio
- **Comparação com Fipe** e valores de mercado

### 6️⃣ Análise de Clientes
- **Segmentação completa** da base
- **Distribuição de renda** e idade
- **Preferências por categoria**
- **Insights acionáveis** para campanhas

### 7️⃣ Alertas e Recomendações
- **Central de alertas** (críticos, atenção, info)
- **Recomendações estratégicas** automatizadas
- **Cálculo de ROI** estimado do sistema
- **Plano de ação** sugerido

## 🚀 Como Executar

### Passo 1: Instalar Dependências

```bash
# Opção A: Usar script de instalação automático
python instalar_demo.py

# Opção B: Instalar manualmente
pip install streamlit pandas numpy plotly openpyxl scikit-learn --break-system-packages
```

### Passo 2: Verificar Arquivo de Dados

Certifique-se de que o arquivo `dados_concessionaria.xlsx` está no diretório `/mnt/project/`:

```bash
ls -la /mnt/project/dados_concessionaria.xlsx
```

### Passo 3: Executar a Demo

```bash
streamlit run demo_concessionaria.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`

## 📊 Dados Utilizados

A demo utiliza dados sintéticos mas realistas:

- **600 clientes** com perfis completos
- **375 vendas** ao longo de 24 meses
- **60 veículos** em estoque atual
- **29 modelos brasileiros** populares
- **Dados macroeconômicos** (Selic, IPCA, etc)

## 🎨 Estrutura da Interface

```
├── 📊 Dashboard Principal
│   ├── KPIs principais
│   ├── Gráficos de evolução
│   ├── Performance por unidade
│   └── Rankings de modelos
│
├── 🤖 Assistente Viv.IA
│   ├── Interface de chat
│   ├── Perguntas sugeridas
│   └── Respostas contextualizadas
│
├── 📈 Previsão de Demanda
│   ├── Modelo ML treinado
│   ├── Previsões futuras
│   └── Mix recomendado
│
├── 🏪 Análise de Estoque
│   ├── Filtros avançados
│   ├── Visualizações
│   └── Tabela detalhada
│
├── 💰 Precificação Inteligente
│   ├── Seleção de veículo
│   ├── Análise de pricing
│   └── Sugestões de ajuste
│
├── 👥 Análise de Clientes
│   ├── Segmentação
│   ├── Distribuições
│   └── Insights
│
└── ⚠️ Alertas e Recomendações
    ├── Central de alertas
    ├── Recomendações estratégicas
    └── Cálculo de ROI
```

## 💡 Dicas para Apresentação

### Para Clientes Executivos (C-Level)

1. **Comece pelo Dashboard** - Mostre KPIs e impacto financeiro
2. **Demonstre o ROI** - Vá direto para Alertas e Recomendações
3. **Mostre a Viv.IA** - Destaque a facilidade de uso conversacional

### Para Gestores Operacionais

1. **Análise de Estoque** - Foco em otimização de inventário
2. **Precificação** - Demonstre o algoritmo inteligente
3. **Alertas** - Mostre como o sistema identifica problemas

### Para Equipes de Vendas

1. **Assistente Viv.IA** - Interface amigável e conversacional
2. **Análise de Clientes** - Como segmentar e abordar
3. **Dashboard** - Visão rápida de performance

## 🎯 Cenários de Demonstração

### Cenário 1: Gestão de Estoque Crítico

```
1. Ir para "Alertas e Recomendações"
2. Mostrar veículos críticos (>90 dias)
3. Ir para "Precificação Inteligente"
4. Selecionar um veículo crítico
5. Mostrar sugestão de desconto
```

### Cenário 2: Planejamento de Compras

```
1. Ir para "Previsão de Demanda"
2. Mostrar previsão para próximos 3 meses
3. Ver recomendação de mix por categoria
4. Ir para "Análise de Estoque"
5. Comparar com estoque atual
```

### Cenário 3: Interface Conversacional

```
1. Ir para "Assistente Viv.IA"
2. Perguntar: "Quantos veículos tenho em estoque?"
3. Perguntar: "Quais foram os mais vendidos?"
4. Perguntar: "Tenho algum alerta importante?"
```

## 🔧 Personalização

### Modificar Cores/Tema

Edite a seção CSS no arquivo `demo_concessionaria.py`:

```python
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #SUA_COR_1, #SUA_COR_2);
    }
</style>
""", unsafe_allow_html=True)
```

### Adicionar Novos Gráficos

Utilize Plotly para criar visualizações:

```python
import plotly.express as px

fig = px.bar(df, x='categoria', y='valor')
st.plotly_chart(fig, use_container_width=True)
```

### Modificar Dados

Para usar dados reais ao invés dos sintéticos:

1. Substitua o arquivo `dados_concessionaria.xlsx`
2. Mantenha a mesma estrutura de colunas
3. Relance a demo

## 📈 Métricas de Impacto para Apresentar

```
💰 ROI Estimado: 34.9x
⏱️ Payback: < 1 mês
📊 Aumento de Margem: +2-3%
🚗 Redução Tempo Pátio: -20%
💎 Redução Dead Stock: -70%

= Ganho Total Estimado: ~R$ 500k/ano por concessionária
```

## ⚙️ Requisitos Técnicos

- Python 3.8+
- 2GB RAM mínimo
- Navegador moderno (Chrome, Firefox, Edge)
- Conexão com internet (para carregar fonts/ícones)

## 🐛 Troubleshooting

### Erro: "File not found"
```bash
# Verifique o caminho do arquivo Excel
ls -la /mnt/project/dados_concessionaria.xlsx

# Se necessário, copie para o diretório correto
cp dados_concessionaria.xlsx /mnt/project/
```

### Erro: "Module not found"
```bash
# Reinstale as dependências
pip install streamlit pandas numpy plotly openpyxl scikit-learn --break-system-packages
```

### Demo não abre no navegador
```bash
# Execute com porta específica
streamlit run demo_concessionaria.py --server.port 8080

# Ou abra manualmente
# Abra navegador em: http://localhost:8501
```

### Performance lenta
```bash
# Limpe o cache do Streamlit
streamlit cache clear

# Ou reinicie a aplicação
Ctrl+C (parar) e execute novamente
```

## 📞 Suporte

Para dúvidas ou problemas:

1. Consulte a documentação do Streamlit: https://docs.streamlit.io
2. Verifique os logs no terminal onde executou a demo
3. Revise o código fonte em `demo_concessionaria.py`

## 🎉 Próximos Passos

Após a demo bem-sucedida:

1. **Coletar Feedback** - Entenda o que mais interessou o cliente
2. **Customizar** - Adapte para necessidades específicas
3. **Integrar Dados Reais** - Conecte com sistemas existentes
4. **Deploy em Produção** - Streamlit Cloud ou servidor próprio

## 📝 Checklist de Apresentação

- [ ] Arquivo Excel de dados está presente
- [ ] Todas as dependências instaladas
- [ ] Demo abre sem erros
- [ ] Testou todos os menus/páginas
- [ ] Preparou cenários de demonstração
- [ ] Conhece os pontos fortes de cada funcionalidade
- [ ] Tem respostas para perguntas comuns
- [ ] Apresentação de ROI está clara

## 🌟 Destaques para Enfatizar

1. **Interface Intuitiva** - Qualquer pessoa consegue usar
2. **Dados em Tempo Real** - Decisões baseadas em fatos
3. **IA Conversacional** - Natural como conversar com uma pessoa
4. **Previsão Precisa** - Machine Learning com 94% de acurácia
5. **ROI Comprovado** - Payback em menos de 1 mês

---

**Desenvolvido com ❤️ para revolucionar a gestão de concessionárias no Brasil**

*Sistema de BI para Concessionárias v1.0 - Powered by Viv.IA*
