"""
app.py
Main Flask application for the A/B Testing Web App.

This file handles:
- Routing for the intro page and home pages
- Random A/B assignment
- Session stickiness
- Button click tracking (metrics)
"""

from flask import Flask, render_template, session, request
import random
import json
import datetime
import os

# ---------------------------------------------------------
# Flask App Setup
# ---------------------------------------------------------
app = Flask(__name__)

# Secret key is required for session management.
# In production, this should be stored securely.
app.secret_key = "replace_with_any_secret_key"

# Ensure the metrics directory exists so the app doesn't crash.
os.makedirs("metrics", exist_ok=True)


# ---------------------------------------------------------
# Intro Page Route
# ---------------------------------------------------------
@app.route("/")
def intro():
    """
    Displays the intro page.
    This page is static and simply links to /home.
    """
    return render_template("intro.html")


# ---------------------------------------------------------
# Home Page Route (A/B Logic)
# ---------------------------------------------------------
@app.route("/home")
def home():
    """
    Determines whether the user sees Version A or Version B.

    A/B Assignment Logic:
    - If the user does NOT have a version stored in session,
      randomly assign them to A or B.
    - If they DO have a version stored, always show the same one.
      This ensures "stickiness" required for valid A/B testing.
    """

    # If no version assigned yet, randomly assign one
    if "version" not in session:
        # 50/50 split — adjust probability if needed
        session["version"] = "A" if random.random() < 0.5 else "B"

    # Render the correct version
    if session["version"] == "A":
        return render_template("home_A.html")
    else:
        return render_template("home_B.html")


# ---------------------------------------------------------
# Metrics Tracking Route
# ---------------------------------------------------------
@app.route("/track", methods=["POST"])
def track():
    """
    Tracks button clicks from Version A or Version B.

    Captured Data:
    - Timestamp
    - User IP address
    - Assigned version (A or B)

    Data is appended to metrics/interactions.json
    """

    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "ip": request.remote_addr,
        "version": session.get("version")
    }

    # Append the interaction to the JSON file
    with open("metrics/interactions.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    # Return empty response (204 = No Content)
    return ("", 204)


# ---------------------------------------------------------
# Run the Flask App
# ---------------------------------------------------------
if __name__ == "__main__":
    # debug=True enables auto-reload during development
    app.run(debug=True)