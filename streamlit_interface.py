import streamlit as st
from flux_control import handle_input
import re

# Carrega imagem da FURIA
avatar_url_assistant = "https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png"
avatar_url_user = "https://cdn-icons-png.flaticon.com/512/9742/9742847.png"

# Edita links para se tornarem clicáveis
def linkify(text):
    pattern = r"\[(https://www\.hltv\.org[^\]]+)\]"
    return re.sub(pattern, r'[<a href="\1" target="_blank">\1</a>]', text)

# Mostra ícones personalizados nas mensagens
def show_avatar_message(message, avatar_url, align="left", bg="#1B1035", text_color="#FFF"):
    alignment = "flex-start" if align == "left" else "flex-end"
    message = message.replace('\n', '<br>')
    message = linkify(message)
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

# Customização do tema do chatbot
st.markdown(
    """
    <style>

    .stApp {
        background-color: #010202;
    }

    </style>
    """, unsafe_allow_html=True
)

# Executa a aplicação
def streamlit_interface():

    st.header("😼 Oi, meu nome é FURIOSO!")
    st.write("### Vamos bater um papo sobre o time da FURIA?")

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

            # Atualiza a interface com todas as mensagens até agora
            for message in st.session_state["messages"]:
                if message["entity"] == "user":
                    st.markdown(show_avatar_message(message["text"], avatar_url_user, align="right", bg="#9B870C",
                                                    text_color="#f5f5f5"), unsafe_allow_html=True)
                else:
                    st.markdown(show_avatar_message(message["text"], avatar_url_assistant, align="left", bg="#211939",
                                                    text_color="#f5f5f5"), unsafe_allow_html=True)

            # Adiciona na lista mensagens o texto do assistente
            assistant_message = handle_input(user_message)
            messages.append({"entity": "assistant", "text": assistant_message})

            # Re-renderiza a mensagem do assistente
            st.markdown(show_avatar_message(assistant_message, avatar_url_assistant, align="left", bg="#211939",
                                            text_color="#f5f5f5"), unsafe_allow_html=True)
        else:
            st.session_state["messages"] = []

streamlit_interface()