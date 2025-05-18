import re
import sys
from collections import defaultdict


def extract_data(text):
    # Dictionary to store all extracted data by type
    extracted_data = defaultdict(list)

    # Email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    extracted_data['Email Addresses'] = emails

    # URLs
    url_pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    urls = re.findall(url_pattern, text)
    extracted_data['URLs'] = urls

    # Credit card numbers
    cc_pattern = r'(?:\d{4}[-\s]?){4}|\d{16}'
    cc_numbers = re.findall(cc_pattern, text)
    # format credit card numbers
    cleaned_cc = []
    for cc in cc_numbers:
        cc_clean = re.sub(r'[-\s]', '', cc)
        # validate if the number is 16 digits
        if len(cc_clean) == 16:
            cleaned_cc.append(cc)
    extracted_data['Credit Card Numbers'] = cleaned_cc

    # Time (12-hour and 24-hour formats)
    time_pattern = r'\b(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])\b'
    times = re.findall(time_pattern, text)
    extracted_data['Time Formats'] = times

    # HTML tags
    html_pattern = r'<[^>]+>'
    html_tags = re.findall(html_pattern, text)
    extracted_data['HTML Tags'] = html_tags

    # Hashtags
    hashtag_pattern = r'#[A-Za-z0-9_]+'
    hashtags = re.findall(hashtag_pattern, text)
    extracted_data['Hashtags'] = hashtags

    # Currency amounts
    currency_pattern = r'[$€£¥][\d,.]+|\b\d+(?:\.\d{1,2})?\s?(?:USD|EUR|GBP|JPY|RWF|dollars|euros|pounds)\b'
    currencies = re.findall(currency_pattern, text)
    extracted_data['Currency Amounts'] = currencies

    return extracted_data


def display_results(extracted_data):
    print("\n=== EXTRACTION RESULTS ===\n")

    total_items = 0
    for category, items in extracted_data.items():
        if items:
            print(f"{category} ({len(items)}):")
            for item in items:
                print(f"  - {item}")
            print()
            total_items += len(items)

    print(f"Total items extracted: {total_items}")


def main():
    # Test with a sample text
    sample_text = """
    Here's some sample data:
    Email me at john.doe@example.com or contact support@company.co.uk
    Check out our website at https://www.example.com or our documentation at https://docs.example.org/api
    Payment received on credit card 1234 5678 9012 3456
    Another payment on 4111-1111-1111-1111
    Meeting scheduled for 14:30 or 2:30 PM tomorrow

    <div class="content">This is some HTML content with <strong>bold text</strong></div>

    Popular hashtags: #Python #RegEx #DataExtraction

    Total amount charged: $129.99 or 150.00 EUR or £100.00 or 1500000 RWF
    """

    results = extract_data(sample_text)
    display_results(results)


if __name__ == "__main__":
    main()