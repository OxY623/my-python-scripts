# 🐍 Python Scripts Collection
## Ubuntu setup guide
1. Install Python (system deps)
`sudo apt install python3-full`

2. Create virtual environment
`python3 -m venv venv`

3. Activate virtual environment
`source venv/bin/activate`

4. Upgrade pip & install dependencies
`python -m pip install --upgrade pip`
`pip install -r requirements.txt`

5. Verify environment
`which python`
`pip -V`


Expected result: paths must point to ./venv/

6. Deactivate environment
`deactivate`

7. Run scripts with sudo (for network tools like Scapy)
`sudo venv/bin/python [your_folder]/[your_script].py`



8. Freeze packages
`pip freeze > requirements.txt`
