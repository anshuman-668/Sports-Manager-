# Project Statement & Scope

## 1. Problem Statement

Managing a sports tournament manually can become difficult when the number of teams and matches increases. Organizers need to maintain accurate information about teams, fixtures, match results, points, and tournament standings. Manual calculations can result in errors when updating wins, draws, losses, scores, and points.

Specifically:

- **Team & Fixture Management:** Creating and maintaining fixtures manually can be time-consuming and may result in missing or duplicate matchups.
- **Match Result Management:** Recording match scores and keeping track of completed and uncompleted fixtures manually can make tournament management difficult.
- **Tournament Standings:** Calculating wins, draws, losses, scores, goal difference, and points after every match requires repeated manual calculations.
- **Leader Tracking:** Identifying the current tournament leader from the latest results can be inconvenient when standings are maintained manually.
- **Result Persistence:** Tournament results can be lost when the program ends if they are not stored in a persistent file.

This project addresses these challenges by providing a lightweight, menu-driven Python command-line application for managing sports tournaments. The application generates fixtures automatically, records match results, calculates tournament standings, identifies the current leader, and stores completed results locally.

---

## 2. Scope of the Project

### In-Scope:

- **Team Management:** Adding teams to the tournament while preventing empty or duplicate team names.
- **Fixture Generation:** Automatically generating a round-robin fixture list in which every unique pair of teams plays one match.
- **Match Result Entry:** Recording scores for individual fixtures and validating match numbers and score values.
- **Tournament Table Calculation:** Calculating matches played, wins, draws, losses, scores for, scores against, goal difference, and points.
- **Tournament Standings:** Displaying teams in order of points and then goal difference.
- **Current Leader:** Displaying the team with the highest number of tournament points.
- **Local Result Persistence:** Saving completed match results to `tournament_results.txt` and loading previously saved results when fixtures are generated.
- **Input Validation:** Handling invalid team counts, duplicate team names, invalid match selections, negative scores, and non-numeric input.

### Out-of-Scope:

- Online or cloud-based tournament management.
- Multi-user authentication and user accounts.
- Database-based storage systems.
- Graphical user interface (GUI) or mobile application.
- Automatic synchronization with external sports platforms or APIs.
- Live match data from external sources.

---

## 3. Target Users

- **Sports Tournament Organizers:** Individuals who need a simple system to manage teams, fixtures, results, and standings.
- **Students & Academic Project Users:** Users demonstrating fundamental Python programming concepts such as functions, lists, dictionaries, loops, conditionals, input validation, and file handling.
- **Small Tournament Administrators:** Users managing small-scale tournaments where a command-line application is sufficient.

---

## 4. High-Level Features

- **Team Management:** Allows users to add and display tournament teams while preventing duplicate or empty team names.
- **Fixture Generation Engine:** Automatically creates matches between every unique pair of registered teams.
- **Match Result Management:** Allows users to enter scores for completed matches and prevents an existing result from being overwritten.
- **Points Calculation Engine:** Awards 3 points for a win, 1 point for a draw, and 0 points for a loss.
- **Tournament Table Engine:** Dynamically calculates and displays complete team statistics including P, W, D, L, GF, GA, GD, and PTS.
- **Leader Tracking:** Identifies the team currently having the highest points total.
- **File-Based Persistence:** Stores completed match results in `tournament_results.txt` so that recorded results can be loaded again.
- **Command-Line Interface:** Provides a simple numbered menu through which users can access all tournament-management functions.
