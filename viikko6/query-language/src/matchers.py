class Matcher:
    def matches(self, player) -> bool:
        pass

class And(Matcher):
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        return all([matcher.matches(player) for matcher in self._matchers])

class Or(Matcher):
    def __init__(self, *matchers) -> None:
        self._matchers = matchers
    
    def matches(self, player) -> bool:
        return any([matcher.matches(player) for matcher in self._matchers])

class PlaysIn(Matcher):
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast(Matcher):
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All(Matcher):
    def __init__(self, matcher) -> None:
        self._matcher = matcher
    
    def matches(self, player) -> bool:
        return True

class Not(Matcher):
    def __init__(self, matcher) -> None:
        self.matcher = matcher
    
    def matches(self, player) -> bool:
        return not self.matcher.matches(player)

class HasFewerThan(HasAtLeast):
    def __init__(self, value, attr) -> None:
        super().__init__(value, attr)
    
    def matches(self, player):
        return not super().matches(player)
