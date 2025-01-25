import pandas as pd
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, API_KEY_WAPI
from datetime import datetime
import requests

def get_date():
    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_wapi(api_key,query):
    url_clima = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'
    try :
        response = requests.get(url_clima).json()
    except Exception as e:
        print(e)
        return None

    return response

def get_forecast(response,i):
    fecha = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
    hora = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
    condicion = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
    tempe = response['forecast']['forecastday'][0]['hour'][i]['temp_c']
    rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
    prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']

    return fecha,hora,condicion,tempe,rain,prob_rain

def create_df(data):
    col = ['Fecha','Hora','Condicion','Temperatura','Lluvia','prob_lluvia']
    df = pd.DataFrame(data,columns=col)
    df = df.sort_values(by = 'Hora',ascending = True)

    df_hot =  df[(df['Temperatura']>30) & (df['Hora']>6) & (df['Hora']< 22)]
    df_hot = df_hot[['Hora','Temperatura','Condicion']]
    df_hot.set_index('Hora', inplace = True)

    return df_hot

def send_message(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, input_date, df, query, PHONE_NUMBER):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    traducciones = {
        "Sunny": "Soleado",
        "Partly cloudy": "Parcialmente nublado",
        "Cloudy": "Nublado",
        "Overcast": "Cubierto",
        "Patchy rain nearby": "Lluvia dispersa cercana",
        "Light rain": "Lluvia ligera",
        "Heavy rain": "Lluvia intensa",
        "Thunderstorm": "Tormenta eléctrica",
        "Fog": "Niebla",
        "Snow": "Nieve"
    }

    # Contar cuántas veces aparece cada condición climática
    condiciones_contadas = df['Condicion'].value_counts()

    # Determinar la condición más frecuente y traducirla
    condicion_predominante = condiciones_contadas.idxmax()
    condicion_traducida = traducciones.get(condicion_predominante, condicion_predominante)  # Si no está en el diccionario, deja el original

    # Construir el mensaje
    mensaje = f"🌞🌤️☁️🌧️\n\nHola! \n\nLas horas donde la temperatura en Mendoza será superior a 30°C el día {input_date} son:\n\n"

    # Agregar los datos de cada hora con temperatura mayor a 30°C y traducir condiciones
    for hora, fila in df.iterrows():
        condicion_es = traducciones.get(fila['Condicion'], fila['Condicion'])
        mensaje += f"🕒 {hora}: {fila['Temperatura']}°C - {condicion_es}\n"

    mensaje += f"\n🔎 El clima predominante en esas horas será: {condicion_traducida}."

    try:
        message = client.messages.create(
            to=PHONE_NUMBER,
            from_="+12345678",
            body=mensaje
        )
        print(mensaje)
        return message.sid
    except Exception as e:
        print(e)
        return None