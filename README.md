# Tank-You 🚛⛽

Egy Django alapú webalkalmazás üzemanyag-nyilvántartáshoz és tankolási folyamatok kezeléséhez.

A projekt neve egy szójáték: **"Tank You"** = "Thank You" + tankolás.

## ✨ Funkciók

- Felhasználói regisztráció és bejelentkezés
- Tankolási események rögzítése (dátum, mennyiség, ár, üzemanyag típus, jármű, benzinkút)
- Járművek és benzinkutak kezelése
- Tankolási előzmények listázása és szűrése
- Alapvető REST API endpoint-ek
- Reszponzív webes felület
- Django admin felület az adatok könnyű kezelésére

## 🛠 Tech Stack

- **Backend**: Python + Django
- **Frontend**: HTML, CSS, JavaScript (Django templates)
- **API**: Django REST Framework
- **Adatbázis**: SQLite (fejlesztéshez)

## 🚀 Telepítés és futtatás

### 1. Repository klónozása

```bash
git clone https://github.com/Snewkovits/tank-you.git
cd tank-you
```
2. Virtuális környezet létrehozása
Bashpython -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
3. Függőségek telepítése
Bashpip install -r requirements.txt
4. Környezeti változók beállítása
Bashcp .env.example .env
Szerkeszd a .env fájlt a saját beállításaid szerint (különösen a SECRET_KEY és az adatbázis beállítások).
5. Migrációk futtatása
Bashpython manage.py migrate
6. Admin felhasználó létrehozása (opcionális)
Bashpython manage.py createsuperuser
7. Fejlesztői szerver indítása
Bashpython manage.py runserver
Nyisd meg a böngészőben: http://127.0.0.1:8000/
📁 Fő könyvtárak

config/ – Projekt beállítások (settings, urls, wsgi)
refuelling/ – Fő alkalmazás (modellek, view-k, API, template-ek)
templates/ – HTML sablonok
static/ – Statikus fájlok (CSS, JS)
