# 🤖 Prompt Enhancement Assistant

A Python-based tool that enhances text prompts using advanced AI language models. This tool provides multiple token length options and features an interactive console interface with real-time visual feedback.

## ✨ Features

- **Multiple Token Length Options**:
  - 64 tokens: Ultra Concise (mid-sentence cutoff)
  - 128 tokens: Brief & Clear
  - 256 tokens: Balanced & Rich
  - 512 tokens: Detailed & Full

- **Interactive Console Interface**:
  - Beautiful ASCII/Emoji hybrid display
  - Real-time typing effects
  - Progress indicators
  - Error handling
  - Cross-platform compatibility

- **Smart Text Processing**:
  - AI-powered text enhancement
  - Configurable output lengths
  - Maintains context and coherence
  - Special handling for ultra-concise mode

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository or download the files
2. Install the required packages:
```bash
pip install -r requirements.txt
```

### Usage

Run the script from your terminal:
```bash
python prompt.py
```

Follow the interactive prompts:
1. Enter your text prompt
2. Choose desired token length (1-4)
3. Wait for AI enhancement
4. View the enhanced result

## 🛠️ Technical Details

- Uses Hugging Face Transformers library
- Model: gokaygokay/Flux-Prompt-Enhance
- Supports both emoji and ASCII display modes
- Automatic terminal capability detection
- UTF-8 encoding support

## ⚙️ Configuration

The script automatically:
- Detects terminal emoji support
- Configures appropriate display mode
- Suppresses unnecessary warnings
- Handles cross-platform encoding

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Hugging Face for the Transformers library
- Flux-Prompt-Enhance model creators
