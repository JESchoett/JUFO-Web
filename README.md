<h1 align="center" id="title">Jufo-Turnierplaner</h1>

<p id="description">Mit dem Turnierplaner können nach Login Turniere erstellt werden. Für beliebig viele Gruppen mit beliebig vielen Teams generiert er einen Spielplan mit Hin- und oder Rückrunde. Spiele können eingetragen werden sodass eine Tabelle automatisch generiert wird.</p>

<h2>Project Screenshots:</h2>

<img src="https://raw.githubusercontent.com/JESchoett/JUFO-Web/main/project_img/klassendiagram.png" alt="project-screenshot" width="100%" height="400/">
<p> </p>
<img src="https://raw.githubusercontent.com/JESchoett/JUFO-Web/main/project_img/index.png" alt="project-screenshot" width="100%" height="400/">
<p> </p>
<img src="https://raw.githubusercontent.com/JESchoett/JUFO-Web/main/project_img/admin.png" alt="project-screenshot" width="100%" height="400/">

<h2>🛠️ Installation Steps:</h2>

<p>1. Clones des Repos</p>

<p>2. Definieren der Flask App</p>

```
export FLASK_APP=app.py
```

<p>3. Aufsetzen der Flask Datenbank</p>

```
/bin/python3 -m flask db init
```

```
/bin/python3 -m flask db migrate
```

```
/bin/python3 -m flask db upgrade
```

<p>6. Verifizieren der Funktionsfähigkeit mit einer Ausführung der run.py</p>

<p>7. Erstellung eines Accounts um alle Funktionen nutzen zu können</p>