from rich.console import Console
from rich.panel import Panel

console = Console()

# Role-based Ai Chatbot CLI

# Chatbot guard
forbiden_words = [
    "bomb","kill","attack","murder",
    "nuclear","weapon","terrorist","death","suicide",
    "assassination","crime", "fuck you"
]

# List of predefined keyword response pairs
conversation_rules = [
    ("hello", "Hi there! How can I help you today?"),
    ("how are you", "I'm a bot, so I don't have feelings, but I'm functioning perfectly!"),
    ("what is your name", "I am a rule-based AI assistant."),
    ("bye", "Goodbye! Have a great day!"),
    ("what is the weather like today", "I'm not sure about the weather today. You can check a weather app for the latest forecast."),
    ("tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
    ("what can you do", "I can answer basic questions, tell you jokes, and have simple conversations."),
    ("who created you", "I was created by a developer as a rule-based AI assistant."),
    ("how old are you", "I don't have an age. I'm a computer program."),
    ("what is the capital of France", "The capital of France is Paris."),
]

# chatbot response
def chatbot_response(user_input):
    # Sanitizing user input
    cleaned_input = user_input.lower().strip()
    for word in forbiden_words:
        if word in cleaned_input:
            return "Sorry, but I can't help you with that."
    for keyword, response in conversation_rules:
        if keyword in cleaned_input:
            return response
    return "I don't understand that. Can you rephrase?"


# Main Loop
def main():
    welcome_panel = Panel(
        "[bold magenta]Welcome to the Rule-based AI Chatbot! Type 'quit' to exit.[/bold magenta]",
        title="🤖 AI Chatbot",
        border_style="cyan"
    )
    console.print(welcome_panel)
    
    try:
        while True:
            user_input = console.input('[bold blue]You : [/bold blue]')
            if user_input.lower() == 'quit':
                console.print(Panel("[bold magenta]Goodbye![/bold magenta]", border_style="magenta"))
                break
            
            response = chatbot_response(user_input)
            
            if response == "Sorry, but I can't help you with that.":
                response_panel = Panel(
                    f"[red]{response}[/]",
                    title="[bold red]Chatbot[/]",
                    title_align="left",
                    border_style="red"
                )
            else:
                response_panel = Panel(
                    f"[green]{response}[/]",
                    title="[bold green]Chatbot[/]",
                    title_align="left",
                    border_style="green"
                )
                
            console.print(response_panel)
    except KeyboardInterrupt:
        console.print()
        console.print(Panel("[bold magenta]Goodbye![/bold magenta]", border_style="magenta"))

if __name__ == "__main__":
    main()