import streamlit as st
from flux_control import handle_input

# Carrega imagem da FURIA
avatar_url_assistant = "https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png"
avatar_url_user = "https://img.freepik.com/premium-vector/icon-human-icon_1076610-59590.jpg?w=740"

# Mostra ícones personalizados nas mensagens
def show_avatar_message(message, avatar_url, align="left", bg="#1B1035", text_color="#FFF"):
    alignment = "flex-start" if align == "left" else "flex-end"
    return f"""
        <div style="display:flex; justify-content:{alignment}; margin-bottom:16px;">
            <div style="display: flex; justify-content: center; align-items: center; margin-right:12px;">
                <img src="{avatar_url}" style="border-radius:10px; width:45px; height:45px; object_fit: contain">
            </div>
            <div style="background-color:{bg}; color:{text_color}; padding:12px; border-radius:10px; max-width:80%;">
                {message}
            </div>
        </div>
        """

# Executa a aplicação
def streamlit_interface():
    st.header("🤖 Chatbot FURIOSO", divider=True)
    st.write("### Tire suas dúvidas com o Chatbot da **FURIA**!")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    messages = st.session_state["messages"]

    # Armazena a mensagens do usuário
    user_message = st.chat_input("Insira sua mensagem ou 'cls' para limpar o chat)")

    # Inicializa ou recupera a lista de mensagens do usuário
    if user_message: # Se o usuário inseriu uma mensagem...
        # Limpa a lista (fins de teste)
        if user_message.lower() != "cls":
            # Adiciona na lista mensagens o texto do usuário
            messages.append({"entity": "user", "text": user_message})

            # Adiciona na lista mensagens o texto do assistente
            assistant_message = handle_input(user_message)
            messages.append({"entity": "assistant", "text": assistant_message})

            # Mostra as mensagens atuais no chat com estilização
            for message in messages:
                if message["entity"] == "assistant":
                    st.markdown(show_avatar_message(message["text"], avatar_url_assistant, align="left", bg="#211939",
                                                    text_color="#CCC"), unsafe_allow_html=True)
                else:
                    st.markdown(show_avatar_message(message["text"], avatar_url_user, align="right", bg="#010101",
                                                    text_color="#CCC"), unsafe_allow_html=True)

        else:
            st.session_state["messages"] = []

streamlit_interface()