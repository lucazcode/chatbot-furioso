import streamlit as st
from flux_control import handle_input

# Função que executa a aplicação
def streamlit_interface():
    st.header("Chatbot FURIOSO", divider = True)
    st.write("### Tire suas dúvidas com o Chatbot da FURIA!")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    messages = st.session_state["messages"]

    # Armazena a mensagens do usuário
    user_message = st.chat_input("Insira sua mensagem ou 'cls' para limpar o chat)")

    # Inicializa ou recupera a lista de mensagens do usuário
    if user_message: # Se o usuário inseriu uma mensagem...
        # Limpar a lista (fins de teste)
        if user_message.lower() != "cls":
            # Adiciona na lista mensagens o texto do usuário
            messages.append({"entity": "user", "text": user_message})

            # Adiciona na lista mensagens o texto do assistente
            assistant_message = handle_input(user_message)
            messages.append({"entity": "assistant", "text": assistant_message})

            # Mostra as mensagens atuais no chat
            for message in messages:
                with st.chat_message(message["entity"]):
                    st.write(message["text"])
        else:
            st.session_state["messages"] = []

streamlit_interface()