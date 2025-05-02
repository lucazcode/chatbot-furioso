import random
from unidecode import unidecode
import datetime

# Ano atual para respostas personalizadas
data_atual = datetime.datetime.now()
ano_atual = data_atual.year

# Dicionário de palavras-chave com respostas associadas
keywords_responses = {
    'jogos': {
        "jogo": "O próximo jogo da FURIA promete! Preparados para ver a FURIA arrebentar mais uma vez?",
        "partida": "Essa partida da FURIA vai ser épica, pode ter certeza! Vamos pra vitória!",
        "jogam": "Quando a FURIA joga, o coração da torcida bate mais forte! Fique ligado!",
        "proximo jogo": "O próximo jogo da FURIA está chegando! Já estamos ansiosos para mais uma vitória!",
        "quando jogam": "A FURIA joga em breve! Prepare-se para vibrar a cada round!",
        "agenda": "Confere a agenda da FURIA! Tem jogo chegando e a torcida vai à loucura!",
        "horario do jogo": "Fique ligado no horário do jogo da FURIA! Não podemos perder esse espetáculo!",
        "quem enfrentam": "O próximo adversário da FURIA vai sentir a pressão! Estamos prontos pra mais uma vitória!",
        "adversario": "A FURIA está pronta pra enfrentar qualquer adversário! Vem mais uma vitória!",
        "proximo adversario": "O próximo adversário da FURIA vai ver o que é ser superado por um time de elite!",
        "match": "Match da FURIA? Só pode ser vitória! Estamos no caminho certo!",
        "calendar": "Olha a agenda da FURIA! Vai ter jogo, vai ter show!",
        "fixtures": "Confira os fixtures da FURIA, a gente vai dominar tudo!",
        "round": "Cada round que a FURIA entra é uma chance de brilhar! Vamos pra vitória!"
    },
    'times': {
        "time": "A FURIA é o time mais forte do cenário! Ninguém consegue parar essa equipe!",
        "equipe": "A equipe da FURIA está mais unida e preparada do que nunca! Vamos pra vitória!",
        "lineup": "O lineup da FURIA está recheado de estrelas! Vai ser difícil parar essa galera!",
        "elenco": "O elenco da FURIA é top! Não tem time que bata de frente com a gente!",
        "jogadores": "Os jogadores da FURIA são imbatíveis, estão jogando demais!",
        "squad": "O squad da FURIA vai atropelar qualquer um no caminho!",
        "composicao": "A composição da FURIA está afiada! É só vitória pra gente!",
        "mudanca de time": "Mudança de time? FURIA sempre se adapta e sai mais forte!",
        "transferencia": "Com essa transferência, a FURIA vai ficar ainda mais imbatível!",
        "team": "O time da FURIA está arrasando, cada vez mais forte!",
        "roster": "O roster da FURIA é só craque! Estamos prontos pra vencer tudo!",
        "substituicao": "Substituição na FURIA? A equipe é forte de qualquer jeito!",
        "novato": "Os novatos da FURIA estão arrasando! O futuro do time é promissor!",
        "coach": "O coach da FURIA sabe exatamente o que fazer! Vitória atrás de vitória!",
        "tecnico": "O técnico da FURIA é uma lenda, sempre preparado para a vitória!",
        "treinador": "Com esse treinador, a FURIA nunca para de crescer! Estamos dominando!"
    },
    'torneios': {
        "campeonato": "A FURIA no campeonato é sinônimo de vitória! Vamos mostrar como se faz!",
        "torneio": "Quando a FURIA entra em um torneio, já sabe, é só vitória!",
        "liga": "A FURIA vai arrasar na liga! Nenhum time consegue nos parar!",
        "major": "A FURIA no Major é pura emoção! Estamos prontos para conquistar o título!",
        "qualifier": "Os qualificatórios? FURIA é só atropelo, vamos garantir nossa vaga!",
        "eliminatoria": "Nas eliminatórias, a FURIA brilha ainda mais! Vamos passar por cima de todos!",
        "competicao": "Em qualquer competição, a FURIA é favorita! A vitória é nossa!",
        "evento": "O evento da FURIA vai ser histórico, já pode esperar pelo show!",
        "final": "A FURIA vai pra final, com certeza! Vamos buscar mais um troféu!",
        "semi-final": "FURIA chegando nas semifinais! Vai ser difícil nos parar!",
        "playoffs": "Nos playoffs, a FURIA vai deixar todo mundo para trás!",
        "fase de grupos": "Na fase de grupos, a FURIA já está dominando! Só vitória!",
        "bracket": "O bracket da FURIA está recheado de vitórias, vem mais uma!",
        "classificacao": "A FURIA está na classificação, pronto para avançar mais uma vez!",
        "ranking": "O ranking está vendo a FURIA subir! Estamos no topo!"
    },
    'cenario': {
        "cenario": "O cenário está quente, e a FURIA não para de brilhar!",
        "csgo": "A FURIA sempre foi uma lenda no CS:GO, e no CS2, estamos dominando também!",
        "cs2": "O CS2 chegou e a FURIA está arrasando! Vamos continuar no topo!",
        "atualizacao": "Com cada atualização, a FURIA fica mais forte!",
        "meta": "A FURIA sempre está na vanguarda do meta! Não tem pra ninguém!",
        "mudanca de meta": "A mudança de meta é só uma oportunidade para a FURIA brilhar ainda mais!",
        "mudanca no csgo": "Mudança no CS:GO? A FURIA sempre se adapta e vence!",
        "cenario atual": "O cenário atual não assusta a FURIA, estamos dominando tudo!",
        "ranking mundial": "A FURIA está no topo do ranking mundial! Estamos prontos para mais vitórias!",
        "hltv ranking": "O HLTV ranking vê a FURIA crescer cada vez mais! Vamos para o topo!",
        "ranking csgo": "No ranking do CS:GO, a FURIA é imbatível!",
        "patch notes": "Cada patch só faz a FURIA ficar ainda mais forte!",
        "update": "Cada atualização só melhora o desempenho da FURIA!",
        "balanco": "A FURIA está no auge, todo o cenário está vendo nossa força!",
        "mudancas": "Mudanças no cenário? A FURIA vai se adaptar e dominar!",
        "rival": "Nosso rival? Só se for no papo, porque no jogo, a FURIA sempre dá show!",
        "rivais": "Nossos rivais? Só se for no papo, porque no jogo, a FURIA sempre dá show!"
    },
    'resultados': {
        "resultado": "O resultado da FURIA não poderia ser diferente: vitória!",
        "score": "O score da FURIA é impressionante, vitória atrás de vitória!",
        "placar": "O placar nunca mente, a FURIA venceu novamente!",
        "quantos rounds": "Em quantos rounds a FURIA venceu? A resposta é sempre: rápido e forte!",
        "ganhou": "A FURIA ganhou mais uma, como sempre! Vitória atrás de vitória!",
        "perdeu": "Perdeu? Não conhecemos essa palavra aqui na FURIA!",
        "quem venceu": "Quem venceu? Claro que foi a FURIA! Vamos sempre brilhar!",
        "desempenho": "O desempenho da FURIA é impecável! Cada jogo é uma vitória!",
        "estatisticas": "As estatísticas mostram: FURIA sempre no topo!",
        "kda": "KDA da FURIA? Impecável, sempre superior aos adversários!",
        "rating": "O rating da FURIA é sempre top! Não tem pra ninguém!",
        "mvp": "O MVP da FURIA é um monstro! Não tem quem segure esse time!",
        "melhor jogador": "Quem é o melhor jogador? FURIA sempre no topo com seus craques!",
        "top fragger": "O top fragger da FURIA sempre arrasa! Só vitórias para a nossa equipe!",
        "frag lider": "A FURIA lidera em frags, não tem como competir com essa equipe!"
    },
    'historico': {
        "historico": "O histórico da FURIA é recheado de vitórias! Sempre arrasando!",
        "ultimos jogos": "Nos últimos jogos, a FURIA só deu show! Vitória atrás de vitória!",
        "retrospecto": "O retrospecto da FURIA é perfeito, o time não para de crescer!",
        "ultimas partidas": "As últimas partidas da FURIA mostram o que é ser imbatível!",
        "ultimos resultados": "Os últimos resultados mostram: FURIA sempre dominando!",
        "estatisticas passadas": "As estatísticas passadas são só mais uma prova da força da FURIA!",
        "ultimos confrontos": "Nos últimos confrontos, a FURIA só deu vitórias!",
        "head-to-head": "O head-to-head mostra a FURIA sempre na frente!"
    },
    'curiosidades': {
        "brasil": "Você sabia que a FURIA foi a primeira equipe brasileira a disputar as semifinais da IEM Katowice, um dos torneios mais prestigiados do mundo?",
        "recorde": "Em 2020, a FURIA alcançou o 3º lugar no ranking mundial da HLTV — o mais alto já conquistado por uma equipe brasileira desde a era SK/LG!",
        "superacao": "A FURIA nasceu em 2017 com poucos recursos, e em menos de 3 anos já estava entre os melhores do mundo. Superação é o que não falta!",
        "conquista": "A FURIA foi campeã da Elisa Masters Espoo 2023, vencendo a Apeks na final e mostrando sua força no cenário europeu!",
        "estrelas": "Jogadores como KSCERATO e yuurih são considerados entre os melhores do mundo, figurando em rankings da HLTV em diversos anos.",
        "momentos marcantes": "O Major do Rio em 2022 foi inesquecível: a FURIA foi a única equipe brasileira a chegar aos playoffs, jogando com a torcida enlouquecida no Jeunesse Arena!",
        "eua": "A FURIA foi uma das primeiras organizações brasileiras a estabelecer uma base fixa nos EUA, investindo pesado em estrutura e preparação.",
        "ceo": "A FURIA é liderada por dois co-CEOs: Jaime Pádua, especialista em gestão e negócios, e André Akkari, campeão mundial de pôquer e referência no eSports!",
        "sede": "A FURIA tem sedes em São Paulo e nos Estados Unidos, com estrutura profissional em Miami e Los Angeles! Isso permite que o time treine e dispute campeonatos internacionais com qualidade de ponta!"
    },
    'jogadores especificos': {
        "art": "O ART é o verdadeiro capitão! Com ele no comando, a FURIA vai longe!",
        "yuurih": "Yuurih é um monstro! Cada partida é uma exibição de talento!",
        "kscerato": "Kscerato é sempre decisivo! Esse cara é puro talento!",
        "fallen": "O Fallen sempre joga com maestria! Lenda do CS, não tem como parar!",
        "chelo": "Chelo é imbatível! Sempre trazendo resultados incríveis para a FURIA!",
        "xand": "Xand é pura habilidade! Quando ele joga, é sempre um show à parte!",
        "guerri": "Guerri é o cérebro por trás da FURIA! Ele sabe como fazer a equipe vencer!"
    },
    'saudacoes': {
        "furioso": "Eu mesmo! estou aqui pra te auxiliar a ficar ligadão nas notícias da FURIA e do CS! Do que precisa?",
        "ola": "Olá! Pronto pra mais uma batalha com a FURIA?",
        "saudacoes": "Saudações! O rugido da torcida é eterno!",
        "cumprimentos": "Cumprimentos! Aqui é raça e dedicação!",
        "prazer": "O prazer é meu! Vamos juntos com a FURIA!",
        "oi": "Oi! Se chegou pra somar, tá no lugar certo!",
        "opa": "Opa! Chegou chegando!",
        "salve": "Salve! O rugido da torcida nunca para!",
        "beleza": "Beleza pura por aqui! E contigo?",
        "yo": "Yo! tranquilão? É nóis no clutch!",
        "ae": "Aê! Chegou pesado na resenha!",
        "oie": "Oie! Que bom te ver por aqui!",
        "boa": "Boa! tudo certo hoje? o que manda?",
        "eai": "Eaí mano! o que manda hoje?",
        "fala": "Fala tu, tudo tranquilo?"
    }
}

# Dicionário de combinações de palavras-chave com respostas contextualizadas
contextual_responses = {
    'jogos': {
        ("quando", "proximo", "jogo"): "O próximo jogo da FURIA será em breve! A torcida já está ansiosa para mais uma vitória!",
        ("horario", "jogo", "hoje"): "O jogo de hoje da FURIA vai ser incrível! Fique ligado no horário!",
        ("onde", "assistir", "jogo"): "Você pode assistir aos jogos da FURIA nos melhores canais de esportes eletrônicos!",
        ("contra", "quem", "jogam"): "A FURIA está preparada para enfrentar os melhores times do mundo!",
        ("data", "proximo", "match"): "O próximo match da FURIA está marcado e promete ser eletrizante!",
    },
    'torneios': {
        ("qual", "proximo", "torneio"): "A FURIA está classificada para os principais torneios internacionais!",
        ("quando", "major", "cs2"): "O próximo Major de CS2 está chegando e a FURIA está treinando forte!",
        ("furia", "classificada", "para"): "A FURIA está sempre classificada para os maiores eventos!",
        ("quais", "campeonatos", "participando"): "A FURIA está nos principais campeonatos mundiais!",
    },
    'jogadores': {
        ("como", "esta", "fallen"): "O Fallen está em grande forma, liderando a FURIA para vitórias!",
        ("quem", "melhor", "kda"): "Nossos jogadores estão sempre entre os melhores em estatísticas!",
        ("quais", "jogadores", "time"): "A FURIA tem um time completo de estrelas do CS!",
        ("quem", "joga", "awp"): "Nossos atiradores estão afiados e prontos para o combate!",
    },
    'historia': {
        ("titulo", "furia"): "A FURIA já conquistou vários títulos importantes!",
        ("titulos", "furia"): "A FURIA já conquistou vários títulos importantes!",
        ("anos", "organizacao"): f"A FURIA está dominando tudo no cenário há {ano_atual - 2017} anos!",
        ("anos", "furia"): f"A FURIA está dominando tudo no cenário há {ano_atual - 2017} anos!",
        ("maior", "conquista"): "A FURIA tem conquistas históricas no cenário mundial!",
        ("maiores", "conquistas"): "A FURIA tem conquistas históricas no cenário mundial!",
        ("furia", "existe"): "A FURIA vem fazendo história no cenário de e-sports desde 2017!",
        ("existe", "tempo"): "A FURIA vem fazendo história no cenário de e-sports desde 2017!",
    },
    'noticias': {
        ("tem", "novidades", "time"): "Sempre tem novidades na FURIA! O time está em constante evolução!",
        ("mudou", "algo", "elenco"): "A FURIA sempre busca o melhor para o seu elenco!",
        ("vai", "ter", "mudanca"): "A FURIA está sempre se reinventando para vencer!"
    },
    'saudacoes': {
        ("bom", "dia"): "Bom dia! Que hoje seja um dia de vitória pra você e pra FURIA!",
        ("boa", "tarde"): "Boa tarde! Bora seguir firme com a FURIA!",
        ("boa", "noite"): "Boa noite! Que o descanso venha depois de uma vitória!",
        ("como", "vai"): "Vou na bala, sempre na torcida com a FURIA! E você?",
        ("como", "esta"): "Sempre no ritmo da vitória! E você?",
        ("tudo", "bem"): "Tudo ótimo por aqui! Ainda melhor falando com um verdadeiro fã da FURIA!",
        ("tudo", "certo"): "Tudo certo e no foco! Salve!",
        ("com", "licenca"): "Licença concedida! Aqui é território da FURIA!",
        ("fala", "ai"): "Fala aí! Sempre bom te ouvir!",
        ("ta", "tranquilo"): "Tranquilo e na expectativa da próxima vitória da FURIA!",
        ("tudo", "beleza"): "Tudo beleza! Bora que hoje é dia de FURIA!",
        ("de", "boa"): "De boa e com a FURIA no coração!",
        ("ae", "man"): "Aê man! Já dominou o servidor!",
        ("oi", "oi"): "Oi oi! Preparado pra torcer com tudo?",
        ("fala", "mano"): "Fala mano! No pique da FURIA!",
        ("fala", "campeao"): "Fala campeão! FURIA no coração!",
        ("fala", "guerreiro"): "Fala guerreiro! Um verdadeiro campeão!",
        ("fala", "brother"): "Fala brother! Raça e dedicação é o que move a FURIA!",
        ("fala", "truta"): "Fala truta! FURIA de corpo e alma!",
        ("fala", "chefe"): "Fala chefe! É sempre uma honra falar com você!",
        ("fala", "fera"): "Fala fera! Vamos com tudo pra mais uma vitória!",
        ("fala", "meu", "consagrado"): "Fala meu consagrado! FURIA é nossa!",
        ("seu", "nome"): "Opa! tranquilo? meu nome é FURIOSO e estou aqui pra te auxiliar a ficar ligadão nas notícias da FURIA e do CS! Do que precisa?",
        ("teu", "nome"): "Opa! tranquilo? meu nome é FURIOSO e estou aqui pra te auxiliar a ficar ligadão nas notícias da FURIA e do CS! Do que precisa?",
        ("quem", "e", "voce"): "Opa! tranquilo? meu nome é FURIOSO e estou aqui pra te auxiliar a ficar ligadão nas notícias da FURIA e do CS! Do que precisa?",
        ("quem", "e", "vc"): "Opa! tranquilo? meu nome é FURIOSO e estou aqui pra te auxiliar a ficar ligadão nas notícias da FURIA e do CS! Do que precisa?",
        ("quem", "e", "tu"): "Opa! tranquilo? meu nome é FURIOSO e estou aqui pra te auxiliar a ficar ligadão nas notícias da FURIA e do CS! Do que precisa?"
    }
}

# Listas de emojis categorizados por tom
emojis_hype = ["🔥", "💥", "🏆", "🎮"]
emojis_confidence = ["💪", "⚡", "🌟"]
emojis_friendly = ["😎", "🤝", "🙌"]

# Retorna um emoji apropriado baseado no tom da resposta
def get_emoji_for_response(response_text):
    # Verifica palavras-chave que indicam hype
    hype_words = ["arrebentar", "epica", "loucura", "espetaculo", "dominar", "brilhar", "show", "emoçao", "amassar"]
    if any(word in response_text.lower() for word in hype_words):
        return random.choice(emojis_hype)

    # Verifica palavras-chave que indicam confiança
    confidence_words = ["vencer", "vitoria", "imbativel", "forte", "lenda", "decisivo", "maestria", "cerebro"]
    if any(word in response_text.lower() for word in confidence_words):
        return random.choice(emojis_confidence)

    # Padrão para respostas amigáveis
    return random.choice(emojis_friendly)

def fallback_response(user_text):
    # Padroniza a entrada do usuário para melhor verificação
    user_text = unidecode(user_text.lower())

    # Verifica se a entrada contém alguma combinação de palavra-chave
    for category, phrases in contextual_responses.items():
        for keyword_combination, response in phrases.items():
            if all(keyword in user_text for keyword in keyword_combination):
                emoji = get_emoji_for_response(response)

                # Informações adicionais para categorias específicas
                additional_phrase = ""
                if category in ['jogos', 'torneios', 'jogadores especificos', 'noticias', 'historia']:
                    additional_phrases = {
                        'jogos': "\n\nSe quiser mais infomações sobre os jogos da FURIA, acesse:\n[https://www.hltv.org/team/8297/furia#tab-matchesBox]",
                        'torneios': "\n\nSe quiser mais infomações sobre os torneios que a FURIA disputa no CS, acesse:\n[https://www.hltv.org/team/8297/furia#tab-eventsBox]",
                        'jogadores especificos': "\n\nSe quiser mais infomações sobre os jogadores da FURIA no CS, acesse:\n[https://www.hltv.org/team/8297/furia#tab-rosterBox]",
                        'noticias': "\n\nSe quiser mais notícias sobre a FURIA no CS, acesse:\n[https://www.hltv.org/team/8297/furia#tab-newsBox]",
                        'historia': "\n\nSe quiser mais infomações sobre a história da FURIA, acesse:\n[https://www.furia.gg/quem-somos]"
                    }
                    additional_phrase = additional_phrases.get(category, "")

                return {
                    "response": response,
                    "emoji": emoji,
                    "additional_phrase": additional_phrase
                }

    # Keywords para curiosidades específicas
    curiosidades = keywords_responses['curiosidades']

    # Verifica se alguma chave exata de curiosidades está na entrada
    for keyword in curiosidades.keys():
        if keyword in user_text:
            response = curiosidades[keyword]
            emoji = get_emoji_for_response(response)
            return {
                "response": response,
                "emoji": emoji,
                "additional_phrase": "\n\nQuer mais curiosidades? É só perguntar! 🔍"
            }

    # Verifica se partes da chave estão na entrada
    for chave in curiosidades.keys():
        if any(palavra in user_text.split() for palavra in chave.split()):
            response = curiosidades[chave]
            emoji = get_emoji_for_response(response)
            return {
                "response": response,
                "emoji": emoji,
                "additional_phrase": "\n\nA FURIA tem muito mais história pra contar! 🔍"
            }

    # Verificação específica para curiosidades
    if 'curiosidade' in user_text or 'curiosidades' in user_text:
        curiosidades = keywords_responses['curiosidades']
        random_key = random.choice(list(curiosidades.keys()))
        response = curiosidades[random_key]
        emoji = get_emoji_for_response(response)
        return {
            "response": response,
            "emoji": emoji,
            "additional_phrase": "\n\nQuer mais curiosidades? A FURIA tem muita história pra contar! 🔍"
        }

    # Verifica se a entrada contém alguma palavra-chave
    for category, responses in keywords_responses.items():
        # Verifica se alguma palavra-chave da categoria está presente na entrada do usuário
        for keyword, response in responses.items():
            if keyword in user_text:
                # Adiciona um emoji apropriado à resposta
                emoji = get_emoji_for_response(response)

                # Informações adicionais para categorias específicas
                additional_phrase = ""
                if category in ['jogos', 'times', 'torneios', 'cenario', 'resultados', 'historico', 'jogadores especificos']:
                    additional_phrases = {
                        'jogos': "\n\nSe quiser mais infomações sobre os jogos da FURIA, acesse:\n[https://www.hltv.org/team/8297/furia#tab-matchesBox]",
                        'times': "\n\nSe quiser mais infomações sobre o time de CS da FURIA, acesse:\n[https://www.hltv.org/team/8297/furia]",
                        'torneios': "\n\nSe quiser mais infomações sobre os torneios que a FURIA disputa no CS, acesse:\n[https://www.hltv.org/team/8297/furia#tab-eventsBox]",
                        'cenario': "\n\nSe quiser mais notícias sobre cenário de CS, acesse:\n[https://www.hltv.org/]",
                        'resultados': "\n\nSe quiser mais infomações sobre os resultados da FURIA no CS, acesse:\n[https://www.hltv.org/team/8297/furia#tab-matchesBox]",
                        'historico': "\n\nSe quiser mais infomações sobre o histórico da FURIA no CS, acesse:\n[https://www.hltv.org/team/8297/furia#tab-statsBox]",
                        'jogadores especificos': "\n\nSe quiser mais infomações sobre os jogadores da FURIA no CS, acesse:\n[https://www.hltv.org/team/8297/furia#tab-rosterBox]"
                    }
                    additional_phrase = additional_phrases.get(category, "")

                return {
                    "response": response,
                    "emoji": emoji,
                    "additional_phrase": additional_phrase
                }

    # Se nenhuma palavra-chave for encontrada, retorna uma resposta genérica
    return {
        "response": random.choice([
            "Essa aí me pegou de jeito! Vou treinar mais pra responder igual a FURIA joga, fechô? 🤝\n",
            "Poxa! Não tenho resposta pra essa pergunta agora, mas logo trago notícias, belê? 😎\n",
            "Boa pergunta, parceiro! Vou ficar de olho e trazer essa informação pra torcida. 🔥\n",
        ]),
        "emoji": "",
        "additional_phrase": "\nSe quiser mais infomações sobre o time de CS da FURIA, acesse:\n[https://www.hltv.org/team/8297/furia]"
    }