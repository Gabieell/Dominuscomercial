import streamlit as st
import random
import pandas as pd
from datetime import datetime
import io

# Lista de cidades e estados do Brasil
cidades_brasil = [
    ('São Paulo', 'SP'), ('Rio de Janeiro', 'RJ'), ('Belo Horizonte', 'MG'),
    ('Brasília', 'DF'), ('Curitiba', 'PR'), ('Porto Alegre', 'RS'),
    ('Salvador', 'BA'), ('Recife', 'PE'), ('Fortaleza', 'CE'),
    ('Manaus', 'AM'), ('Belém', 'PA'), ('Goiânia', 'GO'), ('Campinas', 'SP'),
    ('São Luís', 'MA'), ('Vitória', 'ES'), ('Maceió', 'AL'), ('Natal', 'RN'),
    ('João Pessoa', 'PB'), ('Cuiabá', 'MT'), ('Campo Grande', 'MS'),
    ('Teresina', 'PI'), ('Aracaju', 'SE'), ('Macapá', 'AP'), ('Boa Vista', 'RR'),
    ('Palmas', 'TO'), ('Florianópolis', 'SC'), ('Maringá', 'PR'), ('Santos', 'SP'),
    ('Londrina', 'PR'), ('Uberlândia', 'MG'), ('Joinville', 'SC'), ('São Bernardo do Campo', 'SP'),
    ('Sorocaba', 'SP'), ('Niterói', 'RJ'), ('Ribeirão Preto', 'SP'), ('Caxias do Sul', 'RS'),
    ('Campina Grande', 'PB'), ('Lages', 'SC'), ('Aracaju', 'SE'), ('Porto Velho', 'RO')
]

# Função que retorna as informações do cronograma
def obter_cronograma(dia_semana):
    cronograma = {
        'segunda': {
            'segmento': 'Clínicas Odontológicas',
        },
        'terça': {
            'segmento': 'Clínicas de Estética',
        },
        'quarta': {
            'segmento': 'Olaria',
        },
        'quinta': {
            'segmento': 'Poços Artesianos',
        },
        'sexta': {
            'segmento': 'Auto Escolas',
        },
        'sábado': {
            'segmento': 'Cirurgião Plástico',
        },
        'domingo': {
            'segmento': 'Venda de Jalecos',
        }
    }

    # Converte o dia da semana para o formato correto
    dia = dia_semana.lower()

    if dia in cronograma:
        return cronograma[dia]
    else:
        return "Dia da semana inválido!"

# Saudação
st.title('Bem-vindo ao Cronograma de Pesquisa de Leads!')
st.write('Escolha o dia da semana abaixo para ver as informações de pesquisa:')

# Preenchendo o nome do Comercial
nome_comercial = st.text_input("Nome do Comercial")

# Seletor de dia da semana
dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
dia_selecionado = st.selectbox('Selecione o dia da semana:', dias)

# Obter as informações para o dia selecionado
informacoes_do_dia = obter_cronograma(dia_selecionado)

# Gerar meta de contatos aleatória
meta_aleatoria = random.randint(20, 50)

# Sugestão de cidade aleatória do Brasil
cidade_aleatoria, estado_aleatorio = random.choice(cidades_brasil)

# Mostrar as informações
if isinstance(informacoes_do_dia, dict):
    st.subheader(f"Segmento para hoje ({dia_selecionado.capitalize()}):")
    st.write(f"**Segmento:** {informacoes_do_dia['segmento']}")
    st.write(f"**Meta de Contatos para hoje:** {meta_aleatoria}")
    st.write(f"**Cidade sugerida para pesquisa:** {cidade_aleatoria} - {estado_aleatorio}")
    st.write("**Sites recomendados para pesquisa:**")
    
    # Adicionar os links de pesquisa
    st.write(f"- [Google](https://www.google.com.br/search?q={informacoes_do_dia['segmento']})")
    st.write(f"- [Instagram](https://www.instagram.com/explore/tags/{informacoes_do_dia['segmento'].replace(' ', '')}/)")
    st.write(f"- [Telelistas](https://www.telelistas.net)")
    st.write(f"- [Apontador](https://www.apontador.com.br)")

    # Gerar o modelo de relatório
    st.subheader("Modelo de Relatório")
    st.write("Clique no botão abaixo para gerar o modelo do relatório para preenchimento:")

    # Gerar o modelo de relatório em Excel
    if st.button("Gerar Modelo de Relatório"):
        # Gerar DataFrame com a meta de contatos
        data_atual = datetime.today().strftime('%Y-%m-%d')
        dados_relatorio = {
            'Data': [data_atual] * meta_aleatoria,
            'Nome do Comercial': [nome_comercial] * meta_aleatoria,
            'Cidade': [cidade_aleatoria] * meta_aleatoria,
            'Segmento': [informacoes_do_dia['segmento']] * meta_aleatoria,
            'Empresa': [''] * meta_aleatoria,
            'Telefone': [''] * meta_aleatoria,
            'Redes Sociais': [''] * meta_aleatoria,
            'Observações': [''] * meta_aleatoria
        }
        
        df_relatorio = pd.DataFrame(dados_relatorio)

        # Gerar o arquivo Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_relatorio.to_excel(writer, index=False, sheet_name='Relatório', header=True)
        
        # Salvar e gerar o download do arquivo
        output.seek(0)
        st.download_button(
            label="Baixar Modelo de Relatório (Excel)",
            data=output,
            file_name=f"modelo_relatorio_{data_atual}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

else:
    st.write(informacoes_do_dia)
