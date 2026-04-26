# A/B Testing Web Application (Flask)

This project is a simple web application built with Python and Flask to demonstrate A/B testing, session stickiness, and basic interaction tracking. Users are randomly assigned to either Version A or Version B of a home page, and their interactions (button clicks) are logged for analysis. This project was developed as part of an academic assignment on web development and experimentation.

---

## 🚀 Features

- **Static Intro Page**  
  A simple landing page that introduces the application and links to the A/B-tested home page.

- **A/B Testing Logic**  
  Users are randomly assigned to Version A or Version B on their first visit.  
  Session cookies ensure they continue to see the same version (“stickiness”).

- **Interaction Tracking**  
  Button clicks on each version are logged with:
  - Timestamp  
  - IP address  
  - Assigned version (A or B)

- **Lightweight Flask Backend**  
  Easy to run locally and simple to understand.

---

## 📁 Project Structure

```
ab-testing-webapp/
│── app.py
│── requirements.txt
│── /templates
│     ├── intro.html
│     ├── home_A.html
│     ├── home_B.html
│── /static
│     └── styles.css
│── /metrics
│     └── interactions.json
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ab-testing-webapp.git
cd ab-testing-webapp
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask development server:

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧪 How A/B Testing Works

When a user visits `/home`:

1. The server checks whether the user already has a version stored in their session.
2. If not, the user is randomly assigned to:
   - **Version A** (50% chance)  
   - **Version B** (50% chance)
3. The assigned version is stored in the session to ensure **stickiness**.
4. The user continues to see the same version on every visit.

This mirrors real-world A/B testing practices where consistency is required for valid results.

---

## 📊 Interaction Tracking

Each version contains a button that triggers a POST request to `/track`.

The following data is logged:

- Timestamp (`ISO 8601 format`)
- User IP address
- Assigned version (A or B)

Logs are stored in:

```
/metrics/interactions.json
```

Each entry is written as a single JSON object per line, making it easy to parse or convert to CSV later.

Example log entry:

```json
{"timestamp": "2026-04-25T22:10:12.12345", "ip": "127.0.0.1", "version": "A"}
```

---

## 🎨 Styling

A minimal `styles.css` file provides consistent styling across all pages.  
The assignment emphasizes functionality over design, so styling is intentionally simple.

---

## 📚 References (APA 7th Edition)

Algolia. (n.d.). *Implementing A/B testing*. [https://www.algolia.com/ecommerce-merchandising-playbook/ab-testing/](https://www.algolia.com/ecommerce-merchandising-playbook/ab-testing/)

Johnston, J. (2024, March 13). *A beginner’s guide to web application development (2024)*. [https://budibase.com/blog/web-application-development/](https://budibase.com/blog/web-application-development/)

Mozilla Developer Network. (n.d.). *MDN Web Docs: Web development basics*. [https://developer.mozilla.org/](https://developer.mozilla.org/)

---

## 📄 License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.