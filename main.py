#!/usr/bin/env python3
"""
EduMentor: AI-Powered Educational Assistant
Main Application File
"""

import sys
import argparse
from agents import EduMentorAgent, TutorAgent, AssessmentAgent
from tools import (
    educational_tools, 
    format_response, 
    calculate_score,
    get_difficulty_level,
    lesson_templates
)

def display_banner():
    """Display application banner"""
    banner = """
    ╔══════════════════════════════════════════╗
    ║         🎓 EduMentor AI System           ║
    ║     Intelligent Educational Assistant    ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)

def initialize_system():
    """Initialize all system components"""
    print("Initializing EduMentor System...")
    
    agents = {
        "main": EduMentorAgent(),
        "tutor": TutorAgent(),
        "assessor": AssessmentAgent()
    }
    
    print(f"Agents initialized: {list(agents.keys())}")
    print(f"Available tools: {educational_tools}")
    
    return agents

def interactive_mode():
    """Run interactive mode"""
    agents = initialize_system()
    main_agent = agents["main"]
    
    print("\nInteractive Mode Activated")
    print("Type 'exit' to quit, 'help' for commands")
    
    while True:
        try:
            user_input = input("\nStudent Query: ").strip()
            
            if user_input.lower() == 'exit':
                print("Closing EduMentor. Have a great learning session!")
                break
            elif user_input.lower() == 'help':
                print("\nAvailable Commands:")
                print("- exit: Close application")
                print("- tools: List available tools")
                print("- agents: List available agents")
                print("- template [science|math|history]: Show template")
                continue
            elif user_input.lower() == 'tools':
                print(f"\nTools: {educational_tools}")
                continue
            elif user_input.lower() == 'agents':
                print("\nAvailable Agents:")
                for name, agent in agents.items():
                    print(f"  - {name}: {agent.specialization}")
                continue
            elif user_input.startswith('template '):
                template_type = user_input.split(' ', 1)[1]
                if template_type in lesson_templates:
                    print(f"\n{template_type.capitalize()} Template:")
                    print(lesson_templates[template_type])
                else:
                    print(f"Unknown template type. Available: {list(lesson_templates.keys())}")
                continue
            
            # Process query
            if user_input:
                print("\nProcessing your query...")
                response = main_agent.assist(user_input)
                formatted = format_response(response)
                print(f"\nResponse:\n{formatted}")
                
        except KeyboardInterrupt:
            print("\n\nInterrupted. Closing EduMentor.")
            break
        except Exception as e:
            print(f"Error: {e}")

def demo_mode():
    """Run demonstration mode"""
    print("\nRunning EduMentor Demo...")
    
    agents = initialize_system()
    main_agent = agents["main"]
    
    # Demo queries
    demo_queries = [
        "Explain photosynthesis in simple terms",
        "What is the Pythagorean theorem?",
        "Tell me about the French Revolution"
    ]
    
    for i, query in enumerate(demo_queries, 1):
        print(f"\n{'='*50}")
        print(f"Demo {i}: {query}")
        print(f"{'='*50}")
        
        response = main_agent.assist(query)
        print(f"Response: {format_response(response, 200)}")
        
        # Show assessment example
        if i == 1:
            print(f"\nAssessment Example:")
            assessment = agents["assessor"].evaluate("Photosynthesis converts sunlight to energy")
            print(f"Score: {assessment['score']}/100")
            print(f"Feedback: {assessment['feedback']}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='EduMentor AI Educational System')
    parser.add_argument('--mode', choices=['interactive', 'demo', 'test'], 
                       default='demo', help='Run mode')
    parser.add_argument('--query', type=str, help='Direct query (for test mode)')
    
    args = parser.parse_args()
    
    display_banner()
    
    if args.mode == 'interactive':
        interactive_mode()
    elif args.mode == 'demo':
        demo_mode()
    elif args.mode == 'test' and args.query:
        agents = initialize_system()
        response = agents["main"].assist(args.query)
        print(f"\nQuery: {args.query}")
        print(f"Response: {response}")
    else:
        print("Invalid mode or missing query. Use --help for options")

if __name__ == "__main__":
    main()
