from selenium import webdriver
browser = webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')

#WebDriver Methods for finding elements

# browser.find_element_by_class_name(name) - CSS class
# browser.find_elements_by_class_name(name)

# browser.find_element_by_css_selector(selector) - CSS selector
# browser.find_elements_by_css_selector(selector)

# browser.find_element_by_id(id) - matching id attribute value
# browser.find_elements_by_id(id)

# browser.find_element_by_link_text(text) - COMPLETE MATCH
# browser.find_elements_by_link_text(text)

# browser.find_element_by_partial_link_text(text) - partial match
# browser.find_elements_by_partial_link_text(text)

# browser.find_element_by_name(name) - "name" attribute value
# browser.find_elements_by_name(name)

# browser.find_element_by_tag_name(name) - matching tag name, case insensitive
# browser.find_elements_by_tag_name(name)

# NoSuchElement exception if not found - try/except


# WebElement attributes or methods

# tag_name - The tag name, such as 'a' for an <a> element

# get_attribute(name) - The value for the element’s name attribute

# text - The text within the element, such as 'hello' in <span>hello </span>

# clear() - For text field or text area elements, clears the text typed into it

# is_displayed() - Returns True if the element is visible; otherwise returns False

# is_enabled() - For input elements, returns True if the element is enabled; otherwise returns False

# is_selected() - For checkbox or radio button elements, returns True if the element is selected; otherwise returns False

# location - A dictionary with keys 'x' and 'y' for the position of the element in the page