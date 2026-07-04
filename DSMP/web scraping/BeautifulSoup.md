# Web Scraping with BeautifulSoup - Reference Guide

## 1. Setup & Parsing HTML
Before extracting data, you must parse the raw HTML into a BeautifulSoup object.

    import requests
    from bs4 import BeautifulSoup

    # Fetch the HTML
    html_content = requests.get('https://example.com').text

    # Parse the HTML (use 'html.parser' or the faster 'lxml')
    soup = BeautifulSoup(html_content, 'html.parser')

## 2. Finding Elements (Search Methods)
These are the core methods for locating specific HTML tags.

* **find(tag)**: Returns the **first** tag that matches.

    heading = soup.find('h1')

* **find_all(tag)**: Returns a **list** of all matching tags.

    paragraphs = soup.find_all('p')

    first_three_links = soup.find_all('a', limit=3)

* **Search by CSS Class (class_)**:
  Because class is a reserved keyword in Python, add an underscore.

    container = soup.find('div', class_='container')

    highlights = soup.find_all('p', class_='highlight')

* **Search by ID**:

    main_section = soup.find(id='main-content')

* **Search by Custom Attributes (attrs)**:

    submit_btn = soup.find('input', attrs={'type': 'submit'})

## 3. Extracting Data
Once an element is found, you extract its inner text or attributes.

* **Extracting Text**:

    element = soup.find('h1')
    print(element.text) 
    print(element.get_text(strip=True))

* **Extracting Attributes (href, src, data-*, etc.)**:

    link = soup.find('a') # <a href="https://google.com">Search</a>
    
    # Method 1: Dictionary style
    url = link['href']
    
    # Method 2: Safe get method (returns None if attribute doesn't exist)
    url = link.get('href')

## 4. CSS Selectors (Advanced Search)
For complex, nested selections, use standard CSS selector syntax.

* **select_one(selector)**: Returns the first match.

### Find first p tag inside a div with class "content"
    paragraph = soup.select_one('div.content > p')

* **select(selector)**: Returns a list of all matches.

### Find all a tags inside an element with id="footer"
    footer_links = soup.select('#footer a')
    
### Find elements with BOTH "btn" and "primary" classes
    buttons = soup.select('.btn.primary')

## 5. Navigating the HTML Tree
Move around the document relative to a specific element.

* **.parent**: Moves up one level to the parent container.
* **.children**: Iterates over the direct nested tags.
* **.next_sibling / .previous_sibling**: Moves sideways to the next/previous element at the exact same indentation level. (Note: This often catches empty text nodes/newlines, so use carefully).

---

## 6. Real-World Cheat Sheet Example
Given the following HTML block:

    <div class="product" id="prod-99">
        <h2 class="title">Wireless Mouse</h2>
        <span class="price" data-currency="USD">$25.00</span>
        <a href="/buy/99">Buy Now</a>
    </div>

**Extracting everything:**

    product_div = soup.find('div', class_='product')

    # Extract inner text
    title = product_div.find('h2', class_='title').text
    price = product_div.find('span', class_='price').get_text(strip=True)

    # Extract attributes
    currency = product_div.find('span', class_='price').get('data-currency')
    link = product_div.find('a').get('href')