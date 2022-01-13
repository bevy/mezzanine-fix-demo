import pytest

@pytest.mark.django_db
def test_page_create():
    from mezzanine.pages.models import RichTextPage
    RichTextPage.objects.create(title="Emoji page 😀", content="foo")
