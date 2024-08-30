import os
import json

CITATION_DIR = os.path.expanduser("~/.citations/")

os.makedirs(CITATION_DIR, exist_ok=True)

def prompt_citation_type():
    print("Choose the type of source to cite:")
    print("1. Book")
    print("2. Journal Article")
    print("3. Website")
    choice = input("Enter the number: ")
    return choice

def gather_citation_details(choice):
    if choice == "1":
        return gather_book_details()
    elif choice == "2":
        return gather_journal_details()
    elif choice == "3":
        return gather_website_details()
    else:
        print("Invalid choice!")
        return None

def gather_book_details():
    author = input("Author(s): ")
    title = input("Title: ")
    year = input("Year: ")
    publisher = input("Publisher: ")
    return {
        "type": "book",
        "citation": f"{author} ({year}) *{title}*. {publisher}.",
        "inline": f"({author}, {year})"
    }

def gather_journal_details():
    author = input("Author(s): ")
    title = input("Title of Article: ")
    journal = input("Journal Name: ")
    year = input("Year: ")
    volume = input("Volume: ")
    issue = input("Issue: ")
    pages = input("Pages: ")
    return {
        "type": "journal",
        "citation": f"{author} ({year}) '{title}', *{journal}*, vol. {volume}, no. {issue}, pp. {pages}.",
        "inline": f"({author}, {year})"
    }

def gather_website_details():
    author = input("Author(s): ")
    title = input("Title: ")
    url = input("URL: ")
    access_date = input("Date Accessed: ")
    return {
        "type": "website",
        "citation": f"{author} ({access_date}) *{title}*, available at: {url} (Accessed: {access_date}).",
        "inline": f"({author}, {access_date})"
    }

def save_citation(project_name, citation):
    project_file = os.path.join(CITATION_DIR, f"{project_name}.json")
    citations = load_citations(project_name)
    citations.append(citation)
    with open(project_file, "w") as file:
        json.dump(citations, file, indent=4)
    print(f"Citation saved to project '{project_name}'.")

def load_citations(project_name):
    project_file = os.path.join(CITATION_DIR, f"{project_name}.json")
    if os.path.exists(project_file):
        with open(project_file, "r") as file:
            return json.load(file)
    return []

def view_citations(project_name):
    citations = load_citations(project_name)
    if not citations:
        print("No citations found for this project.")
        return
    print(f"\nCitations for project '{project_name}':\n")
    for i, citation in enumerate(citations, 1):
        print(f"{i}. {citation['citation']}")
    print()

def export_citations(project_name, export_format="txt"):
    citations = load_citations(project_name)
    if not citations:
        print("No citations to export.")
        return
    export_file = os.path.join(CITATION_DIR, f"{project_name}.{export_format}")
    with open(export_file, "w") as file:
        for citation in citations:
            file.write(f"{citation['citation']}\n")
    print(f"Citations exported to '{export_file}'.")

def main():
    print("Welcome to the Harvard Citation Generator CLI!")
    project_name = input("Enter the project name: ")
    while True:
        print("\nOptions:")
        print("1. Add a new citation")
        print("2. View saved citations")
        print("3. Export citations to a file")
        print("4. Exit")
        choice = input("Enter the number: ")

        if choice == "1":
            citation_type = prompt_citation_type()
            citation = gather_citation_details(citation_type)
            if citation:
                print(f"\nGenerated Citation:\n{citation['citation']}\n")
                save_citation(project_name, citation)
        elif choice == "2":
            view_citations(project_name)
        elif choice == "3":
            export_format = input("Enter export format (txt, bib): ")
            export_citations(project_name, export_format)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
