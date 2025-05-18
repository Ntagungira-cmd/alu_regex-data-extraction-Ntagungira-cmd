# Regular Expression Data Extraction

This project uses regular expressions to extract various types of data from text, including email addresses, URLs, credit card numbers, time formats, HTML tags, hashtags, and currency amounts.

## Project Overview

In API responses, it's common to receive large amounts of unstructured text data. This utility helps to extract structured information from such text using the power of regular expressions. The implemented regex patterns can identify and extract:

1. **Email Addresses** - Standard email formats including those with subdomains
2. **URLs** - Web addresses with various protocols and domains
3. **Credit Card Numbers** - 16-digit numbers in various formats (spaces, dashes)
4. **Time Formats** - Both 12-hour and 24-hour time notations
5. **HTML Tags** - Various HTML elements in text
6. **Hashtags** - Social media style tags
7. **Currency Amounts** - Monetary values in different formats and currencies

## Setup Instructions

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Ntagungira-cmd/alu_regex-data-extraction-Ntagungira-cmd.git
cd alu_regex-data-extraction-Ntagungira-cmd
```

2. No additional dependencies are required as the script uses only the Python standard library.

## Usage

Run the script directly:

```bash
python Main.py
```

The script includes a sample text with various data types to extract. You can modify the `sample_text` variable in the `main()` function to test with your own data.

## Regex Patterns Explained

### Email Addresses
```python
r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
```
This pattern matches standard email formats including those with dots, underscores, and hyphens in the username part, and domains with various TLDs.

### URLs
```python
r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
```
Matches HTTP and HTTPS URLs, including subdomains and various path formats.

### Credit Card Numbers
```python
r'(?:\d{4}[-\s]?){4}|\d{16}'
```
Matches 16-digit numbers with or without spaces/dashes between groups of 4 digits.

### Time Formats
```python
r'\b(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])\b'
```
Matches both 12-hour time format (with AM/PM) and 24-hour time format.

### HTML Tags
```python
r'<[^>]+>'
```
Matches HTML tags with any attributes.

### Hashtags
```python
r'#[A-Za-z0-9_]+'
```
Matches hashtags consisting of alphanumeric characters and underscores.

### Currency Amounts
```python
r'[$€£¥][\d,.]+|\b\d+(?:\.\d{1,2})?\s?(?:USD|EUR|GBP|JPY|RWF|dollars|euros|pounds)\b'
```
Matches currency amounts with various symbols and abbreviations.

## Edge Cases Handled

- Email addresses with multiple dots and different TLDs
- URLs with subdirectories and query parameters
- Credit card numbers with or without separators
- Time in both AM/PM and 24-hour formats
- Various HTML tag formats
- Currency amounts with different symbols and formats

## Sample Output

When run with the included sample text, the program outputs:

```
=== EXTRACTION RESULTS ===

Email Addresses (2):
  - john.doe@example.com
  - support@company.co.uk

URLs (2):
  - https://www.example.com
  - https://docs.example.org/api

Credit Card Numbers (2):
  - 1234 5678 9012 3456
  - 4111-1111-1111-1111

Time Formats (2):
  - 14:30
  - 2:30 PM

HTML Tags (2):
  - <div class="content">
  - <strong>

Hashtags (3):
  - #Python
  - #RegEx
  - #DataExtraction

Currency Amounts (4):
  - $129.99
  - 150.00 EUR
  - £100.00
  - 1500000 RWF

Total items extracted: 17
```
