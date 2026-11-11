# Debate Society Manager

A command-line tool I built to help run the Livingstone College Debate Society.

When I revived the society in fall 2026, about 30 students signed up. Keeping track of who
joined, who came to each session, and splitting people into fair debate rooms by hand took
time at the start of every meeting. This program does those jobs in a few seconds.

## What it does

- **Member list**: add members with their year and debate experience (New, Intermediate,
  Experienced), view them, and remove them. Members are saved to `members.csv`, so the list
  is still there next time the program runs.
- **Attendance**: go down the member list and mark who is here. Each session is saved to
  `attendance.csv` with the date.
- **Attendance report**: shows how many sessions each member has attended.
- **BP room generator**: splits the people who are present into Parliamentary Debate rooms
  (2 teams of 2 per room: Government, Opposition). Teams pair an experienced debater with a newer one so no team is all
  beginners. People left over become judges, starting with the most experienced.

## How to run it

```
python project.py
```

## How to run the tests

```
pip install pytest
pytest test_project.py
```

## How it's built

- Python standard library only: `csv` for saving data, `random` for shuffling rooms,
  `datetime` for session dates, `os` to check whether a file exists.
- Logic (pairing, room assignment, attendance counting) is kept in small functions that don't
  ask for input, so they can be tested with `pytest`.

## Ideas for later

- Smaller 2-team rooms when fewer than 8 people show up
- Remember past pairings so people debate with new partners
- A simple web page version
