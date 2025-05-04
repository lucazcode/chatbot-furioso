import streamlit as st
from flux_control import handle_input
import time
import re

# Carrega imagem da FURIA e do usuário
avatar_url_assistant = "https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png"
avatar_url_user = "https://conpedi.org.br/wp-content/uploads/2023/11/user-branco.png"
background_pattern = "https://cdn.dribbble.com/users/123162/screenshots/2676465/attachments/538970/gaming-pattern.png"

# Edita links para se tornarem clicáveis
def linkify(text):
    pattern = r"\[(https://www[^\]]+)\]"
    return re.sub(pattern, r'[<a href="\1" target="_blank">\1</a>]', text)

# Mostra ícones personalizados nas mensagens
def show_avatar_message(message, avatar_url, align="left", bg="#1B1035", text_color="#FFF"):
    # Remove espaços em branco extras e verifica se a mensagem é vazia
    message = message.strip()

    # Retorna uma string vazia caso a entrada seja vazia
    if not message:
        return ""

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
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{background_pattern}");
        background-size: 27.7rem;
        background-attachment: fixed;
        background-repeat: repeat;
        background-position: center;
    }}
    
    [data-testid="stHeader"] {{
        box-shadow: 0 1.7rem .8rem 0 #100520;
    }}
    
    [data-testid="stBottom"] {{
        margin-top: 1.5rem;
        box-shadow: 0 -1.2rem 1.5rem 0 #100520;
    }}
    
    .stApp {{
        background-color: transparent;
    }}
    
    .furioso-box {{
        background-color: #211939;
        border-left: 0.3125rem solid #d29f3d;
        padding: 1.25rem;
        border-radius: 0.75rem;
        margin-bottom: 1.25rem;
    }}

    .furioso-title {{
        font-size: 2rem;
        font-weight: bold;
        color: #f5f5f5;
    }}
    
    .highlight-name {{
        color: #d29f3d
    }}

    .furioso-subtitle {{
        font-size: 1.125rem;
        color: #f5f5f5;
    }}
    
    .st-emotion-cache-6shykm {{
            padding-bottom: 9.5rem;
        }}
    </style>
    """, unsafe_allow_html=True
)

# Adiciona efeito de digitação na resposta do chatbot
def simulate_typing(message, avatar_url, align="left", bg="#211939", text_color="#f5f5f5", delay=0.005):
    placeholder = st.empty()
    typed_text = ""
    for char in message:
        typed_text += char
        rendered_message = show_avatar_message(typed_text, avatar_url, align, bg, text_color)
        placeholder.markdown(rendered_message, unsafe_allow_html=True)
        time.sleep(delay)

# Executa a aplicação
def streamlit_interface():
    # Bloco estilizado
    st.markdown("""
        <div class="furioso-box">
            <div class="furioso-title">😼 <span class="highlight-name">Eaí, meu nome é FURIOSO!</span></div>
            <div class="furioso-subtitle">Vamos bater um papo sobre o time da <strong>FURIA</strong>?</div>
        </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    messages = st.session_state["messages"]

    # Armazena a mensagens do usuário
    user_message = st.chat_input("Insira sua mensagem ou 'cls' para limpar o chat")

    # Inicializa ou recupera a lista de mensagens do usuário
    if user_message:
        # Limpa a lista
        if user_message.lower() != "cls":
            # Adiciona na lista mensagens o texto do usuário
            messages.append({"entity": "user", "text": user_message})

            # Atualiza a interface com todas as mensagens até agora
            for message in st.session_state["messages"]:
                if message["entity"] == "user":
                    st.markdown(show_avatar_message(message["text"], avatar_url_user, align="right", bg="#d29f3d",
                                                    text_color="#f5f5f5"), unsafe_allow_html=True)
                else:
                    st.markdown(show_avatar_message(message["text"], avatar_url_assistant, align="left", bg="#211939",
                                                    text_color="#f5f5f5"), unsafe_allow_html=True)

            # Adiciona na lista mensagens o texto do assistente
            assistant_message = handle_input(user_message)
            messages.append({"entity": "assistant", "text": assistant_message})

            # Re-renderiza a mensagem do assistente
            simulate_typing(assistant_message, avatar_url_assistant, align="left", bg="#211939", text_color="#f5f5f5")
        else:
            st.session_state["messages"] = []

streamlit_interface()