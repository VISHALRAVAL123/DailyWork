# Importing required modules
import pickle

# Function to generate a new note
def generate_note():
    note_title = input("Enter note title: ")
    note_content = input("Enter note content: ")

    # Saving the note to a file using pickle
    with open('notes.pickle', 'ab') as file:
        pickle.dump({'title': note_title, 'content': note_content}, file)
    
    print("Note generated successfully!")

# Function to view all existing notes
def view_notes():
    try:
        # Loading the notes from the file using pickle
        with open('notes.pickle', 'rb') as file:
            notes = []
            while True:
                try:
                    note = pickle.load(file)
                    notes.append(note)
                except EOFError:
                    break

        # Displaying all notes
        if len(notes) > 0:
            print("Existing Notes:")
            for idx, note in enumerate(notes):
                print(f"\nNote {idx+1}:")
                print(f"Title: {note['title']}")
                print(f"Content: {note['content']}")
        else:
            print("No notes found.")
    
    except FileNotFoundError:
        print("No notes found.")

# Main program loop
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

