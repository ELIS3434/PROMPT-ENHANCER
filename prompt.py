import warnings
import os
import logging
import sys
import time

# Import ML libraries first
import torch
import transformers
from transformers import pipeline

# Suppress TensorFlow warnings and logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0=all, 1=info, 2=warning, 3=error
logging.getLogger('tensorflow').setLevel(logging.ERROR)
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

# Disable Hugging Face warnings
transformers.logging.set_verbosity_error()

# Enable UTF-8 output
if sys.platform.startswith('win'):
    os.system('chcp 65001')

# Define symbols based on terminal support
try:
    # Test if terminal supports emojis
    print("🔄", end="", flush=True)
    print("\r", end="", flush=True)
    USE_EMOJI = True
except UnicodeEncodeError:
    USE_EMOJI = False

# Symbol sets
SYMBOLS = {
    'star': '🌟' if USE_EMOJI else '*',
    'robot': '🤖' if USE_EMOJI else '[AI]',
    'ruler': '📏' if USE_EMOJI else '>',
    'numbers': ['1️⃣', '2️⃣', '3️⃣', '4️⃣'] if USE_EMOJI else ['1.', '2.', '3.', '4.'],
    'target': '🎯' if USE_EMOJI else '>',
    'sparkles': '✨' if USE_EMOJI else '>',
    'error': '❌' if USE_EMOJI else 'x',
    'processing': '🔄' if USE_EMOJI else '...',
    'success': '✅' if USE_EMOJI else '+',
    'palette': '🎨' if USE_EMOJI else '#',
    'memo': '📝' if USE_EMOJI else '>',
    'chart': '📊' if USE_EMOJI else '>',
    'pencil': '✏️' if USE_EMOJI else '>',
    'wave': '👋' if USE_EMOJI else '>'
}

def print_with_style(text, symbol="", delay=0.03):
    """Print text with a typing effect and optional symbol"""
    print(symbol, end=" ")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def display_welcome():
    """Display welcome message with ASCII art"""
    welcome = f"""
    {SYMBOLS['star']} ================================== {SYMBOLS['star']}
    {SYMBOLS['robot']} Prompt Enhancement Assistant v1.0 {SYMBOLS['robot']}
    {SYMBOLS['star']} ================================== {SYMBOLS['star']}
    """
    print(welcome)

def get_token_length():
    """
    Get user input for token length choice with styled output
    """
    while True:
        print(f"\n{SYMBOLS['ruler']} Select Response Length:")
        print("╭" + "─" * 40 + "╮")
        print(f"│ {SYMBOLS['numbers'][0]}  64 tokens   │  Ultra Concise      │")
        print(f"│ {SYMBOLS['numbers'][1]}  128 tokens  │  Brief & Clear      │")
        print(f"│ {SYMBOLS['numbers'][2]}  256 tokens  │  Balanced & Rich    │")
        print(f"│ {SYMBOLS['numbers'][3]}  512 tokens  │  Detailed & Full    │")
        print("╰" + "─" * 40 + "╯")
        
        try:
            choice = input(f"\n{SYMBOLS['target']} Enter your choice (1-4): ")
            if choice == "1":
                print_with_style("Selected: Ultra Concise mode", SYMBOLS['sparkles'])
                return 64
            elif choice == "2":
                print_with_style("Selected: Brief & Clear mode", SYMBOLS['sparkles'])
                return 128
            elif choice == "3":
                print_with_style("Selected: Balanced & Rich mode", SYMBOLS['sparkles'])
                return 256
            elif choice == "4":
                print_with_style("Selected: Detailed & Full mode", SYMBOLS['sparkles'])
                return 512
            print(f"{SYMBOLS['error']} Please enter 1, 2, 3, or 4")
        except ValueError:
            print(f"{SYMBOLS['error']} Please enter a valid number (1-4)")

def enhance_prompt(prompt_text: str, max_length: int = 512) -> str:
    """
    Enhance a given prompt using the Flux-Prompt-Enhance model.
    """
    try:
        print_with_style(f"\n{SYMBOLS['processing']} Processing your prompt...", delay=0.05)
        
        # Initialize the pipeline
        pipe = pipeline("text2text-generation", model="gokaygokay/Flux-Prompt-Enhance")
        
        # Generate enhanced prompt with adjusted parameters for mid-sentence cutoff
        params = {
            'max_length': max_length,
            'do_sample': True,
            'temperature': 0.7,
            'num_beams': 1,
            'early_stopping': False,  # Don't stop at end of sentence
            'no_repeat_ngram_size': 2,
            'length_penalty': 1.0,  # Neutral length penalty
            'pad_token_id': pipe.tokenizer.pad_token_id,
            'eos_token_id': pipe.tokenizer.eos_token_id,
        }
        
        # For 64 tokens, adjust parameters to encourage mid-sentence cutoff
        if max_length == 64:
            params.update({
                'min_length': 60,  # Ensure we use most of the 64 tokens
                'temperature': 0.9,  # More randomness
                'length_penalty': 0.8,  # Slight penalty for longer sequences
                'early_stopping': False,  # Definitely don't stop at sentence end
            })
        
        result = pipe(prompt_text, **params)
        
        print_with_style(f"{SYMBOLS['success']} Enhancement complete!", delay=0.05)
        return result[0]['generated_text']
    
    except Exception as e:
        print_with_style(f"{SYMBOLS['error']} Error: {str(e)}", delay=0.05)
        return prompt_text

def display_results(original, length, enhanced):
    """Display results with styled formatting"""
    print("\n" + "═" * 50)
    print_with_style(f"{SYMBOLS['palette']} Enhancement Results:", delay=0.02)
    print("═" * 50)
    
    print(f"\n{SYMBOLS['memo']} Original Prompt:")
    print("╭" + "─" * 48 + "╮")
    # Split original text into lines if it's too long
    original_lines = [original[i:i+44] for i in range(0, len(original), 44)]
    for line in original_lines:
        print(f"│ {line:<44} │")
    print("╰" + "─" * 48 + "╯")
    
    print(f"\n{SYMBOLS['chart']} Token Length: {length} tokens")
    
    print(f"\n{SYMBOLS['sparkles']} Enhanced Prompt:")
    print("╭" + "─" * 48 + "╮")
    # Split enhanced text into lines of 44 characters
    enhanced_lines = [enhanced[i:i+44] for i in range(0, len(enhanced), 44)]
    for line in enhanced_lines:
        print(f"│ {line:<44} │")
    print("╰" + "─" * 48 + "╯")
    print("\n" + "═" * 50)

# Example usage
if __name__ == "__main__":
    try:
        display_welcome()
        
        # Get user input for prompt
        print_with_style(f"\n{SYMBOLS['pencil']} Enter your prompt:", delay=0.03)
        sample_prompt = input("> ")
        
        # Get token length choice from user
        max_length = get_token_length()
        
        # Enhance the prompt
        enhanced = enhance_prompt(sample_prompt, max_length=max_length)
        
        # Display results
        display_results(sample_prompt, max_length, enhanced)
        
        print_with_style(f"\n{SYMBOLS['wave']} Thank you for using Prompt Enhancement Assistant!", delay=0.03)
        
    except KeyboardInterrupt:
        print_with_style(f"\n\n{SYMBOLS['wave']} Goodbye! Have a great day!", delay=0.03)
    except Exception as e:
        print_with_style(f"\n{SYMBOLS['error']} An error occurred: {str(e)}", delay=0.03)