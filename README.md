# UI Elements Automation with Selenium

This project focuses on practicing UI automation by interacting with different types of web elements using **Selenium, Python, and PyCharm**.

The application provides stable `id` and `data-testid` attributes, allowing me to practice reliable element identification and automation.

## Automated UI Elements

- Text field and input validation
- Button click counter
- Checkboxes
- Radio buttons
- Dropdown menus
- Table sorting
- And other UI components

## Patterns and Best Practices

- **Page Object Model (POM)** for maintainable and reusable test code
- Project structure separated into:
  - `locators.py`
  - `pages.py`
  - `test_ui.py`
- `WebDriverWait` with `expected_conditions` instead of fixed waits
- Proper use of Selenium's `Select` class for native `<select>` elements
- Inspecting the actual DOM to create reliable locators
- Parameterized methods such as `select_dropdown_country(country)` instead of hardcoding values

## Challenge Resolved

During automation, I encountered an `ElementClickInterceptedException` when trying to click the **"Click Me"** button.

After inspecting the page, I identified that a **Google DoubleClick advertisement was overlapping the button near the bottom of the viewport**.

**Solution:** I used `scrollIntoView()` to reposition the element and performed a normal Selenium click, with a JavaScript click as a fallback when necessary.

## Technologies

`Python` · `Selenium` · `Pytest` · `PyCharm` · `Git` · `GitHub`
