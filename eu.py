def process_toc(toc):
    if not is_supported_toc(toc):
        raise NotSupportedTOCError("The Table of Contents format is not supported.")

def is_supported_toc(toc):
    # Logic to determine if the TOC format is supported
    return False  # Placeholder logic for demonstration purposes

# Example usage:
toc_data = {...}  # Some Table of Contents data
try:
    process_toc(toc_data)
except NotSupportedTOCError as e:
    print(f"Error: {str(e)}")
    # Handle the error or exception accordingly
