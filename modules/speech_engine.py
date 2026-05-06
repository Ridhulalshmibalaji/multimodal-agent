"""
Speech Engine Module - TTS with adaptive prosody
"""

import pyttsx3
import time


_engine = None


def get_speech_engine():
    """
    Get or initialize the speech engine.
    
    Returns:
        pyttsx3.Engine: The TTS engine
    """
    global _engine
    
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty('rate', 150)  # Default rate
        _engine.setProperty('volume', 1.0)
    
    return _engine


def narrate(text, emotion, prosody_params):
    """
    Narrate text with prosody adjustments.
    
    Args:
        text (str): Text to narrate
        emotion (str): Emotion type
        prosody_params (dict): Prosody parameters
    """
    engine = get_speech_engine()
    
    # Apply prosody parameters
    engine.setProperty('rate', prosody_params['rate'])
    engine.setProperty('volume', 1.0)
    
    # Split text into paragraphs
    paragraphs = text.split('\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    
    print("\n" + "=" * 70)
    print(f"🎙️  {emotion.upper()} - {prosody_params['description']}")
    print("=" * 70)
    print(f"📊 Rate: {prosody_params['rate']} wpm | Pitch: {prosody_params['pitch']}x")
    print("=" * 70)
    
    # Narrate each paragraph
    for i, paragraph in enumerate(paragraphs, 1):
        total = len(paragraphs)
        print(f"\n🎙️  Speaking ({i}/{total})...")
        print(f"📝 {paragraph[:80]}{'...' if len(paragraph) > 80 else ''}")
        
        engine.say(paragraph)
        engine.runAndWait()
        
        # Add pause between paragraphs
        if i < total:
            time.sleep(prosody_params['pause'])
    
    print("\n✅ Narration complete!\n")


def list_voices():
    """
    List available voices.
    
    Returns:
        list: Voice objects
    """
    engine = get_speech_engine()
    return engine.getProperty('voices')


def set_voice(voice_id):
    """
    Set the voice to use.
    
    Args:
        voice_id (int): Voice index
    """
    engine = get_speech_engine()
    voices = engine.getProperty('voices')
    
    if 0 <= voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    else:
        raise ValueError(f"Invalid voice ID: {voice_id}")
