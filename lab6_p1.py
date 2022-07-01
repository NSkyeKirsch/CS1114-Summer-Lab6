class Character:
    def __init__(self, name, char_type, attack, defense, health_points, stamina_points):
        self.name = name
        self.type = char_type
        self.stats = {'Attack': attack, 'Defense': defense, 'HP': health_points, 'SP': stamina_points}

    def __str__(self):
        return "{} ({}): Attack: {}, Defense: {}, HP: {}, SP: {}".format(self.name, self.type, self.stats['Attack'],
                                                                         self.stats['Defense'], self.stats['HP'],
                                                                         self.stats['SP'])


class Team:
    def __init__(self, filename):
        self.file = filename
        self.team = self.read_file()

    def __str__(self):
        final_str = ""
        for character in self.team:
            final_str += str(character)
            final_str += "\n" + "-------------" + "\n"

        return final_str


    def read_file(self):
        save_file = open(self.file, 'r')
        team_list = []
        save_file.readline()
        for line in save_file:
            line_items = line.strip().split(',')
            new_char = Character(line_items[0], line_items[1], line_items[2], line_items[3],
                                 line_items[4], line_items[5])
            team_list.append(new_char)
        save_file.close()
        return team_list

    def get_all_members(self):
        return self.team


def main():
    new_char = Character("Mario", "Plumber", 100, 60, 200, 150)
    print(new_char)
    print()
    team = Team("saveData.csv")
    print("PRINTING ONE MEMBER ONLY:")
    members_list = team.get_all_members()  # get_all_members returns a list!
    print(members_list[0])  # prints first team member
    print()
    print("PRINTING WHOLE TEAM:")
    print(team)


if __name__ == "__main__":
    main()