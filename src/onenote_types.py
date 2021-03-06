from enum import Enum

PARENT_UID_KEY = "parentUid"
PAGES_OF_SAME_SECTION_ALREADY_LOADED = "pagesOfSameSectionAlreadyLoaded"
PAGE_UID_KEY = "pageUid"
ONENOTE_TYPE_KEY = "onenoteType"
NOTEBOOKS_KEY = "notebooks"


class OneNoteType(str, Enum):
    NOTEBOOK = "notebook"
    SECTION_GROUP = "sectionGroup"
    SECTION = "section"
    PAGE = "page"


class OneNoteElement(object):
    def __init__(self, title, autocomplete, uid, subtitle, arg, icon, icontype, onenoteType, parentUid,
                 lastModifiedDateTime, match):
        self.title = title
        self.autocomplete = autocomplete
        self.uid = uid
        self.subtitle = subtitle
        self.arg = arg
        self.icon = icon
        self.icontype = icontype
        self.onenoteType = onenoteType
        self.parentUid = parentUid
        self.lastModifiedDateTime = lastModifiedDateTime
        self.match = match


def as_onenoteelement(data):
    return OneNoteElement(data['title'], data['autocomplete'], data['uid'], data['subtitle'], data['arg'], data['icon'],
                          data['icontype'], data['onenoteType'], data['parentUid'], data['lastModifiedDateTime'],
                          data['match'])
