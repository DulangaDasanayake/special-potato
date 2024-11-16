import socket
import threading
from tkinter import Tk, Text, Entry, Button, Label, filedialog
from PIL import Image, ImageTk  # Import Pillow for better image support

# Client setup
HOST = '127.0.0.1'
PORT = 5000

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        
        # GUI setup
        self.root = Tk()
        self.root.title("Chat App")
        self.root.geometry("400x600")
        
        # Background image
        self.background_label = Label(self.root)
        self.set_background_image("assets/background.png")  # Ensure correct path
        self.background_label.place(relwidth=1, relheight=1)  # Place background image
        
        # Chat display (set the background color to None for transparency effect)
        self.chat_display = Text(self.root, bg=None, fg="black", wrap="word", state="disabled", font=("Arial", 12))
        self.chat_display.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)
        
        # Remove the border for a clean look
        self.chat_display.config(borderwidth=0, highlightthickness=0)

        # Message entry
        self.msg_entry = Entry(self.root, font=("Arial", 12))
        self.msg_entry.place(relx=0.05, rely=0.8, relwidth=0.6, height=30)
        
        # Send button
        self.send_button = Button(self.root, text="Send", command=self.send_message, font=("Arial", 12), bg="blue", fg="white")
        self.send_button.place(relx=0.7, rely=0.8, relwidth=0.25, height=30 )
        
        # Change background button
        self.bg_button = Button(self.root, text="Change Background", command=self.change_background, font=("Arial", 10))
        self.bg_button.place(relx=0.35, rely=0.9, relwidth=0.3, height=30)
        
        # Start threads for receiving messages
        threading.Thread(target=self.receive_messages, daemon=True).start()
        
        self.root.mainloop()

    def set_background_image(self, image_path):
        try:
            # Load the image using Pillow (supports more formats)
            image = Image.open(image_path)
            bg_image = ImageTk.PhotoImage(image)
            self.background_label.config(image=bg_image)
            self.background_label.image = bg_image  # Keep reference to prevent garbage collection
            print("Background image loaded successfully.")
        except Exception as e:
            print(f"Error loading background image: {e}")

    def change_background(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.set_background_image(file_path)

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            self.client.send(msg.encode())
            self.msg_entry.delete(0, "end")

    def receive_messages(self):
        while True:
            try:
                msg = self.client.recv(1024).decode()
                if msg:
                    self.chat_display.config(state="normal")
                    self.chat_display.insert("end", f"{msg}\n")
                    self.chat_display.config(state="disabled")
                    self.chat_display.see("end")
            except:
                break


# Run the client
ChatClient()
