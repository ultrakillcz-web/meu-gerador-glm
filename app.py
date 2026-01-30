import streamlit as st

# Configuração da página
st.set_page_config(page_title="GLM-4.7 Prompt Master", page_icon="🚀")

st.title("🚀 GLM-4.7 Prompt Master")

# --- LÓGICA DO PROMPT ---
def get_prompt_instructions(task_type):
    if task_type == "Web App Full-stack":
        return "Foco em arquitetura escalável, UI moderna (Tailwind), banco de dados e rotas de API seguras."
    elif task_type == "Automação de API":
        return "Foco em scripts Python eficientes, tratamento de erros, bibliotecas 'requests' ou 'selenium' e logs detalhados."
    elif task_type == "Refatoração de Código":
        return "Analise o código fornecido, identifique gargalos de performance, melhore a legibilidade e aplique Clean Code."
    elif task_type == "Dashboards de Dados":
        return "Foco em visualização de dados (bibliotecas como Plotly ou Recharts), limpeza de dados e insights visuais claros."
    return "Siga as melhores práticas."

def generate_glm_prompt(task_type, context, tech_stack, complexity):
    thinking = "Utilize o modo 'Preserved Thinking' para planejar a solução passo a passo." if complexity == "Alta (Deep Thinking)" else ""
    specific_instructions = get_prompt_instructions(task_type)
    
    prompt = f"""### SISTEMA: MODO EXPERT (GLM-4.7)
{thinking}

### PERFIL
Você é um Engenheiro de Software Sênior especializado em {task_type}.

### OBJETIVO
{context}

### INSTRUÇÕES TÉCNICAS
{specific_instructions}

### TECH STACK
{tech_stack}

### SAÍDA ESPERADA
Planejamento seguido da implementação completa do código."""
    return prompt

# --- INTERFACE REATIVA (SEM FORMULÁRIO TRAVADO) ---

with st.expander("❓ Guia Rápido (Clique para abrir)"):
    st.markdown("Selecione o tipo de projeto, preencha os dados e gere o prompt.")

# 1. Seleção (Agora fora do formulário para atualizar na hora)
task_options = {
    "Web App Full-stack": "Cria sites completos (Lojas, Sistemas). Foco em Visual + Banco de Dados.",
    "Automação de API": "Robôs que conectam sistemas. Ex: Enviar planilha para o WhatsApp.",
    "Refatoração de Código": "Limpeza. Transforma código ruim em código profissional.",
    "Dashboards de Dados": "Gráficos. Transforma dados brutos em visualizações bonitas."
}

# Ao mudar este item, o app recarrega instantaneamente
task_type = st.selectbox("1. O que vamos criar?", list(task_options.keys()))

# A explicação agora vai mudar sempre que o item acima mudar
st.info(f"💡 {task_options[task_type]}")

st.markdown("---")

# 2. Outros inputs
tech_stack = st.text_input("2. Tecnologias", "Next.js, Tailwind, TypeScript", help="Ferramentas que o robô vai usar.")

st.markdown("---")

complexity = st.radio("3. Nível de Raciocínio", ["Padrão", "Alta (Deep Thinking)"])

st.markdown("---")

context = st.text_area("4. Descreva sua ideia:", height=100, placeholder="Ex: Um robô que lê meu e-mail...")

# Botão de ação final
if st.button("Gerar Prompt Mágico ✨", type="primary"):
    st.success("Prompt Gerado! Copie abaixo:")
    final_prompt = generate_glm_prompt(task_type, context, tech_stack, complexity)
    st.code(final_prompt, language="markdown")

# FIM DO ARQUIVO
