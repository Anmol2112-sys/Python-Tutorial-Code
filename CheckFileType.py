data = {
    'py': "Python file",
    'txt': "Text file",
    'csv': "Comma Separated Values file",
    'docx': "Microsoft Word file",
    'c': "C programming file",
    'cpp': "C++ programming file",
    'java': "Java programming file",
    'html': "HTML file",
    'css': "CSS file",
    'js': "JavaScript file",
    'dart': "Dart programming file",
}

name = input("Enter file name with extension: ")

file = name.split(".")

extension = file[1]

print(data.get(extension, "File type not found"))