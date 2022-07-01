import lab6_p1_character as character_class
import lab6_p1_team as team_class


def main():
    new_char = character_class.Character("Mario", "Plumber", 100, 60, 200, 150)
    print(new_char)
    print()
    team = team_class.Team("saveData.csv")
    print("PRINTING ONE MEMBER ONLY:")
    members_list = team.get_all_members()  # get_all_members returns a list!
    print(members_list[0])  # prints first team member
    print()
    print("PRINTING WHOLE TEAM:")
    print(team)


if __name__ == "__main__":
    main()