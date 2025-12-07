#!/usr/bin/env python3
"""
Duolingo Copilot - An AI-powered bot to automate Duolingo Japanese learning lessons
using browser-use library for browser automation.
"""

import asyncio
import os
import sys
from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatBrowserUse


class DuolingoCopilot:
    """AI-powered Duolingo learning assistant."""
    
    def __init__(self, manual_login_wait_time: int = 30):
        """Initialize the Duolingo copilot.
        
        Args:
            manual_login_wait_time: Seconds to wait for manual login (default: 30)
        """
        load_dotenv()
        
        # Get credentials from environment
        self.username = os.getenv('DUOLINGO_USERNAME')
        self.password = os.getenv('DUOLINGO_PASSWORD')
        self.browser_use_api_key = os.getenv('BROWSER_USE_API_KEY')
        self.manual_login_wait_time = manual_login_wait_time
        
        # Validate environment variables
        if not self.browser_use_api_key:
            raise ValueError(
                "BROWSER_USE_API_KEY not found in environment. "
                "Get your API key from https://cloud.browser-use.com/new-api-key"
            )
        
        # Initialize browser and LLM
        self.browser = Browser()
        self.llm = ChatBrowserUse()
    
    async def login_to_duolingo(self):
        """
        Log in to Duolingo account.
        
        Returns:
            Agent: The agent that performed the login
        """
        if not self.username or not self.password:
            print("Warning: DUOLINGO_USERNAME and DUOLINGO_PASSWORD not set.")
            print("Proceeding without automatic login. You may need to log in manually.")
            return None
        
        login_task = f"""
        Go to https://www.duolingo.com and log in with the following credentials:
        - Username/Email: {self.username}
        - Password: {self.password}
        
        After logging in successfully, verify that you're on the home page or learning dashboard.
        """
        
        agent = Agent(
            task=login_task,
            llm=self.llm,
            browser=self.browser,
        )
        
        await agent.run()
        return agent
    
    async def complete_japanese_lesson(self):
        """
        Complete a Japanese lesson on Duolingo.
        
        This will navigate to the Japanese course, start a lesson,
        and use AI to answer the questions.
        
        Returns:
            Agent: The agent that completed the lesson
        """
        lesson_task = """
        Navigate to the Japanese course on Duolingo. If not already on the course page:
        1. Go to the home page or courses section
        2. Select the Japanese course
        3. Find and start the next available lesson or practice session
        
        Once in the lesson:
        1. Read each question carefully
        2. For multiple choice questions: Select the correct answer based on Japanese language knowledge
        3. For translation questions: Type the correct translation
        4. For listening questions: Listen and type what you hear or select the correct option
        5. For speaking questions: Skip or handle as best as possible
        6. For matching questions: Match the correct pairs
        
        Continue answering questions until the lesson is complete.
        If you make a mistake, learn from the correction and continue.
        Complete the entire lesson and reach the lesson completion screen.
        """
        
        agent = Agent(
            task=lesson_task,
            llm=self.llm,
            browser=self.browser,
        )
        
        await agent.run()
        return agent
    
    async def practice_japanese(self):
        """
        Start a practice session for Japanese.
        
        Returns:
            Agent: The agent that completed the practice
        """
        practice_task = """
        On Duolingo's Japanese course:
        1. Find and click on a practice or review button
        2. Complete the practice session by answering all questions
        3. Use your knowledge of Japanese to answer correctly
        4. Continue until the practice is complete
        """
        
        agent = Agent(
            task=practice_task,
            llm=self.llm,
            browser=self.browser,
        )
        
        await agent.run()
        return agent
    
    async def run_full_session(self):
        """
        Run a full Duolingo learning session.
        
        This will:
        1. Log in (if credentials provided)
        2. Complete a Japanese lesson
        """
        print("🤖 Starting Duolingo Copilot...")
        print("=" * 60)
        
        # Step 1: Login
        if self.username and self.password:
            print("\n📝 Step 1: Logging in to Duolingo...")
            await self.login_to_duolingo()
            print("✅ Login complete!")
        else:
            print("\n⚠️  Step 1: Skipping login (no credentials provided)")
            print("Please log in manually to Duolingo in the browser window.")
            print(f"Waiting {self.manual_login_wait_time} seconds for manual login...")
            await asyncio.sleep(self.manual_login_wait_time)
        
        # Step 2: Complete lesson
        print("\n📚 Step 2: Starting Japanese lesson...")
        await self.complete_japanese_lesson()
        print("✅ Lesson complete!")
        
        print("\n" + "=" * 60)
        print("🎉 Duolingo Copilot session complete!")


async def main():
    """Main entry point for the Duolingo copilot."""
    try:
        copilot = DuolingoCopilot()
        await copilot.run_full_session()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\n📋 Setup Instructions:")
        print("1. Copy .env.example to .env")
        print("2. Get your Browser Use API key from https://cloud.browser-use.com/new-api-key")
        print("3. Add your API key and Duolingo credentials to .env")
        print("4. Run the script again")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
