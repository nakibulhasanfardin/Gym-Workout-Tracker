from project import load_data
from project import get_last_session
from project import save_data

def test_load_data_missing_file(tmp_path):
    filename = tmp_path / "workouts.json"

    assert load_data(filename) == {}


def test_save_and_load_data(tmp_path):
    filename = tmp_path / "workouts.json"
    data = {
        "Chest": [
            {
                "date": "2026-10-27",
                "exercises": {
                    "Bench Press": {
                        "weight": 20,
                        "sets": 3,
                        "reps": 8,
                        "difficulty": 7
                    }
                }
            }
        ]
    }

    save_data(data, filename)

    assert load_data(filename) == data


def test_get_last_session():
    first = {"date": "2026-10-26", "exercises": {}}
    second = {"date": "2026-10-27", "exercises": {}}
    data = {"Chest": [first, second]}

    assert get_last_session(data, "Chest") == second
    assert get_last_session(data, "Back") is None
