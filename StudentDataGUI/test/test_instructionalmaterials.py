<file_path>
StudentDataGUI/StudentDataGUI/test/test_instructionalmaterials.py
</file_path>

<edit_description>
Write tests for InstructionalMaterials module.
</edit_description>
```

```python
import pytest
from nicegui import ui
from StudentDataGUI.appPages.InstructionalMaterials import create

@pytest.fixture
def setup_ui():
    """Fixture to set up the NiceGUI app for testing."""
    ui.run(headless=True)
    yield
    ui.stop()

def test_instructional_materials_page_render(setup_ui):
    """
    Test if the Instructional Materials page renders correctly.
    """
    create()
    page = ui.page("/instructionalmaterials")
    assert page is not None, "Instructional Materials page did not render."

def test_instructional_materials_links(setup_ui):
    """
    Test if the links on the Instructional Materials page are correctly defined.
    """
    create()
    links = [
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/Abacus1.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/Abacus2.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/AbacusMadeEasy.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UsingCranmerAbacus.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/abacusUseTheory.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/AdvancedAbacus.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/NLSLOCLessons1-11.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UEBAustralianTrainingManual.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UEBTechnicalCourse.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UEBTechnicalGuidelines.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/NemethUEBContext.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/NVDATrainings.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/WindowsScreenreaderPrimer.zip",
        "https://github.com/mrhunsaker/Materials/blob/main/instructionMaterials/GettingStartedWindows11.doc",
        "https://github.com/mrhunsaker/Materials/raw/main/datasheets/BlankVisionTemplate.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/datasheets/GenericDataSheets.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/datasheets/ProgressMonitoring.pdf",
        "https://github.com/mrhunsaker/Materials/raw/main/visionAssessments/EducationVisionAssessments.pdf",
    ]
    for link in links:
        assert link in ui.get_links(), f"Link {link} is missing from the page."
