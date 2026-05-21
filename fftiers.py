from flask import Flask, render_template

app = Flask(__name__)

# Data Pemain
data_pemain = [
    {"nama": "Erland Ramja iblis", "poin": 999},
    {"nama": "gema bot", "poin": 666},
    {"nama": "aura bot", "poin": 89},
    {"nama": "alif bot", "poin": 21},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67},
    {"nama": "keano bot", "poin": 67}
]

def tentukan_tier(poin):
    if poin >= 300: return "HT1"
    elif poin >= 250: return "HT2"
    elif poin >= 200: return "LT1"
    else: return "LT2"

@app.route('/')
def home():
    # Mengurutkan dan menambahkan tier ke setiap pemain
    for p in data_pemain:
        p['tier'] = tentukan_tier(p['poin'])
    
    sorted_pemain = sorted(data_pemain, key=lambda x: x["poin"], reverse=True)
    return render_template('index.html', pemain=sorted_pemain)

if __name__ == '__main__':
    app.run(debug=True, port=5000)