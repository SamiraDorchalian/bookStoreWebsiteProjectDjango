from django.utils.translation import gettext as _

def add_variable_to_context(request):
    return {
        'homePage': _('HomePage'),
        'welcome': _('Welcome'),
        'logout': _('Log Out'),
        'login': _('Log In'),
        'signup': _('Sign Up'),
        'booksTitle': _('Books'),
        'home': _('Home'),
        'addNewBook': _('Add New Book'),
        'or': _('Or'),
        'link': _('Link'),
        'github': _('GitHub'),
        'FotgotYourPassword': _('Fotgot Your Password'),
    }