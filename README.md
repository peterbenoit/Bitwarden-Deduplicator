# Bitwarden Deduplicator

A Python-based tool to identify and remove duplicate entries from Bitwarden export files. This project simplifies the management of your Bitwarden vault by allowing you to filter, deduplicate, and save results in a structured format.

## Features

-   **Filter by Entry Type**:
    -   Login
    -   Secure Note
    -   Card
    -   Identity
-   **Identify and Save Duplicates**: Separate duplicates for manual review.
-   **Save Unique Entries**: Clean your vault by keeping only unique items.
-   **Interactive and CLI Mode**:
    -   Configure the script interactively via the provided shell script.
    -   Use command-line arguments for direct execution.

## Requirements

-   Python 3.7 or higher
-   **Virtual Environment (Recommended):** This prevents conflicts between dependencies of different projects and ensures a clean and consistent development environment.

### Setting Up a Virtual Environment

1. **Create a Virtual Environment**:
   Run this command in the project directory:

    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment**:

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```cmd
        venv\Scripts\activate
        ```

3. **Install Project Dependencies**:
   After activating the virtual environment, install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. **Deactivate the Virtual Environment**:
   When you're done working on the project, deactivate the environment:
    ```bash
    deactivate
    ```

By using a virtual environment, you can ensure your project dependencies are isolated and easy to manage.

## How It Works

1. Export your Bitwarden vault into JSON format from the web or desktop application.
2. Clone the repository:
    ```bash
    git clone https://github.com/peterbenoit/Bitwarden-Deduplicator
    cd Bitwarden-Deduplicator
    ```
3. Run the provided shell script to process your export:
    ```bash
    ./run_python.sh
    ```
4. Review the output files:
    - **`bitwarden_cleaned.json`**: Contains unique entries.
    - **`bitwarden_duplicates.json`**: Contains duplicates for review.
5. Import the cleaned file back into Bitwarden after reviewing and validating its content.

## Disclaimer and Warnings

-   **Review and Validate Output**:

    -   The tool does not auto-update your Bitwarden vault. You must manually review the generated files (`bitwarden_cleaned.json` and `bitwarden_duplicates.json`) before importing anything back into your vault.

-   **Sensitive Data**:

    -   The tool processes sensitive information (passwords, card details, etc.). Ensure you run it in a secure environment and delete the processed files after use if they’re no longer needed.

-   **Back Up Your Vault**:

    -   Always back up your Bitwarden vault before making any changes. Mistakes during import or manual edits can lead to data loss.

-   **No Liability**:
    -   Use the tool **at your own risk**. We are not responsible for any data loss or issues arising from the use of this tool.

## Setup

1. **Clone the Repository**

    ```bash
    git clone <your-repo-url>
    cd Bitwarden-Deduplicator
    ```

2. **Run the Setup Script**
   Use the provided `run_python.sh` script to set up and execute the project:

    ```bash
    ./run_python.sh
    ```

    This script will:

    - Create a virtual environment (if not already present).
    - Install required dependencies from `requirements.txt`.
    - Run the Python deduplication script interactively.

3. **Install Dependencies Manually (Optional)**
   If you prefer, you can install dependencies directly:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Output

-   **`bitwarden_cleaned.json`**: Contains unique items.
-   **`bitwarden_duplicates.json`**: Contains duplicates for review.

## Project Structure

```
Bitwarden-Deduplicator/
├── deduplicate.py       # Python script for processing
├── run_python.sh        # Shell script for managing the virtual environment and running the Python script
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
