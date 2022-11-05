

class MessageEntityTypes:
    URL = 'url'
    TEXT_URL = 'text_url'
    BOLD = 'bold'
    ITALIC = 'italic'
    UNDERLINE = 'underline'
    EMAIL = 'email'
    PHONE = 'phone'
    MENTION_NAME = 'mention_name'
    MENTION = 'mention'

    CHOICES = (
        (URL, 'URL'),
        (TEXT_URL, 'Text URL'),
        (BOLD, 'Bold'),
        (ITALIC, 'Italic'),
        (UNDERLINE, 'Underline'),
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
        (MENTION_NAME, 'Mention Name'),
        (MENTION, 'Mention')
    )

    MAP_CLASSES = dict((
        ('MessageEntityUrl', URL),
        ('MessageEntityTextUrl', TEXT_URL),
        ('MessageEntityBold', BOLD),
        ('MessageEntityItalic', ITALIC),
        ('MessageEntityUnderline', UNDERLINE),
        ('MessageEntityEmail', EMAIL),
        ('MessageEntityPhone', PHONE),
        ('MessageEntityMentionName', MENTION_NAME),
        ('MessageEntityMention', MENTION),
    ))
    