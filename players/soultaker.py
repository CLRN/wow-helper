from combat.priest import Model


class PlayerSettings:
    def model(self):
        return Model(self)

    def smite(self):
        return '2'

    def heal(self):
        return '3'

    def drink(self):
        return '7'