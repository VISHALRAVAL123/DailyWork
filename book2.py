import os

def generate_note():
    note_title = input("Enter note title: ")
    note_content = input("Enter note content: ")

    filename = f"{note_title}.txt"
    with open(filename, 'w') as file:
        file.write(note_content)
    
    print("Note generated successfully!")

def view_notes():
    notes = []
    for file in os.listdir():
        if file.endswith('.txt'):
            with open(file, 'r') as note_file:
                title = os.path.splitext(file)[0]
                content = note_file.read()
                notes.append({'title': title, 'content': content})
    
    if len(notes) > 0:
        print("Existing Notes:")
        for idx, note in enumerate(notes):
            print(f"\nNote {idx+1}:")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
    else:
        print("No notes found.")

while True:
    print("\nPython E-Note Book")
    print("1. Generate Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        generate_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please try again.")
