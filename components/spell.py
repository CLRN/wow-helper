class Spell:
    def __init__(self, id, min_range, max_range, cast_time, bind_key, cooldown):
        self.id = id
        self.min_range = min_range
        self.max_range = max_range
        self.cast_time = cast_time
        self.bind_key = bind_key
        self.cooldown = cooldown

