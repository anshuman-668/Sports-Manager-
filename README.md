# Sports Tournament Manager

A Python command-line application for managing sports tournaments. It allows users to add teams, automatically generate round-robin fixtures, record match results, calculate tournament standings, display the current leader, and save match results locally.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Data Storage](#data-storage)
- [Scoring System](#scoring-system)
- [Example](#example)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)

---

## Problem Statement

Managing a sports tournament manually can make it difficult to keep track of teams, fixtures, match results, and tournament standings. Manual calculations can also lead to errors when updating wins, draws, losses, scores, and points.

This project provides a simple command-line solution that automates these tasks and keeps tournament results organized in a local file.

---

## Objective

To develop a Python-based command-line Sports Tournament Manager that can:

- Register multiple teams.
- Generate fixtures automatically using a round-robin format.
- Record scores for completed matches.
- Calculate team statistics and points.
- Display the tournament standings.
- Identify the current leader.
- Save and reload match results using a text file.

---

## Key Features

* **Team Management:** Add multiple teams while preventing empty or duplicate team names.
* **Automatic Fixture Generation:** Generates one fixture for every unique pair of teams.
* **Match Result Entry:** Records scores for each fixture and prevents an already completed match from being overwritten.
* **Tournament Table:** Calculates played matches, wins, draws, losses, scores, conceded scores, goal difference, and points.
* **Current Leader:** Displays the team with the highest number of points.
* **Persistent Results:** Saves completed match results to `tournament_results.txt` and loads them when fixtures are generated.
* **Input Validation:** Handles invalid menu choices, team counts, match numbers, and negative/non-numeric scores.

---

## Tech Stack

* **Core Language:** Python 3
* **Programming Style:** Functions and list/dictionary data structures
* **User Interface:** Command-line interface (CLI)
* **Data Storage:** Plain text file (`tournament_results.txt`)
* **Libraries:** Python standard library only

---

## Project Architecture

```text
sports-tournament-manager/
├── main.py                  # Main application and tournament management logic
├── tournament_results.txt   # Saved match results
└── README.md                # Project documentation
```

### Main Program Components

```text
main.py
│
├── add_teams()
├── display_teams()
├── generate_matches()
├── display_matches()
├── enter_result()
├── create_table()
├── calculate_table()
├── display_table()
├── show_leader()
├── save_results()
├── load_results()
└── main()
```

The program uses `main()` as the entry point and provides a menu-driven interface for accessing tournament features.

---

## Installation & Setup

### 1. Download the project

Download the project files or clone the repository containing the project.

### 2. Navigate to the project directory

```bash
cd sports-tournament-manager
```

### 3. Verify Python installation

Make sure Python 3 is installed:

```bash
python --version
```

If your system uses `python3`, use:

```bash
python3 --version
```

---

## Usage Guide

Run the main application from the terminal:

```bash
python main.py
```

The program displays the following menu:

```text
1. Add Teams
2. Display Teams
3. Generate Fixtures
4. Display Fixtures
5. Enter Match Result
6. Display Tournament Table
7. Show Current Leader
8. Exit
```

### Interactive Options

**1. Add Teams**

Enter the number of teams and then provide each team name. The program requires at least two teams and rejects empty or duplicate names.

**2. Display Teams**

Displays all teams currently registered in the tournament.

**3. Generate Fixtures**

Creates a round-robin fixture list. Every unique pair of teams receives one match.

For `n` teams, the number of generated matches is:

```text
n × (n - 1) / 2
```

**4. Display Fixtures**

Shows every generated fixture and whether the match has been played.

**5. Enter Match Result**

Select a fixture and enter the scores for both teams. Scores must be non-negative integers.

**6. Display Tournament Table**

Displays the current standings with:

```text
Team | P | W | D | L | GF | GA | GD | PTS
```

The table is sorted by points and then by goal difference.

**7. Show Current Leader**

Displays the team currently having the highest number of points.

**8. Exit**

Saves the current match results and exits the application.

---

## Data Storage

Completed match results are stored in:

```text
tournament_results.txt
```

Each saved result follows this format:

```text
team1|team2|score1|score2
```

For example:

```text
rcb|daddu|300|250
kaddu|daddu|5|6
```

The application writes completed matches to the file and loads matching results when fixtures are generated.

---

## Scoring System

The tournament uses the following points system:

| Result | Points |
|---|---:|
| Win | 3 |
| Draw | 1 |
| Loss | 0 |

For every completed match, the program updates:

- **P:** Matches played
- **W:** Matches won
- **D:** Matches drawn
- **L:** Matches lost
- **GF:** Scores/goals for
- **GA:** Scores/goals against
- **GD:** Goal difference (`GF - GA`)
- **PTS:** Total points

The tournament table is ordered by points, with goal difference used as the secondary sorting criterion.

---

## Example

Suppose the tournament contains:

```text
RCB
DADDU
KADDU
```

The generated fixtures will contain every unique pairing:

```text
RCB vs DADDU
RCB vs KADDU
DADDU vs KADDU
```

After entering results, the application automatically calculates the updated standings.

Example results:

```text
RCB vs DADDU → 300 - 250
KADDU vs DADDU → 5 - 6
```

The exact tournament table depends on all results entered by the user.

---

## Limitations

- Teams and fixtures exist only during the current program session; completed match results are persisted.
- The current leader is determined by points only.
- If two teams have the same points, the leader display does not apply the table's goal-difference tie-breaker.
- Fixture generation is based on the teams currently entered and does not save the complete team list.
- The application is designed for a single tournament session rather than multiple independently named tournaments.

---

## Future Improvements

Possible extensions include:

- Save and load the complete team list.
- Prevent accidental regeneration of fixtures after results have been entered.
- Add multiple tournament formats.
- Apply complete tie-breaking rules when determining the leader.
- Add team statistics and performance history.
- Add a graphical user interface.
- Add automated unit tests.
- Use JSON or SQLite for more structured persistent storage.
