import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from pickle import load
from PIL import Image
import yfinance as yf
st.set_page_config(layout="wide")

st.title('Robo-advisor')

st.write("# Paso 1: Complete el cuestionario")

Sexo = st.select_slider('Sexo', options=['Hombre', 'Mujer'])
Edad = st.select_slider('Edad', options=['<35', '35-44', '45-54', '55-64', '65-74', '>75'])
Educacion = st.select_slider('Educación', options=['ESO', 'Bachillerato', 'FP Grado superior', 'Grado Universidad'])
Casado = st.select_slider('Estado civil', options=['Casado', 'Soltero/Divorciado/Viudo'])
Hijos = st.select_slider('Número de hijos', options=[0, 1, 2, 3, 4, 5, 6, 7])
Raza = st.select_slider('Raza', options=['Caucásico', 'Afroamericano', 'Hispano', 'Otro'])
Trabajo = st.select_slider('Estado laboral',
                           options=['Contratado', 'Autónomo/empresario', 'Estudiante/jubilado',
                                    'Desempleado'])
Conocimiento = st.select_slider('De 1 a 10 cómo es tu conocimiento financiero', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Risk = st.select_slider('De 1 a 4 cúanto estarías dispuesto a tomar riesgos financieros', options=['1', '2', '3', '4'])
Patrimonio = st.select_slider('Patrimonio neto', options=['<5.000 €', 'Entre 5.000 € y 75.000 €',
                                                          'Entre 75.000 € y 180.000 €',
                                                          'Entre 180.000 € y 370.000 €',
                                                          'Entre 370.000 € y 1.350.000 €'])
Renta = st.select_slider('Renta anual', options=['<900 €', 'Entre 900 € y 1.350 €', 'Entre 1.350 € y 1.700 €',
                                                 'Entre 1.700 € y 2.400 €', 'Entre 2.400 € y 3.500 €', '>3.500 €'])

if Sexo == 'Hombre':
    Sexo = 1
else:
    Sexo = 2

if Edad == '<35':
    Edad = 1
elif Edad == '35-44':
    Edad = 2
elif Edad == '45-54':
    Edad = 3
elif Edad == '55-64':
    Edad = 4
elif Edad == '65-74':
    Edad = 5
else:
    Edad = 6

if Educacion == 'ESO':
    Educacion = 1
elif Educacion == 'Bachillerato':
    Educacion = 2
elif Educacion == 'FP Grado superior':
    Educacion = 3
else:
    Educacion = 4

if Casado == 'Casado':
    Casado = 1
else:
    Casado = 2

if Raza == 'Caucásico':
    Raza = 1
elif Raza == 'Afroamericano':
    Raza = 2
elif Raza == 'Hispano':
    Raza = 3
else:
    Raza = 5

if Trabajo == 'Contratado':
    Trabajo = 1
elif Trabajo == 'Autónomo/empresario':
    Trabajo = 2
elif Trabajo == 'Estudiante/jubilado':
    Trabajo = 3
else:
    Trabajo = 4

if Risk == '1':
    NoRisk = 1
    YesRisk = 0
elif Risk == '4':
    YesRisk = 1
    NoRisk = 0
else:
    NoRisk = 0
    YesRisk = 0

if Patrimonio == '<5.000 €':
    Patrimonio = 1
elif Patrimonio == 'Entre 5.000 € y 75.000 €':
    Patrimonio = 2
elif Patrimonio == 'Entre 75.000 € y 180.000 €':
    Patrimonio = 3
elif Patrimonio == 'Entre 180.000 € y 370.000 €':
    Patrimonio = 4
else:
    Patrimonio = 5

if Renta == '<900 €':
    Renta = 1
elif Renta == 'Entre 900 € y 1.350 €':
    Renta = 2
elif Renta == 'Entre 1.350 € y 1.700 €':
    Renta = 3
elif Renta == 'Entre 1.700 € y 2.400 €':
    Renta = 4
elif Renta == 'Entre 2.400 € y 3.000 €':
    Renta = 5
else:
    Renta = 6

filename = 'Modelo_aprendizaje_supervisado.pkl'
loaded_model = load(open(filename, 'rb'))

@st.cache
def prediction( Sexo, Edad, Educacion, Casado, Hijos, Raza, Trabajo, Conocimiento, YesRisk, NoRisk, Patrimonio, Renta):

    lst = [[Sexo, Edad, Educacion, Casado, Hijos, Raza, Trabajo, Conocimiento, YesRisk, NoRisk, Patrimonio, Renta]]
    X = pd.DataFrame(lst, columns=['HHSEX', 'AGECL', 'EDCL', 'MARRIED', 'KIDS', 'RACE', 'OCCAT1', 'KNOWL', 'YESFINRISK',
                                   'NOFINRISK', 'NWCAT', 'INCCAT'])
    predictions = loaded_model.predict(X)
    return predictions


if st.button('Descubra su perfil de inversor'):

    Tolerancia = prediction(Sexo, Edad, Educacion, Casado, Hijos, Raza, Trabajo, Conocimiento, YesRisk, NoRisk,
                            Patrimonio, Renta)

    if Tolerancia < 0.4:
        st.write('Su perfil de inversor es conservador')
    elif Tolerancia > 0.75:
        st.write('Su perfil de inversor es agresivo')
    else:
        st.write('Su perfil de inversor es moderado')


st.write('# Paso 2:')
graficos_acciones = st.selectbox(
    'Selecciona el tipo de inversor que eres para ver en qué activos invertir',
    ('Inversor conservador', 'Inversor moderado', 'Inversor agresivo')
)


def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df


df = load_data()

if graficos_acciones == 'Inversor conservador':

    st.write('Portafolio inversor conservador')
    labels = 'SP500 ETF', 'International market ETF', 'Bonos', 'Cash', 'Large & mid caps'
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#99ffff']
    sizes = [20, 10, 40, 20, 10]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    np.load('stocks_conservadores.npy', allow_pickle=True)

    st.write('Large & mid caps cluster inversor conservador')
    df_con = df[df.Symbol.isin(
        ['ABT', 'ACN', 'AFL', 'APD', 'ARE', 'ALLE', 'LNT', 'ALL', 'AEE', 'AEP', 'AXP', 'AMT', 'AWK', 'AME', 'AMGN',
         'APH', 'AON', 'AIV', 'ADM', 'AJG',
         'AIZ', 'ATO', 'ADP', 'AVB', 'BAX', 'BBT', 'BDX', 'BXP', 'CBRE', 'CNP', 'CB', 'CINF', 'CTXS', 'CME', 'CMS',
         'KO', 'CMCSA', 'ED', 'COST', 'CCI',
         'DHR', 'DRI', 'DLR', 'D', 'DOV', 'DTE', 'DUK', 'DRE', 'ECL', 'ETR', 'EFX', 'EQIX', 'EQR', 'ESS', 'EVRG', 'ES',
         'RE', 'EXC', 'EXPD', 'EXR', 'FRT',
         'FIS', 'FE', 'FRC', 'GPC', 'GL', 'HIG', 'HCP', 'HSIC', 'HSY', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'IEX', 'INFO',
         'IR', 'ICE', 'JKHY', 'JCI', 'JPM',
         'KMB', 'KIM', 'KMI', 'LDOS', 'LLY', 'LIN', 'LMT', 'L', 'MMC', 'MCD', 'MDT', 'MRK', 'MAA', 'MDLZ', 'NDAQ',
         'NEE', 'NI', 'OKE', 'ORCL', 'PAYX', 'PEP',
         'PFE', 'PNW', 'PPL', 'PG', 'PLD', 'PEG', 'PSA', 'DGX', 'RTN', 'O', 'REG', 'RSG', 'ROL', 'ROP', 'SBAC', 'SRE',
         'SHW', 'SO', 'SYK', 'SYY', 'TMUS', 'TRV',
         'UDR', 'USB', 'UTX', 'VTR', 'VRSK', 'VZ', 'WMT', 'DIS', 'WM', 'WEC', 'WELL', 'WU', 'WLTW', 'XEL', 'XYL', 'YUM',
         'ZBH'])]
    df_con = df_con.drop(labels=['SEC filings', 'Headquarters Location', 'Date first added', 'CIK'], axis=1)
    df_con = df_con.reset_index(drop=True)
    st.write(df_con)

    image = Image.open('Stocks conservadores.jpg')
    st.image(image, caption='Evolución portafolio compuesto por una acción de cada empresa del cluster conservador')

    st.write('SP500 ETF - Ticker VOO')
    tickerData1 = yf.Ticker('VOO')
    tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf1.Close)

    st.write('International market ETF - Ticker IEFA')
    tickerData2 = yf.Ticker('IEFA')
    tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf2.Close)

elif graficos_acciones == 'Inversor moderado':

    st.write('Portafolio inversor moderado')
    labels = 'SP500 ETF', 'International ETF', 'Bonos', 'Cash', 'Large & mid caps'
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#99ffff']
    sizes = [30, 15, 25, 10, 20]
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)

    np.load('stocks_moderados.npy', allow_pickle=True)

    st.write('Large & mid caps cluster inversor moderado')
    df_mod = df[df.Symbol.isin(
        ['ADBE', 'AAP', 'AES', 'A', 'AKAM', 'GOOGL', 'GOOG', 'AMZN', 'ADI', 'ANSS', 'AAPL', 'AZO', 'BLL', 'BA', 'BSX',
         'BR', 'CDNS', 'KMX',
         'CDW', 'CE', 'CHTR', 'CHD', 'CTAS', 'CSCO', 'COO', 'CPRT', 'CSX', 'DG', 'EW', 'EL', 'EXPE', 'FAST', 'FISV',
         'FLT', 'FLIR', 'FTNT',
         'GRMN', 'IT', 'GPN', 'GWW', 'HAS', 'HCA', 'IDXX', 'INTU', 'ISRG', 'IQV', 'JEC', 'KSU', 'KEYS', 'KLAC', 'LHX',
         'LW', 'LOW', 'MKTX',
         'MLM', 'MA', 'MKC', 'MSFT', 'MCO', 'MSI', 'MSCI', 'NKE', 'NSC', 'NOC', 'NRG', 'ORLY', 'PYPL', 'PGR', 'RMD',
         'ROST', 'CRM', 'SPGI',
         'SBUX', 'SNPS', 'TGT', 'TFX', 'TXN', 'TMO', 'TJX', 'TSCO', 'TDG', 'UNP', 'UAL', 'UHS', 'VFC', 'VRSN', 'V',
         'WCG', 'ZTS'])]
    df_mod = df_mod.drop(labels=['SEC filings', 'Headquarters Location', 'Date first added', 'CIK'], axis=1)
    df_mod = df_mod.reset_index(drop=True)
    st.write(df_mod)

    image = Image.open('Stocks moderados.jpg')
    st.image(image, caption='Evolución portafolio compuesto por una acción de cada empresa del cluster moderado')

    st.write('SP500 ETF - Ticker VOO')
    tickerData1 = yf.Ticker('VOO')
    tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf1.Close)

    st.write('International market ETF - Ticker IEFA')
    tickerData2 = yf.Ticker('IEFA')
    tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf2.Close)

else:

    st.write('Portafolio inversor agresivo')
    labels = 'SP500 ETF', 'International ETF', 'Bonos', 'Cash', 'Large & mid caps', 'Bitcoin'
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#99ffff', '#cca37a']
    sizes = [30, 15, 15, 5, 25, 10]
    fig3, ax3 = plt.subplots()
    ax3.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')
    st.pyplot(fig3)

    np.load('stocks_agresivos.npy', allow_pickle=True)

    st.write('Large & mid caps cluster inversor agresivo')
    df_agr = df[df.Symbol.isin(
        ['ABMD', 'AMD', 'ALGN', 'ANET', 'ADSK', 'CMG', 'HES', 'ILMN', 'LRCX', 'MU', 'NFLX', 'NVDA', 'QRVO', 'STX',
         'SYMC', 'TTWO',
         'TWTR', 'TRIP', 'ULTA', 'UAA', 'UA', 'XLNX'])]
    df_agr = df_agr.drop(['SEC filings', 'Headquarters Location', 'Date first added', 'CIK'], axis=1)
    df_agr = df_agr.reset_index(drop=True)
    st.write(df_agr)

    image = Image.open('Stocks agresivos.jpg')
    st.image(image, caption='Evolución portafolio compuesto por una acción de cada empresa del cluster agresivo')

    st.write('SP500 ETF - Ticker VOO')
    tickerData1 = yf.Ticker('VOO')
    tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf1.Close)

    st.write('International market ETF - Ticker IEFA')
    tickerData2 = yf.Ticker('IEFA')
    tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf2.Close)

    st.write('Bitcoin - Ticker BTC')
    tickerData3 = yf.Ticker('BTC-USD')
    tickerDf3 = tickerData3.history(period='1d', start='2017-1-1', end='2021-5-2')
    st.line_chart(tickerDf3.Close)