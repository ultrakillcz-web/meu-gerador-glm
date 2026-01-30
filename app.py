import streamlit as st

# Configuração da página
st.set_page_config(page_title="GLM-4.7 Prompt Master", page_icon="🚀")

st.title("🚀 GLM-4.7 Prompt Master")

# --- LÓGICA DO PROMPT (CÉREBRO DO APP) ---
def get_prompt_instructions(task_type):
    # Aqui definimos instruções diferentes para cada tipo de tarefa
    if task_type == "Web App Full-stack":
        return "Foco em arquitetura escalável, UI moderna (Tailwind), banco de dados e rotas de API seguras."
    elif task_type == "Automação de API":
        return "Foco em scripts Python eficientes, tratamento de erros, bibliotecas 'requests' ou 'selenium' e logs detalhados."
    elif task_type == "Refatoração de Código":
        return "Analise o código fornecido, identifique gargalos de performance, melhore a legibilidade e aplique Clean Code."
    elif task_type == "Dashboards de Dados":
        return "Foco em visualização de dados (bibliotecas como Plotly ou Recharts), limpeza de dados e insights visuais claros."
    return "Siga as melhores práticas de desenvolvimento."

def generate_glm_prompt(task_type, context, tech_stack, complexity):
    thinking = "Utilize o modo 'Preserved Thinking' para planejar a solução passo a passo antes de codificar." if complexity == "Alta (Deep Thinking)" else ""
    specific_instructions = get_prompt_instructions(task_type)
    
    return f"""### SISTEMA: MODO EXPERT (GLM-4.7)
{thinking}

### PERFIL
Você é um Engenheiro de Software Sênior especializado em {task_type}.

### OBJETIVO
{context}

### INSTRUÇÕES TÉCNICAS ESPECÍFICAS
{specific_instructions}

### TECH STACK
{tech_stack}

### SAÍDA ESPERADA
Planejamento seguido da implementação completa do código."""

# --- INTERFACE (CORPO DO APP) ---

with st.expander("❓ Guia Rápido (Clique para abrir)"):
    st.markdown("Selecione o tipo de projeto abaixo para ver a explicação e gerar o prompt ideal.")

with st.form("prompt_form"):
    
    # 1. Dicionário de Opções e Descrições
    # A chave é o nome no menu, o valor é a explicação da caixa azul
    task_options = {
        "Web App Full-stack": "Cria sites completos (Lojas, Sistemas). Foco em Visual + Banco de Dados.",
        "Automação de API": "Robôs que conectam sistemas. Ex: Enviar planilha para o WhatsApp.",
        "Refatoração de Código": "Limpeza e otimização. Transforma código ruim em código profissional.",
        "Dashboards de Dados": "Gráficos e Relatórios. Transforma dados brutos em visualizações bonitas."
    }
    
    # O selectbox mostra as chaves (nomes)
    task_type = st.selectbox("1. O que vamos criar?", list(task_options.keys()))
    
    # A caixa azul mostra o valor correspondente à chave selecionada
    st.info(f"💡 {task_options[task_type]}")

    st.markdown("---")
    
    # 2. Tech Stack (Sugestão muda conforme a escolha? Podemos deixar fixo por enquanto para simplificar)
    tech_stack = st.text_input("2. Tecnologias", "Next.js, Tailwind, TypeScript", help="Ferramentas que o robô vai usar.")

    st.markdown("---")
    
    # 3. Nível
    complexity = st.radio("3. Nível de Raciocínio", ["Padrão", "Alta (Deep Thinking)"])

    st.markdown("---")
    
    # 4. Contexto
    context = st.text_area("4. Descreva sua ideia:", height=100, placeholder="Ex: Um robô que lê meu e-mail e salva os anexos no Drive...")
    
    submitted = st.form_submit_button("Gerar Prompt ✨")

if submitted:
    st.success("Prompt Gerado! Copie abaixo:")
    # Chama a função que agora é inteligente e muda o texto baseada na escolha
    final_prompt = generate_glm_prompt(task_type, context, tech_stack, complexity)
    st.code(final_prompt, language="markdown")
