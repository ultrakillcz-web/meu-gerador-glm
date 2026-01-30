import streamlit as st

# Configuração da página (deixa o app com cara de profissional no celular)
st.set_page_config(page_title="GLM-4.7 Prompt Master", page_icon="🚀")

st.title("🚀 GLM-4.7 Prompt Master")

# NOVO: Botão de Ajuda (Expander)
with st.expander("❓ Como utilizar e o que significam as siglas?"):
    st.markdown("""
    ### Guia Rápido:
    1. **Tipo de Projeto:** Define o objetivo. *Full-stack* significa criar o app inteiro (visual e lógica).
    2. **Stack Tecnológica:** São as ferramentas. **Next.js** e **Tailwind** são padrões modernos para sites rápidos e bonitos.
    3. **Deep Thinking:** Ativa o modo de 'raciocínio profundo' do GLM-4.7. Ideal para problemas difíceis.
    4. **Descrição:** Diga o que o app faz. Ex: 'Um app de lista de compras'.
    
    **O que fazer com o resultado?**
    Copie o texto gerado e cole no [chat.z.ai](https://chat.z.ai).
    """)

def generate_glm_prompt(task_type, context, tech_stack, complexity):
    thinking = "Utilize o modo 'Preserved Thinking' para analisar o projeto." if complexity == "Alta (Deep Thinking)" else ""
    return f"""### SISTEMA: MODO FULL-STACK EXPERT (GLM-4.7)\n{thinking}\n\n### OBJETIVO\n{context}\n\n### TECH STACK\n{tech_stack}\n\n### TAREFA\nTipo: {task_type}\nImplemente a arquitetura completa."""

with st.form("prompt_form"):
    task_type = st.selectbox("Tipo de Projeto", ["Web App Full-stack", "Automação de API", "Refatoração de Código"], help="Selecione o que deseja criar.")
    tech_stack = st.text_input("Stack Tecnológica", "Next.js, Tailwind, TypeScript", help="Linguagens que o robô vai usar.")
    complexity = st.radio("Nível de Raciocínio", ["Padrão", "Alta (Deep Thinking)"])
    context = st.text_area("Descreva o que o app deve fazer:")
    
    submitted = st.form_submit_button("Gerar Prompt")

if submitted:
    st.subheader("Seu Prompt Pronto:")
    st.code(generate_glm_prompt(task_type, context, tech_stack, complexity), language="markdown")
