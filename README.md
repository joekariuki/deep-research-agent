# Deep Research Agent

An intelligent research automation system that uses AI agents to perform comprehensive web research, synthesize findings into detailed reports, and deliver them via email. Built with OpenAI Agents, Gradio, and SendGrid.

## Overview

Deep Research Agent is a multi-agent system that automates the entire research workflow:

1. **Planning**: An AI planner agent analyzes your query and creates a strategic search plan
2. **Searching**: Multiple web searches are performed in parallel based on the plan
3. **Synthesis**: A writer agent compiles all findings into a comprehensive markdown report
4. **Delivery**: The final report is automatically sent via email

The system features a user-friendly Gradio web interface for easy interaction and provides real-time progress updates throughout the research process.

## How It Works

The system consists of four specialized AI agents working together:

### 1. Planner Agent

- Analyzes your research query
- Generates a strategic plan with multiple search terms (default: 5 searches)
- Provides reasoning for each search query
- Uses GPT-5-mini model for efficient planning

### 2. Search Agent

- Performs web searches using OpenAI's WebSearchTool
- Summarizes search results into concise 2-3 paragraph summaries
- Executes searches in parallel for faster results
- Uses GPT-5-mini model with required tool usage

### 3. Writer Agent

- Synthesizes all search results into a cohesive report
- Creates detailed markdown reports (5-10 pages, 1000+ words)
- Generates a short summary and follow-up questions
- Uses GPT-5-mini model for report generation

### 4. Email Agent

- Formats the report into clean HTML
- Sends the report via SendGrid email service
- Creates appropriate subject lines

## Features

- **Multi-Agent Architecture**: Specialized agents for each stage of research
- **Parallel Web Searching**: Multiple searches executed simultaneously
- **Comprehensive Reports**: Detailed markdown reports with summaries and follow-up questions
- **Email Delivery**: Automatic email delivery via SendGrid
- **Web Interface**: User-friendly Gradio UI with real-time updates
- **Traceability**: OpenAI trace links for debugging and monitoring

<!-- ## Demo

See the Deep Research Agent in action:

![Demo GIF showing the Deep Research Agent workflow](demo.gif)

The demo shows:

- Entering a research query in the Gradio interface
- Real-time progress updates as searches are planned and executed
- The final comprehensive report being generated and displayed
- Email delivery confirmation -->

## Prerequisites

- Python 3.12 or higher
- OpenAI API key
- SendGrid API key (for email functionality)
- Environment variables configured (see Installation)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd deep-research-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Using `uv` (recommended):

```bash
uv pip install -r requirements.txt
```

Or using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
SENDGRID_API_KEY=your_sendgrid_api_key_here
EMAIL_FROM=your_sender_email@example.com
EMAIL_TO=your_recipient_email@example.com
```

**Note**: Make sure to add `.env` to your `.gitignore` file to keep your API keys secure.

### 5. Get API Keys

- **OpenAI API Key**: Sign up at [OpenAI Platform](https://platform.openai.com/) and create an API key
- **SendGrid API Key**: Sign up at [SendGrid](https://sendgrid.com/) and create an API key in Settings > API Keys

## Usage

### Running the Web Interface

Start the Gradio web interface:

```bash
python deep_research.py
```

The interface will open in your browser at `http://127.0.0.1:7860`. Enter your research query in the text box and click "Run" or press Enter.

### Using Programmatically

You can also use the `ResearchManager` class directly in your Python code:

```python
import asyncio
from research_agents.research_manager import ResearchManager

async def main():
    manager = ResearchManager()
    query = "What are the latest developments in quantum computing?"

    async for update in manager.run(query):
        print(update)

asyncio.run(main())
```

## Project Structure

```
deep-research-agent/
├── deep_research.py          # Main entry point with Gradio UI
├── research_agents/
│   ├── __init__.py
│   ├── research_manager.py   # Orchestrates the research workflow
│   ├── planner_agent.py      # Plans search queries
│   ├── search_agent.py        # Performs web searches
│   ├── writer_agent.py        # Generates reports
│   └── email_agent.py         # Sends email reports
├── pyproject.toml            # Project configuration
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## Configuration

### Adjusting Number of Searches

Edit `research_agents/planner_agent.py` to change the `HOW_MANY_SEARCHES` constant:

```python
HOW_MANY_SEARCHES = 5  # Change this value
```

### Changing AI Models

All agents currently use `gpt-5-mini`. To use different models, update the `model` parameter in each agent file:

```python
planner_agent = Agent(
    name="Planner Agent",
    instructions=instructions,
    model=("gpt-4o"),  # Change model here
    output_type=WebSearchPlan,
)
```

## Troubleshooting

### Email Not Sending

- Verify your SendGrid API key is correct
- Check that `EMAIL_FROM` and `EMAIL_TO` are valid email addresses
- Ensure your SendGrid account is verified
- Check SendGrid dashboard for any delivery issues

### Search Failures

- Verify your OpenAI API key is valid and has sufficient credits
- Check your internet connection
- Review the trace link provided in the console output for detailed error information

### Import Errors

- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using Python 3.12 or higher
- Check that you're in the correct virtual environment

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
