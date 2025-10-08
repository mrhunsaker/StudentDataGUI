<file_path>
StudentDataGUI/StudentDataGUI/test/test_homepage.py
</file_path>

<edit_description>
Write tests for homepage module.
</edit_description>
```

```python
import pytest
from nicegui import ui
from StudentDataGUI.appPages.homepage import content

@pytest.fixture
def setup_ui():
    """
    Fixture to set up the NiceGUI app for testing.
    """
    ui.run(headless=True)
    yield
    ui.stop()

def test_homepage_render(setup_ui):
    """
    Test if the homepage renders correctly.
    """
    content()
    page = ui.page("/")
    assert page is not None, "Homepage did not render."

def test_homepage_tabs(setup_ui):
    """
    Test if the tabs on the homepage are correctly defined.
    """
    content()
    tabs = ui.get_tabs()
    expected_tabs = ["DATA INPUT", "DATA SUMMARY"]
    for tab in expected_tabs:
        assert tab in tabs, f"Tab {tab} is missing from the homepage."
