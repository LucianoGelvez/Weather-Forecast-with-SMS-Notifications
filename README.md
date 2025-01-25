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

1.  **Clone the repository:**
    ```bash
    git clone [Repository URL]
    cd [project directory name]
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Create a `twilio_config.py` file (Do NOT upload to GitHub):**
    *   In this file, define the following variables with your credentials:
        ```python
        TWILIO_ACCOUNT_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' 
        TWILIO_AUTH_TOKEN = 'your_auth_token'  
        PHONE_NUMBER = '+1234567890'  
        API_KEY_WAPI = 'your_api_key_weather' 
       ```
4.  **Run the script:**
    ```bash
    python twilio_script.py
    ```

The script will send an SMS message with the weather forecast for Mendoza for the current day.

**Important:**

*   **Security:** Never include your credentials in the repository. Use environment variables or a `.env` file (and remember to add it to `.gitignore`).
*   **API Key:** Get a free API key at [WeatherAPI](https://www.weatherapi.com/).
*   **Location:** The default city is Mendoza. To change it, modify the `query` variable in `twilio_script.py`.

