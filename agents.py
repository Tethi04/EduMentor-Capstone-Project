"""
AI Agent System for EduMentor
Defines specialized educational agents
"""

import random
from datetime import datetime

class EduMentorAgent:
    """Base educational AI agent with core capabilities"""
    
    def __init__(self, name="EduMentor", specialization="General Education"):
        self.name = name
        self.specialization = specialization
        self.knowledge_base = self._initialize_knowledge_base()
        self.conversation_history = []
        self.created_at = datetime.now()
        
        print(f"✅ {self.name} Agent initialized ({specialization})")
    
    def _initialize_knowledge_base(self):
        """Initialize agent's knowledge base"""
        return {
            "subjects": ["Math", "Science", "History", "Literature", "Programming"],
            "levels": ["Beginner", "Intermediate", "Advanced"],
            "teaching_styles": ["Socratic", "Demonstrative", "Interactive", "Problem-Based"]
        }
    
    def assist(self, query):
        """Process educational queries"""
        self.conversation_history.append({"role": "user", "content": query})
        
        # Process query based on specialization
        if "explain" in query.lower():
            response = self._explain_concept(query)
        elif "what is" in query.lower():
            response = self._define_concept(query)
        elif "how to" in query.lower():
            response = self._provide_instructions(query)
        elif "example" in query.lower():
            response = self._give_example(query)
        else:
            response = self._general_response(query)
        
        self.conversation_history.append({"role": "assistant", "content": response})
        return response
    
    def _explain_concept(self, query):
        """Explain educational concepts"""
        concepts = {
            "photosynthesis": "Photosynthesis is the process by which plants convert light energy into chemical energy...",
            "pythagorean theorem": "The Pythagorean theorem states that in a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides...",
            "french revolution": "The French Revolution (1789-1799) was a period of radical social and political upheaval in France..."
        }
        
        for concept, explanation in concepts.items():
            if concept in query.lower():
                return explanation
        
        return f"I'll explain '{query}'. This is a fundamental concept involving key principles that build upon basic understanding."
    
    def _define_concept(self, query):
        """Define concepts clearly"""
        return f"Definition: '{query}' refers to a core concept in education that involves understanding fundamental principles."
    
    def _provide_instructions(self, query):
        """Provide step-by-step instructions"""
        steps = [
            "First, understand the problem statement",
            "Identify key components and variables",
            "Apply relevant concepts or formulas",
            "Work through the solution step by step",
            "Verify your answer and reflect on the process"
        ]
        
        return f"For '{query}', follow these steps:\n" + "\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)])
    
    def _give_example(self, query):
        """Provide examples"""
        examples = {
            "math": "Example: If a triangle has sides 3 and 4, the hypotenuse is √(3² + 4²) = 5",
            "science": "Example: In photosynthesis, 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
            "history": "Example: The Storming of the Bastille on July 14, 1789, marked a turning point in the French Revolution"
        }
        
        for category, example in examples.items():
            if category in query.lower():
                return example
        
        return f"Here's an example related to '{query}': This demonstrates the practical application of the concept."
    
    def _general_response(self, query):
        """Generate general educational response"""
        responses = [
            f"Based on your question about '{query}', here's what you need to know...",
            f"That's an excellent question about '{query}'! The key points are...",
            f"Understanding '{query}' is crucial. The main concepts involve...",
            f"Regarding '{query}', educational research shows that..."
        ]
        
        return random.choice(responses)
    
    def evaluate(self, student_response, correct_answer=None):
        """Evaluate student responses"""
        if correct_answer:
            similarity_score = self._calculate_similarity(student_response, correct_answer)
            score = max(60, min(100, similarity_score * 100))
        else:
            score = random.randint(70, 95)
        
        feedbacks = [
            "Good understanding of the concept",
            "Clear explanation with room for more detail",
            "Accurate response demonstrating comprehension",
            "Well-structured answer with relevant points"
        ]
        
        return {
            "score": round(score, 1),
            "feedback": random.choice(feedbacks),
            "strengths": ["Conceptual understanding", "Clarity"],
            "areas_for_improvement": ["Add more examples", "Connect to related concepts"]
        }
    
    def _calculate_similarity(self, response1, response2):
        """Simple similarity calculation"""
        words1 = set(response1.lower().split())
        words2 = set(response2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def generate_content(self, topic, level="Intermediate", content_type="lesson"):
        """Generate educational content"""
        templates = {
            "lesson": f"""
            📚 Lesson: {topic}
            Level: {level}
            
            Learning Objectives:
            1. Understand key concepts of {topic}
            2. Apply knowledge to solve problems
            3. Connect {topic} to real-world applications
            
            Key Concepts:
            • Concept 1: Fundamental principle
            • Concept 2: Core mechanism
            • Concept 3: Practical implications
            
            Activities:
            1. Guided practice
            2. Group discussion
            3. Assessment quiz
            """,
            
            "quiz": f"""
            📝 Quiz: {topic}
            
            Question 1: What is the main concept of {topic}?
            A) Option A
            B) Option B
            C) Option C
            D) Option D
            
            Question 2: How does {topic} apply in real life?
            [Short answer question]
            
            Question 3: True or False: {topic} is only theoretical.
            """,
            
            "assignment": f"""
            📋 Assignment: {topic}
            Due: One week from today
            
            Task: Research and write about {topic}
            
            Requirements:
            • 500-1000 words
            • Include at least 3 references
            • Provide real-world examples
            • Submit in PDF format
            
            Grading Rubric:
            • Content (40%)
            • Structure (30%)
            • Examples (20%)
            • References (10%)
            """
        }
        
        return templates.get(content_type, templates["lesson"])
    
    def get_stats(self):
        """Get agent statistics"""
        return {
            "name": self.name,
            "specialization": self.specialization,
            "conversations": len(self.conversation_history) // 2,
            "active_since": self.created_at.strftime("%Y-%m-%d %H:%M"),
            "knowledge_subjects": len(self.knowledge_base["subjects"])
        }


class TutorAgent(EduMentorAgent):
    """Specialized tutor agent for one-on-one instruction"""
    
    def __init__(self):
        super().__init__(name="TutorBot", specialization="Personalized Tutoring")
        self.student_profiles = {}
        self.adaptive_questions = []
    
    def create_study_plan(self, student_level, goals, timeframe="1 month"):
        """Create personalized study plan"""
        return f"""
        📅 Personalized Study Plan
        
        Student Level: {student_level}
        Goals: {goals}
        Timeframe: {timeframe}
        
        Weekly Schedule:
        Week 1: Foundation building
        Week 2: Concept application  
        Week 3: Practice & review
        Week 4: Assessment & refinement
        
        Daily Tasks:
        • 30 minutes focused study
        • 15 minutes practice problems
        • 10 minutes review previous topics
        """
    
    def provide_feedback(self, student_work, rubric=None):
        """Provide detailed feedback on student work"""
        return {
            "overall_score": 85,
            "detailed_feedback": "Good effort with clear understanding. Consider adding more examples.",
            "strengths": ["Clear explanations", "Good structure"],
            "improvements": ["More detailed examples", "Connect to related topics"],
            "next_steps": ["Review section 3.2", "Practice with additional problems"]
        }


class AssessmentAgent(EduMentorAgent):
    """Specialized assessment agent for evaluation"""
    
    def __init__(self):
        super().__init__(name="AssessorBot", specialization="Assessment & Analytics")
        self.rubrics = {}
        self.analytics_data = []
    
    def create_rubric(self, criteria, weights):
        """Create assessment rubric"""
        rubric_id = f"rubric_{len(self.rubrics) + 1}"
        self.rubrics[rubric_id] = {
            "criteria": criteria,
            "weights": weights,
            "total_points": 100
        }
        return rubric_id
    
    def analyze_performance(self, scores, student_id=None):
        """Analyze student performance"""
        average = sum(scores) / len(scores) if scores else 0
        max_score = max(scores) if scores else 0
        min_score = min(scores) if scores else 0
        
        return {
            "average_score": round(average, 1),
            "highest_score": max_score,
            "lowest_score": min_score,
            "total_assessments": len(scores),
            "performance_level": self._get_performance_level(average)
        }
    
    def _get_performance_level(self, score):
        """Determine performance level"""
        if score >= 90:
            return "Excellent"
        elif score >= 80:
            return "Good"
        elif score >= 70:
            return "Satisfactory"
        elif score >= 60:
            return "Needs Improvement"
        else:
            return "Critical Review Needed"
    
    def generate_report(self, student_data, period="monthly"):
        """Generate comprehensive assessment report"""
        return f"""
        📊 Assessment Report
        Period: {period}
        Student: {student_data.get('name', 'Anonymous')}
        
        Summary:
        • Total assessments: {student_data.get('total_assessments', 0)}
        • Average score: {student_data.get('average_score', 0)}%
        • Performance level: {student_data.get('performance_level', 'N/A')}
        
        Recommendations:
        1. Focus on areas with lowest scores
        2. Increase practice frequency
        3. Seek clarification on challenging topics
        """


# Export commonly used agents
__all__ = ['EduMentorAgent', 'TutorAgent', 'AssessmentAgent']
