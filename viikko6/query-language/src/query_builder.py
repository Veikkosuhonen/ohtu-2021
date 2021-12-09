from matchers import And, HasAtLeast, HasFewerThan, Matcher, All, PlaysIn, Or

class QueryBuilder:
    def __init__(self) -> None:
        self.matcher = All()
    
    def playsIn(self, team):
        self.matcher = And(self.matcher, PlaysIn(team))
        return self
    
    def hasAtLeast(self, value, attr):
        self.addMatcher(HasAtLeast(value, attr))
        return self
    
    def hasFewerThan(self, value, attr):
        self.addMatcher(HasFewerThan(value, attr))
        return self
    
    def addMatcher(self, matcher):
        self.matcher = And(self.matcher, matcher)

    def oneOf(self, *matchers):
        self.addMatcher(Or(*matchers))
        return self

    def build(self) -> Matcher:
        matcher = self.matcher
        self.matcher = All()
        return matcher
