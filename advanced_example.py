#!/usr/bin/env python3
"""
Advanced Duolingo Copilot Example

This script demonstrates advanced usage of the Duolingo Copilot including:
- Custom tasks for specific lesson types
- Multiple lessons in sequence
- Custom tools and actions
"""

import asyncio
import os
from datetime import datetime
from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatBrowserUse, Tools


class AdvancedDuolingoCopilot:
    """Advanced Duolingo copilot with custom capabilities."""
    
    def __init__(self, log_file: str = 'lesson_log.txt'):
        """Initialize the advanced copilot.
        
        Args:
            log_file: Path to the lesson log file (default: 'lesson_log.txt')
        """
        load_dotenv()
        
        # Validate environment
        browser_use_api_key = os.getenv('BROWSER_USE_API_KEY')
        if not browser_use_api_key:
            raise ValueError(
                "BROWSER_USE_API_KEY not found in environment. "
                "Get your API key from https://cloud.browser-use.com/new-api-key"
            )
        
        self.log_file = log_file
        self.browser = Browser()
        self.llm = ChatBrowserUse()
        
        # Create custom tools
        self.tools = Tools()
        self._register_custom_tools()
    
    def _register_custom_tools(self):
        """Register custom tools for the agent."""
        
        @self.tools.action(
            description='Get a hint for a Japanese translation question. '
                       'Provide the Japanese text to get translation help.'
        )
        def get_translation_hint(japanese_text: str) -> str:
            """Provide a hint for Japanese translation."""
            return f"For '{japanese_text}': Think about common Japanese particles and sentence structure."
        
        @self.tools.action(
            description='Log lesson progress and track completed lessons.'
        )
        def log_progress(lesson_name: str, status: str) -> str:
            """Log lesson completion."""
            try:
                with open(self.log_file, 'a') as f:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    f.write(f"{timestamp} - {lesson_name}: {status}\n")
                return f"Logged: {lesson_name} - {status}"
            except (IOError, OSError) as e:
                error_msg = f"Failed to log progress: {str(e)}"
                print(f"Warning: {error_msg}")
                return error_msg
    
    async def complete_specific_skill(self, skill_name: str):
        """
        Complete a specific skill by name.
        
        Args:
            skill_name: The name of the skill to practice (e.g., "Hiragana 1")
        """
        task = f"""
        Navigate to the Japanese course on Duolingo and find the skill called "{skill_name}".
        Click on it to start a lesson for this specific skill.
        Complete the entire lesson, answering all questions correctly.
        """
        
        agent = Agent(
            task=task,
            llm=self.llm,
            browser=self.browser,
            tools=self.tools,
        )
        
        await agent.run()
    
    async def complete_multiple_lessons(self, num_lessons: int = 3):
        """
        Complete multiple lessons in sequence.
        
        Args:
            num_lessons: Number of lessons to complete
        """
        task = f"""
        On Duolingo's Japanese course, complete {num_lessons} lessons in sequence.
        
        For each lesson:
        1. Start the next available lesson
        2. Answer all questions to the best of your ability
        3. Complete the lesson and see the results
        4. Use the log_progress tool to record completion
        5. Move on to the next lesson
        
        Continue until you have completed all {num_lessons} lessons.
        """
        
        agent = Agent(
            task=task,
            llm=self.llm,
            browser=self.browser,
            tools=self.tools,
        )
        
        await agent.run()
    
    async def practice_weak_skills(self):
        """Practice skills that need strengthening."""
        task = """
        On Duolingo's Japanese course:
        1. Look for skills that are marked as needing practice (usually shown with a cracked icon or lower strength)
        2. Click on "Practice weak skills" or select a skill that needs practice
        3. Complete the practice session
        4. Log the completion using the log_progress tool
        """
        
        agent = Agent(
            task=task,
            llm=self.llm,
            browser=self.browser,
            tools=self.tools,
        )
        
        await agent.run()
    
    async def earn_daily_goal(self):
        """Complete lessons to achieve daily XP goal."""
        task = """
        On Duolingo:
        1. Check your daily XP goal and current progress
        2. Complete lessons until you reach your daily goal
        3. For each completed lesson, use log_progress to track it
        4. Stop when the daily goal is achieved
        """
        
        agent = Agent(
            task=task,
            llm=self.llm,
            browser=self.browser,
            tools=self.tools,
        )
        
        await agent.run()


async def example_specific_skill():
    """Example: Complete a specific skill."""
    print("📚 Example 1: Completing a specific skill")
    print("=" * 60)
    
    copilot = AdvancedDuolingoCopilot()
    await copilot.complete_specific_skill("Hiragana 1")
    
    print("✅ Specific skill completed!")


async def example_multiple_lessons():
    """Example: Complete multiple lessons."""
    print("📚 Example 2: Completing multiple lessons")
    print("=" * 60)
    
    copilot = AdvancedDuolingoCopilot()
    await copilot.complete_multiple_lessons(num_lessons=3)
    
    print("✅ Multiple lessons completed!")


async def example_practice_weak():
    """Example: Practice weak skills."""
    print("📚 Example 3: Practicing weak skills")
    print("=" * 60)
    
    copilot = AdvancedDuolingoCopilot()
    await copilot.practice_weak_skills()
    
    print("✅ Weak skills practiced!")


async def example_daily_goal():
    """Example: Achieve daily goal."""
    print("📚 Example 4: Achieving daily XP goal")
    print("=" * 60)
    
    copilot = AdvancedDuolingoCopilot()
    await copilot.earn_daily_goal()
    
    print("✅ Daily goal achieved!")


async def main():
    """Main entry point."""
    print("🤖 Advanced Duolingo Copilot Examples")
    print("=" * 60)
    print()
    print("Select an example to run:")
    print("1. Complete a specific skill (Hiragana 1)")
    print("2. Complete multiple lessons (3 lessons)")
    print("3. Practice weak skills")
    print("4. Achieve daily XP goal")
    print("5. Exit")
    print()
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        await example_specific_skill()
    elif choice == "2":
        await example_multiple_lessons()
    elif choice == "3":
        await example_practice_weak()
    elif choice == "4":
        await example_daily_goal()
    elif choice == "5":
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Please run again and select 1-5.")


if __name__ == "__main__":
    asyncio.run(main())
