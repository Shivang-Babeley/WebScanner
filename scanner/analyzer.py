def analyze_headers(headers):
    server = headers.get("Server", "Unknown")
    content_type = headers.get("Content-Type", "Unknown")
    return {
        "server": server,
        "content_type": content_type
    }
