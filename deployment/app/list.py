import os
import json
from package.featuretoggles import TogglesList

class ReleaseToggle(TogglesList):
    renderHTML: bool

def get_files(folder_name):
    """Get all files in a folder recursively."""
    files = []
    for root, dirs, file_names in os.walk(folder_name):
        for file_name in file_names:
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                files.append(file_name)
    return files

def renderHTML(files):
    """Render HTML."""
    file_list_html = ""

    for folder in files:
        file_list_html += "<h2>{}</h2>".format(folder)
        file_list_html += "<ul>"
        for file in files[folder]:
            file_list_html += "<li><a href=\"{0}/{1}\">{1}</a></li>".format(folder, file)
        file_list_html += "</ul>"

    return """
    <html>
        <head>
            <title>Threat Hunting</title>
        </head>
        <body>
            <h1>Threat Hunting</h1>
            {}
        </body>
    </html>
    """.format(file_list_html)

def main(event, lambda_context):
    """Main function."""
    files = {}
    folders = ["threat/actor", "domain/study"]
    for folder in folders:
        for file in get_files(folder):
            if folder not in files:
                files[folder] = []
            files[folder].append(file)

    toggles = ReleaseToggle('toggle.yaml')

    return {
        'statusCode': 200,
        "headers": {
            'Content-Type': 'text/html' if toggles.renderHTML else 'application/json',
        },
        'body': renderHTML(files) if toggles.renderHTML else json.dumps({
            "data": files,
        }),
    }