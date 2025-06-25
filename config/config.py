COMMON_PATHS = [
    "/.git/", "/.env", "/config.php", "/phpinfo.php",
    "/.htaccess", "/.htpasswd", "/backup/", "/admin/", "/wp-config.php",
    "/etc/passwd",  # directory traversal target
    "/../../../../../../etc/passwd",  # direct attempt
    "/..%2f..%2f..%2fetc%2fpasswd",  # encoded traversal
    "/server-status", "/debug", "/test", "/dev", "/logs","/sitemap.xml","/backup.zip","git/config","/robots.txt"
]
