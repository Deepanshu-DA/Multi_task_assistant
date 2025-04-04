# My Desktop Assistant

A cross-platform desktop assistant built with Python, offering voice and GUI control to perform a wide range of tasks simultaneously.

## ✨ Features
- Voice and Text input
- Open applications
- Web search (Google & YouTube)
- Set reminders
- Send emails
- Get current weather
- Play music/videos from YouTube
- Multithreaded task management
- GUI with task monitor and voice control

## 📁 Project Structure
```
├── main.py                # Entry point
├── gui.py                 # GUI using Tkinter
├── command_parser.py      # Command interpretation logic
├── listener.py            # Wake-word listener (optional)
├── wake_listener.py       # Background listener support
├── history_logger.py      # Logs command history
├── task_manager.py        # Thread/task management
├── services/              # Modular features
│   ├── apps.py            # Application launcher
│   ├── emailer.py         # Email service
│   ├── geolocation.py     # Location fetch
│   ├── media.py           # YouTube search and play
│   ├── reminder.py        # Reminder setter
│   ├── speech.py          # TTS & STT
│   └── weather.py         # Weather data fetch
├── .env                   # Environment variables (API keys, email credentials)
```

## 🔧 Setup
1. **Clone the repo**
```bash
git clone https://github.com/yourusername/desktop-assistant.git
cd desktop-assistant
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Configure `.env`**
```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
WEATHER_API_KEY=your_openweathermap_api_key
```

## 🚀 Run the Assistant
```bash
python main.py
```
Or launch the GUI:
```bash
python gui.py
```

## 🧠 Example Commands
- "Open Chrome"
- "Search cats on YouTube"
- "Set reminder for 18:30"
- "Send email"
- "What's the weather?"

## 🔒 Security Note
Keep your `.env` file safe and never expose it publicly.

## ✅ Todo / Enhancements
- Wake-word detection
- Command history via GUI
- Configurable voice options
- Smart error handling and offline support

## 📄 License
MIT License
