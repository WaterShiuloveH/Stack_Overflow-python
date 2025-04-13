from typing import List
from datetime import datetime
from votable import Votable
from commentable import Commentable
from tag import Tag
from comment import Comment
from vote import Vote

class Question(Votable, Commentable):
    def __init__(self, author, title, content, tag_names):
        self.id = id(self)
        self.author = author
        self.title = title
        self.content = content
        self.creation_date = datetime.now()
        self.answers = []
        self.comments = []
        self.tags = [Tag(name) for name in tag_names]
        self.votes = []
    
    def add_answer(self, answer):
        """Add an answer to the question."""
        if answer not in self.answers:
            self.answers.append(answer)

    def vote(self, user, value):
        """Increase the vote count by one."""
        if value not in [-1, 1]:
            raise ValueError("Vote value must be -1 or 1.")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.update_reputation(value * 5) # +5 for upvote, -5 for downvote

    def get_vote_count(self):
        return sum(v.value for v in self.votes)
    
    def add_comment(self, comment: str):
        self.comments.append(comment)
    
    def get_comments(self) -> List["Comment"]:
        return self.comments.copy()