import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from pickle import load
from PIL import Image
import yfinance as yf

st.set_page_config(layout="centered")

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


st.text("")
st.text("")
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

    st.write('# Portafolio inversor conservador')
    st.text("")

    fig1, ax1 = plt.subplots(figsize=(10, 6))

    size = 0.3
    vals = np.array([[15, 40], [30, 0], [7.5, 7.5]])

    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3) * 4)
    inner_colors = cmap([1, 2, 5, 6, 9, 10])
    labels = 'Bonds', 'Stock market', 'Commodities'
    labels2 = '15% US Bond intermediate-term (IEI)', '40% US Bond long-term (TLT)', '30% US large cap (VTI)', '',\
              '7,5% Gold (GLD)', '7,5% Other commodities (GSG)'

    ax1.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
            wedgeprops=dict(width=size, edgecolor='w'))

    ax1.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))

    ax1.set(aspect="equal")

    st.pyplot(fig1)

    np.load('stocks_conservadores.npy', allow_pickle=True)

    st.write('# Large & mid caps cluster inversor conservador')
    st.text("")
    st.text("")
    st.text("")
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
    df_con.rename(columns={'Symbol': 'Ticker', 'Security': 'Company', 'GICS Sector': 'Sector',
                           'GICS Sub-Industry': 'Sub-Industry'}, inplace=True)
    df_con = df_con.reset_index(drop=True)
    st.write(df_con)

    image = Image.open('Stocks conservadores.jpg')
    st.image(image, caption='Evolución portafolio compuesto por una acción de cada empresa del cluster conservador')

    st.write('# ¿Por qué SP500 ETF?')
    st.write('SP500 ETF - Ticker VOO')
    tickerData1 = yf.Ticker('VOO')
    tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf1.Close)

    st.write('1. Exposición a las 500 empresas más grandes de los EE.UU.')
    st.write('2. El objetivo es replicar el rendimiento del índice S&P 500.')
    st.write('3. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
             'crecimiento a largo plazo.')
    st.write('4. Con un rendimiento anual medio del 15.74% desde el año de lanzamiento.')

    st.write('# ¿Por qué International market ETF?')
    st.write('International market ETF - Ticker IEFA')
    tickerData2 = yf.Ticker('IEFA')
    tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf2.Close)

    st.write('1. Exposición a un amplio rango de empresas de Europa, Australia y Asia.')
    st.write('2. Acceso completo y de bajo costo a valores de renta variable de alta, mediana y baja capitalización de '
             'mercados desarrollados.')
    st.write('3. Hágalo parte fundamental de su cartera para diversificarse internacionalmente y buscar crecimiento a '
             'largo plazo.')
    st.write('4. Con un rendimiento anual medio del 7.56% desde el año de lanzamiento.')

    st.write('# ¿Por qué Bonos?')
    st.write('Rentabilidad bono Estados Unidos a 10 años')
    tickerData4 = yf.Ticker('^TNX')
    tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf4.Close)

    st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
    st.write('2. Diversifica y reduce la volatilidad del portafolio.')

elif graficos_acciones == 'Inversor moderado':

    st.write('# Portafolio inversor moderado')
    st.text("")
    fig2, ax2 = plt.subplots(figsize=(10, 6))

    size = 0.3
    vals = np.array([[10, 25, 0], [10, 30, 15], [5, 5, 0]])

    a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
    outer_colors = [a(0.6), b(0.6), c(0.6)]
    inner_colors = [a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), b(0.3), c(0.5), c(0.4)]
    labels = 'Bonds', 'Stock market', 'Commodities'
    labels2 = '10% US Bond intermediate-term (IEI)', '25% US Bond long-term (TLT)', '', '10% Real Estate (VNQ)', \
              '30% US large cap (VTI)', '15% International large cap (VEU)', '5% Gold (GLD)', \
              '5% Other commodities (GSG)', ''

    ax2.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
           wedgeprops=dict(width=size, edgecolor='w'))

    ax2.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
           wedgeprops=dict(width=size, edgecolor='w'))

    ax2.set(aspect="equal")
    st.pyplot(fig2)

    np.load('stocks_moderados.npy', allow_pickle=True)

    st.write('# Large & mid caps cluster inversor moderado')
    st.text("")
    st.text("")
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
    df_mod.rename(columns={'Symbol': 'Ticker', 'Security': 'Company', 'GICS Sector': 'Sector',
                           'GICS Sub-Industry': 'Sub-Industry'}, inplace=True)
    df_mod = df_mod.reset_index(drop=True)
    st.write(df_mod)

    image = Image.open('Stocks moderados.jpg')
    st.image(image, caption='Evolución portafolio compuesto por una acción de cada empresa del cluster moderado')

    st.write('# ¿Por qué SP500 ETF?')
    st.write('SP500 ETF - Ticker VOO')
    tickerData1 = yf.Ticker('VOO')
    tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf1.Close)

    st.write('1. Exposición a las 500 empresas más grandes de los EE.UU.')
    st.write('2. El objetivo es replicar el rendimiento del índice S&P 500.')
    st.write('3. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
             'crecimiento a largo plazo.')
    st.write('4. Con un rendimiento anual medio del 15.74% desde el año de lanzamiento.')

    st.write('# ¿Por qué International market ETF?')
    st.write('International market ETF - Ticker IEFA')
    tickerData2 = yf.Ticker('IEFA')
    tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf2.Close)

    st.write('1. Exposición a un amplio rango de empresas de Europa, Australia y Asia.')
    st.write('2. Acceso completo y de bajo costo a valores de renta variable de alta, mediana y baja capitalización de '
             'mercados desarrollados.')
    st.write('3. Hágalo parte fundamental de su cartera para diversificarse internacionalmente y buscar crecimiento a '
             'largo plazo.')
    st.write('4. Con un rendimiento anual medio del 7.56% desde el año de lanzamiento.')

    st.write('# ¿Por qué Bonos?')
    st.write('Rentabilidad bono Estados Unidos a 10 años')
    tickerData4 = yf.Ticker('^TNX')
    tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf4.Close)

    st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
    st.write('2. Diversifica y reduce la volatilidad del portafolio.')

else:

    st.write('# Portafolio inversor agresivo')
    st.text("")
    fig3, ax3 = plt.subplots(figsize=(10, 6))

    size = 0.3
    vals = np.array([[5, 15, 0, 0, 0], [10, 35, 15, 5, 5], [5, 5, 0, 0, 0]])

    a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
    outer_colors = [a(0.6), b(0.6), c(0.6)]
    inner_colors = [a(0.5), a(0.4), a(0.3), a(0.2), a(0.1), b(0.5), b(0.4), b(0.3), b(0.2), b(0.1), c(0.5), c(0.4)]
    labels = 'Bonds', 'Stock market', 'Commodities'
    labels2 = '10% US Bond intermediate-term (IEI)', '25% US Bond long-term (TLT)', '', '', '', '10% Real Estate (VNQ)'\
        , '35% US large cap (VTI)', '15% International large cap (VEU)', '5% Emerging markets large cap (EEM)'\
        , '5% Bitcoin (BTC)', '5% Gold (GLD)', '5% Other commodities (GSG)', '', '', ''

    ax3.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
           wedgeprops=dict(width=size, edgecolor='w'))

    ax3.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
           wedgeprops=dict(width=size, edgecolor='w'))

    ax3.set(aspect="equal")
    st.pyplot(fig3)

    np.load('stocks_agresivos.npy', allow_pickle=True)

    st.write('# Large & mid caps cluster inversor agresivo')
    st.text("")
    st.text("")
    df_agr = df[df.Symbol.isin(
        ['ABMD', 'AMD', 'ALGN', 'ANET', 'ADSK', 'CMG', 'HES', 'ILMN', 'LRCX', 'MU', 'NFLX', 'NVDA', 'QRVO', 'STX',
         'SYMC', 'TTWO',
         'TWTR', 'TRIP', 'ULTA', 'UAA', 'UA', 'XLNX'])]
    df_agr = df_agr.drop(['SEC filings', 'Headquarters Location', 'Date first added', 'CIK'], axis=1)
    df_agr.rename(columns={'Symbol': 'Ticker', 'Security': 'Company', 'GICS Sector': 'Sector',
                           'GICS Sub-Industry': 'Sub-Industry'}, inplace=True)
    df_agr = df_agr.reset_index(drop=True)
    st.write(df_agr)

    image = Image.open('Stocks agresivos.jpg')
    st.image(image, caption='Evolución portafolio compuesto por una acción de cada empresa del cluster agresivo')

    st.write('# ¿Por qué SP500 ETF?')
    st.write('SP500 ETF - Ticker VOO')
    tickerData1 = yf.Ticker('VOO')
    tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf1.Close)

    st.write('1. Exposición a las 500 empresas más grandes de los EE.UU.')
    st.write('2. El objetivo es replicar el rendimiento del índice S&P 500.')
    st.write('3. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
             'crecimiento a largo plazo.')
    st.write('4. Con un rendimiento anual medio del 15.74% desde el año de lanzamiento.')

    st.write('# ¿Por qué International market ETF?')
    st.write('International market ETF - Ticker IEFA')
    tickerData2 = yf.Ticker('IEFA')
    tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf2.Close)

    st.write('1. Exposición a un amplio rango de empresas de Europa, Australia y Asia.')
    st.write('2. Acceso completo y de bajo costo a valores de renta variable de alta, mediana y baja capitalización de '
             'mercados desarrollados.')
    st.write('3. Hágalo parte fundamental de su cartera para diversificarse internacionalmente y buscar crecimiento a '
             'largo plazo.')
    st.write('4. Con un rendimiento anual medio del 7.56% desde el año de lanzamiento.')

    st.write('# ¿Por qué Bonos?')
    st.write('Rentabilidad bono Estados Unidos a 10 años')
    tickerData4 = yf.Ticker('^TNX')
    tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-2')
    st.line_chart(tickerDf4.Close)

    st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
    st.write('2. Diversifica y reduce la volatilidad del portafolio.')

    st.write('# ¿Por qué BTC?')
    st.write('Bitcoin - Ticker BTC')
    tickerData3 = yf.Ticker('BTC-USD')
    tickerDf3 = tickerData3.history(period='1d', start='2017-1-1', end='2021-5-2')
    st.line_chart(tickerDf3.Close)

    image1 = Image.open('newplot.png')
    st.image(image1, caption='Sharpe Ratio (ROI / Volatilidad) de diferentes activos')

    image2 = Image.open('newplot (1).png')
    st.image(image2, caption='Volatilidad Bitcoin vs otros activos')

    st.write('1. Diversificación, exposición al mercado de las criptomonedas.')
    st.write('2. Alta rentabilidad, con una mayor adopción cada año y con una alta volatilidad pero descendente.')
    st.write('3. Activo deflacionario contra el sistema monetario inflacionario actual, el 24% del total de dólares en '
             'circulación se crearon en 2020.')
