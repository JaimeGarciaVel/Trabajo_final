import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from pickle import load
from PIL import Image
import yfinance as yf

st.set_page_config(layout="centered")

st.title('# Robo-advisor')

tipo_inversor = st.selectbox(
    '# ¿Conoce ya su tipo de inversor?',
    ('Sí.', 'No.')
)

if tipo_inversor == 'Sí.':
    graficos_acciones = st.selectbox(
        '# Selecciona el tipo de inversor que eres para ver en qué activos invertir',
        ('Inversor conservador', 'Inversor moderado', 'Inversor agresivo')
    )

    if graficos_acciones == 'Inversor conservador':

        st.write('# Portafolio inversor conservador')
        st.text("")

        fig1, ax1 = plt.subplots(figsize=(10, 6))

        size = 0.3
        vals = np.array([[15, 40], [30, 0], [7.5, 7.5]])

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)
        inner_colors = cmap([1, 2, 5, 6, 9, 10])
        labels = 'Bonos', 'Stock market', 'Commodities'
        labels2 = '15% US Bond intermediate-term (IEI)', '40% US Bond long-term (TLT)', '30% US large cap (VTI)', '', \
                  '7,5% Gold (GLD)', '7,5% Other commodities (GSG)'

        ax1.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax1.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax1.set(aspect="equal")

        st.pyplot(fig1)

        st.write('# Rendimiento portfolio')

        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')

        cons = tickerDf2['Close'] * 0.40 + tickerDf1['Close'] * 0.3 + tickerDf3['Close'] * 0.15 + tickerDf4[
            'Close'] * 0.075 + \
               tickerDf5['Close'] * 0.075
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.plot(cons)
        st.pyplot(fig4)
        st.write('1. Portfolio compuesto de un 30% de stocks, 55% de bonos y 15% de commodities.')
        st.write(
            '2. Portfolio resistente a las crisis, el peor año ha sido el 2015 con una caída de un -3.73% y el mejor '
            'año ha sido el 2019 con una subida del 18.22%.')
        st.write(
            '3. Con un rendimiento anual medio en los últimos 10 años del 7.22% y un rendimiento total del 107.09%.')

        st.write('# ¿Por qué Stock market?')
        st.write('➤Total US stock market ETF - Ticker VTI')
        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf1.Close)

        st.write(
            '1. Exposición al mercado americano, con empresas large-, mid- y small-caps con estilos value y growth.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
                 'crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.8%.')
        st.write(
            '4. Diversificación por sectores: Technology (25.5%), Consumer Discretionary (16.4%), Industrials (14.2%),'
            ' Health Care (13.1%), Financials (11.9%), Consumer Staples (5%), Real Estate (3.4%), Utilities (2.9%), '
            'Energy(2.8%), Telecommunications (2.6%), Basic Materials (2.2%).')
        st.write('5. Top 10 valores en el ETF: Apple, Microsoft, Amazon, Alphabet, Facebook, Tesla, Berkshire Hathaway,'
                 ' JPMorgan Chase, Johnson & Johnson y Visa.')

        st.write('# ¿Por qué Bonos?')
        st.write('➤Bono EEU. UU. largo plazo - Ticker TLT')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf2.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a largo (20 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 6.66%.')

        st.text("")

        st.write('➤Bono EEU. UU. medio plazo - Ticker IEI')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf3.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a medio (3-7 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 2.68%.')

        st.write('# ¿Por qué Commodities?')
        st.write('➤Oro - Ticker GLD')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf4.Close)

        st.write('1. Exposición al mercado del oro.')
        st.write('3. Diversifica el portafolio.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')

        st.text("")

        st.write('➤Other commodities - Ticker GSG')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf5.Close)

        st.write('1. Exposición a un amplio rango de mercancías, diversificando el portafolio.')
        st.write('2. Acceso a mercados de energía, metales industriales y preciosos, agricultura y ganadería.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')
        st.write(
            '4. Compuesto por: Energía (53.64%), Agricultura (21.55%), Metales industriales (12.55%), Ganado (7.04%) y'
            ' Metales Preciosos (5.22%).')


    elif graficos_acciones == 'Inversor moderado':

        st.write('# Portafolio inversor moderado')
        st.text("")
        fig2, ax2 = plt.subplots(figsize=(10, 6))

        size = 0.3
        vals = np.array([[10, 25, 0], [10, 30, 15], [5, 5, 0]])

        a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
        outer_colors = [a(0.6), b(0.6), c(0.6)]
        inner_colors = [a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), b(0.3), c(0.5), c(0.4)]
        labels = 'Bonos', 'Stock market', 'Commodities'
        labels2 = '10% US Bond intermediate-term (IEI)', '25% US Bond long-term (TLT)', '', '10% Real Estate (VNQ)', \
                  '30% US large cap (VTI)', '15% International large cap (VEU)', '5% Gold (GLD)', \
                  '5% Other commodities (GSG)', ''

        ax2.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax2.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax2.set(aspect="equal")
        st.pyplot(fig2)

        st.write('# Rendimiento portfolio')

        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')

        cons = tickerDf2['Close'] * 0.25 + tickerDf1['Close'] * 0.3 + tickerDf3['Close'] * 0.1 + tickerDf4[
            'Close'] * 0.05 + \
               tickerDf5['Close'] * 0.05 + tickerDf6['Close'] * 0.1 + tickerDf7['Close'] * 0.15
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.plot(cons)
        st.pyplot(fig4)
        st.write('1. Portfolio compuesto de un 55% de stocks, 35% de bonos y 10% de commodities.')
        st.write(
            '2. Portfolio con caídas moderadas en las crisis, con gran diversificación en el mercado estadounidense e '
            'internacional.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 8.4% y un rendimiento total del 123.7%.')

        st.write('# ¿Por qué Stock market?')
        st.write('➤Total US stock market ETF - Ticker VTI')
        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf1.Close)

        st.write(
            '1. Exposición al mercado americano, con empresas large-, mid- y small-caps con estilos value y growth.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
                 'crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.8%.')
        st.write(
            '4. Diversificación por sectores: Technology (25.5%), Consumer Discretionary (16.4%), Industrials (14.2%),'
            ' Health Care (13.1%), Financials (11.9%), Consumer Staples (5%), Real Estate (3.4%), Utilities (2.9%), '
            'Energy(2.8%), Telecommunications (2.6%), Basic Materials (2.2%).')
        st.write(
            '5. Top 10 valores en el ETF: Apple, Microsoft, Amazon, Alphabet, Facebook, Tesla, Berkshire Hathaway, '
            ' JPMorgan Chase, Johnson & Johnson y Visa ')

        st.text("")

        st.write('➤Real Estate - Ticker VNQ')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf6.Close)

        st.write(
            '1. Exposición al mercado de real estate americano, con empresas que compran edificios, hoteles y otras '
            'propiedades.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse y buscar crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 9%.')
        st.write(
            '4. Top 10 valores en el ETF: Vanguard Real Estate II Index Fund, American Tower Corp., Prologis, Crown '
            'Castle International Corp, Equinix, Public Storage, Digital Realty Trust, Simon Property Group, SBA '
            'Communications Corp. y Welltower.')

        st.text("")

        st.write('➤International stock market ETF - Ticker VEU')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf7.Close)

        st.write('1. Exposición al mercado de valores internacional, con empresas large-, mid- y small-caps.')
        st.write(
            '2. Hágalo parte fundamental de su cartera para diversificarse en mercados desarrollados y en desarrollo, '
            'excluyendo EE. UU..')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 5.23%.')
        st.write(
            '4. Diversificación por regiones: Emerging Markets (25.7%), Europe (39.1%), Pacific (28.6%), North America'
            ' (5.6%), Middle East (0.3%) y Otros (0.7%).')
        st.write(
            '5. Top 10 valores en el ETF: Taiwan Semiconductor Manufacturing, Tencent Holdings, Alibaba Group Holding,'
            ' Samsung Electronics, Nestle, ASML Holding, Roche Holding, Toyota Motor Corp., Novartis y LVMH.')

        st.write('# ¿Por qué Bonos?')
        st.write('➤Bono EEU. UU. largo plazo - Ticker TLT')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf2.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a largo (20 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 6.66%.')

        st.text("")

        st.write('➤Bono EEU. UU. medio plazo - Ticker IEI')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf3.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a medio (3-7 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 2.68%.')

        st.write('# ¿Por qué Commodities?')
        st.write('➤Oro - Ticker GLD')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf4.Close)

        st.write('1. Exposición al mercado del oro.')
        st.write('3. Diversifica el portafolio.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')

        st.text("")

        st.write('➤Other commodities - Ticker GSG')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf5.Close)

        st.write('1. Exposición a un amplio rango de mercancías, diversificando el portafolio.')
        st.write('2. Acceso a mercados de energía, metales industriales y preciosos, agricultura y ganadería.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')
        st.write(
            '4. Compuesto por: Energía (53.64%), Agricultura (21.55%), Metales industriales (12.55%), Ganado (7.04%) y'
            ' Metales Preciosos (5.22%).')


    else:

        st.write('# Portafolio inversor agresivo')
        st.text("")
        fig3, ax3 = plt.subplots(figsize=(10, 6))

        size = 0.3
        vals = np.array([[5, 15, 0, 0], [10, 35, 15, 10], [5, 5, 0, 0]])

        a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
        outer_colors = [a(0.6), b(0.6), c(0.6)]
        inner_colors = [a(0.5), a(0.4), a(0.3), a(0.2), b(0.5), b(0.4), b(0.3), b(0.2), c(0.5), c(0.4), c(0.3), c(0.2)]
        labels = 'Bonos', 'Stock market', 'Commodities'
        labels2 = '5% US Bond intermediate-term (IEI)', '15% US Bond long-term (TLT)', '', '', '10% Real Estate (VNQ)', \
                  '35% US large cap (VTI)', '15% International large cap (VEU)', '10% US small cap (IJT)', \
                  '5% Gold (GLD)', '5% Other commodities (GSG)', '', ''

        ax3.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax3.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax3.set(aspect="equal")
        st.pyplot(fig3)

        st.write('# Rendimiento portfolio')

        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData8 = yf.Ticker('IJT')
        tickerDf8 = tickerData8.history(period='1d', start='2011-1-1', end='2021-5-13')

        cons = tickerDf2['Close'] * 0.15 + tickerDf1['Close'] * 0.35 + tickerDf3['Close'] * 0.05 + tickerDf4[
            'Close'] * 0.05 + \
               tickerDf5['Close'] * 0.05 + tickerDf6['Close'] * 0.1 + tickerDf7['Close'] * 0.15 + tickerDf8[
                   'Close'] * 0.1
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.plot(cons)
        st.pyplot(fig4)
        st.write('1. Portfolio compuesto de un 70% de stocks, 20% de bonos y 10% de commodities.')
        st.write('2. Portfolio volátil, con alto riesgo pero también con alto rendimiento.')
        st.write(
            '3. Con un rendimiento anual medio en los últimos 10 años del 9.75% y un rendimiento total del 154.54%.')

        st.write('# ¿Por qué Stock market?')
        st.write('➤Total US stock market ETF - Ticker VTI')
        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf1.Close)

        st.write(
            '1. Exposición al mercado americano, con empresas large-, mid- y small-caps con estilos value y growth.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
                 'crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.8%.')
        st.write(
            '4. Diversificación por sectores: Technology (25.5%), Consumer Discretionary (16.4%), Industrials (14.2%),'
            ' Health Care (13.1%), Financials (11.9%), Consumer Staples (5%), Real Estate (3.4%), Utilities (2.9%), '
            'Energy(2.8%), Telecommunications (2.6%), Basic Materials (2.2%).')
        st.write(
            '5. Top 10 valores en el ETF: Apple, Microsoft, Amazon, Alphabet, Facebook, Tesla, Berkshire Hathaway, '
            ' JPMorgan Chase, Johnson & Johnson y Visa ')

        st.text("")

        st.write('➤Real Estate - Ticker VNQ')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf6.Close)

        st.write(
            '1. Exposición al mercado de real estate americano, con empresas que compran edificios, hoteles y otras '
            'propiedades.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse y buscar crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 9%.')
        st.write(
            '4. Top 10 valores en el ETF: Vanguard Real Estate II Index Fund, American Tower Corp., Prologis, Crown '
            'Castle International Corp, Equinix, Public Storage, Digital Realty Trust, Simon Property Group, SBA '
            'Communications Corp. y Welltower.')

        st.text("")

        st.write('➤International stock market ETF - Ticker VEU')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf7.Close)

        st.write('1. Exposición al mercado de valores internacional, con empresas large-, mid- y small-caps.')
        st.write(
            '2. Hágalo parte fundamental de su cartera para diversificarse en mercados desarrollados y en desarrollo, '
            'excluyendo EE. UU..')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 5.23%.')
        st.write(
            '4. Diversificación por regiones: Emerging Markets (25.7%), Europe (39.1%), Pacific (28.6%), North America'
            ' (5.6%), Middle East (0.3%) y Otros (0.7%).')
        st.write(
            '5. Top 10 valores en el ETF: Taiwan Semiconductor Manufacturing, Tencent Holdings, Alibaba Group Holding,'
            ' Samsung Electronics, Nestle, ASML Holding, Roche Holding, Toyota Motor Corp., Novartis y LVMH.')

        st.text("")

        st.write('➤US small cap ETF - Ticker IJT')
        tickerData8 = yf.Ticker('IJT')
        tickerDf8 = tickerData8.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf8.Close)

        st.write(
            '1. Exposición a pequeñas empresas de EE. UU. cuyas ganancias se espera que aumenten a una tasa superior '
            'al promedio en comparación con el mercado.')
        st.write(
            '2. Hágalo parte fundamental de su cartera para diversificarse en acciones estadounidenses y para orientar'
            ' su cartera hacia acciones "growth".')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.55%.')
        st.write(
            '4. Diversificación por sector: Industrial (18.67%), Tecnología (18.01%), Consumer discretionary (17.01%),'
            ' Health Care (16.74%), Financieros (9.97%), Inmobiliario (5.45%), Productos básicos de consumo (4.7%), '
            'Materiales (4.17%), Energía (2.14%), Comunicación (2.14%) y Servivios (1%).')

        st.write('# ¿Por qué Bonos?')
        st.write('➤Bono EEU. UU. largo plazo - Ticker TLT')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf2.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a largo (20 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 6.66%.')

        st.text("")

        st.write('➤Bono EEU. UU. medio plazo - Ticker IEI')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf3.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a medio (3-7 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 2.68%.')

        st.write('# ¿Por qué Commodities?')
        st.write('➤Oro - Ticker GLD')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf4.Close)

        st.write('1. Exposición al mercado del oro.')
        st.write('3. Diversifica el portafolio.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')

        st.text("")

        st.write('➤Other commodities - Ticker GSG')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf5.Close)

        st.write('1. Exposición a un amplio rango de mercancías, diversificando el portafolio.')
        st.write('2. Acceso a mercados de energía, metales industriales y preciosos, agricultura y ganadería.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')
        st.write(
            '4. Compuesto por: Energía (53.64%), Agricultura (21.55%), Metales industriales (12.55%), Ganado (7.04%) y'
            ' Metales Preciosos (5.22%).')

        st.write('# ¿Se puede añadir BTC a mi portfolio?')
        st.write('Bitcoin - Ticker BTC')
        tickerData9 = yf.Ticker('BTC-USD')
        tickerDf9 = tickerData9.history(period='1d', start='2017-1-1', end='2021-5-13')
        st.line_chart(tickerDf9.Close)

        image1 = Image.open('newplot.png')
        st.image(image1, caption='Sharpe Ratio (ROI / Volatilidad) de diferentes activos')

        image2 = Image.open('newplot (1).png')
        st.image(image2, caption='Volatilidad Bitcoin vs otros activos')

        st.write(' Es recomendable por estas razones:')
        st.write('1. Diversificación, exposición al mercado de las criptomonedas.')
        st.write('2. Alta rentabilidad, con una mayor adopción cada año y con una alta volatilidad pero descendente.')
        st.write(
            '3. Activo deflacionario contra el sistema monetario inflacionario actual, el 24% del total de dólares en '
            'circulación se crearon en 2020.')
else:
    st.write("# Complete el cuestionario")

    Sexo = st.select_slider('Sexo', options=['Hombre', 'Mujer'])
    Edad = st.select_slider('Edad', options=['<35', '35-44', '45-54', '55-64', '65-74', '>75'])
    Educacion = st.select_slider('Educación', options=['ESO', 'Bachillerato', 'FP Grado superior', 'Grado Universidad'])
    Casado = st.select_slider('Estado civil', options=['Casado', 'Soltero/Divorciado/Viudo'])
    Hijos = st.select_slider('Número de hijos', options=[0, 1, 2, 3, 4, 5, 6, 7])
    Raza = st.select_slider('Raza', options=['Caucásico', 'Afroamericano', 'Hispano', 'Otro'])
    Trabajo = st.select_slider('Estado laboral',
                               options=['Contratado', 'Autónomo/empresario', 'Estudiante/jubilado',
                                        'Desempleado'])
    Conocimiento = st.select_slider('De 1 a 10 cómo es tu conocimiento financiero',
                                    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Risk = st.select_slider('De 1 a 4 cúanto estarías dispuesto a tomar riesgos financieros',
                            options=['1', '2', '3', '4'])
    Patrimonio = st.select_slider('Patrimonio neto', options=['<5.000 €', 'Entre 5.000 € y 75.000 €',
                                                              'Entre 75.000 € y 180.000 €',
                                                              'Entre 180.000 € y 370.000 €',
                                                              'Entre 370.000 € y 1.350.000 €'])
    Renta = st.select_slider('Renta mensual', options=['<900 €', 'Entre 900 € y 1.350 €', 'Entre 1.350 € y 1.700 €',
                                                       'Entre 1.700 € y 2.400 €', 'Entre 2.400 € y 3.500 €',
                                                       '>3.500 €'])

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
    def prediction(Sexo, Edad, Educacion, Casado, Hijos, Raza, Trabajo, Conocimiento, YesRisk, NoRisk, Patrimonio,
                   Renta):

        lst = [[Sexo, Edad, Educacion, Casado, Hijos, Raza, Trabajo, Conocimiento, YesRisk, NoRisk, Patrimonio, Renta]]
        X = pd.DataFrame(lst,
                         columns=['HHSEX', 'AGECL', 'EDCL', 'MARRIED', 'KIDS', 'RACE', 'OCCAT1', 'KNOWL', 'YESFINRISK',
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
        '# Selecciona el tipo de inversor que eres para ver en qué activos invertir',
        ('Inversor conservador', 'Inversor moderado', 'Inversor agresivo')
    )

    if graficos_acciones == 'Inversor conservador':

        st.write('# Portafolio inversor conservador')
        st.text("")

        fig1, ax1 = plt.subplots(figsize=(10, 6))

        size = 0.3
        vals = np.array([[15, 40], [30, 0], [7.5, 7.5]])

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)
        inner_colors = cmap([1, 2, 5, 6, 9, 10])
        labels = 'Bonos', 'Stock market', 'Commodities'
        labels2 = '15% US Bond intermediate-term (IEI)', '40% US Bond long-term (TLT)', '30% US large cap (VTI)', '', \
                  '7,5% Gold (GLD)', '7,5% Other commodities (GSG)'

        ax1.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax1.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax1.set(aspect="equal")

        st.pyplot(fig1)

        st.write('# Rendimiento portfolio')

        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')

        cons = tickerDf2['Close'] * 0.40 + tickerDf1['Close'] * 0.3 + tickerDf3['Close'] * 0.15 + tickerDf4[
            'Close'] * 0.075 + \
               tickerDf5['Close'] * 0.075
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.plot(cons)
        st.pyplot(fig4)
        st.write('1. Portfolio compuesto de un 30% de stocks, 55% de bonos y 15% de commodities.')
        st.write(
            '2. Portfolio resistente a las crisis, el peor año ha sido el 2015 con una caída de un -3.73% y el mejor '
            'año ha sido el 2019 con una subida del 18.22%.')
        st.write(
            '3. Con un rendimiento anual medio en los últimos 10 años del 7.22% y un rendimiento total del 107.09%.')

        st.write('# ¿Por qué Stock market?')
        st.write('➤Total US stock market ETF - Ticker VTI')
        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf1.Close)

        st.write(
            '1. Exposición al mercado americano, con empresas large-, mid- y small-caps con estilos value y growth.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
                 'crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.8%.')
        st.write(
            '4. Diversificación por sectores: Technology (25.5%), Consumer Discretionary (16.4%), Industrials (14.2%),'
            ' Health Care (13.1%), Financials (11.9%), Consumer Staples (5%), Real Estate (3.4%), Utilities (2.9%), '
            'Energy(2.8%), Telecommunications (2.6%), Basic Materials (2.2%).')
        st.write('5. Top 10 valores en el ETF: Apple, Microsoft, Amazon, Alphabet, Facebook, Tesla, Berkshire Hathaway,'
                 ' JPMorgan Chase, Johnson & Johnson y Visa.')

        st.write('# ¿Por qué Bonos?')
        st.write('➤Bono EEU. UU. largo plazo - Ticker TLT')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf2.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a largo (20 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 6.66%.')

        st.text("")

        st.write('➤Bono EEU. UU. medio plazo - Ticker IEI')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf3.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a medio (3-7 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 2.68%.')

        st.write('# ¿Por qué Commodities?')
        st.write('➤Oro - Ticker GLD')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf4.Close)

        st.write('1. Exposición al mercado del oro.')
        st.write('3. Diversifica el portafolio.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')

        st.text("")

        st.write('➤Other commodities - Ticker GSG')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf5.Close)

        st.write('1. Exposición a un amplio rango de mercancías, diversificando el portafolio.')
        st.write('2. Acceso a mercados de energía, metales industriales y preciosos, agricultura y ganadería.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')
        st.write(
            '4. Compuesto por: Energía (53.64%), Agricultura (21.55%), Metales industriales (12.55%), Ganado (7.04%) y'
            ' Metales Preciosos (5.22%).')


    elif graficos_acciones == 'Inversor moderado':

        st.write('# Portafolio inversor moderado')
        st.text("")
        fig2, ax2 = plt.subplots(figsize=(10, 6))

        size = 0.3
        vals = np.array([[10, 25, 0], [10, 30, 15], [5, 5, 0]])

        a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
        outer_colors = [a(0.6), b(0.6), c(0.6)]
        inner_colors = [a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), b(0.3), c(0.5), c(0.4)]
        labels = 'Bonos', 'Stock market', 'Commodities'
        labels2 = '10% US Bond intermediate-term (IEI)', '25% US Bond long-term (TLT)', '', '10% Real Estate (VNQ)', \
                  '30% US large cap (VTI)', '15% International large cap (VEU)', '5% Gold (GLD)', \
                  '5% Other commodities (GSG)', ''

        ax2.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax2.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax2.set(aspect="equal")
        st.pyplot(fig2)

        st.write('# Rendimiento portfolio')

        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')

        cons = tickerDf2['Close'] * 0.25 + tickerDf1['Close'] * 0.3 + tickerDf3['Close'] * 0.1 + tickerDf4[
            'Close'] * 0.05 + \
               tickerDf5['Close'] * 0.05 + tickerDf6['Close'] * 0.1 + tickerDf7['Close'] * 0.15
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.plot(cons)
        st.pyplot(fig4)
        st.write('1. Portfolio compuesto de un 55% de stocks, 35% de bonos y 10% de commodities.')
        st.write(
            '2. Portfolio con caídas moderadas en las crisis, con gran diversificación en el mercado estadounidense e '
            'internacional.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 8.4% y un rendimiento total del 123.7%.')

        st.write('# ¿Por qué Stock market?')
        st.write('➤Total US stock market ETF - Ticker VTI')
        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf1.Close)

        st.write(
            '1. Exposición al mercado americano, con empresas large-, mid- y small-caps con estilos value y growth.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
                 'crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.8%.')
        st.write(
            '4. Diversificación por sectores: Technology (25.5%), Consumer Discretionary (16.4%), Industrials (14.2%),'
            ' Health Care (13.1%), Financials (11.9%), Consumer Staples (5%), Real Estate (3.4%), Utilities (2.9%), '
            'Energy(2.8%), Telecommunications (2.6%), Basic Materials (2.2%).')
        st.write(
            '5. Top 10 valores en el ETF: Apple, Microsoft, Amazon, Alphabet, Facebook, Tesla, Berkshire Hathaway, '
            ' JPMorgan Chase, Johnson & Johnson y Visa ')

        st.text("")

        st.write('➤Real Estate - Ticker VNQ')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf6.Close)

        st.write(
            '1. Exposición al mercado de real estate americano, con empresas que compran edificios, hoteles y otras '
            'propiedades.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse y buscar crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 9%.')
        st.write(
            '4. Top 10 valores en el ETF: Vanguard Real Estate II Index Fund, American Tower Corp., Prologis, Crown '
            'Castle International Corp, Equinix, Public Storage, Digital Realty Trust, Simon Property Group, SBA '
            'Communications Corp. y Welltower.')

        st.text("")

        st.write('➤International stock market ETF - Ticker VEU')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf7.Close)

        st.write('1. Exposición al mercado de valores internacional, con empresas large-, mid- y small-caps.')
        st.write(
            '2. Hágalo parte fundamental de su cartera para diversificarse en mercados desarrollados y en desarrollo, '
            'excluyendo EE. UU..')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 5.23%.')
        st.write(
            '4. Diversificación por regiones: Emerging Markets (25.7%), Europe (39.1%), Pacific (28.6%), North America'
            ' (5.6%), Middle East (0.3%) y Otros (0.7%).')
        st.write(
            '5. Top 10 valores en el ETF: Taiwan Semiconductor Manufacturing, Tencent Holdings, Alibaba Group Holding,'
            ' Samsung Electronics, Nestle, ASML Holding, Roche Holding, Toyota Motor Corp., Novartis y LVMH.')

        st.write('# ¿Por qué Bonos?')
        st.write('➤Bono EEU. UU. largo plazo - Ticker TLT')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf2.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a largo (20 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 6.66%.')

        st.text("")

        st.write('➤Bono EEU. UU. medio plazo - Ticker IEI')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf3.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a medio (3-7 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 2.68%.')

        st.write('# ¿Por qué Commodities?')
        st.write('➤Oro - Ticker GLD')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf4.Close)

        st.write('1. Exposición al mercado del oro.')
        st.write('3. Diversifica el portafolio.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')

        st.text("")

        st.write('➤Other commodities - Ticker GSG')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf5.Close)

        st.write('1. Exposición a un amplio rango de mercancías, diversificando el portafolio.')
        st.write('2. Acceso a mercados de energía, metales industriales y preciosos, agricultura y ganadería.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')
        st.write(
            '4. Compuesto por: Energía (53.64%), Agricultura (21.55%), Metales industriales (12.55%), Ganado (7.04%) y'
            ' Metales Preciosos (5.22%).')


    else:

        st.write('# Portafolio inversor agresivo')
        st.text("")
        fig3, ax3 = plt.subplots(figsize=(10, 6))

        size = 0.3
        vals = np.array([[5, 15, 0, 0], [10, 35, 15, 10], [5, 5, 0, 0]])

        a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
        outer_colors = [a(0.6), b(0.6), c(0.6)]
        inner_colors = [a(0.5), a(0.4), a(0.3), a(0.2), b(0.5), b(0.4), b(0.3), b(0.2), c(0.5), c(0.4), c(0.3), c(0.2)]
        labels = 'Bonos', 'Stock market', 'Commodities'
        labels2 = '5% US Bond intermediate-term (IEI)', '15% US Bond long-term (TLT)', '', '', '10% Real Estate (VNQ)', \
                  '35% US large cap (VTI)', '15% International large cap (VEU)', '10% US small cap (IJT)', \
                  '5% Gold (GLD)', '5% Other commodities (GSG)', '', ''

        ax3.pie(vals.sum(axis=1), radius=1 - size, labels=labels, colors=outer_colors, labeldistance=0.65,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax3.pie(vals.flatten(), radius=1, labels=labels2, colors=inner_colors,
                wedgeprops=dict(width=size, edgecolor='w'))

        ax3.set(aspect="equal")
        st.pyplot(fig3)

        st.write('# Rendimiento portfolio')

        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')
        tickerData8 = yf.Ticker('IJT')
        tickerDf8 = tickerData8.history(period='1d', start='2011-1-1', end='2021-5-13')

        cons = tickerDf2['Close'] * 0.15 + tickerDf1['Close'] * 0.35 + tickerDf3['Close'] * 0.05 + tickerDf4[
            'Close'] * 0.05 + \
               tickerDf5['Close'] * 0.05 + tickerDf6['Close'] * 0.1 + tickerDf7['Close'] * 0.15 + tickerDf8[
                   'Close'] * 0.1
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.plot(cons)
        st.pyplot(fig4)
        st.write('1. Portfolio compuesto de un 70% de stocks, 20% de bonos y 10% de commodities.')
        st.write('2. Portfolio volátil, con alto riesgo pero también con alto rendimiento.')
        st.write(
            '3. Con un rendimiento anual medio en los últimos 10 años del 9.75% y un rendimiento total del 154.54%.')

        st.write('# ¿Por qué Stock market?')
        st.write('➤Total US stock market ETF - Ticker VTI')
        tickerData1 = yf.Ticker('VTI')
        tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf1.Close)

        st.write(
            '1. Exposición al mercado americano, con empresas large-, mid- y small-caps con estilos value y growth.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse en el mercado estadounidense y buscar '
                 'crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.8%.')
        st.write(
            '4. Diversificación por sectores: Technology (25.5%), Consumer Discretionary (16.4%), Industrials (14.2%),'
            ' Health Care (13.1%), Financials (11.9%), Consumer Staples (5%), Real Estate (3.4%), Utilities (2.9%), '
            'Energy(2.8%), Telecommunications (2.6%), Basic Materials (2.2%).')
        st.write(
            '5. Top 10 valores en el ETF: Apple, Microsoft, Amazon, Alphabet, Facebook, Tesla, Berkshire Hathaway, '
            ' JPMorgan Chase, Johnson & Johnson y Visa ')

        st.text("")

        st.write('➤Real Estate - Ticker VNQ')
        tickerData6 = yf.Ticker('VNQ')
        tickerDf6 = tickerData6.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf6.Close)

        st.write(
            '1. Exposición al mercado de real estate americano, con empresas que compran edificios, hoteles y otras '
            'propiedades.')
        st.write('2. Hágalo parte fundamental de su cartera para diversificarse y buscar crecimiento a largo plazo.')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 9%.')
        st.write(
            '4. Top 10 valores en el ETF: Vanguard Real Estate II Index Fund, American Tower Corp., Prologis, Crown '
            'Castle International Corp, Equinix, Public Storage, Digital Realty Trust, Simon Property Group, SBA '
            'Communications Corp. y Welltower.')

        st.text("")

        st.write('➤International stock market ETF - Ticker VEU')
        tickerData7 = yf.Ticker('VEU')
        tickerDf7 = tickerData7.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf7.Close)

        st.write('1. Exposición al mercado de valores internacional, con empresas large-, mid- y small-caps.')
        st.write(
            '2. Hágalo parte fundamental de su cartera para diversificarse en mercados desarrollados y en desarrollo, '
            'excluyendo EE. UU..')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 5.23%.')
        st.write(
            '4. Diversificación por regiones: Emerging Markets (25.7%), Europe (39.1%), Pacific (28.6%), North America'
            ' (5.6%), Middle East (0.3%) y Otros (0.7%).')
        st.write(
            '5. Top 10 valores en el ETF: Taiwan Semiconductor Manufacturing, Tencent Holdings, Alibaba Group Holding,'
            ' Samsung Electronics, Nestle, ASML Holding, Roche Holding, Toyota Motor Corp., Novartis y LVMH.')

        st.text("")

        st.write('➤US small cap ETF - Ticker IJT')
        tickerData8 = yf.Ticker('IJT')
        tickerDf8 = tickerData8.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf8.Close)

        st.write(
            '1. Exposición a pequeñas empresas de EE. UU. cuyas ganancias se espera que aumenten a una tasa superior '
            'al promedio en comparación con el mercado.')
        st.write(
            '2. Hágalo parte fundamental de su cartera para diversificarse en acciones estadounidenses y para orientar'
            ' su cartera hacia acciones "growth".')
        st.write('3. Con un rendimiento anual medio en los últimos 10 años del 13.55%.')
        st.write(
            '4. Diversificación por sector: Industrial (18.67%), Tecnología (18.01%), Consumer discretionary (17.01%),'
            ' Health Care (16.74%), Financieros (9.97%), Inmobiliario (5.45%), Productos básicos de consumo (4.7%), '
            'Materiales (4.17%), Energía (2.14%), Comunicación (2.14%) y Servivios (1%).')

        st.write('# ¿Por qué Bonos?')
        st.write('➤Bono EEU. UU. largo plazo - Ticker TLT')
        tickerData2 = yf.Ticker('TLT')
        tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf2.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a largo (20 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 6.66%.')

        st.text("")

        st.write('➤Bono EEU. UU. medio plazo - Ticker IEI')
        tickerData3 = yf.Ticker('IEI')
        tickerDf3 = tickerData3.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf3.Close)

        st.write('1. Inversión segura, activo que proporciona estabilidad y ofrece un flujo de ingresos predecible.')
        st.write('2. Diversifica y reduce la volatilidad del portafolio.')
        st.write('3. Exposición a los Bonos de Tesoro de EE.UU. a medio (3-7 años) plazo.')
        st.write('4. Con un rendimiento anual medio en los últimos 10 años del 2.68%.')

        st.write('# ¿Por qué Commodities?')
        st.write('➤Oro - Ticker GLD')
        tickerData4 = yf.Ticker('GLD')
        tickerDf4 = tickerData4.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf4.Close)

        st.write('1. Exposición al mercado del oro.')
        st.write('3. Diversifica el portafolio.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')

        st.text("")

        st.write('➤Other commodities - Ticker GSG')
        tickerData5 = yf.Ticker('GSG')
        tickerDf5 = tickerData5.history(period='1d', start='2011-1-1', end='2021-5-13')
        st.line_chart(tickerDf5.Close)

        st.write('1. Exposición a un amplio rango de mercancías, diversificando el portafolio.')
        st.write('2. Acceso a mercados de energía, metales industriales y preciosos, agricultura y ganadería.')
        st.write('3. Buena actuación en épocas de crecimiento económico y/o alta inflación.')
        st.write(
            '4. Compuesto por: Energía (53.64%), Agricultura (21.55%), Metales industriales (12.55%), Ganado (7.04%) y'
            ' Metales Preciosos (5.22%).')

        st.write('# ¿Se puede añadir BTC a mi portfolio?')
        st.write('Bitcoin - Ticker BTC')
        tickerData9 = yf.Ticker('BTC-USD')
        tickerDf9 = tickerData9.history(period='1d', start='2017-1-1', end='2021-5-13')
        st.line_chart(tickerDf9.Close)

        image1 = Image.open('newplot.png')
        st.image(image1, caption='Sharpe Ratio (ROI / Volatilidad) de diferentes activos')

        image2 = Image.open('newplot (1).png')
        st.image(image2, caption='Volatilidad Bitcoin vs otros activos')

        st.write(' Es recomendable por estas razones:')
        st.write('1. Diversificación, exposición al mercado de las criptomonedas.')
        st.write('2. Alta rentabilidad, con una mayor adopción cada año y con una alta volatilidad pero descendente.')
        st.write(
            '3. Activo deflacionario contra el sistema monetario inflacionario actual, el 24% del total de dólares en '
            'circulación se crearon en 2020.')




