SEARCHFILE_QUERY = """
SELECT * FROM fileserverDB.files
WHERE category=%(CATEGORY)s and filename=%(FILENAME)s;
"""

SEARCHLIST_QUERY = """
SELECT filename FROM fileserverDB.files
WHERE category=%(CATEGORY)s;
"""