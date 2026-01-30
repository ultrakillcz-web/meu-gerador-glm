import streamlit as st

def generate_glm_prompt(task_type, context, tech_stack, complexity):
    thinking_instruction = ""
    if complexity == "Alta (Deep Thinking)":
        thinking_instruction = "Utilize o modo 'Preserved Thinking' para decompor esta tarefa em sub-etapas lógicas antes de escrever qualquer código."
    
    prompt = f"""
### SISTEMA: MODO FULL-STACK EXPERT (GLM-4.7)
Você é um Engenheiro de Software Full-stack Senior especializado em GLM-4.7 Agentic Workflows.
{thinking_instruction}

### OBJETIVO
{context}

### TECH STACK OBRIGATÓRIA
{tech_stack}

### DIRETRIZES DE EXECUÇÃO (VIBE CODING)
1. UI/UX: Utilize Tailwind CSS e priorize uma estética moderna e minimalista.
2. ESTRUTURA: Gere um boilerplate completo, incluindo configurações de backend e integração de banco de dados se necessário.
3. QUALIDADE: O código deve ser 'production-ready', com tratamento de erros e tipagem estrita.
4. AGENTIC: Se precisar de ferramentas externas, descreva o plano de ação antes da execução.

### TAREFA ESPECÍFICA
Tipo de Tarefa: {task_type}
Por favor, forneça o plano de arquitetura seguido pela implementação completa dos arquivos.
"""
    return prompt

# Interface Streamlit
st.set_page_config(page_title="GLM-4.7 Prompt Generator", page_icon="🚀")
st.title("🚀 GLM-4.7 Prompt Generator")
st.markdown("Gerador de prompts otimizados para a função Full-stack do novo GLM-4.7.")

with st.form("prompt_form"):
    task_type = st.selectbox("Tipo de Projeto", ["Web App Full-stack", "Automação de API", "Refatoração de Código", "Dashboards de Dados"])
    tech_stack = st.text_input("Stack Tecnológica (ex: Next.js, FastAPI, Supabase, Tailwind)", "Next.js, Tailwind, TypeScript")
    complexity = st.radio("Nível de Raciocínio", ["Padrão", "Alta (Deep Thinking)"])
    context = st.text_area("Descreva o que o app deve fazer:", "Crie um sistema de gerenciamento de tarefas com autenticação e drag-and-drop.")
    
    submitted = st.form_submit_button("Gerar Prompt")

if submitted:
    final_prompt = generate_glm_prompt(task_type, context, tech_stack, complexity)
    st.subheader("Seu Prompt para o GLM-4.7:")
    st.code(final_prompt, language="markdown")
    st.info("💡 Dica: No chat.z.ai, certifique-se de que o modelo GLM-4.7 está selecionado para melhores resultados com este prompt.")
