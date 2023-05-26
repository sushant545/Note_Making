from flask import jsonify, request

@app.route('/delete-note', methods=['POST'])
def delete_note():
    note_id = request.json.get('noteId')
    if note_id is None:
        return jsonify({'error': 'Note ID not provided'}), 400

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


    return jsonify({'success': 'Note deleted'})