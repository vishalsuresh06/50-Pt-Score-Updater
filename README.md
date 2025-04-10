# 50-Pt-Score-Updater

## Purpose

The **50-Pt-Score-Updater** is a Python-based project designed to track NBA players who score 50 points or more in a game. The project uses the **NBA API** to retrieve real-time game data and player statistics. Once a player scores 50 points, the system sends a notification via **iMessage** to a predefined list of recipients.

The project includes the following features:
- **Tracking player performances**: The system checks NBA games to see if any player scores 50 or more points.
- **iMessage notifications**: When a player reaches the 50-point threshold, a message is sent via iMessage to alert users.
- **Flask Server**: A Flask web server is used to serve the iMessage API for sending messages.

I created this project because doordash has a promo code when an NBA player scores 50 points. Since I did not have time to constantly keep track of the scores. I decided to automate it.

---

## Project Structure

- **`iMessage_API/`**: Contains the Flask server that interfaces with the iMessage API.
- **`script.py`**: A Python script that checks NBA games for players scoring 50+ points and sends iMessage notifications.
- **`venv/`**: Virtual environment that contains all dependencies for the project.
- **`logs/`**: Directory where log files are stored to track the execution and performance of the script.
- **`.github/workflows/`**: Contains GitHub Actions workflows for automating the execution of the script on a schedule.

---

## Features

1. **Real-time NBA Data**: 
   - Tracks live game statistics using the **NBA API**.
   - Identifies players who score 50+ points in a game.

2. **Automated iMessage Notifications**:
   - Sends a message to a predefined list of phone numbers when a player scores 50+ points.
   - Message includes the player's name and the number of points scored.

3. **Scheduling and Automation**:
   - The system can be automated via **GitHub Actions** to run daily.
   - The Flask server and the script run in sequence, ensuring that data is checked and notifications are sent automatically.

4. **Logs and Debugging**:
   - Detailed logs are created for each execution, making it easy to track the status and success of notifications.

---

## Prerequisites

1. **Python 3.6+**: The project requires Python 3.x installed.
2. **Required Libraries**: 
   - Install the required Python libraries using the following command:
     ```bash
     pip install -r requirements.txt
     ```

3. **NBA API Key**: An API key from the [NBA API](https://www.balldontlie.io/#get-all-games) may be required depending on the version you're using.

4. **iMessage API**: Make sure you have an iMessage API setup to send notifications to recipients.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vishalsuresh06/50-Pt-Score-Updater.git
   cd 50-Pt-Score-Updater
   ```

2. ** Set Up Virtual Environment:
   - Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
   - Activate the virtual environment:
     - For macOS/Linux:
     ```bash
     python3 -m venv venv
     ```
     - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```


