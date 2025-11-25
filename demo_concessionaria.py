"""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║              🚗 DEMO - SISTEMA DE BI PARA CONCESSIONÁRIAS                  ║
║                    Powered by Viv.IA Intelligence                          ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

Demo interativa para apresentação a clientes
Demonstra todas as funcionalidades do sistema de BI Automotivo
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Sistema BI Automotivo - Viv.IA",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .alert-critical {
        background-color: #ffebee;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #f44336;
    }
    .alert-warning {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #ff9800;
    }
    .alert-success {
        background-color: #e8f5e9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #4caf50;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: #f5f5f5;
        margin-right: 20%;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# CARREGAR DADOS (com cache para performance)
# ============================================================================


@st.cache_data
def carregar_dados():
    """Carrega todos os datasets necessários"""
    try:
        df_inventario = pd.read_excel('dados_concessionaria.xlsx',
                                      sheet_name='Inventario_Atual')
        df_vendas = pd.read_excel('dados_concessionaria.xlsx',
                                  sheet_name='Historico_Vendas')
        df_clientes = pd.read_excel('dados_concessionaria.xlsx',
                                    sheet_name='Clientes')
        df_macro = pd.read_excel('dados_concessionaria.xlsx',
                                 sheet_name='Dados_Macro')

        # Converter datas
        df_inventario['data_entrada'] = pd.to_datetime(
            df_inventario['data_entrada'])
        df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
        df_vendas['data_entrada_estoque'] = pd.to_datetime(
            df_vendas['data_entrada_estoque'])
        df_macro['data'] = pd.to_datetime(df_macro['data'])

        return df_inventario, df_vendas, df_clientes, df_macro
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None, None, None, None


# Carregar dados
df_inventario, df_vendas, df_clientes, df_macro = carregar_dados()

# Verificar se dados foram carregados
if df_inventario is None:
    st.error(
        "❌ Erro ao carregar dados. Verifique se o arquivo Excel existe no diretório correto.")
    st.stop()

# ============================================================================
# SIDEBAR - NAVEGAÇÃO
# ============================================================================

st.sidebar.markdown("## 🚗 Sistema BI Automotivo")
st.sidebar.markdown("### Powered by Viv.IA")
st.sidebar.markdown("---")

pagina = st.sidebar.radio(
    "Navegação",
    ["📊 Dashboard Principal",
     "🤖 Assistente Viv.IA",
     "📈 Previsão de Demanda",
     "🏪 Análise de Estoque",
     "💰 Precificação Inteligente",
     "👥 Análise de Clientes",
     "⚠️ Alertas e Recomendações"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**📌 Demo do Sistema**
- Dados sintéticos realistas
- 600 clientes cadastrados
- 375 vendas (24 meses)
- 60 veículos em estoque
""")

# ============================================================================
# PÁGINA 1: DASHBOARD PRINCIPAL
# ============================================================================

if pagina == "📊 Dashboard Principal":

    st.markdown('<div class="main-header">📊 Dashboard Executivo - Visão Geral</div>',
                unsafe_allow_html=True)

    # KPIs Principais
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_estoque = len(df_inventario)
        valor_estoque = df_inventario['valor_compra'].sum()
        st.metric(
            "🚗 Veículos em Estoque",
            f"{total_estoque}",
            f"R$ {valor_estoque/1e6:.1f}M investidos"
        )

    with col2:
        vendas_mes = len(df_vendas[df_vendas['data_venda'] >
                                   df_vendas['data_venda'].max() - timedelta(days=30)])
        receita_mes = df_vendas[df_vendas['data_venda'] >
                                df_vendas['data_venda'].max() - timedelta(days=30)]['valor_venda'].sum()
        st.metric(
            "📅 Vendas (30 dias)",
            f"{vendas_mes}",
            f"R$ {receita_mes/1e6:.2f}M"
        )

    with col3:
        margem_media = df_vendas['margem_percentual'].mean()
        lucro_total = df_vendas['lucro_bruto'].sum()
        st.metric(
            "💹 Margem Média",
            f"{margem_media:.1f}%",
            f"R$ {lucro_total/1e6:.1f}M lucro total"
        )

    with col4:
        tempo_medio = df_inventario['dias_em_patio'].mean()
        criticos = len(
            df_inventario[df_inventario['status_estoque'] == 'Crítico'])
        st.metric(
            "⏱️ Tempo Médio Pátio",
            f"{tempo_medio:.0f} dias",
            f"{criticos} críticos",
            delta_color="inverse"
        )

    st.markdown("---")

    # Gráficos Principais
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Evolução de Vendas Mensal")

        # Preparar dados
        vendas_por_mes = df_vendas.groupby(df_vendas['data_venda'].dt.to_period('M')).agg({
            'venda_id': 'count',
            'valor_venda': 'sum',
            'lucro_bruto': 'sum'
        }).reset_index()
        vendas_por_mes['data_venda'] = vendas_por_mes['data_venda'].astype(str)

        # Criar gráfico
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=vendas_por_mes['data_venda'],
            y=vendas_por_mes['venda_id'],
            name='Quantidade',
            marker_color='steelblue'
        ))

        fig.update_layout(
            height=350,
            showlegend=False,
            xaxis_title="Mês",
            yaxis_title="Vendas",
            hovermode='x unified'
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🎯 Vendas por Categoria")

        # Dados por categoria
        vendas_categoria = df_vendas.groupby('categoria').agg({
            'venda_id': 'count',
            'valor_venda': 'sum'
        }).reset_index()

        fig = px.pie(
            vendas_categoria,
            values='venda_id',
            names='categoria',
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=350)

        st.plotly_chart(fig, use_container_width=True)

    # Performance por Concessionária
    st.subheader("🏢 Performance por Concessionária")

    perf_conc = df_vendas.groupby('concessionaria_nome').agg({
        'venda_id': 'count',
        'valor_venda': 'sum',
        'lucro_bruto': 'sum',
        'margem_percentual': 'mean'
    }).round(2).reset_index()

    perf_conc.columns = ['Concessionária',
                         'Vendas', 'Receita', 'Lucro', 'Margem %']
    perf_conc['Receita'] = perf_conc['Receita'].apply(lambda x: f"R$ {x:,.2f}")
    perf_conc['Lucro'] = perf_conc['Lucro'].apply(lambda x: f"R$ {x:,.2f}")

    st.dataframe(perf_conc, use_container_width=True, hide_index=True)

    # Top Modelos Vendidos
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏆 Top 10 Modelos Mais Vendidos")
        top_modelos = df_vendas['modelo'].value_counts().head(10)

        fig = go.Figure(go.Bar(
            x=top_modelos.values,
            y=top_modelos.index,
            orientation='h',
            marker_color='coral'
        ))

        fig.update_layout(
            height=400,
            xaxis_title="Vendas",
            yaxis_title="Modelo",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📊 Distribuição de Estoque por Status")
        status_estoque = df_inventario['status_estoque'].value_counts()

        cores_status = {
            'Novo': '#4caf50',
            'Normal': '#2196f3',
            'Atenção': '#ff9800',
            'Crítico': '#f44336'
        }

        fig = go.Figure(go.Bar(
            x=status_estoque.index,
            y=status_estoque.values,
            marker_color=[cores_status.get(s, 'gray')
                          for s in status_estoque.index]
        ))

        fig.update_layout(
            height=400,
            xaxis_title="Status",
            yaxis_title="Quantidade",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PÁGINA 2: ASSISTENTE VIV.IA
# ============================================================================

elif pagina == "🤖 Assistente Viv.IA":

    st.markdown('<div class="main-header">🤖 Assistente Conversacional Viv.IA</div>',
                unsafe_allow_html=True)

    st.markdown("""
    ### Faça perguntas em linguagem natural!
    
    O assistente Viv.IA pode responder sobre:
    - 📦 Estoque de veículos
    - 💰 Análise de vendas
    - 💵 Sugestões de preço
    - ⚠️ Alertas importantes
    - 📈 Previsões de demanda
    """)

    # Sugestões de perguntas
    st.subheader("💡 Experimente perguntar:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📦 Quantos veículos tenho em estoque?"):
            query_selecionada = "Quantos veículos tenho em estoque?"
        else:
            query_selecionada = None

    with col2:
        if st.button("🏆 Quais foram os mais vendidos?"):
            query_selecionada = "Quais foram os mais vendidos?"
        else:
            query_selecionada = query_selecionada if query_selecionada else None

    with col3:
        if st.button("⚠️ Tenho algum alerta importante?"):
            query_selecionada = "Tenho algum alerta importante?"
        else:
            query_selecionada = query_selecionada if query_selecionada else None

    # Input de texto
    user_input = st.text_input(
        "Sua pergunta:",
        value=query_selecionada if query_selecionada else "",
        placeholder="Ex: Quantos Onix tenho em estoque?"
    )

    if user_input:
        # Processar query
        query_lower = user_input.lower()

        with st.spinner("🤔 Analisando..."):

            # Simular processamento
            import time
            time.sleep(0.5)

            # Lógica de resposta (simplificada)
            if any(word in query_lower for word in ['estoque', 'tenho', 'quantos']):
                resposta = f"""
**📦 ESTOQUE ATUAL:**

Total de veículos: **{len(df_inventario)}**  
Capital investido: **R$ {df_inventario['valor_compra'].sum():,.2f}**

**Por categoria:**
"""
                for cat, qtd in df_inventario.groupby('categoria').size().items():
                    resposta += f"\n- {cat.capitalize()}: {qtd} unidades"

                # Adicionar modelo específico se mencionado
                for modelo in df_inventario['modelo'].unique():
                    if modelo.lower() in query_lower:
                        veiculos = df_inventario[df_inventario['modelo'] == modelo]
                        resposta += f"\n\n**{modelo}:** {len(veiculos)} unidades"
                        for _, v in veiculos.iterrows():
                            resposta += f"\n  - {v['concessionaria_nome']}: {v['ano_modelo']} {v['cor']}"

            elif any(word in query_lower for word in ['vendido', 'venda', 'mais']):
                top_5 = df_vendas['modelo'].value_counts().head(5)
                resposta = "**🏆 TOP 5 MODELOS MAIS VENDIDOS:**\n\n"
                for i, (modelo, qtd) in enumerate(top_5.items(), 1):
                    resposta += f"{i}. **{modelo}**: {qtd} unidades\n"

            elif any(word in query_lower for word in ['alerta', 'problema', 'crítico']):
                criticos = df_inventario[df_inventario['status_estoque'] == 'Crítico']
                resposta = f"**⚠️ ALERTAS IMPORTANTES:**\n\n"

                if len(criticos) > 0:
                    capital = criticos['valor_compra'].sum()
                    resposta += f"🚨 **CRÍTICO:** {len(criticos)} veículos parados >90 dias\n"
                    resposta += f"   Capital preso: R$ {capital:,.2f}\n\n"

                atencao = df_inventario[df_inventario['status_estoque'] == 'Atenção']
                if len(atencao) > 0:
                    resposta += f"⚡ **ATENÇÃO:** {len(atencao)} veículos entre 60-90 dias\n"

                if len(criticos) == 0 and len(atencao) == 0:
                    resposta += "✅ Nenhum alerta crítico no momento!"

            else:
                resposta = """
**❓ Não entendi completamente sua pergunta.**

Você pode perguntar sobre:
- 📦 Estoque ("Quantos Onix tenho?")
- 💰 Vendas ("Quais os mais vendidos?")
- ⚠️ Alertas ("Algum problema?")
- 📈 Previsões ("Quanto vou vender?")
"""

        # Exibir resposta
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>👤 Você:</strong> {user_input}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>🤖 Viv.IA:</strong><br>{resposta}
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PÁGINA 3: PREVISÃO DE DEMANDA
# ============================================================================

elif pagina == "📈 Previsão de Demanda":

    st.markdown('<div class="main-header">📈 Previsão de Demanda com Machine Learning</div>',
                unsafe_allow_html=True)

    st.info("🤖 Modelo treinado com 24 meses de histórico + indicadores macroeconômicos")

    # Preparar dados para modelo
    vendas_mes = df_vendas.groupby(df_vendas['data_venda'].dt.to_period('M')).agg({
        'venda_id': 'count'
    }).reset_index()
    vendas_mes['mes_numero'] = range(len(vendas_mes))

    # Merge com dados macro
    df_macro['ano_mes'] = df_macro['data'].dt.to_period('M')
    vendas_mes['ano_mes'] = vendas_mes['data_venda']
    modelo_df = vendas_mes.merge(
        df_macro[['ano_mes', 'selic', 'confianca_consumidor']],
        on='ano_mes',
        how='left'
    )

    # Treinar modelo
    X = modelo_df[['mes_numero', 'selic', 'confianca_consumidor']].fillna(
        method='ffill')
    y = modelo_df['venda_id']

    modelo = LinearRegression()
    modelo.fit(X, y)

    # Fazer previsões
    y_pred = modelo.predict(X)

    # Previsões futuras (3 meses)
    ultimo_mes = modelo_df['mes_numero'].max()
    selic_atual = df_macro['selic'].iloc[-1]
    confianca_atual = df_macro['confianca_consumidor'].iloc[-1]

    previsoes_futuras = []
    for i in range(1, 4):
        mes_futuro = ultimo_mes + i
        X_futuro = np.array([[mes_futuro, selic_atual, confianca_atual]])
        prev = modelo.predict(X_futuro)[0]
        previsoes_futuras.append(prev)

    # Visualização
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Histórico vs Previsão")

        fig = go.Figure()

        # Histórico real
        fig.add_trace(go.Scatter(
            x=list(range(len(y))),
            y=y,
            mode='lines+markers',
            name='Vendas Reais',
            line=dict(color='steelblue', width=3)
        ))

        # Previsão no histórico
        fig.add_trace(go.Scatter(
            x=list(range(len(y))),
            y=y_pred,
            mode='lines',
            name='Modelo (Fitted)',
            line=dict(color='coral', width=2, dash='dash')
        ))

        # Previsões futuras
        x_futuro = list(range(len(y), len(y) + 3))
        fig.add_trace(go.Scatter(
            x=x_futuro,
            y=previsoes_futuras,
            mode='lines+markers',
            name='Previsão Futura',
            line=dict(color='red', width=3),
            marker=dict(size=10)
        ))

        fig.update_layout(
            height=400,
            xaxis_title="Período (mês)",
            yaxis_title="Vendas",
            hovermode='x unified',
            showlegend=True
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🎯 Previsões")

        for i, prev in enumerate(previsoes_futuras, 1):
            st.metric(
                f"Mês +{i}",
                f"{int(round(prev))} unidades",
                f"±{int(prev * 0.1)} (10%)"
            )

        st.markdown("---")

        # Performance do modelo
        from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
        mae = mean_absolute_error(y, y_pred)
        mape = mean_absolute_percentage_error(y, y_pred) * 100

        st.markdown(f"""
        **📊 Performance do Modelo:**
        - MAE: {mae:.2f} unidades
        - MAPE: {mape:.1f}%
        - Acurácia: {100-mape:.1f}%
        """)

    # Recomendações por categoria
    st.subheader("🎨 Recomendação de Mix por Categoria")

    proporcoes = df_vendas['categoria'].value_counts(normalize=True)
    previsao_proximo_mes = int(round(previsoes_futuras[0]))

    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]

    for i, (cat, prop) in enumerate(proporcoes.items()):
        with cols[i]:
            unidades = int(round(previsao_proximo_mes * prop))
            st.metric(
                f"🎯 {cat.capitalize()}",
                f"{unidades} un.",
                f"{prop*100:.0f}% do total"
            )

# ============================================================================
# PÁGINA 4: ANÁLISE DE ESTOQUE
# ============================================================================

elif pagina == "🏪 Análise de Estoque":

    st.markdown('<div class="main-header">🏪 Análise Detalhada de Estoque</div>',
                unsafe_allow_html=True)

    # Filtros
    col1, col2, col3 = st.columns(3)

    with col1:
        conc_selecionada = st.selectbox(
            "Concessionária:",
            ["Todas"] + list(df_inventario['concessionaria_nome'].unique())
        )

    with col2:
        cat_selecionada = st.selectbox(
            "Categoria:",
            ["Todas"] + list(df_inventario['categoria'].unique())
        )

    with col3:
        status_selecionado = st.selectbox(
            "Status:",
            ["Todos"] + list(df_inventario['status_estoque'].unique())
        )

    # Aplicar filtros
    df_filtrado = df_inventario.copy()

    if conc_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['concessionaria_nome']
                                  == conc_selecionada]
    if cat_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['categoria'] == cat_selecionada]
    if status_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado['status_estoque']
                                  == status_selecionado]

    # Métricas filtradas
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🚗 Veículos", len(df_filtrado))
    with col2:
        st.metric("💰 Valor Total",
                  f"R$ {df_filtrado['valor_compra'].sum()/1e6:.1f}M")
    with col3:
        st.metric("📅 Tempo Médio",
                  f"{df_filtrado['dias_em_patio'].mean():.0f} dias")
    with col4:
        st.metric("💎 Ticket Médio",
                  f"R$ {df_filtrado['valor_compra'].mean()/1e3:.0f}k")

    st.markdown("---")

    # Visualizações
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⏱️ Distribuição por Tempo em Pátio")

        fig = px.histogram(
            df_filtrado,
            x='dias_em_patio',
            nbins=20,
            color='status_estoque',
            color_discrete_map={
                'Novo': '#4caf50',
                'Normal': '#2196f3',
                'Atenção': '#ff9800',
                'Crítico': '#f44336'
            }
        )

        fig.update_layout(
            height=350,
            xaxis_title="Dias em Pátio",
            yaxis_title="Quantidade"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("💰 Valor por Categoria")

        valor_cat = df_filtrado.groupby(
            'categoria')['valor_compra'].sum().reset_index()

        fig = px.bar(
            valor_cat,
            x='categoria',
            y='valor_compra',
            color='categoria',
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_layout(
            height=350,
            xaxis_title="Categoria",
            yaxis_title="Valor Total (R$)",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    # Tabela detalhada
    st.subheader("📋 Inventário Detalhado")

    # Preparar dados para exibição
    df_display = df_filtrado[[
        'modelo', 'ano_modelo', 'cor', 'km',
        'dias_em_patio', 'preco_anunciado', 'status_estoque'
    ]].copy()

    df_display['preco_anunciado'] = df_display['preco_anunciado'].apply(
        lambda x: f"R$ {x:,.2f}"
    )

    df_display.columns = ['Modelo', 'Ano', 'Cor',
                          'KM', 'Dias Pátio', 'Preço', 'Status']

    # Aplicar cores nas linhas baseado no status
    def highlight_status(row):
        if row['Status'] == 'Crítico':
            return ['background-color: #ffebee'] * len(row)
        elif row['Status'] == 'Atenção':
            return ['background-color: #fff3e0'] * len(row)
        else:
            return [''] * len(row)

    st.dataframe(
        df_display.style.apply(highlight_status, axis=1),
        use_container_width=True,
        hide_index=True
    )

# ============================================================================
# PÁGINA 5: PRECIFICAÇÃO INTELIGENTE
# ============================================================================

elif pagina == "💰 Precificação Inteligente":

    st.markdown('<div class="main-header">💰 Sistema de Precificação Dinâmica</div>',
                unsafe_allow_html=True)

    st.markdown("""
    ### Algoritmo de Precificação Baseado em:
    - ⏱️ Tempo em pátio
    - 📊 Valores de referência Fipe
    - 🎯 Performance da categoria
    - 📈 Demanda histórica
    """)

    # Seleção de veículo
    veiculos_lista = [
        f"{row['modelo']} {row['ano_modelo']} - {row['cor']} ({row['veiculo_id']})"
        for _, row in df_inventario.iterrows()
    ]

    veiculo_selecionado = st.selectbox(
        "Selecione um veículo para análise:",
        veiculos_lista
    )

    # Extrair ID do veículo
    veiculo_id = veiculo_selecionado.split('(')[1].split(')')[0]
    veiculo = df_inventario[df_inventario['veiculo_id'] == veiculo_id].iloc[0]

    # Análise de precificação
    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📋 Informações do Veículo")

        st.markdown(f"""
        **Modelo:** {veiculo['modelo']}  
        **Ano:** {veiculo['ano_modelo']}  
        **Cor:** {veiculo['cor']}  
        **KM:** {veiculo['km']:,}  
        **Combustível:** {veiculo['combustivel']}  
        **Estado:** {veiculo['estado_conservacao']}  
        **Concessionária:** {veiculo['concessionaria_nome']}
        
        ---
        
        **Entrada:** {veiculo['data_entrada'].strftime('%d/%m/%Y')}  
        **Dias em pátio:** {veiculo['dias_em_patio']} dias  
        **Status:** {veiculo['status_estoque']}
        """)

    with col2:
        st.subheader("💡 Análise de Precificação")

        # Lógica de precificação dinâmica
        tempo_patio = veiculo['dias_em_patio']
        preco_atual = veiculo['preco_anunciado']
        valor_fipe = veiculo['valor_fipe_referencia']
        valor_compra = veiculo['valor_compra']

        # Calcular ajuste baseado no tempo
        if tempo_patio < 30:
            ajuste = 1.0
            status_preco = "✅ Preço competitivo"
            cor_status = "success"
        elif tempo_patio < 60:
            ajuste = 0.97
            status_preco = "⚡ Considere pequeno desconto"
            cor_status = "warning"
        elif tempo_patio < 90:
            ajuste = 0.93
            status_preco = "⚠️ Desconto recomendado"
            cor_status = "warning"
        else:
            ajuste = 0.90
            status_preco = "🚨 Desconto urgente necessário"
            cor_status = "error"

        preco_sugerido = preco_atual * ajuste
        desconto = ((preco_atual - preco_sugerido) / preco_atual) * 100
        margem_atual = ((preco_atual - valor_compra) / valor_compra) * 100
        margem_sugerida = (
            (preco_sugerido - valor_compra) / valor_compra) * 100

        # Exibir métricas
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.metric("💵 Preço Atual", f"R$ {preco_atual:,.2f}")
        with col_b:
            st.metric("💎 Preço Sugerido", f"R$ {preco_sugerido:,.2f}",
                      f"{-desconto:.1f}%" if desconto > 0 else "Manter")
        with col_c:
            st.metric("📊 Valor Fipe", f"R$ {valor_fipe:,.2f}")

        st.markdown("---")

        # Status colorido
        if cor_status == "success":
            st.success(f"**{status_preco}**")
        elif cor_status == "warning":
            st.warning(f"**{status_preco}**")
        else:
            st.error(f"**{status_preco}**")

        # Análise detalhada
        st.markdown(f"""
        **📊 Análise Detalhada:**
        
        - **Margem Atual:** {margem_atual:.1f}%
        - **Margem Sugerida:** {margem_sugerida:.1f}%
        - **Desconto Recomendado:** {desconto:.1f}%
        - **Lucro Estimado:** R$ {(preco_sugerido - valor_compra):,.2f}
        
        **🎯 Racional da Sugestão:**
        
        O algoritmo considera que veículos com {tempo_patio} dias em pátio 
        apresentam custo de oportunidade elevado. Um ajuste de {desconto:.1f}% 
        no preço pode acelerar a venda mantendo margem saudável de {margem_sugerida:.1f}%.
        
        **📈 Comparação com Mercado:**
        
        - Preço atual está {((preco_atual/valor_fipe - 1) * 100):.1f}% em relação ao Fipe
        - Preço sugerido ficaria {((preco_sugerido/valor_fipe - 1) * 100):.1f}% em relação ao Fipe
        """)

        # Gráfico de comparação
        fig = go.Figure()

        categorias = ['Valor Compra', 'Preço Atual',
                      'Preço Sugerido', 'Valor Fipe']
        valores = [valor_compra, preco_atual, preco_sugerido, valor_fipe]
        cores = ['lightblue', 'orange', 'lightgreen', 'gray']

        fig.add_trace(go.Bar(
            x=categorias,
            y=valores,
            marker_color=cores,
            text=[f'R$ {v:,.0f}' for v in valores],
            textposition='outside'
        ))

        fig.update_layout(
            height=300,
            showlegend=False,
            yaxis_title="Valor (R$)"
        )

        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PÁGINA 6: ANÁLISE DE CLIENTES
# ============================================================================

elif pagina == "👥 Análise de Clientes":

    st.markdown('<div class="main-header">👥 Análise de Base de Clientes</div>',
                unsafe_allow_html=True)

    # KPIs de clientes
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Total Clientes", len(df_clientes))
    with col2:
        st.metric("💰 Renda Média",
                  f"R$ {df_clientes['renda_mensal'].mean():,.0f}")
    with col3:
        st.metric("🎂 Idade Média", f"{df_clientes['idade'].mean():.0f} anos")
    with col4:
        compradores = len(df_clientes[df_clientes['ja_comprou_antes'] == True])
        st.metric("🔄 Já Compraram",
                  f"{compradores} ({compradores/len(df_clientes)*100:.0f}%)")

    st.markdown("---")

    # Visualizações
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Distribuição por Segmento")

        segmentos = df_clientes['segmento'].value_counts()

        fig = px.pie(
            values=segmentos.values,
            names=segmentos.index,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=350)

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("💰 Distribuição de Renda")

        fig = px.histogram(
            df_clientes,
            x='renda_mensal',
            nbins=30,
            color='segmento',
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_layout(
            height=350,
            xaxis_title="Renda Mensal (R$)",
            yaxis_title="Quantidade"
        )

        st.plotly_chart(fig, use_container_width=True)

    # Análise por categoria preferida
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Preferência por Categoria")

        pref_cat = df_clientes['preferencia_categoria'].value_counts()

        fig = go.Figure(go.Bar(
            x=pref_cat.index,
            y=pref_cat.values,
            marker_color='steelblue'
        ))

        fig.update_layout(
            height=300,
            xaxis_title="Categoria",
            yaxis_title="Clientes"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("💳 Forma de Pagamento Preferencial")

        forma_pag = df_clientes['forma_pagamento_preferencial'].value_counts()

        fig = px.pie(
            values=forma_pag.values,
            names=forma_pag.index,
            color_discrete_sequence=['#FF6B6B', '#4ECDC4']
        )

        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=300)

        st.plotly_chart(fig, use_container_width=True)

    # Insights
    st.subheader("💡 Insights Principais")

    segmento_maior = df_clientes['segmento'].value_counts().index[0]
    categoria_preferida = df_clientes['preferencia_categoria'].value_counts(
    ).index[0]
    pct_financiado = (df_clientes['forma_pagamento_preferencial']
                      == 'Financiado').sum() / len(df_clientes) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(f"""
        **🎯 Público-Alvo Principal:**
        
        Segmento **{segmento_maior}** representa a maior 
        fatia da base de clientes. Concentre campanhas 
        e estoque para este perfil.
        """)

    with col2:
        st.success(f"""
        **🚗 Categoria Mais Procurada:**
        
        Veículos da categoria **{categoria_preferida}** 
        são os mais desejados. Mantenha estoque 
        adequado desta categoria.
        """)

    with col3:
        st.warning(f"""
        **💳 Financiamento:**
        
        {pct_financiado:.0f}% dos clientes preferem 
        financiamento. Tenha parcerias bancárias 
        competitivas.
        """)

# ============================================================================
# PÁGINA 7: ALERTAS E RECOMENDAÇÕES
# ============================================================================

elif pagina == "⚠️ Alertas e Recomendações":

    st.markdown('<div class="main-header">⚠️ Central de Alertas e Recomendações</div>',
                unsafe_allow_html=True)

    # Coletar todos os alertas
    alertas_criticos = []
    alertas_atencao = []
    alertas_info = []

    # Alerta 1: Veículos críticos
    criticos = df_inventario[df_inventario['status_estoque'] == 'Crítico']
    if len(criticos) > 0:
        capital_preso = criticos['valor_compra'].sum()
        alertas_criticos.append({
            'titulo': f'🚨 {len(criticos)} veículos em situação CRÍTICA',
            'descricao': f'Capital preso: R$ {capital_preso:,.2f}. Veículos parados há mais de 90 dias.',
            'acao': 'Reduzir preços urgentemente para liquidar estoque'
        })

    # Alerta 2: Estoque baixo de best-sellers
    vendas_recentes = df_vendas[df_vendas['data_venda'] >
                                df_vendas['data_venda'].max() - timedelta(days=30)]
    top_3_vendidos = vendas_recentes['modelo'].value_counts().head(3)

    for modelo, qtd_vendida in top_3_vendidos.items():
        estoque_modelo = len(df_inventario[df_inventario['modelo'] == modelo])
        if estoque_modelo < 2:
            alertas_atencao.append({
                'titulo': f'⚡ Estoque baixo: {modelo}',
                'descricao': f'Apenas {estoque_modelo} unidade(s) em estoque. Vendeu {qtd_vendida} no último mês.',
                'acao': f'Comprar mais unidades de {modelo} para atender demanda'
            })

    # Alerta 3: Margem baixa recente
    margem_recente = vendas_recentes['margem_percentual'].mean()
    if margem_recente < 12:
        alertas_atencao.append({
            'titulo': '📉 Margem média abaixo do ideal',
            'descricao': f'Margem média recente: {margem_recente:.1f}% (meta: >15%)',
            'acao': 'Revisar estratégia de precificação e negociação de compra'
        })

    # Alerta 4: Performance por concessionária
    perf_conc = vendas_recentes.groupby('concessionaria_nome').agg({
        'venda_id': 'count'
    })

    if len(perf_conc) > 0:
        conc_mais_vendas = perf_conc['venda_id'].idxmax()
        conc_menos_vendas = perf_conc['venda_id'].idxmin()

        if perf_conc.loc[conc_mais_vendas, 'venda_id'] > perf_conc.loc[conc_menos_vendas, 'venda_id'] * 1.5:
            alertas_info.append({
                'titulo': '📊 Desempenho desigual entre concessionárias',
                'descricao': f'{conc_mais_vendas} vendendo 50% mais que {conc_menos_vendas}',
                'acao': 'Investigar fatores de sucesso e replicar boas práticas'
            })

    # Alerta 5: Sazonalidade
    mes_atual = datetime.now().month
    if mes_atual == 12:
        alertas_info.append({
            'titulo': '🎄 Dezembro: Mês de Pico de Vendas',
            'descricao': 'Historicamente o melhor mês do ano (+40% vs média)',
            'acao': 'Aumentar estoque e preparar equipe para alta demanda'
        })
    elif mes_atual == 2:
        alertas_info.append({
            'titulo': '📉 Fevereiro: Mês Fraco',
            'descricao': 'Historicamente o mês mais fraco (-30% vs média)',
            'acao': 'Planejar campanhas promocionais e liquidações'
        })

    # Exibir alertas
    st.subheader("🚨 Alertas Críticos")
    if alertas_criticos:
        for alerta in alertas_criticos:
            st.markdown(f"""
            <div class="alert-critical">
                <h4>{alerta['titulo']}</h4>
                <p>{alerta['descricao']}</p>
                <p><strong>✅ Ação recomendada:</strong> {alerta['acao']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("✅ Nenhum alerta crítico no momento!")

    st.markdown("---")

    st.subheader("⚡ Alertas de Atenção")
    if alertas_atencao:
        for alerta in alertas_atencao:
            st.markdown(f"""
            <div class="alert-warning">
                <h4>{alerta['titulo']}</h4>
                <p>{alerta['descricao']}</p>
                <p><strong>✅ Ação recomendada:</strong> {alerta['acao']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("✅ Tudo sob controle!")

    st.markdown("---")

    st.subheader("💡 Informações e Oportunidades")
    if alertas_info:
        for alerta in alertas_info:
            st.markdown(f"""
            <div class="alert-success">
                <h4>{alerta['titulo']}</h4>
                <p>{alerta['descricao']}</p>
                <p><strong>✅ Ação recomendada:</strong> {alerta['acao']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Recomendações Estratégicas
    st.markdown("---")
    st.subheader("🎯 Recomendações Estratégicas")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 📈 Aumentar Faturamento
        
        1. **Precificação Dinâmica**
           - Implementar ajustes automáticos por tempo de pátio
           - Potencial: +R$ 324k/ano
        
        2. **Otimização de Mix**
           - Focar em categorias de maior margem
           - Potencial: +R$ 180k/ano
        
        3. **Redução Tempo Pátio**
           - Meta: reduzir de 50 para 40 dias
           - Potencial: +R$ 140k/ano
        """)

    with col2:
        st.markdown("""
        ### 💰 Reduzir Custos
        
        1. **Liquidação de Críticos**
           - Vender 5 veículos críticos rapidamente
           - Economia: +R$ 39k imediato
        
        2. **Compra Inteligente**
           - Usar previsão de demanda para compras
           - Redução dead stock: -70%
        
        3. **Negociação Bancária**
           - 75% dos clientes financiam
           - Melhores taxas = mais vendas
        """)

    # ROI Estimado
    st.markdown("---")
    st.success("""
    ### 💎 ROI ESTIMADO DO SISTEMA
    
    **Ganhos Anuais Estimados:** R$ 503.000
    - Otimização de margem: +R$ 324k
    - Redução tempo pátio: +R$ 140k  
    - Redução dead stock: +R$ 39k
    
    **Investimento Sistema:** R$ 14.400/ano (R$ 1.200/mês)
    
    **ROI:** 34.9x | **Payback:** < 1 mês
    """)

# ============================================================================
# RODAPÉ
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 2rem;'>
    <p>🚗 <strong>Sistema de BI para Concessionárias v1.0</strong></p>
    <p>Powered by <strong>Viv.IA Intelligence</strong></p>
    <p>Demo desenvolvida com dados sintéticos realistas</p>
</div>
""", unsafe_allow_html=True)
