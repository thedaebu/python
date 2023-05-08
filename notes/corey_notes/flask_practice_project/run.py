# modules found in __init__.py file can be imported
from flask_practice_app import create_app

app = create_app()

# can be used when running file using python command
# automatically updates display when edits are made
if __name__ == '__main__':
    app.run(debug=True)    
