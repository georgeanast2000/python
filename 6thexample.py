from flask import Flask, request
from user_agents import parse # Χρειαζόμαστε αυτό για να "διαβάζει" το User-Agent
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Παίρνουμε το ακατέργαστο κείμενο
    ua_string = request.headers.get('User-Agent')
    
    # Το "μεταφράζουμε" σε κάτι κατανοητό
    user_agent = parse(ua_string)
    
    # Διαλέγουμε τι θέλουμε να δείξουμε
    browser = user_agent.browser.family      # π.χ. Chrome
    os_system = user_agent.os.family         # π.χ. Windows ή Android
    device = user_agent.device.family        # π.χ. iPhone ή Generic Smartphone
    
    return f'''
        <div style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1> Η ταυτότητά σου </h1>
            <p> 🌐 <b>Browser:</b> {browser} </p>
            <p> 💻 <b>Λειτουργικό:</b> {os_system} </p>
            <p> 📱 <b>Συσκευή:</b> {device} </p>
            <hr>
            <p style="color: gray;">Ολόκληρο το User-Agent: <br> <small>{ua_string}</small></p>
        </div>
        '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
