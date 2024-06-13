class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class EmptyResponse(Exception):
    """Вызывается, когда парсер не может найти 'All versions'"""
    pass
