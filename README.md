CiteCLI is a simple command-line tool for generating Harvard-style citations directly from your terminal. It supports different citation types, inline citations, and allows you to save, view, and export citation lists by project.

## Features

- Generate Harvard-style citations for books, journal articles, and websites.
- Automatically create inline citations (e.g., `(Smith, 2023)`).
- Save citations by project name for easy management.
- View and export your citations in various formats (e.g., `.txt`).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OperatorRyu/CiteCLI.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd CiteCLI
   ```

3. **Run the script:**
   ```bash
   python3 CiteCLI.py
   ```

   Ensure you have Python 3 installed on your system.

## Usage

Once you've run the script, you'll be prompted to enter a project name. This project will store all your citations.

### Main Menu

1. **Add a new citation:** Select the source type (Book, Journal, Website) and input the required details. The citation will be formatted and saved under the project name.
   
2. **View saved citations:** Review all citations saved in the current project.
   
3. **Export citations to a file:** Export all citations in the project to a file in your chosen format (`.txt`, `.bib`, etc.).

4. **Exit:** Exit the application.

### Example

To create a new citation for a book:
```bash
Enter the project name: MyResearchProject

Options:
1. Add a new citation
2. View saved citations
3. Export citations to a file
4. Exit
Enter the number: 1

Choose the type of source to cite:
1. Book
2. Journal Article
3. Website
Enter the number: 1

Author(s): John Smith
Title: The World of Python
Year: 2023
Publisher: Tech Books Publishing

Generated Citation:
John Smith (2023) *The World of Python*. Tech Books Publishing.

Citation saved to project 'MyResearchProject'.
```

### Exporting Citations
To export your citations:
```bash
Enter the number: 3
Enter export format (txt, bib): txt

Citations exported to '/home/username/.citations/MyResearchProject.txt'.
```

## Contribution

Feel free to fork this project, submit pull requests, or open issues if you have suggestions or bugs to report.

## License

This project is licensed under the MIT License.
