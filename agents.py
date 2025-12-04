"""
AI Agent System for EduMentor
Defines specialized educational agents including ROOT_AGENT
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


class GeminiAgent(EduMentorAgent):
    """Agent using Google's Gemini API"""
    
    def __init__(self, api_key=None):
        super().__init__(name="GeminiEdu", specialization="Advanced AI Tutoring")
        
        self.api_key = api_key
        self.gemini_available = False
        
        if api_key and api_key != "DEMO_KEY":
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-pro')
                self.gemini_available = True
                print("✅ Gemini AI initialized")
            except Exception as e:
                print(f"⚠️ Gemini initialization failed: {e}")
        else:
            print("⚠️ No valid API key - using fallback mode")
    
    def assist(self, query):
        """Enhanced assistance using Gemini AI"""
        if self.gemini_available:
            try:
                response = self.model.generate_content(query)
                return response.text
            except Exception as e:
                print(f"⚠️ Gemini API error: {e}")
        
        # Fallback to parent class
        return super().assist(query)


class TutorAgent(EduMentorAgent):
    """Specialized tutor agent for one-on-one instruction"""
    
    def __init__(self):
        super().__init__(name="TutorBot", specialization="Personalized Tutoring")
        self.student_profiles = {}


class AssessmentAgent(EduMentorAgent):
    """Specialized assessment agent for evaluation"""
    
    def __init__(self):
        super().__init__(name="AssessorBot", specialization="Assessment & Analytics")
        self.rubrics = {}
        self.analytics_data = []


# ============================================
# ROOT AGENT DEFINITION
# ============================================

# Create the main root agent instance
ROOT_AGENT = EduMentorAgent(
    name="EduMentorRoot",
    specialization="Primary Educational AI Assistant"
)

# Add enhanced capabilities
ROOT_AGENT.version = "1.0.0"
ROOT_AGENT.is_root = True
ROOT_AGENT.capabilities = [
    "Real-time educational Q&A",
    "Multi-subject expertise",
    "Content generation",
    "Student assessment",
    "Personalized learning paths"
]

# Enhanced assist method for root agent
def root_enhanced_assist(query):
    """Enhanced assistance for root agent"""
    enhanced_prompt = f"""
    As the primary educational AI assistant (EduMentorRoot), provide a comprehensive response:
    
    STUDENT QUERY: {query}
    
    Please ensure your response:
    1. Is clear and educational
    2. Includes key concepts
    3. Provides relevant examples
    4. Suggests further learning
    5. Is engaging and encouraging
    """
    
    # Use parent's assist method with enhanced prompt
    return EduMentorAgent.assist(ROOT_AGENT, enhanced_prompt)

# Attach the enhanced method
ROOT_AGENT.enhanced_assist = root_enhanced_assist

# Add usage tracking
ROOT_AGENT.usage_stats = {
    "total_requests": 0,
    "subjects_covered": set(),
    "last_active": datetime.now()
}

def track_and_assist(query):
    """Track usage and provide assistance"""
    ROOT_AGENT.usage_stats["total_requests"] += 1
    ROOT_AGENT.usage_stats["last_active"] = datetime.now()
    
    # Track subjects
    subjects = ["math", "science", "history", "programming", "literature"]
    for subject in subjects:
        if subject in query.lower():
            ROOT_AGENT.usage_stats["subjects_covered"].add(subject)
    
    return ROOT_AGENT.enhanced_assist(query)

ROOT_AGENT.track_and_assist = track_and_assist

# Get detailed stats method
def get_root_stats():
    """Get detailed statistics about root agent"""
    return {
        "agent_name": ROOT_AGENT.name,
        "specialization": ROOT_AGENT.specialization,
        "version": ROOT_AGENT.version,
        "is_root": ROOT_AGENT.is_root,
        "total_requests": ROOT_AGENT.usage_stats["total_requests"],
        "subjects_covered": list(ROOT_AGENT.usage_stats["subjects_covered"]),
        "last_active": ROOT_AGENT.usage_stats["last_active"].strftime("%Y-%m-%d %H:%M:%S"),
        "capabilities": ROOT_AGENT.capabilities,
        "created_at": ROOT_AGENT.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }

ROOT_AGENT.get_root_stats = get_root_stats

print(f"✅ Root Agent '{ROOT_AGENT.name}' initialized with enhanced capabilities")

# Export all agents
__all__ = [
    'EduMentorAgent',
    'GeminiAgent',
    'TutorAgent',
    'AssessmentAgent',
    'ROOT_AGENT'
]
