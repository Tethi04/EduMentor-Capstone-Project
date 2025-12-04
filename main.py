#!/usr/bin/env python3
"""
EduMentor: AI-Powered Educational Assistant
Main Application File - Updated for Kaggle
"""

import sys
import os
import argparse

def setup_api_key():
    """Setup Gemini API key from multiple sources"""
    api_key = None
    
    # 1. Check environment variable
    api_key = os.environ.get('GEMINI_API_KEY')
    
    # 2. Check Kaggle Secrets (if running in Kaggle)
    if not api_key:
        try:
            from kaggle_secrets import UserSecretsClient
            user_secrets = UserSecretsClient()
            api_key = user_secrets.get_secret("GEMINI_API_KEY")
        except:
            pass
    
    # 3. Check file (if saved earlier)
    if not api_key and os.path.exists('/kaggle/working/api_key.txt'):
        with open('/kaggle/working/api_key.txt', 'r') as f:
            api_key = f.read().strip()
    
    return api_key

def main():
    """Main entry point - Updated for API key"""
    print("🎓 EduMentor AI Educational System")
    print("="*50)
    
    # Setup API key
    api_key = setup_api_key()
    
    if api_key:
        print(f"✅ API Key: Found ({api_key[:8]}...{api_key[-4:]})")
        
        # Configure Gemini
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            
            # Test the API
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content("Say 'Hello from EduMentor'")
            print(f"🤖 Gemini API: Connected - '{response.text}'")
            
        except Exception as e:
            print(f"⚠️ Gemini API Error: {e}")
            print("   Continuing in demo mode...")
            api_key = None
    else:
        print("⚠️ No API key found. Running in demo mode.")
    
    # Now import and run the rest of your system
    try:
        from agents import EduMentorAgent, GeminiAgent
        from tools import educational_tools, format_response
        
        print(f"\n📚 Available tools: {len(educational_tools)}")
        
        # Create agents with API key
        basic_agent = EduMentorAgent()
        gemini_agent = GeminiAgent(api_key=api_key)
        
        print(f"🤖 Agents created: {basic_agent.name}, {gemini_agent.name}")
        
        # Run demo
        print("\n" + "="*50)
        print("DEMO MODE")
        print("="*50)
        
        demo_queries = [
            "Explain photosynthesis",
            "What is Python programming?",
            "Tell me about the solar system"
        ]
        
        for query in demo_queries:
            print(f"\n❓ Query: {query}")
            print("-" * 30)
            
            # Get response from Gemini agent if available
            if gemini_agent.gemini_available:
                response = gemini_agent.assist(query)
                print(f"🌟 Gemini: {format_response(response, 100)}")
            else:
                response = basic_agent.assist(query)
                print(f"🤖 Basic: {format_response(response, 100)}")
        
        print("\n" + "="*50)
        print("✅ EduMentor System Ready!")
        print("="*50)
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\nTrying to download files...")
        
        # Try to download files
        github_url = "https://raw.githubusercontent.com/Tethi04/EduMentor-Capstone-Project/main/"
        !curl -s -L -o agents.py {github_url}agents.py
        !curl -s -L -o tools.py {github_url}tools.py
        
        # Try import again
        try:
            from agents import EduMentorAgent
            agent = EduMentorAgent()
            print(f"✅ Success! Agent created: {agent.name}")
        except:
            print("❌ Could not import. Please check your files.")
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
