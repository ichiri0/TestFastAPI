from db.data.test_data import fake_notes


async def get_note_by_id(note_id):
    for note in fake_notes:
        if note["id"] == note_id:
            return note


async def get_notes_by_user_id(user_id):
    user_notes = [note for note in fake_notes if note["user_id"] == user_id]
    return user_notes
