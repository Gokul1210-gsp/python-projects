# Year Calendar Generator

## Overview

The **Year Calendar Generator** is a beginner-friendly Python project that displays the calendar for all twelve months of a specified year. It uses Python's built-in `calendar` module to generate monthly calendars and presents each month inside a bordered frame for better readability.

---

## String Functions Used

### `splitlines()`

Splits a multiline string into a list of individual lines.

**Example**

```python
text = "Hello\nWorld"
print(text.splitlines())
```

**Output**

```text
['Hello', 'World']
```

---

### `ljust()`

Left-aligns a string and pads it with spaces until it reaches the specified width.

**Example**

```python
text = "Python"
print(text.ljust(10, "-"))
```

**Output**

```text
Python----
```

---

## Module Used

### `calendar`

The built-in `calendar` module provides functions for working with dates and calendars.

#### `calendar.month(year, month)`

Returns the calendar for a specified month as a formatted string.

**Example**

```python
import calendar

print(calendar.month(2026, 1))
```

---

## Learning Outcomes

After completing this project, you will understand how to:

* Import and use Python modules.
* Create reusable functions.
* Accept and process user input.
* Iterate using loops.
* Work with multiline strings.
* Format console output.
* Generate calendars using the `calendar` module.

---

## Technologies Used

* Python 3
* Python Standard Library (`calendar`)


