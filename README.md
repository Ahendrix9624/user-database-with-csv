## Login Screen
<img width="507" alt="Screenshot 2023-03-11 at 11 45 06 AM" src="https://user-images.githubusercontent.com/33384698/224506166-0ddf11dd-8273-45e3-b6de-86726579691a.png">

## Once logged in
<img width="359" alt="Screenshot 2023-03-11 at 11 46 26 AM" src="https://user-images.githubusercontent.com/33384698/224506201-77e76022-c169-4762-ae1a-7765bdb36e82.png">

### Would love to build out much more functionality within this program feel free to make a pull request :)

# 1. Create virtual python env
```bash
python -m venv venv && source venv/bin/activate #Linux
python -m venv venv && \venv\Scripts\activate #Windows
```

### Creates virtual python environment 
```bash
python -m venv venv 
```

### Steps into virtual environment 
```bash
source .venv/bin/activate
```

### See the terminal now has the name of your virtual environment
```bash
(venv) drew@Andrews-MacBook-Pro% 
```

### To Step out of the virtual environment 
```bash
deactivate
```

# 2. Install dependencies (Inside of Virtual environment)
```bash
pip install -r requirements.txt
```

# 3 Run the Code
```bash
python main.py
```

# TROUBLESHOOTING
```bash
pip list
python --version 
pip --version 
```
```plain text
If trying to do this with VS CODE ensure you have your files open on the left side aka the workspace 

Command+shift+p select interpreter and chose .venv/bin python
```
