from abc import ABC, abstractmethod

class Votable(ABC):
    @abstractmethod
    def vote(self, user, value):
        """Increase the vote count by one."""
        pass
    
    @abstractmethod
    def get_vote_count(self) -> int:
        """Return the current vote count."""
        pass