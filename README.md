# Simple Python Chat App with GUI

This is a simple, temporary chat app built using Python and Tkinter. It supports sending messages in real time between two users. Additionally, the app allows users to set a background image and change it dynamically.

---

## Features

- **Real-time Chat**: Communicate with another user in real time.
- **Customizable Background**: Users can set and change the background image.
- **Standalone Executable**: Package the app into an executable so others can run it without needing Python.

---

## Requirements

- Python 3.x installed on your machine.
- **PyInstaller** (for creating standalone executables).

---

## Folder Structure

```
chat_app/
│
├── server.py              # The server code (handles connections)
├── client.py              # The client code (with GUI)
├── assets/                # Folder to store background images
│   └── background.jpg     # Default background image
└── README.md              # This file with instructions
```

---

## How to Run the Project

### **Step 1: Install Python and PyInstaller**

1. **Install Python**:
   - Download and install Python 3 from [python.org](https://www.python.org/downloads/).

2. **Install PyInstaller**:
   - Open a terminal or command prompt and install PyInstaller using pip:
     ```bash
     pip install pyinstaller
     ```

---

### **Step 2: Run the Server**

1. **Navigate to the project folder**:
   - Open a terminal (or command prompt) and go to the folder where the `server.py` script is located:
     ```bash
     cd /path/to/chat_app
     ```

2. **Run the server script**:
   - Start the server using Python:
     ```bash
     python server.py
     ```

   The server will start and listen for connections at `127.0.0.1:5000`.

---

### **Step 3: Run the Client (For You and Your Girlfriend)**

1. **Navigate to the project folder**:
   - Open a new terminal and go to the folder where `client.py` is located:
     ```bash
     cd /path/to/chat_app
     ```

2. **Run the client script**:
   - Start the client using Python:
     ```bash
     python client.py
     ```

3. The client GUI will open, allowing you to chat in real-time. You and your girlfriend can both run this on separate machines if you're connected to the same network.

---

### **Step 4: Make the App Easy to Use (Optional)**

If you don’t want others to install Python, you can package the app into standalone executables using **PyInstaller**.

#### **Package the Client as an Executable**:

1. **Navigate to the folder containing `client.py`**:
   ```bash
   cd /path/to/chat_app
   ```

2. **Run PyInstaller** to package the client as an executable:
   ```bash
   pyinstaller --onefile --windowed client.py
   ```

   - `--onefile`: Bundles everything into a single executable.
   - `--windowed`: Ensures the terminal window does not pop up when running the GUI (only applies to GUI apps).

3. The executable will be placed in the `dist/` folder as `client.exe` (on Windows) or `client` (on Mac/Linux).

4. **Send the Executable**: Send the `client.exe` or `client` file to your girlfriend (or any other user). They can just double-click the file to start the chat app without installing Python.

#### **Optional: Package the Server as an Executable**:
You can also package the server script as an executable if you'd like to make it easier for you to run it.

1. **Package the server**:
   ```bash
   pyinstaller --onefile server.py
   ```

   The server executable will be located in the `dist/` folder as `server.exe` (on Windows) or `server` (on Mac/Linux).

---

## Customizing the Background

1. Place your background image in the `assets/` folder.
2. Run the client, and you will see the default background.
3. To change the background, click the "Change Background" button in the app, and select a new image from your file system.

---

## Contributing

Feel free to fork this project and make contributions! If you find any bugs or want to add more features, open a pull request.

---

## License

This project is open-source and available under the MIT License.

---