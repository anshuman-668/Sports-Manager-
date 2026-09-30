# ==========================================
#       SPORTS TOURNAMENT MANAGER
# ==========================================

FILE_NAME = "tournament_results.txt"


# ------------------------------------------
# ADD TEAMS
# ------------------------------------------

def add_teams(teams):

    print("\n========== ADD TEAMS ==========")

    while True:

        try:
            number = int(input("How many teams do you want to add? ") )

            if number < 2:
                print("You need at least 2 teams.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    for i in range(number):

        while True:

            team = input(f"Enter name of team {i + 1}: ").strip()

            if team == "":
                print("Team name cannot be empty.")

            elif team in teams:
                print("This team already exists.")

            else:
                teams.append(team)
                break

    print("\nTeams added successfully!")


# ------------------------------------------
# DISPLAY TEAMS
# ------------------------------------------

def display_teams(teams):

    if len(teams) == 0:

        print("\nNo teams have been added.")

        return

    print("\n========== TEAMS ==========")

    for i in range(len(teams)):

        print(f"{i + 1}. {teams[i]}")


# ------------------------------------------
# GENERATE MATCHES
# ------------------------------------------

def generate_matches(teams):

    matches = []

    for i in range(len(teams)):

        for j in range(i + 1, len(teams)):

            match = {
                "team1": teams[i],
                "team2": teams[j],
                "score1": None,
                "score2": None
            }

            matches.append(match)

    return matches


# ------------------------------------------
# DISPLAY MATCHES
# ------------------------------------------

def display_matches(matches):

    if len(matches) == 0:

        print("\nNo matches available.")

        return

    print("\n========== MATCH FIXTURES ==========")

    for i in range(len(matches)):

        match = matches[i]

        if match["score1"] is None:

            result = "Not Played"

        else:

            result = (
                str(match["score1"])
                + " - "
                + str(match["score2"])
            )

        print(
            f"{i + 1}. "
            f"{match['team1']} vs {match['team2']} "
            f"→ {result}"
        )


# ------------------------------------------
# ENTER MATCH RESULT
# ------------------------------------------

def enter_result(matches):

    if len(matches) == 0:

        print("\nNo matches available.")

        return

    display_matches(matches)

    while True:

        try:

            match_number = int(
                input("\nEnter match number: ")
            )

            if (
                match_number >= 1
                and match_number <= len(matches)
            ):

                break

            else:

                print("Invalid match number.")

        except ValueError:

            print("Please enter a number.")

    match = matches[match_number - 1]

    if match["score1"] is not None:

        print("\nThis match already has a result.")

        return

    print(
        f"\n{match['team1']} vs {match['team2']}"
    )

    while True:

        try:

            score1 = int(
                input(
                    f"Enter score for "
                    f"{match['team1']}: "
                )
            )

            score2 = int(
                input(
                    f"Enter score for "
                    f"{match['team2']}: "
                )
            )

            if score1 < 0 or score2 < 0:

                print("Score cannot be negative.")

            else:

                break

        except ValueError:

            print("Please enter valid scores.")

    match["score1"] = score1
    match["score2"] = score2

    save_results(matches)

    print("\nResult recorded successfully!")


# ------------------------------------------
# CREATE TOURNAMENT TABLE
# ------------------------------------------

def create_table(teams):

    table = {}

    for team in teams:

        table[team] = {
            "played": 0,
            "won": 0,
            "draw": 0,
            "lost": 0,
            "scored": 0,
            "conceded": 0,
            "points": 0
        }

    return table


# ------------------------------------------
# CALCULATE POINTS
# ------------------------------------------

def calculate_table(teams, matches):

    table = create_table(teams)

    for match in matches:

        if match["score1"] is None:

            continue

        team1 = match["team1"]
        team2 = match["team2"]

        score1 = match["score1"]
        score2 = match["score2"]

        # Both teams played
        table[team1]["played"] += 1
        table[team2]["played"] += 1

        # Goals / scores
        table[team1]["scored"] += score1
        table[team1]["conceded"] += score2

        table[team2]["scored"] += score2
        table[team2]["conceded"] += score1

        # Team 1 wins
        if score1 > score2:

            table[team1]["won"] += 1
            table[team1]["points"] += 3

            table[team2]["lost"] += 1

        # Team 2 wins
        elif score2 > score1:

            table[team2]["won"] += 1
            table[team2]["points"] += 3

            table[team1]["lost"] += 1

        # Draw
        else:

            table[team1]["draw"] += 1
            table[team2]["draw"] += 1

            table[team1]["points"] += 1
            table[team2]["points"] += 1

    return table


# ------------------------------------------
# DISPLAY TOURNAMENT TABLE
# ------------------------------------------

def display_table(teams, matches):

    table = calculate_table(teams, matches)

    if len(teams) == 0:

        print("\nNo teams available.")

        return

    print("\n")
    print("=" * 85)
    print("                         TOURNAMENT TABLE")
    print("=" * 85)

    print(
        f"{'Team':<18}"
        f"{'P':<5}"
        f"{'W':<5}"
        f"{'D':<5}"
        f"{'L':<5}"
        f"{'GF':<7}"
        f"{'GA':<7}"
        f"{'GD':<7}"
        f"{'PTS':<5}"
    )

    print("-" * 85)

    # Sort teams by points
    sorted_teams = sorted(
        teams,
        key=lambda team: (
            table[team]["points"],
            table[team]["scored"]
            - table[team]["conceded"]
        ),
        reverse=True
    )

    for team in sorted_teams:

        data = table[team]

        goal_difference = (
            data["scored"]
            - data["conceded"]
        )

        print(
            f"{team:<18}"
            f"{data['played']:<5}"
            f"{data['won']:<5}"
            f"{data['draw']:<5}"
            f"{data['lost']:<5}"
            f"{data['scored']:<7}"
            f"{data['conceded']:<7}"
            f"{goal_difference:<7}"
            f"{data['points']:<5}"
        )


# ------------------------------------------
# SHOW LEADER
# ------------------------------------------

def show_leader(teams, matches):

    if len(teams) == 0:

        print("\nNo teams available.")

        return

    table = calculate_table(teams, matches)

    leader = teams[0]

    for team in teams:

        if ( table[team]["points"]
            > table[leader]["points"] ):

            leader = team

    print("\n========== CURRENT LEADER ==========")

    print(f"Team   : {leader}")
    print(f"Points : {table[leader]['points']}")


# ------------------------------------------
# SAVE RESULTS
# ------------------------------------------

def save_results(matches):

    file = open(FILE_NAME, "w")

    for match in matches:

        if match["score1"] is not None:

            line = (
                match["team1"]
                + "|"
                + match["team2"]
                + "|"
                + str(match["score1"])
                + "|"
                + str(match["score2"])
                + "\n"
            )

            file.write(line)

    file.close()


# ------------------------------------------
# LOAD RESULTS
# ------------------------------------------

def load_results(matches):

    try:

        file = open(FILE_NAME, "r")

        for line in file:

            line = line.strip()

            if line == "":
                continue

            parts = line.split("|")

            team1 = parts[0]
            team2 = parts[1]

            score1 = int(parts[2])
            score2 = int(parts[3])

            for match in matches:

                if (
                    match["team1"] == team1
                    and match["team2"] == team2
                ):

                    match["score1"] = score1
                    match["score2"] = score2

        file.close()

    except FileNotFoundError:

        pass


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

def main():

    teams = []
    matches = []

    while True:

        print("\n")
        print("=" * 55)
        print("SPORTS TOURNAMENT MANAGER")
        print("=" * 55)

        print("1. Add Teams")
        print("2. Display Teams")
        print("3. Generate Fixtures")
        print("4. Display Fixtures")
        print("5. Enter Match Result")
        print("6. Display Tournament Table")
        print("7. Show Current Leader")
        print("8. Exit")

        print("=" * 55)

        choice = input("Enter your choice: " )

        # Add teams
        if choice == "1":

            add_teams(teams)

        # Display teams
        elif choice == "2":

            display_teams(teams)

        # Generate matches
        elif choice == "3":

            if len(teams) < 2:

                print( "\nAdd at least 2 teams first." )

            else:

                matches = generate_matches(teams)

                load_results(matches)

                print(
                    "\nFixtures generated successfully!"
                )

                print(
                    f"Total matches: {len(matches)}"
                )

        # Display matches
        elif choice == "4":

            display_matches(matches)

        # Enter result
        elif choice == "5":

            enter_result(matches)

        # Display table
        elif choice == "6":

            display_table(teams, matches)

        # Show leader
        elif choice == "7":

            show_leader(teams, matches)

        # Exit
        elif choice == "8":

            save_results(matches)

            print("\nTournament data saved.")

            print("Thank you for using Sports Tournament Manager!" )

            break

        else:

            print("\nInvalid choice. "
            "Please select 1-8." )


# ------------------------------------------
# START PROGRAM
# ------------------------------------------

main()