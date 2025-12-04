"""
Utility tools for EduMentor system
"""

educational_tools = [
    "Content Generator",
    "Quiz Creator", 
    "Progress Tracker",
    "Concept Explainer",
    "Problem Solver"
]

def format_response(text, max_length=500):
    """Format AI responses for readability"""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def calculate_score(correct, total):
    """Calculate percentage score"""
    return (correct / total) * 100 if total > 0 else 0

def get_difficulty_level(age):
    """Determine appropriate difficulty level"""
    if age < 10:
        return "Beginner"
    elif age < 15:
        return "Intermediate"
    else:
        return "Advanced"

# Educational content templates
lesson_templates = {
    "science": "Topic: {topic}\n\nKey Concepts:\n1. {concept1}\n2. {concept2}\n\nExamples:\n- {example1}\n- {example2}",
    "math": "Problem: {problem}\n\nSolution Steps:\n1. {step1}\n2. {step2}\n\nPractice: {practice_question}",
    "history": "Event: {event}\n\nTimeline:\n- {date1}: {event1}\n- {date2}: {event2}\n\nSignificance: {significance}"
}
