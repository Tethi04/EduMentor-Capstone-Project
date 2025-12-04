"""
Utility Tools and Functions for EduMentor
Educational tools and helper functions
"""

import json
import re
from typing import Dict, List, Any, Optional
import random
from datetime import datetime, timedelta

# Core educational tools
educational_tools = [
    "Content Generator",
    "Quiz Creator", 
    "Progress Tracker",
    "Concept Explainer",
    "Problem Solver",
    "Assessment Builder",
    "Lesson Planner",
    "Discussion Facilitator",
    "Resource Finder",
    "Adaptive Learning Engine"
]

# Subject-specific tools
subject_tools = {
    "math": ["Equation Solver", "Graph Plotter", "Theorem Prover", "Calculator"],
    "science": ["Lab Simulator", "Data Analyzer", "Concept Visualizer", "Experiment Designer"],
    "history": ["Timeline Creator", "Source Analyzer", "Event Simulator", "Biography Generator"],
    "literature": ["Text Analyzer", "Writing Assistant", "Literary Device Finder", "Theme Explorer"]
}

def format_response(text: str, max_length: int = 500, include_summary: bool = True) -> str:
    """Format AI responses for readability"""
    if not text:
        return "No response generated."
    
    # Clean and format
    text = text.strip()
    
    # Add summary if requested
    if include_summary and len(text.split()) > 50:
        summary = f"📌 Summary: {text[:100]}..."
        text = f"{summary}\n\n{text}"
    
    # Truncate if too long
    if len(text) > max_length:
        text = text[:max_length] + "...\n\n[Response truncated. Use detailed mode for full response]"
    
    return text

def calculate_score(correct: int, total: int, weights: Optional[List[float]] = None) -> float:
    """Calculate weighted percentage score"""
    if total <= 0:
        return 0.0
    
    if weights and len(weights) == total:
        # Weighted score calculation
        weighted_correct = sum(weights[i] for i in range(total) if i < correct)
        weighted_total = sum(weights)
        return (weighted_correct / weighted_total) * 100
    else:
        # Simple percentage
        return (correct / total) * 100

def get_difficulty_level(age: int, subject: str = "general") -> str:
    """Determine appropriate difficulty level"""
    if age < 8:
        base_level = "Beginner"
    elif age < 12:
        base_level = "Elementary"
    elif age < 16:
        base_level = "Intermediate"
    elif age < 19:
        base_level = "Advanced"
    else:
        base_level = "University"
    
    # Adjust for subject
    subject_adjustments = {
        "math": {"Beginner": "Basic", "University": "Graduate"},
        "science": {"Beginner": "Introductory", "University": "Research"},
        "programming": {"Beginner": "Novice", "University": "Expert"}
    }
    
    return subject_adjustments.get(subject, {}).get(base_level, base_level)

def generate_quiz(topic: str, num_questions: int = 5, q_type: str = "multiple_choice") -> Dict:
    """Generate quiz questions on a topic"""
    question_templates = {
        "multiple_choice": {
            "science": [
                {
                    "question": "What process do plants use to convert sunlight into energy?",
                    "options": ["Respiration", "Photosynthesis", "Transpiration", "Germination"],
                    "answer": 1,
                    "explanation": "Photosynthesis is the process where plants convert light energy into chemical energy."
                }
            ],
            "math": [
                {
                    "question": "What is the value of π (pi) approximately?",
                    "options": ["3.14", "2.71", "1.61", "4.67"],
                    "answer": 0,
                    "explanation": "π is approximately 3.14159, often rounded to 3.14."
                }
            ]
        },
        "true_false": {
            "general": [
                {
                    "question": "The Earth revolves around the Sun.",
                    "answer": True,
                    "explanation": "Yes, the Earth orbits the Sun, which is a fundamental principle of our solar system."
                }
            ]
        }
    }
    
    # Select appropriate template
    subject = "general"
    for sub in ["science", "math", "history"]:
        if sub in topic.lower():
            subject = sub
            break
    
    # Generate questions
    questions = []
    templates = question_templates.get(q_type, {}).get(subject, [])
    
    for i in range(num_questions):
        if templates:
            template = templates[i % len(templates)].copy()
            template["question"] = template["question"].replace("{topic}", topic)
            questions.append(template)
        else:
            # Fallback question
            questions.append({
                "question": f"What is an important fact about {topic}?",
                "options": ["Option A", "Option B", "Option C", "Option D"] if q_type == "multiple_choice" else None,
                "answer": 0 if q_type == "multiple_choice" else True,
                "explanation": f"This question tests your understanding of {topic}."
            })
    
    return {
        "topic": topic,
        "type": q_type,
        "total_questions": num_questions,
        "questions": questions,
        "generated_at": datetime.now().isoformat()
    }

def create_lesson_plan(topic: str, duration: str = "1 hour", level: str = "Intermediate") -> Dict:
    """Create structured lesson plan"""
    plan = {
        "topic": topic,
        "duration": duration,
        "level": level,
        "objectives": [
            f"Understand key concepts of {topic}",
            f"Apply knowledge of {topic} to solve problems",
            f"Analyze real-world applications of {topic}"
        ],
        "materials_needed": [
            "Whiteboard or digital equivalent",
            "Handouts or digital resources",
            "Practice problems"
        ],
        "timeline": [
            {"duration": "10min", "activity": "Introduction & hook"},
            {"duration": "20min", "activity": "Direct instruction"},
            {"duration": "15min", "activity": "Guided practice"},
            {"duration": "10min", "activity": "Independent practice"},
            {"duration": "5min", "activity": "Review & assessment"}
        ],
        "assessment": f"Short quiz or exit ticket on {topic}",
        "differentiation": {
            "support": "Provide additional examples and one-on-one assistance",
            "extension": "Challenge problems or research assignment"
        }
    }
    
    return plan

def analyze_text_complexity(text: str) -> Dict:
    """Analyze text complexity for educational purposes"""
    words = text.split()
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Calculate metrics
    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    unique_words = len(set(word.lower() for word in words))
    lexical_density = (unique_words / len(words)) * 100 if words else 0
    
    # Determine grade level (simplified Flesch-Kincaid)
    grade_level = max(1, min(12, round(0.39 * avg_sentence_length + 11.8 * (avg_word_length/6) - 15.59)))
    
    complexity = "Easy" if grade_level <= 6 else "Moderate" if grade_level <= 9 else "Advanced"
    
    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_word_length": round(avg_word_length, 1),
        "unique_words": unique_words,
        "lexical_density": round(lexical_density, 1),
        "estimated_grade_level": grade_level,
        "complexity": complexity,
        "reading_time_minutes": round(len(words) / 200, 1)  # 200 wpm average
    }

# Educational content templates
lesson_templates = {
    "science": """🔬 Science Lesson: {topic}

🎯 Learning Objectives:
1. Understand the basic principles of {topic}
2. Identify real-world applications
3. Conduct related experiments or observations

📚 Key Concepts:
• Concept 1: {concept1}
• Concept 2: {concept2} 
• Concept 3: {concept3}

🧪 Activities:
1. Demonstration: {demo_activity}
2. Experiment: {experiment}
3. Discussion: {discussion_topic}

📊 Assessment:
• Quiz on key concepts
• Lab report
• Presentation on applications
""",

    "math": """🧮 Math Lesson: {topic}

🎯 Learning Objectives:
1. Master the fundamentals of {topic}
2. Apply formulas correctly
3. Solve real-world problems

📐 Key Formulas:
• Formula 1: {formula1}
• Formula 2: {formula2}

📝 Step-by-Step Examples:
Example 1: {example1}
Solution: {solution1}

Example 2: {example2}  
Solution: {solution2}

💡 Practice Problems:
1. {practice1}
2. {practice2}
3. {practice3}
""",

    "history": """📜 History Lesson: {topic}

🎯 Learning Objectives:
1. Understand the historical context of {topic}
2. Analyze causes and effects
3. Connect to modern implications

📅 Timeline:
• {date1}: {event1}
• {date2}: {event2}
• {date3}: {event3}

👥 Key Figures:
• {figure1}: {role1}
• {figure2}: {role2}

🤔 Discussion Questions:
1. {question1}
2. {question2}

📚 Primary Sources:
• Source 1: {source1}
• Source 2: {source2}
"""
}

def get_template(template_type: str, **kwargs) -> str:
    """Get formatted template with variables filled"""
    template = lesson_templates.get(template_type.lower(), "")
    if template:
        return template.format(**kwargs)
    return f"Template for {template_type} not found."

def create_study_schedule(topics: List[str], days: int = 7, hours_per_day: int = 2) -> Dict:
    """Create personalized study schedule"""
    total_hours = days * hours_per_day
    hours_per_topic = max(1, total_hours // len(topics))
    
    schedule = {}
    current_date = datetime.now().date()
    
    for i, topic in enumerate(topics):
        day_offset = i % days
        study_date = current_date + timedelta(days=day_offset)
        
        schedule[f"Day {i+1}"] = {
            "date": study_date.isoformat(),
            "topic": topic,
            "duration_hours": hours_per_topic,
            "activities": [
                "Review previous concepts",
                "Study new material",
                "Practice problems",
                "Self-assessment"
            ],
            "goals": [
                f"Understand key concepts of {topic}",
                "Complete practice exercises",
                "Identify areas needing review"
            ]
        }
    
    return {
        "total_days": days,
        "total_hours": total_hours,
        "hours_per_day": hours_per_day,
        "topics_covered": topics,
        "schedule": schedule,
        "recommendations": [
            "Take regular breaks (5-10 minutes per hour)",
            "Review previous topics weekly",
            "Practice recall through self-testing"
        ]
    }

def validate_student_response(response: str, expected_keywords: List[str]) -> Dict:
    """Validate student response against expected keywords"""
    response_lower = response.lower()
    
    found_keywords = []
    missing_keywords = []
    
    for keyword in expected_keywords:
        if keyword.lower() in response_lower:
            found_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)
    
    completeness = (len(found_keywords) / len(expected_keywords)) * 100 if expected_keywords else 0
    
    return {
        "response_length": len(response),
        "found_keywords": found_keywords,
        "missing_keywords": missing_keywords,
        "completeness_score": round(completeness, 1),
        "has_adequate_detail": len(response.split()) >= 20,
        "suggestions": f"Include concepts like: {', '.join(missing_keywords)}" if missing_keywords else "Good coverage of key concepts"
    }

# Export all functions and variables
__all__ = [
    'educational_tools',
    'subject_tools',
    'format_response',
    'calculate_score',
    'get_difficulty_level',
    'generate_quiz',
    'create_lesson_plan',
    'analyze_text_complexity',
    'lesson_templates',
    'get_template',
    'create_study_schedule',
    'validate_student_response'
    ]
