# 📘 Stack Overflow System Design

## 🧩 Requirements

- ✅ Users can post **questions**, **answers**, and **comments**.
- ✅ Users can **vote** on questions and answers.
- ✅ Questions are associated with **tags**.
- ✅ Users can **search** questions by **keywords**, **tags**, or **user profiles**.
- ✅ The system maintains **reputation scores** based on user contributions.
- ✅ Ensures **concurrent access handling** and **data consistency**.

---

## 🏗️ Core Classes & Interfaces

### 👤 `User`
Represents a user in the system.

| Property      | Type     | Description                    |
|---------------|----------|--------------------------------|
| `id`          | `int`    | Unique identifier              |
| `username`    | `str`    | Username                       |
| `email`       | `str`    | Email address                  |
| `reputation`  | `int`    | Reputation score               |

---

### ❓ `Question`
Represents a question posted by a user.

| Property       | Type               | Description                        |
|----------------|--------------------|------------------------------------|
| `id`           | `int`              | Unique identifier                  |
| `title`        | `str`              | Question title                     |
| `content`      | `str`              | Full question content              |
| `author`       | `User`             | User who posted the question       |
| `answers`      | `List[Answer]`     | List of answers                    |
| `comments`     | `List[Comment]`    | Comments on the question           |
| `tags`         | `List[Tag]`        | Tags associated with the question |
| `votes`        | `List[Vote]`       | Votes on the question              |
| `creation_date`| `datetime`         | Date the question was posted       |

---

### 💬 `Answer`
Represents an answer to a question.

| Property       | Type               | Description                        |
|----------------|--------------------|------------------------------------|
| `id`           | `int`              | Unique identifier                  |
| `content`      | `str`              | Answer content                     |
| `author`       | `User`             | User who posted the answer         |
| `question`     | `Question`         | Associated question                |
| `comments`     | `List[Comment]`    | Comments on the answer             |
| `votes`        | `List[Vote]`       | Votes on the answer                |
| `creation_date`| `datetime`         | Date the answer was posted         |

---

### 💭 `Comment`
Represents a comment on a question or answer.

| Property       | Type       | Description                |
|----------------|------------|----------------------------|
| `id`           | `int`      | Unique identifier          |
| `content`      | `str`      | Comment content            |
| `author`       | `User`     | User who posted the comment|
| `creation_date`| `datetime` | Date the comment was posted|

---

### 🔖 `Tag`
Represents a tag used to categorize questions.

| Property | Type   | Description       |
|----------|--------|-------------------|
| `id`     | `int`  | Unique identifier |
| `name`   | `str`  | Tag name          |

### 🧠 `StackOverflow`
Central class managing users, questions, answers, and system operations.

| Method                                     | Description                                    |
|-------------------------------------------|------------------------------------------------|
| `create_user(username, email)`            | Registers a new user                          |
| `ask_question(user, title, content, tags)`| User posts a new question                     |
| `answer_question(user, question, content)`| User answers a question                       |
| `add_comment(user, commentable, content)` | Adds a comment to a question or answer        |
| `vote_question(user, question, value)`    | Votes on a question (+1 or -1)                |
| `vote_answer(user, answer, value)`        | Votes on an answer (+1 or -1)                 |
| `accept_answer(answer)`                   | Marks an answer as accepted                   |
| `search_questions(query)`                 | Searches questions by keyword, content, or tag|
| `get_questions_by_user(user)`             | Retrieves questions posted by a specific user |
| `get_user(user_id)`                       | Fetches a user by ID                          |
| `get_question(question_id)`               | Fetches a question by ID                      |
| `get_answer(answer_id)`                   | Fetches an answer by ID                       |
| `get_tag(name)`                           | Fetches a tag by name                         |

---

### 🚀 `StackOverflowDemo`
A sample script demonstrating:

- User creation
- Posting questions and answers
- Adding comments
- Voting
- Searching
- Retrieving questions by tag and user

---