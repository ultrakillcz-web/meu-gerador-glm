import streamlit as st

# Configuração da página
st.set_page_config(page_title="GLM-4.7 Prompt Master", page_icon="🚀")

st.title("🚀 GLM-4.7 Prompt Master")

# Seção de Ajuda Geral
with st.expander("❓ Guia para Iniciantes (Clique aqui)"):
    st.markdown("""
    **Como usar este app:**
    1. Escolha o **Tipo de Projeto** (veja a explicação azul na tela).
    2. Defina a **Tecnologia** (se não souber, mantenha o padrão).
    3. Escreva sua ideia e clique em **Gerar Prompt**.
    4. Copie o código e cole no Chat da Zhipu AI.
    """)

def generate_glm_prompt(task_type, context, tech_stack, complexity):
    thinking = "Utilize o modo 'Preserved Thinking' para decompor esta tarefa passo a passo." if complexity == "Alta (Deep Thinking)" else ""
    return f"""### SISTEMA: MODO FULL-STACK EXPERT (GLM-4.7)\n{thinking}\n\n### OBJETIVO\n{context}\n\n### TECH STACK\n{tech_stack}\n\n### TAREFA\nTipo: {task_type}\nPriorize arquitetura limpa e UI moderna (Vibe Coding)."""

with st.form("prompt_form"):
    # 1. Seleção do Tipo de Projeto
    task_options = {
        "Web App Full-stack": "Cria um sistema completo: O visual (Site) + O cérebro (Servidor/Banco de Dados). Ex: Lojas, Redes Sociais.",
        "Automação de API": "Cria pontes entre apps. Ex: 'Quando alguém preencher o Google Forms, me avise no Telegram'.",
        "Refatoração de Código": "Limpeza. Você cola um código ruim/lento e o robô devolve um código profissional e rápido.",
        "Dashboards de Dados": "Visualização. Transforma planilhas chatas em gráficos interativos e bonitos."
    }
    task_type = st.selectbox("1. O que vamos criar?", list(task_options.keys()))
    
    # Mostra a explicação dinâmica do item selecionado
    st.info(f"💡 **Explicação:** {task_options[task_type]}")

    # 2. Tech Stack
    st.markdown("---") 
    tech_stack = st.text_input(
        "2. Quais ferramentas usar? (Tech Stack)", 
        "Next.js, Tailwind, TypeScript",
        help="Next.js (Site Rápido), Tailwind (Visual Bonito), TypeScript (Segurança). Se não souber, não mude."
    )

    # 3. Nível de Raciocínio
    st.markdown("---")
    complexity = st.radio(
        "3. Nível de Inteligência do Robô", 
        ["Padrão", "Alta (Deep Thinking)"],
        captions=["Respostas rápidas para coisas simples.", "O robô 'pensa' antes de responder. Ideal para projetos grandes."]
    )

    # 4. Descrição
    st.markdown("---")
    context = st.text_area("4. Descreva sua ideia:", placeholder="Ex: Um app para controlar minhas despesas mensais com gráficos...")
    
    submitted = st.form_submit_button("Gerar Prompt Mágico ✨")

if submitted:
    st.success("Prompt gerado com sucesso! Copie abaixo:")
    st.code(generate_glm_prompt(task_type, context, tech_stack, complexity), language="markdown")
