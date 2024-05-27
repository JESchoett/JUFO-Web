from flask import render_template, request, Blueprint, url_for, redirect
from flask_login import current_user

from flask_sqlalchemy import query

import datetime

from turnierseite.turnier.models import Turnier, Gruppe, Team, Spiele
from turnierseite.turnier.turnierForm import TurnierForm, GruppeForm, TeamForm, SpieleForm

from turnierseite.app import db


turnier = Blueprint('turnier', __name__, template_folder='templates')

def lade_turnier_daten(turnier_id):
        turnier = Turnier.query.filter(Turnier.id == turnier_id).first()
        turnier_form = TurnierForm(obj=turnier)
        gruppen = Gruppe.query.filter(Gruppe.turnierId == turnier_id)
        return turnier, turnier_form, gruppen

@turnier.route('/')
def index():
    alle_turniere = Turnier.query.all()
    return render_template("turnier/turnier_overview.html", alle_turniere=alle_turniere)


@turnier.route('/turnier_erstellen', methods=['GET', 'POST'])
def turnier_erstellen():
    turnier_form = TurnierForm()
    if request.method == 'GET':
        return render_template("turnier/turnier_erstellen.html", form=turnier_form)
    elif request.method == 'POST':
        #insert des neuen Turnieres in die Datenbank
        turnier = Turnier(name=turnier_form.name.data, datumDerAustragung=turnier_form.datumDerAustragung.data)
        db.session.add(turnier)
        db.session.commit()

        #laden eines neuen html
        return redirect(url_for('turnier.index'))


@turnier.route('/turnier_details/<turnier_id>', methods=['GET', 'POST'])
def turnier_details(turnier_id):
    turnier, turnier_form, gruppen = lade_turnier_daten(turnier_id)

    if request.method == 'POST':
        # Retrieve the Turnier instance
        turnier = Turnier.query.get(turnier_id)

        if turnier_form.validate_on_submit():
            # Update the Turnier instance with form data
            turnier.name = turnier_form.name.data
            turnier.datumDerAustragung = turnier_form.datumDerAustragung.data

            db.session.add(turnier)

            # Commit the changes to the database
            db.session.commit()

    # Load a new HTML template with the updated data
    return render_template('turnier/turnier_details.html', turnier_form=turnier_form, turnier=turnier, gruppen=gruppen)

@turnier.route('/gruppe_erstellen/<turnier_id>', methods=['GET', 'POST'])
def gruppe_erstellen(turnier_id):
    gruppe_form = GruppeForm()
    if request.method == 'GET':
        turnier, turnier_form, gruppen = lade_turnier_daten(turnier_id)

        return render_template("gruppe/gruppe_erstellen.html", turnier=turnier, turnier_form=turnier_form, gruppe_form=gruppe_form, gruppen=gruppen)
    elif request.method == 'POST':
        #insert des neuen Turnieres in die Datenbank
        gruppe = Gruppe(turnierId=turnier_id, name=gruppe_form.name.data)
        db.session.add(gruppe)
        db.session.commit()

        turnier, turnier_form, gruppen = lade_turnier_daten(turnier_id)
        #laden eines neuen html
        return render_template('turnier/turnier_details.html', turnier_form=turnier_form, turnier=turnier, gruppen=gruppen)

@turnier.route('/gruppe_entfernen/<turnier_id>/<gruppe_id>')
def gruppe_entfernen(turnier_id, gruppe_id):
    gruppe = Gruppe.query.get(gruppe_id)
    if gruppe:
        db.session.delete(gruppe)
        db.session.commit()
    else:
        print(f"Gruppe mit id {gruppe_id} nicht gefunden.")

    turnier, turnier_form, gruppen = lade_turnier_daten(turnier_id)

    # Render the updated template
    return render_template('turnier/turnier_details.html', turnier_form=turnier_form, turnier=turnier, gruppen=gruppen)