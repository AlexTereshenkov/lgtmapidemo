def get_customers(user):
    """Get list of customers."""
    assert is_superuser(user), "User is not a member of superuser group"
    return db.lookup('customers')