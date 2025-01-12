## 🚀 Features

- **TOML file loading**: Allows you to open any TOML file from the file system.
- **Parameter editing**: Users can modify the configuration values of any TOML file.
- **Graphical interface**: A clean and easy-to-use interface with support for dynamic sections and adjustable fields.
- **Save changes**: Automatically saves the changes made to the TOML file.
- **No Python installation required**: It can be exported as a `.exe` executable file, so users can run it without needing to install Python or additional libraries.

## 💻 Requirements

- **Python 3.x**: Make sure you have Python 3.x installed.
- **Required libraries**:
  - `tkinter`
  - `toml`
  - `pyinstaller`

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ModifierTomlPro.git
   cd ModifierTomlPro

2. **Install dependencies**: Make sure Python 3.x is installed, then install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt

3. **Run the script**: To test the application, simply run the Python file:
   ```bash
   python config_toml.py
   ```
## 📦 Create an executable .exe file


- If you want to distribute your application as an executable file without requiring users to have Python installed, you can convert the Python script into a .exe file using PyInstaller.

1. **Install PyInstaller**: If you don't have PyInstaller installed, you can do so by running the following command:
   ```bash
   pip install pyinstaller

2. **Create the .exe file**: Run the following command from the terminal in the directory where your Python file (config_toml.py) is located:
   ```bash
   pyinstaller --onefile --windowed config_toml.py
   ```
- --onefile: This option creates a single .exe file instead of a folder with additional files.
- --windowed: Prevents the console window from showing when the .exe is run, ideal for graphical applications.
  
1. **Generated files**: After running PyInstaller, you'll find a dist folder in the project directory. Inside this folder, the generated .exe file will be located.
2. **Distribute the .exe file**: You can distribute the .exe file to users, who will be able to run it without needing to install Python.

## Customize the .exe file name:
- If you want to change the name of the .exe file, you can use the -n option to specify the name. For example:
  ```bash
   pyinstaller --onefile --windowed -n ModifierTomlPro config_toml.py
   ```
- This will generate an executable file named ModifierTomlPro.exe.

## 🤝 Contributing

- If you'd like to contribute to the project, follow these steps:
  
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3.Make your changes and commit:
   ```bash
   git commit -am 'Add new feature'
   ```
4.Submit a pull request describing the changes.


## 📄 License

- This project is licensed under the MIT License. For more details, check the LICENSE file.


  
   


   

  
