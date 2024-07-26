# Moeen AI - Your Virtual Instruction Execution Assistant

Welcome to the Moeen AI project! Moeen is an AI-powered virtual assistant that can intelligently interpret natural language instructions and autonomously execute them, streamlining your workflows and boosting productivity.

## Project Vision

The goal of Moeen AI is to provide a seamless way for users to translate written instructions into executable actions, all with a simple highlight and right-click. By leveraging advanced natural language processing (NLP) and browser automation, Moeen aims to be your go-to tool for automating repetitive tasks and navigating complex workflows.

## Key Features (MVP)

- **Instruction Parsing**: Highlight text instructions on any webpage and have Moeen analyze and understand the steps involved.
- **Intelligent Execution**: With a single click, Moeen will autonomously carry out the instructions, navigating websites, filling forms, and interacting with page elements as needed.  
- **Chrome Extension**: Moeen will be conveniently accessible right from your browser toolbar, ready to assist whenever you need it.
- **Workflow Automation**: From troubleshooting software issues to drafting emails, let Moeen handle the grunt work while you focus on the bigger picture.

## Tech Stack

- **Language**: Python - for its rich ecosystem of AI/ML and automation libraries
- **NLP**: spaCy - powerful, production-ready library for understanding and processing text
- **Browser Automation**: Puppeteer - flexible and user-friendly tool for controlling Chrome programmatically 
- **UI**: React - to build an intuitive and responsive frontend for the Chrome extension

## Getting Started

### Prerequisites

- Python 3.6+
- Node.js and npm
- Google Chrome browser

### Installation

1. Clone the repo:
   
git clone https://github.com/yourusername/moeen-ai.git
cd moeen-ai

2. Set up the Python environment:

python -m venv venv
source venv/bin/activate  # For Unix/macOS
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

3. Install the frontend dependencies:

cd extension
npm install

## Usage

1. Run the Moeen AI backend:

python main.py

2. Load the Chrome extension:
- Open Chrome and go to `chrome://extensions`
- Enable "Developer mode" 
- Click "Load unpacked" and select the `extension` directory

3. Navigate to any webpage, highlight the instructions you want Moeen to execute, right-click, and select "Execute with Moeen".

4. Sit back and let Moeen work its magic!

## Roadmap

- [ ] Refine NLP model to handle more complex instructions
- [ ] Expand automation capabilities beyond web-based tasks  
- [ ] Implement user accounts and cloud sync
- [ ] Integrate with popular productivity tools like Trello, Asana, etc.
- [ ] Launch on Chrome Web Store for easy installation

## Contributing

We welcome contributions from the community! If you'd like to get involved, please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, ideas, or just want to chat about the project, feel free to reach out:

- Email: careybrands@gmail.com
- X: [@devonjcarey](https://x.com/devonjcarey)
- Project Link: [https://github.com/CB-PORTAL/moeen-ai](https://github.com/CB-PORTAL/moeen-ai)

Let's revolutionize the way we interact with technology, one highlight at a time! 🚀
