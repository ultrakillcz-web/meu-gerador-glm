import streamlit as st
import random

# Configuração da página (Aba do navegador)
st.set_page_config(page_title="GLM Master", page_icon="/home/runner/work/meu-gerador-glm/meu-gerador-glm/icon_prompt_glm.png")

# --- 1. ESTILO VISUAL (CSS) ---
# Aqui reduzimos o tamanho do título para 50% do original e centralizamos
st.markdown("""
    <style>
    .big-font {
        font-size: 26px !important;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextArea textarea {
        font-size: 16px !important;
    }
    </style>
    <div class="big-font">💎 GLM Ultimate Master</div>
    """, unsafe_allow_html=True)

GLM_MODELS = {
    "GLM-4.5 (API - Pago)": {"requires_api": True, "tier": "paid"},
    "GLM-4.5-Air (API - Mais leve)": {"requires_api": True, "tier": "paid"},
    "GLM-4.5-Flash (API - Rápido)": {"requires_api": True, "tier": "paid"},
    "GLM-4-Plus (API)": {"requires_api": True, "tier": "paid"},
    "GLM-4-Long (API - Contexto longo)": {"requires_api": True, "tier": "paid"},
    "GLM-4V (API - Visão)": {"requires_api": True, "tier": "paid"},
    "GLM-Z1-Air (API - Reasoning)": {"requires_api": True, "tier": "paid"},
    "GLM-Z1-Flash (API - Reasoning rápido)": {"requires_api": True, "tier": "paid"},
    "GLM-4-9B-Chat (Open-source)": {"requires_api": False, "tier": "open-source"},
    "GLM-4-9B-Chat-1M (Open-source, contexto longo)": {"requires_api": False, "tier": "open-source"},
}

# --- 2. CÉREBRO DO APP (DADOS & LISTAS) ---
GLM_MODES = {
    "Full-Stack Developer 💻": {
        "desc": "Cria sites e apps. Ativa o modo 'Vibe Coding' (Visual bonito + Código limpo).",
        "instruction": "Atue como Full-Stack Agent. Use 'Artifacts'. HABILITAR: Preserved Thinking. FERRAMENTA: Code Interpreter.",
        # LISTA DE OPÇÕES PARA O MENU SUSPENSO
        "tools_list": [
            "Next.js + Tailwind + TypeScript (Padrão Moderno)",
            "React + Node.js + MongoDB (MERN Stack)",
            "Python + Streamlit (Data Apps)",
            "Python + Django + PostgreSQL (Enterprise)",
            "HTML5 + CSS3 + JavaScript (Simples/Leve)",
            "Flutter + Firebase (App Mobile)"
        ],
        "examples": [
            "Crie um sistema Kanban (tipo Trello) com drag-and-drop.",
            "SaaS de agendamento médico com notificações WhatsApp.",
            "Dashboard financeiro que importa extrato bancário (OFX).",
            "App de Delivery com geolocalização e painel admin.",
            "Landing Page animada para produto de IA (Dark Mode)."
        ]
    },
    "AI Slides / Presentation 📊": {
        "desc": "Gera apresentações. Usa o motor 'GLM Slide Agent' para criar roteiros.",
        "instruction": "Atue como Presentation Agent. Gere código para 'Zhipu Slides'. ESTRUTURA: [Capa] -> [Índice] -> [Conteúdo] -> [Script].",
        "tools_list": [
            "Estilo Corporativo / Clean",
            "Estilo Criativo / Colorido",
            "Estilo Minimalista / Preto e Branco",
            "Estilo Tech / Futurista",
            "Estilo Acadêmico / Formal"
        ],
        "examples": [
            "Pitch Deck para Startup de Energia Solar (10 slides).",
            "Aula didática sobre História da Roma Antiga.",
            "Relatório Trimestral de Marketing com KPIs.",
            "Treinamento de Vendas: Como contornar objeções."
        ]
    },
    "Magic Design / Visual 🎨": {
        "desc": "Cria imagens e UI. Ativa o modelo 'CogView-3' e 'GLM-Image'.",
        "instruction": "Atue como Visual Designer. Para imagens, use 't2i' (Text-to-Image). Para UI, gere código Tailwind/Figma concepts.",
        "tools_list": [
            "UI Design (Interface de App/Site)",
            "Fotorealismo (Estilo Midjourney)",
            "Ilustração 3D / Render",
            "Logo & Identidade Visual",
            "Pixel Art / Retrô"
        ],
        "examples": [
            "Design System completo para app de Meditação.",
            "Imagem realista de uma cidade cyberpunk chuvosa.",
            "Redesign da interface do Instagram (Acessibilidade).",
            "Logo minimalista para uma cafeteria gourmet."
        ]
    },
    "Deep Research / Pesquisa 🔍": {
        "desc": "Pesquisa profunda na web. Ativa a tool 'BrowseComp' (Navegador).",
        "instruction": "Atue como Research Scientist. OBRIGATÓRIO: Use 'web_browser' para buscar dados. CITE: Fontes verificadas.",
        "tools_list": [
            "Análise de Mercado / Tendências",
            "Comparativo Técnico de Produtos",
            "Pesquisa Acadêmica / Científica",
            "Verificação de Fatos (Fact-Checking)",
            "Notícias Financeiras / Crypto"
        ],
        "examples": [
            "Tendências de IA para 2026 e impacto no trabalho.",
            "Comparativo técnico: iPhone 16 vs Samsung S25 Ultra.",
            "Dossiê sobre regulação de criptomoedas no Brasil.",
            "Quais nichos de E-commerce mais cresceram este ano?"
        ]
    },
    "Automação & Scripts 🤖": {
        "desc": "Robôs e Scripts Python para tarefas repetitivas.",
        "instruction": "Atue como Engenheiro de Automação. Crie scripts Python robustos com logs e tratamento de erros.",
        "tools_list": [
            "Python Script (Geral)",
            "Selenium (Web Scraping/Bot)",
            "Pandas (Processamento de Excel/Dados)",
            "API Integration (Conectar Sistemas)",
            "Bash / Shell Script (Linux)"
        ],
        "examples": [
            "Monitorar preço do Bitcoin e enviar SMS se cair 5%.",
            "Organizar pasta de Downloads por tipo de arquivo.",
            "Bot que verifica andamento processual em site jurídico.",
            "Extrair tabelas de 50 PDFs para o Excel."
        ]
    }
}

# --- 3. LÓGICA DE ESTADO (SESSION STATE) ---
# Isso garante que quando você muda o menu, o exemplo muda sozinho.

if 'last_mode' not in st.session_state:
    st.session_state.last_mode = None
if 'current_example' not in st.session_state:
    st.session_state.current_example = ""

# --- 4. INTERFACE ---

# Menu Principal
selected_mode = st.selectbox("1. Qual 'Superpoder' vamos usar?", list(GLM_MODES.keys()))
mode_data = GLM_MODES[selected_mode]

selected_glm_model = st.selectbox("Modelo GLM (Pago + Open-source):", list(GLM_MODELS.keys()))
model_data = GLM_MODELS[selected_glm_model]
api_key_input = ""
if model_data["requires_api"]:
    st.warning("⚠️ Este modelo normalmente exige API key para uso direto em integrações.")
    api_key_input = st.text_input("API Key (opcional):", type="password", placeholder="Cole aqui sua chave...")
else:
    st.info("✅ Modelo open-source selecionado: não exige API key por padrão.")

# Lógica de Atualização Automática:
# Se o usuário trocou de modo, sorteamos um exemplo novo imediatamente.
if st.session_state.last_mode != selected_mode:
    st.session_state.current_example = random.choice(mode_data['examples'])
    st.session_state.last_mode = selected_mode

# Explicação com ícone de apontar
st.info(f"👉🏻 **O que faz:** {mode_data['desc']}")

st.markdown("---")

# Menu de Ferramentas (Agora é Selectbox, não Text Input)
# O label muda dinamicamente para fazer sentido (Tech Stack vs Estilo)
label_ferramentas = "2. Escolha a Tecnologia / Estilo:"
selected_tool = st.selectbox(label_ferramentas, mode_data['tools_list'])

st.markdown("---")

# Seção de Ideias
col1, col2 = st.columns([3, 2])
with col1:
    st.write("3. Descreva sua ideia:")
with col2:
    # Botão para gerar MAIS ideias
    if st.button("💡 Mais Ideias"):
        st.session_state.current_example = random.choice(mode_data['examples'])

# O campo de texto agora sempre tem valor (value), nunca fica vazio
context = st.text_area("Contexto:", value=st.session_state.current_example, height=120, label_visibility="collapsed")

st.markdown("---")

# Nível de Raciocínio
complexity = st.radio("4. Nível de Raciocínio", ["Padrão", "Alta (Deep Thinking/Reasoning)"])

# --- 5. BOTÃO FINAL ---
if st.button("Gerar Prompt Supremo 🚀", type="primary"):
    
    thinking_block = ""
    if complexity == "Alta (Deep Thinking/Reasoning)":
        thinking_block = "Utilize o modo 'Thinking/Reasoning' para planejar detalhadamente antes de executar."

    credencial_bloco = "Sem API key informada."
    if model_data["requires_api"] and api_key_input:
        credencial_bloco = "API key informada pelo usuário."
    elif model_data["requires_api"]:
        credencial_bloco = "Este modelo requer API key para integrações externas."

    prompt_final = f"""### SISTEMA: ATIVAR MODO {selected_mode.upper()} ({selected_glm_model})
{thinking_block}

### PERFIL DE ATUAÇÃO
{mode_data['instruction']}

### MODELO GLM SELECIONADO
{selected_glm_model}
Tipo: {model_data['tier']}
Credencial: {credencial_bloco}

### OBJETIVO DO USUÁRIO
{context}

### CONFIGURAÇÃO / FERRAMENTA ESCOLHIDA
{selected_tool}

### FORMATO DE SAÍDA ESPERADO
Seja extremamente detalhista. Utilize as ferramentas nativas (Browser, Code Interpreter, Canvas) conforme necessário para atingir o objetivo."""

    st.success(f"Prompt Gerado! Copie e cole no {selected_glm_model}:")
    st.code(prompt_final, language="markdown")

# FIM DO ARQUIVO
