import tkinter as tk
from PIL import ImageTk, Image
import random
import urllib.request

def load_star_wars_quotes(urls):
    all_quotes = []
    for url in urls:
        response = urllib.request.urlopen(url)
        lines = response.read().decode('utf-8').splitlines()
        for line in lines:
            if line.strip() and not line.strip().isnumeric():
                parts = line.split('\t', 1)
                if len(parts) > 1:
                    quote = parts[1].strip()  # Extract the quote after the tab character
                    all_quotes.append(quote)
    return all_quotes

# URLs of the dialogue files
urls = [
    'https://raw.githubusercontent.com/gastonstat/StarWars/master/Text_files/EpisodeIV_dialogues.txt',
    'https://raw.githubusercontent.com/gastonstat/StarWars/master/Text_files/EpisodeV_dialogues.txt',
    'https://raw.githubusercontent.com/gastonstat/StarWars/master/Text_files/EpisodeVI_dialogues.txt'
]

# Load Star Wars quotes
star_wars_quotes = load_star_wars_quotes(urls)

# Create the GUI window
window = tk.Tk()
window.title("Star Wars Quote Chat")
window.configure(bg="black")

# Set the background image
bg_image = ImageTk.PhotoImage(Image.open("hyperspace.jpg"))
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create the chat window
chat_window = tk.Text(window, bg="black", fg="white", font=("Courier", 12), width=60, height=20, wrap=tk.WORD)
chat_window.pack(padx=20, pady=20)
chat_window.configure(state="disabled")  # Disable the chat window

# Create a scroll bar for the chat window
scrollbar = tk.Scrollbar(window, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window.config(yscrollcommand=scrollbar.set)

# Define colors for the chat window
chat_window.tag_config("holocron", foreground="green")

# Handle user input
def handle_user_input(event=None):
    user_input = user_input_text.get("1.0", tk.END).strip()
    chat_window.configure(state="normal")  # Enable the chat window
    chat_window.insert(tk.END, f"You: {user_input}\n")
    chat_window.configure(state="disabled")  # Disable the chat window
    
    if user_input.lower() == "hello there":
        delay = random.uniform(0.5, 3)  # Random delay between 0.5 and 3 seconds
        window.after(int(delay * 1000), respond_with_general_kenobi)
    elif user_input.lower() == "exit":
        window.quit()
    else:
        delay = random.uniform(0.5, 3)  # Random delay between 0.5 and 3 seconds
        window.after(int(delay * 1000), respond_with_star_wars_quote)
    
    chat_window.see(tk.END)  # Scroll to the end of the chat window
    user_input_text.delete("1.0", tk.END)
    return 'break'  # Prevent default behavior of the Enter key

# Function to respond with "General Kenobi"
def respond_with_general_kenobi():
    chat_window.configure(state="normal")  # Enable the chat window
    chat_window.insert(tk.END, "Holocron: ", "holocron")  # Green text for the holocron system name
    chat_window.insert(tk.END, "General Kenobi\n")
    chat_window.configure(state="disabled")  # Disable the chat window
    chat_window.see(tk.END)  # Scroll to the end of the chat window

# Function to respond with a random Star Wars quote
def respond_with_star_wars_quote():
    chat_window.configure(state="normal")  # Enable the chat window
    chat_window.insert(tk.END, "Holocron: ", "holocron")  # Green text for the holocron system name
    chat_window.insert(tk.END, f"{get_random_star_wars_quote()}\n")
    chat_window.configure(state="disabled")  # Disable the chat window
    chat_window.see(tk.END)  # Scroll to the end of the chat window

# Create the user input text area
user_input_text = tk.Text(window, font=("Courier", 12), width=60, height=3)
user_input_text.pack(pady=10)
user_input_text.bind("<Return>", handle_user_input)

# Create a submit button for user input
submit_button = tk.Button(window, text="Submit", command=handle_user_input)
submit_button.pack(pady=5)

# Function to get a random Star Wars quote
def get_random_star_wars_quote():
    return random.choice(star_wars_quotes)

# Main program loop
window.mainloop()
