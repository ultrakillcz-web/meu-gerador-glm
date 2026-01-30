import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="GLM-4.7 Ultimate Master", page_icon="💎")

st.title("💎 GLM-4.7 Ultimate Master")

# --- 1. CÉREBRO DO APP (GLM_MODES) ---
# Aqui estão as instruções técnicas PRO que ativam as ferramentas secretas da Zhipu AI.
GLM_MODES = {
    "Full-Stack Developer 💻": {
        "desc": "Cria sites e apps. Ativa o modo 'Vibe Coding' (Visual bonito + Código limpo).",
        "instruction": "Atue como Full-Stack Agent. Use 'Artifacts' para gerar código. HABILITAR: Preserved Thinking. FERRAMENTA: Code Interpreter para scripts complexos.",
        "examples": [
            "Crie um sistema Kanban (tipo Trello) com React e Firebase.",
            "Desenvolva um SaaS de agendamento médico com notificações WhatsApp.",
            "Dashboard financeiro que importa extrato bancário e gera gráficos.",
            "App de Delivery com geolocalização e painel administrativo.",
            "Landing Page animada para produto de IA (foco em conversão)."
        ]
    },
    "AI Slides / Presentation 📊": {
        "desc": "Gera apresentações. Usa o motor 'GLM Slide Agent' para criar roteiros visuais.",
        "instruction": "Atue como Presentation Agent. Gere código para 'Zhipu Slides' ou Markdown estruturado. ESTRUTURA: [Capa] -> [Índice] -> [Conteúdo Visual] -> [Script do Orador].",
        "examples": [
            "Pitch Deck para Startup de Energia Solar (10 slides).",
            "Aula didática sobre História da Roma Antiga (foco visual).",
            "Relatório Trimestral de Marketing com análise de KPI.",
            "Treinamento de Vendas: Como contornar objeções."
        ]
    },
    "Magic Design / Visual 🎨": {
        "desc": "Cria imagens e UI. Ativa o modelo 'CogView-3' e 'GLM-Image'.",
        "instruction": "Atue como Visual Designer. Para imagens, use a tool 't2i' (Text-to-Image) com prompts detalhados. Para UI, gere código Tailwind/Figma concepts.",
        "examples": [
            "Design System (Cores, Tipografia) para app de Meditação.",
            "Imagens realistas de uma cidade futurista cyberpunk (Prompt DALL-E/Flux).",
            "Redesign da interface do Instagram focado em acessibilidade.",
            "Identidade visual (Logo e Paleta) para cafeteria gourmet."
        ]
    },
    "Deep Research / Pesquisa 🔍": {
        "desc": "Pesquisa profunda na web. Ativa a tool 'BrowseComp' (Navegador).",
        "instruction": "Atue como Research Scientist. OBRIGATÓRIO: Use a tool 'web_browser' para buscar dados em tempo real. CITE: Fontes com URLs verificadas e faça análise crítica.",
        "examples": [
            "Tendências de IA para 2026 e impacto no mercado.",
            "Comparativo técnico: iPhone 16 vs Samsung S25 Ultra (baseado em reviews).",
            "Dossiê sobre regulação de criptomoedas no Brasil.",
            "Estudo de mercado: Nichos de E-commerce em crescimento."
        ]
    },
    "Automação & Scripts 🤖": {
        "desc": "Robôs e Scripts Python para tarefas repetitivas.",
        "instruction": "Atue como Engenheiro de Automação. Crie scripts Python robustos. OBRIGATÓRIO: Tratamento de erros (try/except) e logs de execução.",
        "examples": [
            "Script que monitora Bitcoin e envia SMS se cair 5%.",
            "Automação que organiza pasta de Downloads por tipo de arquivo.",
            "Bot que verifica andamento processual em site jurídico.",
            "Extrator de dados de PDF para Excel (OCR)."
        ]
    }
}

# --- 2. INTERFACE INTELIGENTE ---

# Inicializa o sorteio vazio
if 'random_example' not in st.session_state:
    st.session_state.random_example = ""

with st.expander("❓ Guia V7.0 (Funções Completas)"):
    st.markdown("""
    **Modos Disponíveis:**
    * **Full-Stack:** Sites e Apps.
    * **AI Slides:** Apresentações e Roteiros.
    * **Magic Design:** Imagens e Interfaces.
    * **Deep Research:** Pesquisa na Web com Fontes.
    """)

# Menu Principal
selected_mode = st.selectbox("1. Qual 'Superpoder' vamos usar?", list(GLM_MODES.keys()))
mode_data = GLM_MODES[selected_mode]

# Explicação Azul
st.info(f"💡 **O que faz:** {mode_data['desc']}")

st.markdown("---")

# Ferramentas Adaptativas (O nome do campo muda conforme o modo)
label_ferramentas = "2. Stack Tecnológica (ex: Next.js)" 
help_ferramentas = "Linguagens de programação"

if "Slides" in selected_mode:
    label_ferramentas = "2. Estilo da Apresentação"
    help_ferramentas = "Ex: Corporativo, Divertido, Minimalista"
elif "Research" in selected_mode:
    label_ferramentas = "2. Foco da Pesquisa"
    help_ferramentas = "Ex: Dados técnicos, Mercado Financeiro, Acadêmico"
elif "Magic" in selected_mode:
    label_ferramentas = "2. Estilo Visual"
    help_ferramentas = "Ex: Cyberpunk, Pastel, Neobrutalism"

tools_input = st.text_input(label_ferramentas, help=help_ferramentas)

st.markdown("---")

# Botão de Sorteio e Campo de Texto
col1, col2 = st.columns([2, 1])
with col1:
    st.write("3. Descreva sua ideia (ou sorteie uma ao lado):")
with col2:
    if st.button("🎲 Sortear Ideia"):
        st.session_state.random_example = random.choice(mode_data['examples'])

context = st.text_area("Contexto:", value=st.session_state.random_example, height=120, label_visibility="collapsed")

st.markdown("---")

# Nível de Raciocínio
complexity = st.radio("4. Nível de Raciocínio", ["Padrão", "Alta (Deep Thinking/Reasoning)"])

# --- 3. GERADOR DE PROMPT ---
if st.button("Gerar Prompt Supremo 🚀", type="primary"):
    
    thinking_block = ""
    if complexity == "Alta (Deep Thinking/Reasoning)":
        thinking_block = "Utilize o modo 'Thinking/Reasoning' para planejar detalhadamente antes de executar."

    prompt_final = f"""### SISTEMA: ATIVAR MODO {selected_mode.upper()} (GLM-4.7)
{thinking_block}

### PERFIL DE ATUAÇÃO
{mode_data['instruction']}

### OBJETIVO DO USUÁRIO
{context}

### CONFIGURAÇÕES / FERRAMENTAS
{tools_input if tools_input else "Escolha as melhores ferramentas para a tarefa."}

### FORMATO DE SAÍDA ESPERADO
Seja extremamente detalhista. Utilize as ferramentas nativas (Browser, Code Interpreter, Canvas) conforme necessário."""

    st.success("Prompt Gerado! Copie e cole no GLM-4.7:")
    st.code(prompt_final, language="markdown")
