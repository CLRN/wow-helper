from combat.priest import Model


class PlayerSettings:
    model = Model

    def smite(self):
        return '2'

    def heal(self):
        return '3'

    def drink(self):
        return '7'