import ssl

def cert_none_context():
    """Create a SSLContext object to not check hostname."""
    # PROTOCOL_TLS isn't available before 2.7.13 but this code is for 2.7.9+, so use this.
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE
    return context
