from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import  login_required,  current_user
from .models import Note
from . import db
import  json


views = Blueprint('views',__name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category = 'error')

        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added!', category='success')

    return render_template("home.html", user = current_user)


@views.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    try:
        note = json.loads(request.data)
        note_id = note["noteId"]
        note = Note.query.get(note_id)

        if note.author != current_user:
            return jsonify({"success": False})

        db.session.delete(note)
        db.session.commit()
        return jsonify({"success": True})

    except Exception as e:
        print(f"Error deleting note: {e}")
        return jsonify({"success": False})

