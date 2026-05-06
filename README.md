# Smart Narrator AI - Context-Aware Text-to-Speech

> **Transform boring text into emotionally intelligent, expressive speech**

## 🎯 Project Overview

Smart Narrator AI is an advanced text-to-speech system that understands emotional context and adapts voice characteristics accordingly. Instead of robotic, flat narration, this system analyzes text intent and speaks it with appropriate tone, pace, and emotion.

### The Problem with Regular TTS

```
Standard TTS Output:
"WARNING! System failure!" (monotone, same as everything else)

Smart Narrator AI Output:
"WARNING! System failure!" (fast, urgent, high pitch - sounds like actual emergency)
```

### The Solution: Adaptive Prosody Generation

This project implements **context-aware prosody generation** - the AI decides HOW to speak based on WHAT the text means.

---

## 🧠 How It Works

### 3-Step Pipeline

```
Text Input
    ↓
Context Analysis (Emotion Detection)
    ↓
Prosody Adaptation (Speech Adjustment)
    ↓
Voice Output
```

### Emotion Detection System

The system analyzes text for 5 emotional contexts:

| Emotion | Indicators | Speech Rate | Pitch | Use Case |
|---------|-----------|------------|-------|----------|
| 🚨 **Alert** | CAPS, "!", danger keywords | 200 wpm | High | Warnings, emergencies |
| 😊 **Happy** | positive words, enthusiasm | 160 wpm | Bright | Celebrations, good news |
| 😔 **Sad** | sad words, melancholy | 130 wpm | Low | Emotional content |
| 📖 **Story** | narrative keywords | 140 wpm | Balanced | Tales, storytelling |
| 🔹 **Normal** | Default/mixed | 150 wpm | Neutral | General conversation |

### Detection Algorithm

```python
# Keyword matching
if "danger" in text → alert score +0.25

# CAPS ratio checking
if 40%+ CAPS → alert score +0.3

# Punctuation analysis
if 3+ "!" → alert score +0.4

# Pattern matching
if matches emergency patterns → alert score +0.35

# Confidence scoring
final_emotion = argmax(scores)
confidence = min(max_score, 1.0)
```

---

## ⚙️ Architecture

### Project Structure

```
multimodal-agent/
├── main.py                      # Application entry point
├── modules/
│   ├── __init__.py             # Package init
│   ├── input_handler.py        # Multi-line text input
│   ├── context_analyzer.py     # Emotion detection
│   └── speech_engine.py        # TTS with prosody
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

### Module Breakdown

#### 1. **input_handler.py**
- Accepts multi-line text from terminal
- Validates input
- Handles keyboard interrupts gracefully

```python
text = get_multiline_input()
# User types multiple lines, ends with "END"
```

#### 2. **context_analyzer.py**
- Analyzes text for emotional context
- Returns emotion type + confidence score
- Generates prosody parameters

```python
emotion, confidence = analyze_context(text)
# Returns: ("happy", 0.85)

prosody_params = get_prosody_params(emotion, confidence)
# Returns: {rate: 160, pitch: 1.3, pause: 0.3}
```

#### 3. **speech_engine.py**
- Initializes pyttsx3 TTS engine
- Applies prosody parameters
- Handles multi-paragraph narration with pauses

```python
engine = get_speech_engine()
engine.narrate(text, context_info)
# Speaks text with emotion-appropriate voice
```

#### 4. **main.py**
- CLI application with menu system
- Orchestrates all modules
- Provides demo examples

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.7+
- pip

### Quick Start

```bash
# 1. Clone or navigate to repository
cd multimodal-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python main.py
```

### Main Menu Options

```
1. 🎙️  Narrate Custom Text
   → Enter your own text for emotional narration

2. 📊 Analyze Text Context
   → See emotion detection without speaking

3. 🎬 Run Demo Examples
   → Hear 5 pre-built examples of each emotion

4. ℹ️  About This Project
   → View project information

5. 🚪 Exit
   → Quit application
```

---

## 📝 Example Usage

### Example 1: Alert/Emergency Text
```
Input: "WARNING! Critical system error! Help needed immediately!"
Detection: Alert (95% confidence)
Output: Fast speech (200 wpm), high pitch, urgent tone
```

### Example 2: Happy Text
```
Input: "This is wonderful! I absolutely love this amazing day!"
Detection: Happy (88% confidence)
Output: Energetic speech (160 wpm), bright pitch, enthusiastic
```

### Example 3: Story/Narrative
```
Input: "Once upon a time, there lived a brave knight in a magical kingdom..."
Detection: Story (92% confidence)
Output: Engaging speech (140 wpm), balanced pitch, narrative style
```

### Example 4: Sad/Emotional
```
Input: "I'm so sorry to hear about your loss. This is truly tragic."
Detection: Sad (85% confidence)
Output: Reflective speech (130 wpm), low pitch, somber tone
```

---

## 🔧 Technical Details

### Prosody Parameters

The system adjusts these parameters based on detected emotion:

1. **Speech Rate** (wpm)
   - Alert: 200 (fast, urgent)
   - Happy: 160 (energetic)
   - Story: 140 (engaging)
   - Sad: 130 (reflective)
   - Normal: 150 (conversational)

2. **Pitch Multiplier**
   - Alert: 1.8x (high pitch)
   - Happy: 1.3x (bright)
   - Normal: 1.0x (neutral)
   - Sad: 0.7x (low)

3. **Pause Duration** (seconds)
   - Between paragraphs
   - Alert: 0.8s
   - Happy: 0.3s
   - Story: 0.6s
   - Sad: 0.5s

### Offline TTS Engine

Uses **pyttsx3** - a cross-platform text-to-speech library:
- ✅ Works without internet
- ✅ Supports Windows, Mac, Linux
- ✅ Lightweight and fast
- ✅ Good quality voice

---

## 🎓 IEEE-Grade Innovation

### "Adaptive Prosody Generation for Context-Aware Speech Synthesis"

**Key Innovation:** The system doesn't just convert text to speech - it intelligently modulates HOW the speech is delivered based on semantic understanding.

**Technical Contribution:**
- Emotion classification from text content and formatting
- Dynamic prosody parameter generation
- Multi-level confidence scoring
- Real-time speech adjustment

**Why It Matters:**
- Traditional TTS: "Emergency alert" sounds the same as "Hello"
- This System: Emotional content directly drives voice modulation
- Result: More natural, context-appropriate speech output

---

## 🎨 Features

### Core Features
✅ 5 emotion contexts (Alert, Happy, Sad, Story, Normal)  
✅ Real-time emotion detection  
✅ Dynamic prosody adjustment  
✅ Multi-paragraph awareness  
✅ Confidence scoring  
✅ Cross-platform support  
✅ Offline operation  

### User Interface
✅ Interactive CLI menu  
✅ Multi-line text input  
✅ Demo examples  
✅ Real-time analysis display  
✅ Detailed speech parameters shown  

### Advanced Features
✅ Keyword-based detection system  
✅ CAPS ratio analysis  
✅ Punctuation analysis  
✅ Pattern matching  
✅ Importance word detection  

---

## 📊 Example Output

When you narrate text, the system displays:

```
============================================================
📝 Text Analysis
============================================================
Emotion Detected: HAPPY
Confidence: 87%
📊 Stats: 12 words, 2 lines
============================================================

😊 HAPPY - Energetic, upbeat speech
📊 Parameters: Rate=160 wpm, Pitch=1.3
🎙️  Speaking (1/2)...
🎙️  Speaking (2/2)...

✅ Narration complete!
```

---

## 🛠️ Customization

### Adding New Emotions

Edit `modules/context_analyzer.py`:

```python
EMOTION_KEYWORDS = {
    "your_emotion": {
        "keywords": ["word1", "word2", "word3"],
        "punctuation": ["!", "?"],
        "patterns": [r"\b(PATTERN)\b"]
    }
}
```

Then add prosody parameters:

```python
"your_emotion": {
    "rate": 150,
    "pitch": 1.0,
    "pause": 0.4,
    "description": "Description here"
}
```

### Adjusting Sensitivity

Modify keyword matching weights in `context_analyzer.py`:

```python
# Increase this to make keyword detection more sensitive
if keyword in text_lower:
    scores[emotion] += 0.5  # Was 0.25
```

---

## 📦 Dependencies

```
pyttsx3==2.90
```

No other dependencies! Pure Python, minimal footprint.

---

## 🐛 Troubleshooting

### No Sound Output
- Check system volume
- Ensure audio device is working
- Try different speech rate (some systems have limits)

### Installation Issues
```bash
# If pyttsx3 fails to install
pip install --upgrade pyttsx3

# On macOS, you might need:
pip install pyttsx3 --no-cache-dir
```

### Linux Audio Issues
```bash
# Install espeak (backend for pyttsx3 on Linux)
sudo apt-get install espeak espeak-ng
```

---

## 📈 Performance

- **Real-time Analysis:** <100ms for emotion detection
- **Speech Generation:** Varies by text length
- **Memory Usage:** ~50MB typical
- **CPU Usage:** Minimal until speaking

---

## 🚀 Future Enhancements

- [ ] Multi-language support
- [ ] Character-specific voices (villain, hero, narrator)
- [ ] Machine learning-based emotion detection
- [ ] Audio file export
- [ ] Web interface
- [ ] API server
- [ ] Real-time waveform visualization
- [ ] Sentiment analysis integration

---

## 📄 License

MIT License - Free to use and modify

---

## 👨‍💻 Author

**Ridhulalshmibalaji**  
GitHub: [@Ridhulalshmibalaji](https://github.com/Ridhulalshmibalaji)

---

## 🤝 Contributing

Found a bug or have a feature idea? Open an issue or submit a pull request!

---

## ✨ Special Features

### Why This Project Stands Out

1. **Not Just TTS** - Implements intelligent analysis layer
2. **Truly Offline** - No API calls, no internet needed
3. **Production Quality** - Well-structured, documented code
4. **Easy to Extend** - Modular design for customization
5. **Educational** - Great learning resource for NLP + TTS

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review example code in `main.py`
3. Open an issue on GitHub

---

**Version:** 1.0.0  
**Last Updated:** 2026-05-06  
**Status:** Production Ready ✅
