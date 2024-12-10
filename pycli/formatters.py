import json


def clean_markdown(content: str) -> str:
    """Remove navigation, cookie notices, and other clutter from markdown content"""
    lines = content.split("\n")
    cleaned_lines = []
    skip_section = False

    for line in lines:
        # Skip cookie consent and navigation sections
        if any(
            marker in line.lower()
            for marker in [
                "cookie",
                "consent",
                "privacy",
                "navigation",
                "this website uses",
                "necessary cookies",
                "marketing cookies",
                "statistics cookies",
                "preferences cookies",
                "unclassified cookies",
            ]
        ):
            skip_section = True
            continue

        # Resume capturing content at headings
        if skip_section and line.startswith("#"):
            skip_section = False

        if not skip_section:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()


def extract_main_content(content: str) -> str:
    """Extract the main article content from markdown"""
    lines = content.split("\n")
    content_lines = []
    in_content = False

    for line in lines:
        # Start capturing at first heading
        if line.startswith("#"):
            in_content = True

        if in_content:
            content_lines.append(line)

    return "\n".join(content_lines).strip()


def format_output(content: str, format_type: str) -> str:
    """Format the content based on the specified format"""
    if format_type == "plain":
        # Remove markdown formatting
        text = content
        text = text.replace("**", "")  # Remove bold
        text = text.replace("*", "")  # Remove italic
        text = text.replace("###", "")  # Remove h3
        text = text.replace("##", "")  # Remove h2
        text = text.replace("#", "")  # Remove h1

        # Remove links but keep text
        while "[" in text and "](" in text:
            start = text.find("[")
            mid = text.find("](")
            end = text.find(")", mid)
            if start != -1 and mid != -1 and end != -1:
                link_text = text[start + 1 : mid]
                text = text[:start] + link_text + text[end + 1 :]
            else:
                break

        return text.strip()

    elif format_type == "json":
        # Extract title and content
        lines = content.split("\n")
        title = ""
        content_lines = []

        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
            else:
                content_lines.append(line)

        return json.dumps(
            {"title": title, "content": "\n".join(content_lines).strip()}, indent=2
        )

    return content  # Default to markdown
