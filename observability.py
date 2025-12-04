"""
Observability System for EduMentor AI
Implements course concepts: Logging, Tracing, Metrics
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any, Optional
import time
from functools import wraps

class AgentLogger:
    """Comprehensive logging for agent activities"""
    
    def __init__(self, log_file: str = "agent_logs.json"):
        self.log_file = log_file
        self.setup_logging()
        
    def setup_logging(self):
        """Setup structured logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('agent_system.log'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('EduMentorAI')
        self.logger.info("Agent Logger initialized")
    
    def log_agent_activity(self, agent_name: str, activity: str, details: Dict = None):
        """Log agent activity with structured data"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "activity": activity,
            "details": details or {},
            "level": "INFO"
        }
        
        # Write to structured log file
        self._append_to_json_log(log_entry)
        
        # Also use standard logging
        self.logger.info(f"{agent_name}: {activity}")
        if details:
            self.logger.debug(f"Details: {json.dumps(details, indent=2)}")
    
    def log_error(self, agent_name: str, error: Exception, context: Dict = None):
        """Log error with context"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "activity": "ERROR",
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context or {},
            "level": "ERROR"
        }
        
        self._append_to_json_log(log_entry)
        self.logger.error(f"{agent_name} error: {error}", exc_info=True)
    
    def _append_to_json_log(self, log_entry: Dict):
        """Append log entry to JSON log file"""
        try:
            # Read existing logs
            try:
                with open(self.log_file, 'r') as f:
                    logs = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                logs = []
            
            # Append new log
            logs.append(log_entry)
            
            # Write back (limit to last 1000 entries)
            with open(self.log_file, 'w') as f:
                json.dump(logs[-1000:], f, indent=2)
                
        except Exception as e:
            print(f"Failed to write to log file: {e}")


class AgentTracer:
    """Tracing for agent execution flow"""
    
    def __init__(self):
        self.traces = {}
        self.current_trace_id = None
    
    def start_trace(self, trace_id: str, operation: str, metadata: Dict = None):
        """Start a new trace"""
        self.current_trace_id = trace_id
        self.traces[trace_id] = {
            "trace_id": trace_id,
            "operation": operation,
            "start_time": time.time(),
            "metadata": metadata or {},
            "spans": []
        }
        return trace_id
    
    def add_span(self, span_name: str, agent: str, details: Dict = None):
        """Add a span to current trace"""
        if not self.current_trace_id:
            return
        
        span = {
            "span_name": span_name,
            "agent": agent,
            "start_time": time.time(),
            "details": details or {}
        }
        
        self.traces[self.current_trace_id]["spans"].append(span)
        return len(self.traces[self.current_trace_id]["spans"]) - 1
    
    def end_span(self, span_index: int, result: Any = None, error: Exception = None):
        """End a span"""
        if not self.current_trace_id or span_index >= len(self.traces[self.current_trace_id]["spans"]):
            return
        
        span = self.traces[self.current_trace_id]["spans"][span_index]
        span["end_time"] = time.time()
        span["duration"] = span["end_time"] - span["start_time"]
        span["result"] = str(result)[:200] if result else None
        span["error"] = str(error) if error else None
    
    def end_trace(self, result: Any = None, error: Exception = None):
        """End current trace"""
        if not self.current_trace_id:
            return
        
        trace = self.traces[self.current_trace_id]
        trace["end_time"] = time.time()
        trace["duration"] = trace["end_time"] - trace["start_time"]
        trace["result"] = str(result)[:200] if result else None
        trace["error"] = str(error) if error else None
        
        # Save trace
        self._save_trace(self.current_trace_id)
        
        trace_id = self.current_trace_id
        self.current_trace_id = None
        return trace_id
    
    def _save_trace(self, trace_id: str):
        """Save trace to file"""
        filename = f"traces/trace_{trace_id}.json"
        try:
            import os
            os.makedirs("traces", exist_ok=True)
            with open(filename, 'w') as f:
                json.dump(self.traces[trace_id], f, indent=2)
        except Exception as e:
            print(f"Failed to save trace: {e}")


class MetricsCollector:
    """Collect and report agent metrics"""
    
    def __init__(self):
        self.metrics = {
            "agent_calls": {},
            "response_times": [],
            "errors": [],
            "success_rate": 0,
            "total_queries": 0,
            "successful_queries": 0
        }
    
    def record_agent_call(self, agent_name: str, duration: float, success: bool = True):
        """Record agent call metrics"""
        if agent_name not in self.metrics["agent_calls"]:
            self.metrics["agent_calls"][agent_name] = {
                "total_calls": 0,
                "successful_calls": 0,
                "total_duration": 0,
                "avg_duration": 0
            }
        
        agent_metrics = self.metrics["agent_calls"][agent_name]
        agent_metrics["total_calls"] += 1
        agent_metrics["total_duration"] += duration
        
        if success:
            agent_metrics["successful_calls"] += 1
        
        agent_metrics["avg_duration"] = agent_metrics["total_duration"] / agent_metrics["total_calls"]
        
        # Overall metrics
        self.metrics["total_queries"] += 1
        if success:
            self.metrics["successful_queries"] += 1
            self.metrics["response_times"].append(duration)
        
        self.metrics["success_rate"] = (
            self.metrics["successful_queries"] / self.metrics["total_queries"] * 100
            if self.metrics["total_queries"] > 0 else 0
        )
    
    def record_error(self, agent_name: str, error: Exception):
        """Record error metrics"""
        self.metrics["errors"].append({
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "error": str(error),
            "error_type": type(error).__name__
        })
    
    def get_metrics_report(self) -> Dict:
        """Get comprehensive metrics report"""
        # Calculate averages
        avg_response_time = (
            sum(self.metrics["response_times"]) / len(self.metrics["response_times"])
            if self.metrics["response_times"] else 0
        )
        
        # Agent-specific metrics
        agent_performance = {}
        for agent_name, metrics in self.metrics["agent_calls"].items():
            agent_performance[agent_name] = {
                "call_count": metrics["total_calls"],
                "success_rate": metrics["successful_calls"] / metrics["total_calls"] * 100,
                "avg_response_time": metrics["avg_duration"],
                "total_duration": metrics["total_duration"]
            }
        
        return {
            "timestamp": datetime.now().isoformat(),
            "overall": {
                "total_queries": self.metrics["total_queries"],
                "successful_queries": self.metrics["successful_queries"],
                "success_rate": round(self.metrics["success_rate"], 2),
                "avg_response_time": round(avg_response_time, 3),
                "total_errors": len(self.metrics["errors"])
            },
            "agent_performance": agent_performance,
            "recent_errors": self.metrics["errors"][-5:] if self.metrics["errors"] else []
        }
    
    def save_metrics(self, filename: str = "metrics_report.json"):
        """Save metrics to file"""
        report = self.get_metrics_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        return report


# Decorators for easy observability
def trace_agent_operation(operation_name: str):
    """Decorator to trace agent operations"""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Get tracer if available
            tracer = getattr(self, 'tracer', None)
            trace_id = None
            
            if tracer:
                trace_id = tracer.start_trace(
                    trace_id=f"{operation_name}_{int(time.time())}",
                    operation=operation_name,
                    metadata={"agent": self.__class__.__name__}
                )
                span_idx = tracer.add_span("operation_execution", self.__class__.__name__)
            
            start_time = time.time()
            try:
                result = func(self, *args, **kwargs)
                duration = time.time() - start_time
                
                # Record metrics if available
                metrics = getattr(self, 'metrics', None)
                if metrics:
                    metrics.record_agent_call(self.__class__.__name__, duration, success=True)
                
                if tracer and trace_id:
                    tracer.end_span(span_idx, result=result)
                    tracer.end_trace(result=result)
                
                return result
                
            except Exception as e:
                duration = time.time() - start_time
                
                # Record error metrics
                metrics = getattr(self, 'metrics', None)
                if metrics:
                    metrics.record_agent_call(self.__class__.__name__, duration, success=False)
                    metrics.record_error(self.__class__.__name__, e)
                
                if tracer and trace_id:
                    tracer.end_span(span_idx, error=e)
                    tracer.end_trace(error=e)
                
                raise
        
        return wrapper
    return decorator


# Global observability instance
logger = AgentLogger()
tracer = AgentTracer()
metrics = MetricsCollector()

__all__ = ['AgentLogger', 'AgentTracer', 'MetricsCollector', 'trace_agent_operation', 'logger', 'tracer', 'metrics']
