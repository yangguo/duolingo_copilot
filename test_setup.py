#!/usr/bin/env python3
"""
Simple test script to verify the Duolingo Copilot installation.

This script checks:
- Python version
- Required dependencies
- Environment configuration
- Import functionality
"""

import sys
import importlib.util


def check_python_version():
    """Check if Python version is 3.11+"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 11:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} (OK)")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} (Need 3.11+)")
        return False


def check_dependency(package_name):
    """Check if a package is installed."""
    spec = importlib.util.find_spec(package_name)
    return spec is not None


def check_dependencies():
    """Check if all required dependencies are installed."""
    print("\n📦 Checking dependencies...")
    
    required = {
        'browser_use': 'browser-use',
        'dotenv': 'python-dotenv',
        'langchain_openai': 'langchain-openai',
    }
    
    all_installed = True
    for module_name, package_name in required.items():
        if check_dependency(module_name):
            print(f"   ✅ {package_name}")
        else:
            print(f"   ❌ {package_name} (not installed)")
            all_installed = False
    
    return all_installed


def check_environment():
    """Check environment configuration."""
    print("\n⚙️  Checking environment configuration...")
    
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    api_key = os.getenv('BROWSER_USE_API_KEY')
    username = os.getenv('DUOLINGO_USERNAME')
    password = os.getenv('DUOLINGO_PASSWORD')
    
    if api_key:
        print("   ✅ BROWSER_USE_API_KEY is set")
    else:
        print("   ⚠️  BROWSER_USE_API_KEY not set (required)")
    
    if username and password:
        print("   ✅ Duolingo credentials are set")
    else:
        print("   ⚠️  Duolingo credentials not set (optional, can login manually)")
    
    return bool(api_key)


def check_imports():
    """Check if duolingo_copilot module can be imported."""
    print("\n📥 Checking module imports...")
    
    try:
        import duolingo_copilot
        print("   ✅ duolingo_copilot module imports successfully")
        return True
    except Exception as e:
        print(f"   ❌ Failed to import duolingo_copilot: {e}")
        return False


def main():
    """Run all checks."""
    print("=" * 60)
    print("🤖 Duolingo Copilot Installation Test")
    print("=" * 60)
    
    results = []
    
    # Run checks
    results.append(("Python Version", check_python_version()))
    results.append(("Dependencies", check_dependencies()))
    results.append(("Environment", check_environment()))
    results.append(("Module Import", check_imports()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {name}")
    
    all_passed = all(result[1] for result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All tests passed! You're ready to use Duolingo Copilot.")
        print("\nRun: python duolingo_copilot.py")
    else:
        print("⚠️  Some tests failed. Please check the output above.")
        print("\n📋 Next steps:")
        print("1. Install missing dependencies: pip install -r requirements.txt")
        print("2. Create .env file from .env.example")
        print("3. Add your BROWSER_USE_API_KEY to .env")
        print("4. Run this test again")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
