def generate_markdown_content(files_data, no_codeblock):
    """
    Generates a Markdown content string from the provided files data.
    Parameters:
    - files_data (list of dict): A list of dictionaries containing file information and content.
    - no_codeblock (bool): Flag indicating whether to disable wrapping code inside markdown code blocks.
    Returns:
    - str: A Markdown-formatted string containing the table of contents and the file contents.
    """
    table_of_contents = [f"- {file['path']}\n" for file in files_data]
    
    content_parts = []
    for file in files_data:
        file_content = file['content'].strip()
        if len(file_content) > 0:
            file_info = f"## File: {file['path']}\n"
            
            if no_codeblock:
                file_code = f"### Code\n\n{file_content}\n\n"
            else:
                file_code = f"```{file['language']}\n{file_content}\n```\n\n"
            
            content_parts.append(file_info + file_code)
    
    return (
        "# Table of Contents\n"
        + "".join(table_of_contents)
        + "\n"
        + "".join(content_parts)
    )
