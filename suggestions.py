def give_suggestions(personality):

    print("\n--- Personality Insights ---")

    if personality == "INFP":
        print("You are creative, thoughtful, and emotionally aware.")
        print("Strengths: Deep thinking, creativity")
        print("Weakness: Overthinking, procrastination")
        print("Study Style: Quiet, focused environment")
        print("Suggestion: Use Pomodoro technique and start small tasks")
        print("Unsuitable Environment: Noisy places, strict schedules")

    elif personality == "ENFP":
        print("You are energetic, enthusiastic, and creative.")
        print("Strengths: Communication, imagination")
        print("Weakness: Easily distracted")
        print("Study Style: Interactive learning")
        print("Suggestion: Study with friends or use videos")
        print("Unsuitable Environment: Long boring lectures, isolation")

    elif personality == "ISTJ":
        print("You are practical, disciplined, and organized.")
        print("Strengths: Consistency, reliability")
        print("Weakness: Rigidity")
        print("Study Style: Structured and planned study")
        print("Suggestion: Follow a strict timetable")
        print("Unsuitable Environment: Chaotic, last-minute work")

    elif personality == "INTJ":
        print("You are strategic, logical, and independent.")
        print("Strengths: Deep focus, planning")
        print("Weakness: Over-analysis")
        print("Study Style: Long focused sessions")
        print("Suggestion: Break big goals into smaller parts")
        print("Unsuitable Environment: Frequent interruptions")

    else:
        print("Personality insights coming soon!")