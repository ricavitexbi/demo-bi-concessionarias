# ✅ CHECKLIST PRÉ-APRESENTAÇÃO - Demo BI Concessionárias

Use este checklist para garantir que tudo está pronto antes de apresentar a demo aos clientes.

## 🔧 Verificações Técnicas

### Antes da Apresentação (24h antes)

- [ ] **Sistema Operacional**
  - [ ] Sistema atualizado
  - [ ] Reiniciou o computador recentemente
  - [ ] Espaço em disco suficiente (>5GB)

- [ ] **Python e Dependências**
  ```bash
  python3 --version  # Deve ser 3.8+
  pip list | grep streamlit  # Verificar instalação
  ```
  - [ ] Python 3.8+ instalado
  - [ ] Streamlit instalado
  - [ ] Pandas instalado
  - [ ] Plotly instalado
  - [ ] Todas as outras dependências OK

- [ ] **Arquivo de Dados**
  ```bash
  ls -la /mnt/project/dados_concessionaria.xlsx
  ```
  - [ ] Arquivo existe
  - [ ] Tamanho correto (~186KB)
  - [ ] Permissões de leitura OK

- [ ] **Teste de Execução**
  ```bash
  streamlit run demo_concessionaria.py
  ```
  - [ ] Demo inicia sem erros
  - [ ] Todas as páginas carregam
  - [ ] Gráficos aparecem corretamente
  - [ ] Sem mensagens de erro no console

### No Dia da Apresentação (1h antes)

- [ ] **Ambiente**
  - [ ] Fechar outros programas pesados
  - [ ] Limpar cache do navegador
  - [ ] Testar conexão com internet (se remoto)
  - [ ] Configurar modo "não perturbe"

- [ ] **Demo**
  - [ ] Executar demo completa uma vez
  - [ ] Testar todas as funcionalidades
  - [ ] Verificar que dados estão atualizados
  - [ ] Preparar exemplos de perguntas para Viv.IA

- [ ] **Apresentação**
  - [ ] Slides de abertura prontos (se houver)
  - [ ] Roteiro de apresentação revisado
  - [ ] Cenários de demonstração preparados
  - [ ] Perguntas frequentes revisadas

---

## 📋 Roteiro de Apresentação Recomendado

### Abertura (2 minutos)
- [ ] Apresentação pessoal
- [ ] Contexto: "Por que BI é importante para concessionárias?"
- [ ] Objetivo: "Demonstrar como a tecnologia pode aumentar lucro em 30%+"

### Demonstração (15-20 minutos)

#### 1. Dashboard Principal (3 min)
- [ ] Abrir página "Dashboard Principal"
- [ ] Destacar KPIs principais
- [ ] "Em um único lugar, veja toda a saúde do negócio"
- [ ] Interagir com gráficos (zoom, hover)

#### 2. Assistente Viv.IA (4 min)
- [ ] Abrir "Assistente Viv.IA"
- [ ] Demonstrar 3 perguntas:
  - [ ] "Quantos veículos tenho em estoque?"
  - [ ] "Quais foram os mais vendidos?"
  - [ ] "Tenho algum alerta importante?"
- [ ] Destacar: "Natural como conversar com seu time"

#### 3. Previsão de Demanda (3 min)
- [ ] Abrir "Previsão de Demanda"
- [ ] Mostrar gráfico de previsão
- [ ] Explicar acurácia (94%)
- [ ] "Compre o que vai vender, não o que acha que vai vender"

#### 4. Precificação Inteligente (3 min)
- [ ] Abrir "Precificação Inteligente"
- [ ] Selecionar veículo crítico (>90 dias)
- [ ] Mostrar sugestão de desconto
- [ ] "Venda rápido mantendo margem saudável"

#### 5. Alertas (2 min)
- [ ] Abrir "Alertas e Recomendações"
- [ ] Mostrar alertas críticos
- [ ] Destacar ROI: 34.9x
- [ ] "Sistema paga por si mesmo em menos de 1 mês"

### Fechamento (3 minutos)
- [ ] Recapitular benefícios principais
- [ ] Apresentar próximos passos
- [ ] Abrir para perguntas
- [ ] Agendar reunião de implementação

---

## 💡 Frases de Impacto Preparadas

### Abertura
> "E se você pudesse prever exatamente quais carros comprar, quando baixar o preço, e quais clientes abordar? Hoje vou mostrar que isso é possível."

### Dashboard
> "Tudo que você precisa saber sobre seu negócio em uma tela. Sem planilhas, sem reuniões intermináveis."

### Viv.IA
> "Imagine ter um analista disponível 24/7 que conhece cada detalhe do seu estoque. É isso que a Viv.IA faz."

### Previsão
> "94% de acurácia nas previsões. Melhor que a maioria dos 'especialistas' do mercado."

### Precificação
> "Para cada veículo, o sistema calcula o preço ótimo: máxima margem + mínimo tempo de pátio."

### ROI
> "R$ 503 mil de ganho anual. R$ 14 mil de investimento. ROI de 35x. Payback em 3 semanas."

---

## 🎯 Cenários de Demonstração Específicos

### Cenário 1: "Tenho Veículos Parados"
```
Cliente: "Tenho 5 carros parados há mais de 3 meses"

Fluxo na Demo:
1. Alertas → Mostrar identificação automática
2. Estoque → Filtrar por "Crítico"
3. Precificação → Mostrar sugestão de desconto
4. ROI → Calcular quanto está perdendo

Frase de fechamento:
"O sistema não só identifica o problema, como sugere a solução exata para cada veículo."
```

### Cenário 2: "Compro os Carros Errados"
```
Cliente: "Sempre compro carros que ficam no pátio"

Fluxo na Demo:
1. Previsão → Mostrar demanda prevista por categoria
2. Estoque → Comparar com estoque atual
3. Viv.IA → "Quais modelos devo comprar?"

Frase de fechamento:
"Compre baseado em dados, não em intuição. O sistema prevê com 94% de acurácia."
```

### Cenário 3: "Margem Está Baixa"
```
Cliente: "Minha margem vem caindo"

Fluxo na Demo:
1. Dashboard → Mostrar margem atual vs meta
2. Precificação → Demonstrar algoritmo dinâmico
3. Alertas → Identificar oportunidades

Frase de fechamento:
"Aumentar 2% na margem = R$ 324 mil/ano. O sistema encontra essas oportunidades automaticamente."
```

### Cenário 4: "Gestão de Múltiplas Lojas"
```
Cliente: "Tenho 3 lojas, é difícil acompanhar tudo"

Fluxo na Demo:
1. Dashboard → Filtrar por concessionária
2. Comparar performance
3. Viv.IA → Perguntas sobre cada loja
4. Alertas → Específicos por unidade

Frase de fechamento:
"Um dashboard para todas as lojas. Veja quem está performando e por quê."
```

---

## ❓ Perguntas Frequentes - Respostas Preparadas

### "Quanto custa?"
**Resposta:** "R$ 1.200/mês. Com ROI de 35x, o sistema paga por si mesmo em menos de 1 mês. Primeira implementação inclusa."

### "Quanto tempo leva para implementar?"
**Resposta:** "2 semanas para integração básica. 1 mês para integração completa com seus sistemas. Treinamento incluído."

### "Funciona com meu sistema atual?"
**Resposta:** "Sim! Integramos com qualquer DMS. Também podemos importar planilhas Excel. A integração é nosso problema, não o seu."

### "E se eu não tiver dados históricos?"
**Resposta:** "Começamos com previsões básicas e o sistema aprende com o tempo. Em 3 meses, já teremos previsões precisas."

### "Preciso contratar alguém para operar?"
**Resposta:** "Não! A interface foi desenhada para ser intuitiva. Seu time atual opera após 2 dias de treinamento."

### "E se eu tiver dúvidas depois?"
**Resposta:** "Suporte incluído no plano. Chat, telefone e vídeo. Respondemos em até 2 horas durante horário comercial."

### "Posso testar antes de comprar?"
**Resposta:** "Sim! 30 dias grátis com seus dados reais. Sem compromisso, sem cartão de crédito."

### "Funciona em celular?"
**Resposta:** "Sim! 100% responsivo. Dashboard no desktop, alertas no celular, relatórios onde você estiver."

---

## 🚨 Plano B - Se Algo Der Errado

### Demo Não Inicia
**Solução:**
1. Usar vídeo pré-gravado da demo
2. Ou mostrar slides com screenshots
3. Ou agendar nova demo online

### Internet Cai (Apresentação Remota)
**Solução:**
1. Gravar tela antecipadamente
2. Ter slides backup
3. Continuar por telefone narrando slides

### Gráfico Não Carrega
**Solução:**
1. F5 (atualizar página)
2. Mostrar outra página enquanto isso
3. Voltar depois

### Erro ao Filtrar
**Solução:**
1. Resetar filtros
2. Navegar para outra página e voltar
3. Explicar que é demo, na produção é estável

---

## 📊 Dados Memorizados (para falar de cabeça)

Memorize estes números para parecer expert:

- **600** clientes cadastrados
- **375** vendas em 24 meses
- **60** veículos em estoque
- **R$ 31.6M** receita total (histórico)
- **R$ 4.4M** lucro total
- **16.4%** margem média atual
- **R$ 84.3k** ticket médio
- **51 dias** tempo médio em pátio
- **5** veículos críticos (>90 dias)
- **94%** acurácia do modelo de previsão
- **35x** ROI do sistema
- **<1 mês** payback
- **R$ 503k** ganho anual estimado

---

## 🎬 Checklist Final (5 min antes)

- [ ] Demo rodando e testada
- [ ] Navegador em tela cheia (F11)
- [ ] Zoom do navegador em 100%
- [ ] Outras abas fechadas
- [ ] Celular em silencioso
- [ ] Água por perto
- [ ] Contato do cliente confirmado
- [ ] Backup da apresentação pronto
- [ ] Proposta comercial impressa/PDF
- [ ] Cartão de visitas separado
- [ ] Calendário aberto para agendar próximos passos

---

## 🎯 Após a Apresentação

### Imediatamente Após
- [ ] Agradecer o tempo
- [ ] Perguntar impressões
- [ ] Identificar objeções
- [ ] Agendar próximo passo (teste piloto, proposta, etc)

### Até 2 Horas Depois
- [ ] Enviar email agradecendo
- [ ] Anexar material de apoio
- [ ] Incluir link para vídeo da demo
- [ ] Propor data para follow-up

### Até 24 Horas Depois
- [ ] Enviar proposta formal
- [ ] Incluir ROI específico para o cliente
- [ ] Adicionar depoimentos de outros clientes
- [ ] Agendar reunião para discutir proposta

---

## 💪 Mensagem de Confiança

> Você está demonstrando uma solução real, testada, que gera valor mensurável.
> 
> Os dados são realistas. A tecnologia funciona. O ROI é comprovável.
> 
> Você não está vendendo uma promessa. Está oferecendo uma ferramenta que já funciona.
> 
> Confie na demo. Confie nos números. Confie em você.
> 
> Boa apresentação! 🚀

---

**Última atualização:** Antes de cada apresentação  
**Próxima revisão:** Após cada apresentação (incorporar aprendizados)
