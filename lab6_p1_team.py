import lab6_p1_character as character_class


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
            new_char = character_class.Character(line_items[0], line_items[1], line_items[2], line_items[3],
                                 line_items[4], line_items[5])
            team_list.append(new_char)
        save_file.close()
        return team_list

    def get_all_members(self):
        return self.team
