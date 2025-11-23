# 🎵 LambyTune - AI-Powered Song Creation Tool

LambyTune is an innovative AI-powered application that uses multiple specialized AI agents to collaboratively create complete songs with lyrics, structure, and chord progressions. Built with CrewAI, it orchestrates different AI personalities to handle various aspects of songwriting.

## Features

- **Multi-Agent Collaboration**: Five specialized AI agents work together to create your song
- **Complete Song Creation**: From concept to finished product with lyrics and chords
- **Structured Workflow**: Organized pipeline from creative direction to final editing
- **Customizable Themes**: Input any concept or theme for personalized songs
- **Chord Integration**: Automatic chord progression generation in C major
- **Consistent Output**: Ensures chorus sections remain identical throughout the song

## AI Agents

### Creative Director
- **Role**: Plans song structure and emotional flow
- **Responsibility**: Defines title, genre, mood, rhyme scheme, and sections

### Lyricist
- **Role**: Creates poetic and emotionally powerful lyrics
- **Responsibility**: Transforms structure into flowing verses and choruses

### Chorus Adjuster
- **Role**: Ensures chorus consistency
- **Responsibility**: Standardizes chorus sections throughout the song

### Composer
- **Role**: Adds musical harmony
- **Responsibility**: Generates chord progressions aligned with lyrics

### Editor
- **Role**: Final polishing and quality control
- **Responsibility**: Refines flow, removes repetitions, ensures stage-ready output

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Internet connection for AI model access

## Installation

1. **Clone or download the project**:
   ```bash
   cd lambytune
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Enter your song concept**:
   When prompted, input the theme or concept for your song (e.g., "love lost in autumn", "dreams of adventure", "city nightlife")

3. **Wait for creation**:
   The AI agents will work collaboratively to create your song. The process includes:
   - Planning the song structure
   - Writing lyrics
   - Adjusting chorus consistency
   - Adding chord progressions
   - Final editing and polishing

4. **View your song**:
   The complete song with lyrics and chords will be displayed in the terminal

## Project Structure

```
lambytune/
├── main.py              # Main application entry point
├── crew_config.py       # AI agent configuration and setup
├── crew_tasks.py        # Task definitions for the workflow
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Example Output

The application generates songs in this format:

```
Title: Autumn's Goodbye
Genre: Folk Ballad
Mood: Melancholic

[Verse 1]
C                    F
Golden leaves are falling down
Am                   G
On this quiet autumn ground
...

[Chorus]
F                    C
Time moves on, but I remain
G                    Am
Holding on through sun and rain
...
```

## Configuration

### Model Settings
- **Model**: GPT-4
- **Temperature**: 0.8 (for creative output)
- **Default Key**: C Major for chord progressions

### Customization Options
You can modify the following in `crew_config.py`:
- AI model temperature for more or less creative output
- Agent backstories for different creative styles
- Verbose mode settings for debugging

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed via `pip install -r requirements.txt`

2. **OpenAI API Errors**: 
   - Verify your API key is correctly set in the `.env` file
   - Check your OpenAI account has sufficient credits
   - Ensure internet connectivity

3. **Slow Response Times**: 
   - GPT-4 can take time for complex creative tasks
   - Consider reducing the complexity of your prompt

### Debug Mode
Set `verbose=True` in agent configurations for detailed output during execution.

## Future Enhancements

- [ ] Support for different musical keys
- [ ] Genre-specific composition styles
- [ ] Audio file generation
- [ ] Web interface
- [ ] Song export to various formats
- [ ] Collaboration features for human input

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.