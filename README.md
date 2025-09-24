# AI Mood-Based Playlist Generator

## Project Description

This web application leverages AI to generate personalized song recommendations based on a user's mood described in natural language. It uses the Google Gemini API to interpret the mood and the Spotify API to find relevant music, providing a seamless music discovery experience.

## Screenshot
<img width="1364" height="725" alt="Screenshot (54)" src="https://github.com/user-attachments/assets/a69c38f8-8fc5-4985-817c-3d90624284ba" />


![App Screenshot](placeholder-screenshot.png)

## Technology Stack

* **Frontend:** React.js
* **Backend:** Python (with Flask)
* **APIs:**
    * Google Gemini API for natural language processing and recommendations.
    * Spotify API for searching and retrieving track data.

## Features Implemented

* **Natural Language Input:** Users can describe their mood or vibe in a simple text box.
* **AI-Powered Recommendations:** Integrates with the Gemini AI to interpret the user's prompt and suggest relevant musical themes.
* **Spotify Integration:** Connects with the Spotify API to fetch a list of recommended songs.
* **Dynamic UI:** Displays the list of recommended songs with track titles, artists, and album art.

## Setup Instructions

To run this project locally, you will need to have Python, Node.js, and npm installed.

### Backend Setup

1.  Clone the repository and navigate to the `backend` folder:
    ```bash
    git clone [https://github.com/YourUsername/ai-mood-playlist-generator.git](https://github.com/YourUsername/ai-mood-playlist-generator.git)
    cd ai-mood-playlist-generator/backend
    ```

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  Create a `config.py` file for your Gemini API key and a `spotify_config.py` file for your Spotify credentials. Fill them with your secret keys.

4.  Run the Flask server:
    ```bash
    python app.py
    ```
    The backend server will start on `http://127.0.0.1:8888`.

### Frontend Setup

1.  Open a new terminal and navigate to the `frontend` folder:
    ```bash
    cd ../frontend
    ```

2.  Install the required Node modules:
    ```bash
    npm install
    ```

3.  Run the React application:
    ```bash
    npm start
    ```
    The application will open in your browser at `http://localhost:3000`.
