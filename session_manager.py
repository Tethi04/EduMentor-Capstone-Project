"""
Session and Memory Management for EduMentor AI
Implements course concepts: Sessions & Memory, State Management
"""

from datetime import datetime, timedelta
import json
import pickle
from typing import Dict, List, Any, Optional

class Session:
    """Individual student session with memory"""
    
    def __init__(self, student_id: str, session_id: str = None):
        self.student_id = student_id
        self.session_id = session_id or f"session_{student_id}_{datetime.now().timestamp()}"
        self.created_at = datetime.now()
        self.last_activity = datetime.now()
        self.interactions: List[Dict] = []
        self.learning_preferences = {}
        self.progress_tracking = {
            "subjects_studied": set(),
            "questions_asked": 0,
            "average_score": 0,
            "weak_areas": [],
            "strong_areas": []
        }
        self.context_memory = {
            "recent_topics": [],
            "learning_style": None,
            "difficulty_level": "intermediate"
        }
    
    def add_interaction(self, query: str, response: str, metadata: Dict = None):
        """Record a student-agent interaction"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "response": response[:500],  # Limit response length
            "response_time": (datetime.now() - self.last_activity).total_seconds(),
            "metadata": metadata or {}
        }
        
        self.interactions.append(interaction)
        self.last_activity = datetime.now()
        
        # Update progress tracking
        self.progress_tracking["questions_asked"] += 1
        
        # Extract subject from query if possible
        subjects = ["math", "science", "history", "programming", "literature"]
        for subject in subjects:
            if subject in query.lower():
                self.progress_tracking["subjects_studied"].add(subject)
                self.context_memory["recent_topics"].append(subject)
                break
        
        # Keep only last 10 topics
        self.context_memory["recent_topics"] = self.context_memory["recent_topics"][-10:]
    
    def update_learning_style(self, style: str):
        """Update student's preferred learning style"""
        self.context_memory["learning_style"] = style
    
    def update_difficulty(self, level: str):
        """Adjust difficulty based on performance"""
        self.context_memory["difficulty_level"] = level
    
    def get_session_summary(self) -> Dict:
        """Get comprehensive session summary"""
        return {
            "session_id": self.session_id,
            "student_id": self.student_id,
            "duration_minutes": (datetime.now() - self.created_at).total_seconds() / 60,
            "total_interactions": len(self.interactions),
            "active_subjects": list(self.progress_tracking["subjects_studied"]),
            "learning_style": self.context_memory["learning_style"],
            "difficulty_level": self.context_memory["difficulty_level"],
            "recent_topics": self.context_memory["recent_topics"][-5:],
            "session_age_minutes": (datetime.now() - self.last_activity).total_seconds() / 60
        }
    
    def is_active(self, timeout_minutes: int = 30) -> bool:
        """Check if session is still active"""
        return (datetime.now() - self.last_activity) < timedelta(minutes=timeout_minutes)
    
    def save_to_file(self, filename: str):
        """Save session to file for persistence"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Session':
        """Load session from file"""
        with open(filename, 'rb') as f:
            return pickle.load(f)


class SessionManager:
    """Manages multiple student sessions with memory persistence"""
    
    def __init__(self, persistence_file: str = "sessions.json"):
        self.sessions: Dict[str, Session] = {}
        self.persistence_file = persistence_file
        self.load_sessions()
    
    def create_session(self, student_id: str) -> Session:
        """Create new session for student"""
        session = Session(student_id)
        self.sessions[session.session_id] = session
        self.save_sessions()
        return session
    
    def get_session(self, session_id: str) -> Optional[Session]:
        """Get session by ID"""
        return self.sessions.get(session_id)
    
    def get_student_sessions(self, student_id: str) -> List[Session]:
        """Get all sessions for a student"""
        return [s for s in self.sessions.values() if s.student_id == student_id]
    
    def end_session(self, session_id: str):
        """End a session and save data"""
        if session_id in self.sessions:
            session = self.sessions[session_id]
            print(f"Session {session_id} ended for student {session.student_id}")
            print(f"Summary: {session.get_session_summary()}")
            # In production, would save to database
            self.save_sessions()
    
    def cleanup_inactive(self, timeout_minutes: int = 30):
        """Clean up inactive sessions"""
        inactive = []
        for session_id, session in self.sessions.items():
            if not session.is_active(timeout_minutes):
                inactive.append(session_id)
        
        for session_id in inactive:
            self.end_session(session_id)
            del self.sessions[session_id]
    
    def save_sessions(self):
        """Save all sessions to disk (simplified)"""
        # In production, use database
        sessions_data = {}
        for session_id, session in self.sessions.items():
            sessions_data[session_id] = {
                "student_id": session.student_id,
                "created_at": session.created_at.isoformat(),
                "interactions_count": len(session.interactions),
                "summary": session.get_session_summary()
            }
        
        with open(self.persistence_file, 'w') as f:
            json.dump(sessions_data, f, indent=2)
    
    def load_sessions(self):
        """Load sessions from disk (simplified)"""
        try:
            with open(self.persistence_file, 'r') as f:
                sessions_data = json.load(f)
            print(f"Loaded {len(sessions_data)} sessions from {self.persistence_file}")
        except FileNotFoundError:
            print(f"No existing sessions file found at {self.persistence_file}")
            sessions_data = {}
        
        return sessions_data
    
    def get_system_metrics(self) -> Dict:
        """Get metrics for observability"""
        active_sessions = sum(1 for s in self.sessions.values() if s.is_active())
        total_interactions = sum(len(s.interactions) for s in self.sessions.values())
        
        return {
            "total_sessions": len(self.sessions),
            "active_sessions": active_sessions,
            "total_interactions": total_interactions,
            "avg_interactions_per_session": total_interactions / len(self.sessions) if self.sessions else 0,
            "unique_students": len(set(s.student_id for s in self.sessions.values()))
        }


# Memory Bank for long-term student memory
class MemoryBank:
    """Long-term memory storage for student progress"""
    
    def __init__(self, storage_file: str = "memory_bank.json"):
        self.storage_file = storage_file
        self.memories: Dict[str, Dict] = self.load_memories()
    
    def add_memory(self, student_id: str, memory_type: str, content: Any):
        """Add memory for student"""
        if student_id not in self.memories:
            self.memories[student_id] = {}
        
        if memory_type not in self.memories[student_id]:
            self.memories[student_id][memory_type] = []
        
        self.memories[student_id][memory_type].append({
            "timestamp": datetime.now().isoformat(),
            "content": content
        })
        
        self.save_memories()
    
    def get_student_memories(self, student_id: str, memory_type: str = None) -> List:
        """Get memories for student"""
        if student_id not in self.memories:
            return []
        
        if memory_type:
            return self.memories[student_id].get(memory_type, [])
        else:
            # Return all memories
            all_memories = []
            for mem_type, memories in self.memories[student_id].items():
                all_memories.extend(memories)
            return all_memories
    
    def get_student_profile(self, student_id: str) -> Dict:
        """Get comprehensive student profile"""
        if student_id not in self.memories:
            return {"student_id": student_id, "memories": {}}
        
        return {
            "student_id": student_id,
            "memory_types": list(self.memories[student_id].keys()),
            "total_memories": sum(len(m) for m in self.memories[student_id].values()),
            "last_updated": datetime.now().isoformat()
        }
    
    def save_memories(self):
        """Save memories to disk"""
        with open(self.storage_file, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def load_memories(self) -> Dict:
        """Load memories from disk"""
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


# Export for use in main system
__all__ = ['Session', 'SessionManager', 'MemoryBank']
