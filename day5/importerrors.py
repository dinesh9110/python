def handle_import_error():
    try:
        import non_existing_module
    except ImportError:
        print("Error: module not found!")
handle_import_error()