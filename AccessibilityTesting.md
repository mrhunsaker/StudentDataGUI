# Accessibility Testing Checklist for StudentDataGUI

_Last updated: 2024-06_

This document provides a comprehensive checklist and step-by-step instructions for testing the accessibility of the StudentDataGUI application. It covers screen reader compatibility, keyboard navigation, high-contrast mode, and browser zoom/magnification. Guidance is also provided for documenting and addressing any issues found.

---

## 1. Screen Reader Testing (NVDA, JAWS, or VoiceOver)

**Preparation:**
- Install and launch a screen reader:
  - [NVDA (Windows, free)](https://www.nvaccess.org/download/)
  - [JAWS (Windows, commercial)](https://www.freedomscientific.com/Downloads/JAWS)
  - VoiceOver (built into macOS)
- Open the application in a supported browser.

**Steps:**
- Navigate through the app using Tab, Shift+Tab, and arrow keys.
- Ensure all page landmarks (header, navigation, main, footer) are announced.
- Activate the “Skip to main content” link and verify it is announced and works.
- For each form:
  - Move focus to each input field and verify the label is announced.
  - Submit the form with missing required fields. Confirm that error messages are announced and associated with the correct field.
  - Ensure that dialogs/modals are announced as dialogs and that focus is trapped within them.
- For all images and icons, verify that meaningful alternative text or labels are announced, and decorative images are skipped.
- Confirm that notifications (e.g., success/error toasts) are announced if they convey important information.

---

## 2. Keyboard-Only Navigation

**Preparation:**
- Disconnect or do not use a mouse.

**Steps:**
- Use Tab and Shift+Tab to move through all interactive elements (links, buttons, form fields, menus).
- Use Enter or Space to activate buttons, links, and menu items.
- Ensure that:
  - All interactive elements are reachable and usable.
  - Focus is always visible (look for the gold outline and background).
  - The “Skip to main content” link appears and works when tabbed to.
  - Dialogs/modals trap focus and return it to the trigger when closed.
  - Error messages are visible and focus moves to the first invalid field on form submission errors.

---

## 3. High-Contrast Mode and Browser Zoom/Magnification

**Preparation:**
- Enable high-contrast mode in your operating system or use a browser extension.
- Use browser zoom (Ctrl + Plus/Minus or Cmd + Plus/Minus) to increase magnification up to 200% or more.

**Steps:**
- Verify that all text, buttons, and form fields remain readable and do not overlap or disappear.
- Ensure that focus indicators remain visible in high-contrast mode.
- Check that color is not the only means of conveying information (e.g., error messages use both color and text).
- Confirm that all content and controls are accessible and usable at high zoom levels.

---

## 4. Documenting Issues

1. **Record the Issue:**
   - Note the page, component, and specific action that caused the problem.
   - Include details about the assistive technology, browser, and OS used.
   - Take screenshots or screen recordings if possible.

2. **Describe the Expected vs. Actual Behavior:**
   - What should have happened?
   - What actually happened?

3. **Severity and Impact:**
   - Is the issue blocking, major, minor, or cosmetic?
   - Does it prevent users with disabilities from completing a task?

4. **Reporting:**
   - Log the issue in your project’s issue tracker (e.g., GitHub Issues).
   - Assign or tag it as an accessibility issue.

---

## 5. Addressing Issues

- Prioritize issues that block access to core functionality or prevent users from completing tasks.
- Reference [WCAG 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/) criteria for guidance on fixes.
- Test fixes with the same assistive technology and scenarios where the issue was found.
- Mark issues as resolved only after verification by retesting.

---

## References

- [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [NVDA Screen Reader](https://www.nvaccess.org/)
- [JAWS Screen Reader](https://www.freedomscientific.com/Downloads/JAWS)
- [VoiceOver (Apple)](https://support.apple.com/en-us/HT204576)

---

For questions or to report accessibility issues, please open an issue on the [GitHub repository](https://github.com/mrhunsaker/StudentDataGUI/issues).