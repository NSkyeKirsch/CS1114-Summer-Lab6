class Character:
    def __init__(self, name, char_type, attack, defense, health_points, stamina_points):
        self.name = name
        self.type = char_type
        self.stats = {'Attack': attack, 'Defense': defense, 'HP': health_points, 'SP': stamina_points}

    def __str__(self):
        return "{} ({}): Attack: {}, Defense: {}, HP: {}, SP: {}".format(self.name, self.type, self.stats['Attack'],
                                                                         self.stats['Defense'], self.stats['HP'],
                                                                         self.stats['SP'])

