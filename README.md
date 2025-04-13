# 📘 Learn Stack Overflow System Design

## 🧩 Requirements

- ✅ Users can post **questions**, **answers**, and **comments**.
- ✅ Users can **vote** on questions and answers.
- ✅ Questions should have **tags** associated with them.
- ✅ Users can **search** for questions based on **keywords**, **tags**, or **user profiles**.
- ✅ The system assigns **reputation scores** to users based on activity and quality of contributions.
- ✅ The system should handle **concurrent access** and ensure **data consistency**.

---

## 🏗️ Classes, Interfaces, and Enumerations

### 👤 `User`

Represents a user of the system.

| Property      | Type     | Description                       |
|---------------|----------|-----------------------------------|
| `id`          | `int`    | Unique identifier                 |
| `username`    | `str`    | Username                          |
| `email`       | `str`    | Email address                     |
| `reputation`  | `int`    | User's reputation score           |

---

### ❓ `Question`

Represents a posted question.

| Property       | Type               | Description                                 |
|----------------|--------------------|---------------------------------------------|
| `id`           | `int`              | Unique identifier                           |
| `title`        | `str`              | Title of the question                       |
| `content`      | `str`              | Full question content                       |
| `author`       | `User`             | User who posted the question                |
| `answers`      | `List[Answer]`     | List of answers                             |
| `comments`     | `List[Comment]`    | List of comments                            |
| `tags`         | `List[Tag]`        | Associated tags                             |
| `votes`        | `List[Vote]`       | List of votes                               |
| `creation_date`| `datetime`         | Date when question was posted               |

---

### 💬 `Answer`

Represents an answer to a question.

| Property       | Type               | Description                                 |
|----------------|--------------------|---------------------------------------------|
| `id`           | `int`              | Unique identifier                           |
| `content`      | `str`              | Answer content                              |
| `author`       | `User`             | Author of the answer                        |
| `question`     | `Question`         | Associated question                         |
| `comments`     | `List[Comment]`    | Comments on the answer                      |
| `votes`        | `List[Vote]`       | List of votes                               |
| `creation_date`| `datetime`         | Date when answer was posted                 |

---

### 💭 `Comment`

Represents a comment on a question or answer.

| Property       | Type       | Description                                 |
|----------------|------------|---------------------------------------------|
| `id`           | `int`      | Unique identifier                           |
| `content`      | `str`      | Comment content                             |
| `author`       | `User`     | Author of the comment                       |
| `creation_date`| `datetime` | Date when comment was posted                |

---

### 🔖 `Tag`

Represents a tag associated with a question.

| Property | Type   | Description          |
|----------|--------|----------------------|
| `id`     | `int`  | Unique identifier    |
| `name`   | `str`  | Name of the tag      |

---

### 👍 `Vote`

Represents a vote (upvote or downvote).

| Property     | Type          | Description                      |
|--------------|---------------|----------------------------------|
| `id`         | `int`         | Unique identifier                |
| `voter`      | `User`        | Who cast the vote                |
| `is_upvote`  | `bool`        | `True` for upvote, `False` otherwise |
| `target`     | `Union[Question, Answer]` | Voted question or answer |

---

### 🧠 `StackOverflow`

Main class managing the system.

| Method                                  | Description                                      |
|----------------------------------------|--------------------------------------------------|
| `create_user(username, email)`         | Registers a new user                             |
| `post_question(user, title, content, tags)` | Posts a new question                        |
| `post_answer(user, question_id, content)`   | Posts an answer to a question               |
| `add_comment(user, target_id, content)`     | Adds a comment to a question or answer      |
| `vote(user, target_id, is_upvote)`         | Casts a vote on a question or answer         |
| `search_questions(keyword)`               | Searches questions by keyword                 |
| `get_questions_by_tag(tag_name)`          | Retrieves questions with a specific tag       |
| `get_questions_by_user(user_id)`          | Retrieves questions posted by a specific user |

---

### 💡 `StackOverflowDemo`

Demonstrates the usage of the Stack Overflow system:

- Creates users
- Posts questions and answers
- Adds comments
- Casts votes
- Performs searches
- Retrieves questions by tags and users

---