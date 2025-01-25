# Weather Forecast with SMS Notifications

This project is a Python script that retrieves weather forecasts from the WeatherAPI and sends SMS notifications via Twilio. The script focuses on sending information about hours when the temperature exceeds 30°C.

## Features

*   **Forecast Retrieval:** Fetches weather forecasts for a specific location (Mendoza by default) using the WeatherAPI.
*   **Data Filtering:** Filters forecast hours to show only those where the temperature is above 30°C, between 7 AM and 10 PM.
*   **SMS Notifications:** Sends an SMS message via Twilio with the detailed forecast.
*   **Weather Condition Translation:** Translates weather conditions from English to Spanish for easier understanding.

## Project Structure

The project is organized into the following files:

*   `twilio_script.py`: Main script that orchestrates fetching the forecast, data processing, and sending messages.
*   `utils.py`: Contains utility functions for making API requests, processing weather data, and sending SMS messages.
*   `twilio_config.py`: (This file should NOT be uploaded to GitHub) Contains Twilio credentials and the WeatherAPI key. It's recommended to use environment variables for better security.

## Requirements

*   Python 3.6+
*   Python Libraries: `twilio`, `pandas`, `requests`, `tqdm` (install with `pip install -r requirements.txt`)
*   Twilio account.
*   WeatherAPI account.

## Setup and Usage

Para ejecutar el script de forma diaria en un servidor, puedes utilizar una instancia EC2 de AWS. Aquí tienes los pasos básicos:

1.  **Lanzar una instancia EC2:**
    *   Selecciona una AMI (Amazon Machine Image) basada en Linux (ej. Ubuntu).
    *   Elige un tipo de instancia adecuado (t2.micro es suficiente para este script).
    *   Configura el grupo de seguridad para permitir la conexión SSH (puerto 22).
2.  **Conectarse a la instancia EC2 mediante SSH:**
    ```bash
    ssh -i "tu_clave_privada.pem" ubuntu@tu_ip_publica
    ```
3.  **Instalar Python y pip:**
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **Clonar el repositorio:**
    ```bash
    git clone [URL del repositorio]
    cd [nombre del directorio del proyecto]
    ```
5.  **Instalar las dependencias:**
    ```bash
    pip3 install -r requirements.txt
    ```
6.  **Configurar las variables de entorno:**
     ```bash
       export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        export TWILIO_AUTH_TOKEN="your_auth_token"
        export PHONE_NUMBER="+1234567890"
        export API_KEY_WAPI="your_api_key_weather"
     ```
    *   (Reemplaza los valores con tus credenciales).
    *   Para hacer persistentes las variables, considera agregarlas a `~/.bashrc` o `~/.bash_profile`.
7.  **Crear un script ejecutable:**
    *   Crea un archivo llamado `run_script.sh`:
        ```bash
        #!/bin/bash
        python3 /path/to/your/twilio_script.py
        ```
    *   (Reemplaza `/path/to/your/twilio_script.py` con la ruta correcta).
    *   Dale permisos de ejecución al script:
        ```bash
        chmod +x run_script.sh
        ```
8.  **Programar la ejecución del script con cron:**
    *   Abre el crontab:
        ```bash
        crontab -e
        ```
    *   Añade una línea para ejecutar el script diariamente a una hora específica (ej. a las 8 AM):
        ```
        0 8 * * * /path/to/your/run_script.sh
        ```
    *   (Reemplaza `/path/to/your/run_script.sh` con la ruta correcta y ajusta la hora si es necesario).

## Notas Adicionales

*   **Seguridad:** Nunca subas tus credenciales (Twilio SID, token y API key) directamente a GitHub. Utiliza variables de entorno para gestionarlas de manera segura.
*   **API Key:** Obtén una API Key gratuita en [WeatherAPI](https://www.weatherapi.com/).
*   **Flexibilidad:** El código está diseñado para ser fácilmente adaptable a otras ubicaciones. Simplemente modifica el valor de la variable `query` en el archivo `twilio_script.py` si lo deseas.
*   **Limitaciones:**  Esta version del script solo consulta el pronostico para 1 dia.
*   **AWS EC2:** Los pasos proporcionados para AWS EC2 son básicos. Ajusta la configuración de la instancia y las reglas de seguridad según tus necesidades.