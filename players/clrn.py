from combat.druid import Model


class PlayerSettings:
    model = Model

    def cat_form(self):
        return 'shift', '3'

    def attack(self):
        return '1'

    def regrowth(self):
        return '5'

    def healing_touch(self):
        return '3'

    def rejuvenation(self):
        return '4'

    def mark(self):
        return 'v'

    def thorns(self):
        return '='

    def drink(self):
        return None