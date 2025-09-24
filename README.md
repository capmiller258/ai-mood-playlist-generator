# AI Mood-Based Playlist Generator

## [cite_start]Project Description [cite: 56]

This web application leverages AI to generate personalized song recommendations based on a user's mood described in natural language. It uses the Google Gemini API to interpret the mood and the Spotify API to find relevant music, providing a seamless music discovery experience.

## [cite_start]Screenshot [cite: 58]

<img width="1366" height="768" alt="Screenshot (54)" src="https://github.com/user-attachments/assets/e85884e0-b020-47ab-b720-f06482c9bbda" />


![App Screenshot](placeholder-screenshot.png)

## [cite_start]Technology Stack [cite: 60]

* [cite_start]**Frontend:** React.js [cite: 20]
* **Backend:** Python with Flask
* [cite_start]**APIs:** Google Gemini API [cite: 14][cite_start], Spotify API [cite: 15]

## [cite_start]Features Implemented [cite: 62]

* [cite_start]**Natural Language Input Processing:** Allows users to describe their mood or vibe in a simple text box[cite: 13].
* [cite_start]**AI-Powered Recommendations:** Integrates with the Gemini AI to interpret the user's prompt and suggest relevant musical themes[cite: 14].
* [cite_start]**Spotify Integration:** Connects with the Spotify API to fetch a list of recommended songs[cite: 15].
* [cite_start]**Dynamic UI:** Displays the list of recommended songs with track titles, artists, and album art[cite: 16].

## [cite_start]Setup Instructions [cite: 59]

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

## [cite_start]Demo Links [cite: 62]

(If you deploy your project, you can add the live link here. Otherwise, you can remove this section.)
