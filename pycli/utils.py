import re


def sanitize_filename(title: str, max_length: int = 50) -> str:
    """Convert a title to a clean filename"""
    # Remove any text after certain markers that indicate end of main title
    markers = ["|", "-", "—", "–", ":", "•"]
    for marker in markers:
        if marker in title:
            title = title.split(marker)[0]

    # Remove any non-alphanumeric characters (except spaces)
    clean = re.sub(r"[^\w\s-]", "", title)
    # Replace spaces with dashes
    clean = clean.strip().replace(" ", "-")
    # Convert to lowercase
    clean = clean.lower()
    # Remove any repeated dashes
    clean = re.sub(r"-+", "-", clean)
    # Truncate to max length while keeping whole words
    if len(clean) > max_length:
        clean = clean[:max_length].rsplit("-", 1)[0]
    return clean
