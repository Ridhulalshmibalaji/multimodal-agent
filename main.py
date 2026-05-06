"""
Smart Narrator AI - Main Application
Context-aware text-to-speech with adaptive prosody
"""

import sys
from modules.input_handler import get_multiline_input, validate_text, get_text_stats
from modules.context_analyzer import analyze_context, get_prosody_params, get_all_emotions
from modules.speech_engine import get_speech_engine, narrate


def print_header():
    """Print application header."""
    print("\n" + "=" * 70)
    print("🎙️  SMART NARRATOR AI - Context-Aware Text-to-Speech")
    print("=" * 70)
    print("Transform text into emotionally intelligent, expressive speech!")
    print("=" * 70 + "\n")


def print_menu():
    """Print main menu."""
    print("\n" + "─" * 70)
    print("📋 MAIN MENU")
    print("─" * 70)
    print("1. 🎙️  Narrate Custom Text")
    print("2. 📊 Analyze Text Context (without speaking)")
    print("3. 🎬 Run Demo Examples")
    print("4. ℹ️  About This Project")
    print("5. 🚪 Exit")
    print("─" * 70)


def narrate_custom_text():
    """Handle custom text narration."""
    print("\n" + "=" * 70)
    print("🎙️  CUSTOM TEXT NARRATION")
    print("=" * 70)
    
    # Get input
    text = get_multiline_input()
    if text is None:
        return
    
    # Validate text
    is_valid, message = validate_text(text)
    if not is_valid:
        print(f"❌ Validation Error: {message}")
        return
    
    print(f"✅ {message}")
    
    # Analyze context
    emotion, confidence = analyze_context(text)
    prosody_params = get_prosody_params(emotion, confidence)
    
    # Show analysis
    print("\n" + "=" * 70)
    print("📊 TEXT ANALYSIS")
    print("=" * 70)
    print(f"Emotion Detected: {emotion.upper()}")
    print(f"Confidence: {round(confidence * 100, 1)}%")
    
    stats = get_text_stats(text)
    print(f"📝 Stats: {stats['words']} words, {stats['lines']} lines")
    print(f"Prosody: {prosody_params['description']}")
    print("=" * 70)
    
    # Ask for confirmation
    confirm = input("\n🎙️  Ready to narrate? (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ Narration cancelled")
        return
    
    # Narrate
    narrate(text, emotion, prosody_params)


def analyze_text_context():
    """Analyze text without speaking."""
    print("\n" + "=" * 70)
    print("📊 TEXT CONTEXT ANALYSIS")
    print("=" * 70)
    
    # Get input
    text = get_multiline_input()
    if text is None:
        return
    
    # Validate text
    is_valid, message = validate_text(text)
    if not is_valid:
        print(f"❌ Validation Error: {message}")
        return
    
    # Analyze context
    emotion, confidence = analyze_context(text)
    prosody_params = get_prosody_params(emotion, confidence)
    stats = get_text_stats(text)
    
    # Show results
    print("\n" + "=" * 70)
    print("📊 ANALYSIS RESULTS")
    print("=" * 70)
    print(f"Input Text: {text[:100]}{'...' if len(text) > 100 else ''}")
    print()
    print(f"😊 Emotion Detected: {emotion.upper()}")
    print(f"📈 Confidence: {round(confidence * 100, 1)}%")
    print()
    print("📝 Text Statistics:")
    print(f"   • Words: {stats['words']}")
    print(f"   • Lines: {stats['lines']}")
    print(f"   • Characters: {stats['characters']}")
    print(f"   • CAPS Ratio: {round(stats['caps_ratio'] * 100, 1)}%")
    print(f"   • Punctuation Marks: {stats['punctuation_marks']}")
    print()
    print(f"🎙️  Speech Parameters for {emotion.upper()}:")
    print(f"   • Speech Rate: {prosody_params['rate']} wpm")
    print(f"   • Pitch: {prosody_params['pitch']}x")
    print(f"   • Pause Duration: {prosody_params['pause']}s")
    print(f"   • Description: {prosody_params['description']}")
    print("=" * 70 + "\n")


def run_demo():
    """Run demo examples for each emotion."""
    print("\n" + "=" * 70)
    print("🎬 DEMO - Emotion Examples")
    print("=" * 70)
    
    demos = [
        {
            "emotion": "alert",
            "text": "WARNING! CRITICAL SYSTEM ERROR! HELP NEEDED IMMEDIATELY!",
            "description": "🚨 Alert - Fast, urgent speech"
        },
        {
            "emotion": "happy",
            "text": "This is absolutely wonderful! I love this so much! Amazing!",
            "description": "😊 Happy - Energetic, upbeat speech"
        },
        {
            "emotion": "sad",
            "text": "I'm so sorry... This is truly tragic. I feel deeply for you.",
            "description": "😔 Sad - Reflective, somber speech"
        },
        {
            "emotion": "story",
            "text": "Once upon a time, in a magical kingdom far away, there lived a brave knight...",
            "description": "📖 Story - Engaging, narrative speech"
        },
        {
            "emotion": "normal",
            "text": "Hello there. How are you doing today? This is normal conversation.",
            "description": "🔹 Normal - Conversational, neutral speech"
        }
    ]
    
    for i, demo in enumerate(demos, 1):
        print(f"\n[{i}/5] {demo['description']}")
        print("-" * 70)
        
        confirm = input("Play this demo? (y/n/skip-rest): ").strip().lower()
        if confirm == 'skip-rest':
            break
        elif confirm != 'y':
            continue
        
        emotion = demo['emotion']
        text = demo['text']
        prosody_params = get_prosody_params(emotion, 0.95)
        
        narrate(text, emotion, prosody_params)


def print_about():
    """Print about information."""
    print("\n" + "=" * 70)
    print("ℹ️  ABOUT SMART NARRATOR AI")
    print("=" * 70)
    print("""
🎯 PROJECT OVERVIEW
Smart Narrator AI transforms text into emotionally intelligent speech.
Instead of robotic, flat narration, the system analyzes emotional context
and adapts voice characteristics accordingly.

🧠 HOW IT WORKS
1. Text Analysis → Detects emotional context (alert, happy, sad, story)
2. Prosody Calculation → Determines how to speak (speed, pitch, pauses)
3. Speech Synthesis → Narrates text with appropriate emotional tone

🔥 KEY FEATURES
✅ 5 Emotional Contexts (Alert, Happy, Sad, Story, Normal)
✅ Real-time Emotion Detection
✅ Adaptive Speech Prosody
✅ Multi-paragraph Awareness
✅ Offline Operation (No Internet Required)
✅ Cross-platform Support (Windows, Mac, Linux)

💡 USE CASES
• Accessibility: Making text-to-speech more natural and engaging
• Entertainment: Dramatic narration of stories and scripts
• Education: More engaging content delivery
• Alerts: Urgent warnings with appropriate urgency
• Accessibility: Better experience for visually impaired users

🚀 TECHNOLOGY STACK
• Python 3.7+
• pyttsx3 (Cross-platform TTS)
• Custom NLP for emotion detection
• Adaptive prosody algorithm

👨‍💻 AUTHOR
Ridhulalshmibalaji
GitHub: https://github.com/Ridhulalshmibalaji

📖 DOCUMENTATION
See README.md for detailed documentation

📄 LICENSE
MIT License - Free to use and modify
    """)
    print("=" * 70 + "\n")


def main():
    """Main application loop."""
    print_header()
    
    engine = get_speech_engine()
    print(f"✅ Speech Engine Initialized")
    print(f"   Engine: pyttsx3")
    print(f"   Voices Available: {len(engine.list_voices())}")
    print()
    
    while True:
        print_menu()
        choice = input("Select option (1-5): ").strip()
        
        if choice == '1':
            narrate_custom_text()
        elif choice == '2':
            analyze_text_context()
        elif choice == '3':
            run_demo()
        elif choice == '4':
            print_about()
        elif choice == '5':
            print("\n👋 Thank you for using Smart Narrator AI!")
            print("Goodbye!\n")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please select 1-5.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
