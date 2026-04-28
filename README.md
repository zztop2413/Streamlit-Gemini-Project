# 📝 Note Summary & Quiz Generator

A Streamlit-powered web application that transforms images of notes into structured **Bangla summaries**, converts them to **natural-sounding audio**, and generates **customized quiz questions** based on your preferred difficulty level.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.56.0-red?logo=streamlit)](https://streamlit.io/)
[![Gemini AI](https://img.shields.io/badge/Gemini-API-green?logo=google)](https://ai.google.dev/)
[![gTTS](https://img.shields.io/badge/gTTS-Text_to_Speech-orange)](https://gtts.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Overview
Studying from handwritten or printed notes can be time-consuming. This app leverages **Google's Gemini AI** to instantly extract, summarize, and audio-convert your notes. It then tests your understanding by generating difficulty-based quiz questions, making it a complete all-in-one study companion.

## ✨ Features
- 📸 **Multi-Image Upload**: Upload up to 3 images of notes (JPG, PNG, JPEG)
- 🇧🇩 **Bangla Summaries**: AI-generated concise notes in Bangla (≤100 words)
- 🔊 **Text-to-Speech Audio**: Listen to your notes with in-memory audio playback
-  **Adaptive Quizzes**: Generate Easy, Medium, or Hard quizzes with answers
- 🎨 **Clean UI**: Responsive sidebar controls and loading spinners
- 🛡️ **Secure**: API keys managed via environment variables

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **AI Model** | Google Gemini (`google-genai`) |
| **TTS Engine** | gTTS (Google Text-to-Speech) |
| **Image Processing** | Pillow (PIL) |
| **Env Management** | `python-dotenv` |
| **Language** | Python 3.10+ |

