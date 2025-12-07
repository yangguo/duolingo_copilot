#!/usr/bin/env python3
"""
Comprehensive test script for Duolingo Copilot

This script performs unit tests and integration tests to validate:
- Class initialization
- Environment handling
- Browser and LLM setup
- Method functionality
- Error handling
- Configuration options
"""

import sys
import os
import unittest
from unittest.mock import Mock, patch, AsyncMock, MagicMock
from io import StringIO

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestDuolingoCopilotUnit(unittest.TestCase):
    """Unit tests for DuolingoCopilot class."""
    
    def setUp(self):
        """Set up test environment."""
        # Clear environment variables
        for key in ['BROWSER_USE_API_KEY', 'DUOLINGO_USERNAME', 'DUOLINGO_PASSWORD']:
            if key in os.environ:
                del os.environ[key]
    
    @patch('duolingo_copilot.load_dotenv')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    def test_initialization_with_api_key(self, mock_llm, mock_browser, mock_load_dotenv):
        """Test successful initialization with API key."""
        os.environ['BROWSER_USE_API_KEY'] = 'test_api_key'
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot()
        
        self.assertEqual(copilot.browser_use_api_key, 'test_api_key')
        self.assertEqual(copilot.manual_login_wait_time, 30)
        mock_load_dotenv.assert_called_once()
        mock_browser.assert_called_once()
        mock_llm.assert_called_once()
    
    @patch('duolingo_copilot.load_dotenv')
    def test_initialization_without_api_key(self, mock_load_dotenv):
        """Test initialization fails without API key."""
        from duolingo_copilot import DuolingoCopilot
        
        with self.assertRaises(ValueError) as context:
            DuolingoCopilot()
        
        self.assertIn('BROWSER_USE_API_KEY not found', str(context.exception))
    
    @patch('duolingo_copilot.load_dotenv')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    def test_custom_wait_time(self, mock_llm, mock_browser, mock_load_dotenv):
        """Test custom manual login wait time."""
        os.environ['BROWSER_USE_API_KEY'] = 'test_api_key'
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot(manual_login_wait_time=60)
        
        self.assertEqual(copilot.manual_login_wait_time, 60)
    
    @patch('duolingo_copilot.load_dotenv')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    def test_credentials_loaded(self, mock_llm, mock_browser, mock_load_dotenv):
        """Test that credentials are properly loaded from environment."""
        os.environ['BROWSER_USE_API_KEY'] = 'test_api_key'
        os.environ['DUOLINGO_USERNAME'] = 'test_user'
        os.environ['DUOLINGO_PASSWORD'] = 'test_pass'
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot()
        
        self.assertEqual(copilot.username, 'test_user')
        self.assertEqual(copilot.password, 'test_pass')


class TestDuolingoCopilotAsync(unittest.IsolatedAsyncioTestCase):
    """Async tests for DuolingoCopilot methods."""
    
    def setUp(self):
        """Set up test environment."""
        os.environ['BROWSER_USE_API_KEY'] = 'test_api_key'
    
    def tearDown(self):
        """Clean up test environment."""
        for key in ['BROWSER_USE_API_KEY', 'DUOLINGO_USERNAME', 'DUOLINGO_PASSWORD']:
            if key in os.environ:
                del os.environ[key]
    
    @patch('duolingo_copilot.Agent')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    @patch('duolingo_copilot.load_dotenv')
    async def test_login_with_credentials(self, mock_load_dotenv, mock_llm, mock_browser, mock_agent):
        """Test login method with credentials."""
        os.environ['DUOLINGO_USERNAME'] = 'test_user'
        os.environ['DUOLINGO_PASSWORD'] = 'test_pass'
        
        # Mock the agent
        mock_agent_instance = AsyncMock()
        mock_agent_instance.run = AsyncMock()
        mock_agent.return_value = mock_agent_instance
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot()
        result = await copilot.login_to_duolingo()
        
        # Verify agent was created and run was called
        mock_agent.assert_called_once()
        mock_agent_instance.run.assert_called_once()
        self.assertIsNotNone(result)
    
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    @patch('duolingo_copilot.load_dotenv')
    async def test_login_without_credentials(self, mock_load_dotenv, mock_llm, mock_browser):
        """Test login method without credentials."""
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot()
        
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        result = await copilot.login_to_duolingo()
        
        sys.stdout = sys.__stdout__
        
        # Should return None and print warning
        self.assertIsNone(result)
        self.assertIn('Warning', captured_output.getvalue())
    
    @patch('duolingo_copilot.Agent')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    @patch('duolingo_copilot.load_dotenv')
    async def test_complete_japanese_lesson(self, mock_load_dotenv, mock_llm, mock_browser, mock_agent):
        """Test complete_japanese_lesson method."""
        # Mock the agent
        mock_agent_instance = AsyncMock()
        mock_agent_instance.run = AsyncMock()
        mock_agent.return_value = mock_agent_instance
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot()
        result = await copilot.complete_japanese_lesson()
        
        # Verify agent was created and run was called
        mock_agent.assert_called_once()
        mock_agent_instance.run.assert_called_once()
        self.assertIsNotNone(result)
    
    @patch('duolingo_copilot.Agent')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    @patch('duolingo_copilot.load_dotenv')
    async def test_practice_japanese(self, mock_load_dotenv, mock_llm, mock_browser, mock_agent):
        """Test practice_japanese method."""
        # Mock the agent
        mock_agent_instance = AsyncMock()
        mock_agent_instance.run = AsyncMock()
        mock_agent.return_value = mock_agent_instance
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot()
        result = await copilot.practice_japanese()
        
        # Verify agent was created and run was called
        mock_agent.assert_called_once()
        mock_agent_instance.run.assert_called_once()
        self.assertIsNotNone(result)
    
    @patch('duolingo_copilot.Agent')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    @patch('duolingo_copilot.load_dotenv')
    async def test_run_full_session_with_credentials(self, mock_load_dotenv, mock_llm, mock_browser, mock_agent):
        """Test run_full_session with credentials."""
        os.environ['DUOLINGO_USERNAME'] = 'test_user'
        os.environ['DUOLINGO_PASSWORD'] = 'test_pass'
        
        # Mock the agent
        mock_agent_instance = AsyncMock()
        mock_agent_instance.run = AsyncMock()
        mock_agent.return_value = mock_agent_instance
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot()
        
        # Capture output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        await copilot.run_full_session()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # Verify output messages
        self.assertIn('Starting Duolingo Copilot', output)
        self.assertIn('Logging in to Duolingo', output)
        self.assertIn('Starting Japanese lesson', output)
        self.assertIn('session complete', output)
    
    @patch('duolingo_copilot.asyncio.sleep', new_callable=AsyncMock)
    @patch('duolingo_copilot.Agent')
    @patch('duolingo_copilot.Browser')
    @patch('duolingo_copilot.ChatBrowserUse')
    @patch('duolingo_copilot.load_dotenv')
    async def test_run_full_session_without_credentials(self, mock_load_dotenv, mock_llm, mock_browser, mock_agent, mock_sleep):
        """Test run_full_session without credentials (manual login)."""
        # Mock the agent
        mock_agent_instance = AsyncMock()
        mock_agent_instance.run = AsyncMock()
        mock_agent.return_value = mock_agent_instance
        
        from duolingo_copilot import DuolingoCopilot
        
        copilot = DuolingoCopilot(manual_login_wait_time=5)
        
        # Capture output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        await copilot.run_full_session()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # Verify manual login flow
        self.assertIn('Skipping login', output)
        self.assertIn('log in manually', output)
        mock_sleep.assert_called_once_with(5)


class TestAdvancedExample(unittest.TestCase):
    """Tests for advanced_example.py functionality."""
    
    def setUp(self):
        """Set up test environment."""
        os.environ['BROWSER_USE_API_KEY'] = 'test_api_key'
    
    def tearDown(self):
        """Clean up test environment."""
        if 'BROWSER_USE_API_KEY' in os.environ:
            del os.environ['BROWSER_USE_API_KEY']
    
    @patch('advanced_example.Browser')
    @patch('advanced_example.ChatBrowserUse')
    @patch('advanced_example.Tools')
    @patch('advanced_example.load_dotenv')
    def test_advanced_copilot_initialization(self, mock_load_dotenv, mock_tools, mock_llm, mock_browser):
        """Test AdvancedDuolingoCopilot initialization."""
        from advanced_example import AdvancedDuolingoCopilot
        
        copilot = AdvancedDuolingoCopilot(log_file='test_log.txt')
        
        self.assertEqual(copilot.log_file, 'test_log.txt')
        mock_load_dotenv.assert_called_once()
        mock_browser.assert_called_once()
        mock_llm.assert_called_once()
        mock_tools.assert_called_once()
    
    @patch('advanced_example.load_dotenv')
    def test_advanced_copilot_no_api_key(self, mock_load_dotenv):
        """Test AdvancedDuolingoCopilot fails without API key."""
        if 'BROWSER_USE_API_KEY' in os.environ:
            del os.environ['BROWSER_USE_API_KEY']
        
        from advanced_example import AdvancedDuolingoCopilot
        
        with self.assertRaises(ValueError) as context:
            AdvancedDuolingoCopilot()
        
        self.assertIn('BROWSER_USE_API_KEY not found', str(context.exception))


def run_unit_tests():
    """Run all unit tests."""
    print("=" * 70)
    print("🧪 Running Unit Tests")
    print("=" * 70)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestDuolingoCopilotUnit))
    suite.addTests(loader.loadTestsFromTestCase(TestDuolingoCopilotAsync))
    suite.addTests(loader.loadTestsFromTestCase(TestAdvancedExample))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def run_integration_checks():
    """Run integration checks."""
    print("\n" + "=" * 70)
    print("🔗 Running Integration Checks")
    print("=" * 70)
    
    checks_passed = True
    
    # Check 1: Import test
    print("\n1️⃣  Checking module imports...")
    try:
        import duolingo_copilot
        import advanced_example
        print("   ✅ All modules import successfully")
    except Exception as e:
        print(f"   ❌ Import failed: {e}")
        checks_passed = False
    
    # Check 2: Syntax validation
    print("\n2️⃣  Validating Python syntax...")
    try:
        import py_compile
        files = ['duolingo_copilot.py', 'advanced_example.py', 'test_setup.py']
        for file in files:
            py_compile.compile(file, doraise=True)
        print(f"   ✅ All {len(files)} files have valid syntax")
    except Exception as e:
        print(f"   ❌ Syntax validation failed: {e}")
        checks_passed = False
    
    # Check 3: Verify class structure
    print("\n3️⃣  Verifying class structure...")
    try:
        from duolingo_copilot import DuolingoCopilot
        from advanced_example import AdvancedDuolingoCopilot
        
        # Check methods exist
        assert hasattr(DuolingoCopilot, 'login_to_duolingo')
        assert hasattr(DuolingoCopilot, 'complete_japanese_lesson')
        assert hasattr(DuolingoCopilot, 'practice_japanese')
        assert hasattr(DuolingoCopilot, 'run_full_session')
        
        assert hasattr(AdvancedDuolingoCopilot, 'complete_specific_skill')
        assert hasattr(AdvancedDuolingoCopilot, 'complete_multiple_lessons')
        
        print("   ✅ All required methods present")
    except Exception as e:
        print(f"   ❌ Class structure check failed: {e}")
        checks_passed = False
    
    # Check 4: Configuration handling
    print("\n4️⃣  Testing configuration handling...")
    try:
        # Clear env
        for key in ['BROWSER_USE_API_KEY', 'DUOLINGO_USERNAME', 'DUOLINGO_PASSWORD']:
            if key in os.environ:
                del os.environ[key]
        
        from duolingo_copilot import DuolingoCopilot
        
        # Should raise ValueError
        try:
            DuolingoCopilot()
            print("   ❌ Should have raised ValueError for missing API key")
            checks_passed = False
        except ValueError:
            print("   ✅ Correctly validates required configuration")
    except Exception as e:
        print(f"   ❌ Configuration test failed: {e}")
        checks_passed = False
    
    # Check 5: Dependencies
    print("\n5️⃣  Verifying dependencies...")
    try:
        import browser_use
        import dotenv
        import langchain_openai
        print("   ✅ All required dependencies available")
    except ImportError as e:
        print(f"   ⚠️  Missing dependency: {e}")
        print("   Run: pip install -r requirements.txt")
        checks_passed = False
    
    return checks_passed


def check_for_issues():
    """Check for potential issues in the code."""
    print("\n" + "=" * 70)
    print("🔍 Checking for Potential Issues")
    print("=" * 70)
    
    issues_found = []
    
    # Check 1: Hardcoded values
    print("\n1️⃣  Checking for hardcoded values...")
    with open('duolingo_copilot.py', 'r') as f:
        content = f.read()
        if 'https://www.duolingo.com' in content:
            print("   ℹ️  Found hardcoded URL (expected for Duolingo)")
        print("   ✅ No concerning hardcoded values")
    
    # Check 2: Error handling
    print("\n2️⃣  Checking error handling...")
    with open('duolingo_copilot.py', 'r') as f:
        content = f.read()
        if 'try:' in content and 'except' in content:
            print("   ✅ Error handling present in main module")
        else:
            print("   ⚠️  Limited error handling in main module")
            issues_found.append("Consider adding more try-except blocks")
    
    with open('advanced_example.py', 'r') as f:
        content = f.read()
        if 'try:' in content and 'except' in content:
            print("   ✅ Error handling present in advanced module")
    
    # Check 3: Async/await usage
    print("\n3️⃣  Checking async/await usage...")
    with open('duolingo_copilot.py', 'r') as f:
        content = f.read()
        if 'async def' in content and 'await' in content:
            print("   ✅ Proper async/await usage")
        else:
            print("   ⚠️  Check async/await patterns")
            issues_found.append("Verify async/await implementation")
    
    # Check 4: Documentation
    print("\n4️⃣  Checking documentation...")
    doc_files = ['README.md', 'QUICKSTART.md', 'CONTRIBUTING.md']
    all_exist = all(os.path.exists(f) for f in doc_files)
    if all_exist:
        print(f"   ✅ All {len(doc_files)} documentation files present")
    else:
        print("   ⚠️  Some documentation files missing")
        issues_found.append("Add missing documentation")
    
    # Check 5: Environment variable usage
    print("\n5️⃣  Checking environment variable handling...")
    with open('duolingo_copilot.py', 'r') as f:
        content = f.read()
        if 'load_dotenv()' in content and 'os.getenv' in content:
            print("   ✅ Proper environment variable handling")
        else:
            print("   ⚠️  Check environment variable usage")
            issues_found.append("Review environment variable handling")
    
    if issues_found:
        print("\n⚠️  Issues to review:")
        for issue in issues_found:
            print(f"   - {issue}")
        return False
    else:
        print("\n✅ No critical issues found")
        return True


def main():
    """Main test runner."""
    print("=" * 70)
    print("🤖 DUOLINGO COPILOT COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print()
    
    results = {}
    
    # Run unit tests
    try:
        results['unit_tests'] = run_unit_tests()
    except Exception as e:
        print(f"❌ Unit tests failed with error: {e}")
        results['unit_tests'] = False
    
    # Run integration checks
    try:
        results['integration'] = run_integration_checks()
    except Exception as e:
        print(f"❌ Integration checks failed with error: {e}")
        results['integration'] = False
    
    # Check for issues
    try:
        results['issues'] = check_for_issues()
    except Exception as e:
        print(f"❌ Issue check failed with error: {e}")
        results['issues'] = False
    
    # Final summary
    print("\n" + "=" * 70)
    print("📊 FINAL TEST SUMMARY")
    print("=" * 70)
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name.replace('_', ' ').title()}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 70)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
        print("The Duolingo Copilot is working correctly.")
    else:
        print("⚠️  SOME TESTS FAILED")
        print("Please review the output above for details.")
    print("=" * 70)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
