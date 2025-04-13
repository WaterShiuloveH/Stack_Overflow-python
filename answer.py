from datetime import datetime
from votable import Votable
from commentable import Commentable
from vote import Vote

class Answer(Votable, Commentable):
    def __init__(self, author, question, content):
        self.id = id(self)
        self.author = author
        self.question = question
        self.content = content
        self.creation_date = datetime.now()
        self.comments = []
        self.votes = []
        self.is_accepted = False

    def vote(self, user, value):
        """Increase the vote count by one."""
        if value not in [-1, 1]:
            raise ValueError("Vote value must be -1 or 1.")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.update_reputation(value * 10) # +10 for upvote, -10 for downvote

    def get_vote_count(self):
        return sum(v.value for v in self.votes)

    def add_comment(self, comment):
        self.comments.append(comment)
    
    def get_comments(self):
        return self.comments.copy()
    
    def accept(self):
        """Mark this answer as accepted."""
        if self.is_accepted:
            raise ValueError("This question already has an accepted answer.")
        self.is_accepted = True
        self.author.update_reputation(15) # +15 for accepted answer