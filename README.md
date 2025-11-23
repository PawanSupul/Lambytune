# Lambytune 🎵

An AI-powered songwriter agent that generates complete song lyrics based on your ideas. Lambytune uses advanced language models to plan song structures and create coherent, themed lyrics with proper verse-chorus arrangements.

## Features

- **Intelligent Song Planning**: Automatically determines song structure, genre, mood, and rhyme schemes
- **Section-Based Generation**: Creates verses, choruses, bridges with consistent themes
- **Chorus Reuse**: Intelligently reuses choruses for proper song structure
- **Customizable Rhyme Patterns**: Supports various rhyme schemes (AABB, ABAB, etc.)
- **Context-Aware**: Each section builds upon previous lyrics for coherence

## Project Structure

```
lambytune/
├── agent.py          # Main orchestration logic
├── planner.py        # Song structure planning using AI
├── generator.py      # Individual section generation
├── main.py          # Entry point and user interface
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Installation

1. **Clone or download the project**
   ```bash
   cd lambytune
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Get your OpenAI API key from: https://platform.openai.com/api-keys

## Usage

### Basic Usage

Run the songwriter agent:
```bash
python main.py
```

When prompted, enter your song idea:
```
Please enter your song idea (e.g., 'a sad ballad about rain'): a love song about missing someone
```

### Example Output

The agent will:
1. Plan the song structure (title, genre, mood, sections)
2. Generate each section sequentially
3. Present the complete song with proper formatting

Sample output structure:
```
SONG PLAN:
Title: Missing You Tonight
Genre: Pop Ballad
Mood: Melancholic
Sections: ['Verse 1', 'Chorus', 'Verse 2', 'Chorus', 'Bridge', 'Chorus']

# Missing You Tonight

## Verse 1:
[Generated verse lyrics...]

## Chorus:
[Generated chorus lyrics...]

## Verse 2:
[Generated verse lyrics...]
...
```

## How It Works

### 1. Song Planning (`planner.py`)
- Uses LangChain OpenAI to analyze your prompt
- Returns structured JSON with song metadata:
  - Title and genre suggestions
  - Mood and emotional tone
  - Rhyme scheme (AABB, ABAB, etc.)
  - Section order (Verse-Chorus-Bridge structure)

### 2. Section Generation (`generator.py`)
- Generates individual song sections based on:
  - Your original prompt
  - Section type (verse, chorus, bridge)
  - Previous lyrics for context
  - Specified rhyme scheme
- Maintains consistency across the song

### 3. Orchestration (`agent.py`)
- Coordinates the planning and generation process
- Manages chorus reuse for proper song structure
- Cleans and formats the final output
- Returns both the plan and complete lyrics

## Common Song Structures

Lambytune supports various song structures:

- **VCVC**: Verse-Chorus-Verse-Chorus (simple, catchy)
- **VCVCBC**: Verse-Chorus-Verse-Chorus-Bridge-Chorus (most common)
- **AABA**: Verse-Verse-Bridge-Verse (classic structure)

## Configuration

### Adjusting Creativity
Edit the temperature settings in the files:
- `planner.py`: `temperature=0.7` (planning consistency)
- `generator.py`: `temperature=0.85` (creative lyrics)

### Changing Output Length
Modify `max_tokens=250` in `generator.py` for longer/shorter sections.

## Dependencies

- **openai**: OpenAI API client
- **langchain**: Framework for LLM applications  
- **langchain-openai**: OpenAI integration for LangChain
- **python-dotenv**: Environment variable management

## Requirements

- Python 3.8+
- OpenAI API key with sufficient credits
- Internet connection for API calls

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure all dependencies are installed
   pip install -r requirements.txt
   ```

2. **API Key Issues**
   ```bash
   # Verify your .env file contains:
   OPENAI_API_KEY=sk-...your-key-here
   ```

3. **Rate Limiting**
   - The app makes multiple API calls per song
   - Consider adding delays if you hit rate limits

### Error Handling

The application includes error handling for:
- Invalid JSON responses from the AI
- Missing environment variables
- API connection issues

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use and modify as needed.

## Future Enhancements

- [ ] Support for different music genres with genre-specific prompting
- [ ] Melody suggestions and chord progressions
- [ ] Export to common formats (PDF, TXT, etc.)
- [ ] Web interface for easier interaction
- [ ] Batch processing for multiple songs
- [ ] Integration with music production tools

---

**Note**: This tool generates lyrics only. For complete songs, you'll need to add melody and musical arrangement separately.