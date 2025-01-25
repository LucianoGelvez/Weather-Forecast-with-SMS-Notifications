from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, API_KEY_WAPI
import pandas as pd
from tqdm import tqdm
from utils import request_wapi, get_forecast, create_df, send_message, get_date

query = 'Mendoza'
api_key = API_KEY_WAPI

input_date= get_date()
response = request_wapi(api_key,query)

datos = []

for i in tqdm(range(24),colour = 'aqua'):

    datos.append(get_forecast(response,i))


df_hot = create_df(datos)

# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_hot,query,PHONE_NUMBER)


if message_id:
    print('Mensaje Enviado con exito ' + message_id)
else:
    print('Error al enviar el mensaje')