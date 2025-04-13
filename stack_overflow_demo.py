from stack_overflow import StackOverflow

class StackOverflowDemo:
    @staticmethod
    def run():
        system = StackOverflow()

        # Create users
        jimmy = system.create_user("Jimmy", "jimmy@example.com")
        eva = system.create_user("Eva", "eva@example.com")
        eric = system.create_user("Eric", "eric@example.com")

        # Jimmy asks a question
        java_question = system.ask_question(jimmy, "What is polymorphism in Java?",
                                            "Can someone explain polymorphism in Java with an example?",
                                            ["java", "oop"])
        
        # Eva answers jimmy's question
        eva_answer = system.answer_question(eva, java_question, 
                                            "Polymorphism in Java allows methods to do different things based on the object it is acting upon....")
        
        #Eric comments on the question
        system.add_comment(eric, java_question, "This is a great question! I had the same doubt a while ago.")

        #Jimmy comments on Eva's answer
        system.add_comment(jimmy, eva_answer, "Thanks for the detailed explanation!")

        # Eric votes on the question and answer
        system.vote_question(eric, java_question, 1)
        system.vote_answer(eric, eva_answer, 1)

        # Jimmy accepts Eva's answer
        system.accept_answer(eva_answer)

        #Eva asks another question
        python_question = system.ask_question(eva, "How to use list comprehensions in Python?",
                                              "I'm new to Python and I've heard about list comprehensions. Can someone explain how to use them?",
                                              ["python", "list-comprehension"])
        
        # Jimmy answers Eva's question
        jimmy_answer = system.answer_question(jimmy, python_question, 
                                              "List comprehensions provide a concise way to create lists. It consists of brackets containing an expression followed by a for clause...")
        
        # Eric votes on Eva's question and Jimmy's answer
        system.vote_question(eric, python_question, 1)
        system.vote_answer(eric, jimmy_answer, 1)

        #Print out the details
        print(f"Question: {java_question.title}")
        print(f"Asked by: {java_question.author.username}")
        print(f"Tags: {', '.join(tag.name for tag in java_question.tags)}")
        print(f"Votes: {java_question.get_vote_count()}")
        print(f"Comments: {len(java_question.get_comments())}")
        print(f"\nAnswer by {jimmy_answer.author.username}:")
        print(jimmy_answer.content)
        print(f"Votes: {jimmy_answer.get_vote_count()}")
        print(f"Accepted: {jimmy_answer.is_accepted}")
        print(f"Comments: {len(jimmy_answer.get_comments())}")

        print("\nUser Reputations:")
        print(f"Jimmy: {jimmy.reputation}")
        print(f"Eva: {eva.reputation}")
        print(f"Eric: {eric.reputation}")

                # Demonstrate search functionality
        print("\nSearch Results for 'java':")
        search_results = system.search_questions("java")
        for q in search_results:
            print(q.title)
        
        print("\nSearch Results for 'python':")
        search_results = system.search_questions("python")
        for q in search_results:
            print(q.title)

                # Demonstrate getting questions by user
        print("\nEva's Questions:")
        eva_questions = system.get_questions_by_user(eva)
        for q in eva_questions:
            print(q.title)
    
if __name__ == "__main__":
    StackOverflowDemo.run()