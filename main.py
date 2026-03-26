from questions import ask_questions
from logic import calculate_personality
from suggestions import give_suggestions

# Step 1 - Ask Questions and get scores 
scores = ask_questions()


# Step 2 - Claculate Personality 
personality = calculate_personality(scores)


# Step 3 - Show personality 
print("\n---Personality Result---")
print("Your Personality Type is:",personality)


# Step 4 - Show Suggestions 
give_suggestions(personality)