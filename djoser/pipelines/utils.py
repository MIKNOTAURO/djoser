def validate_context_user_for_email(context):
    assert context['user']
    assert context['user'].get_email_field_name


def get_user_email(user):
    return getattr(user, user.get_email_field_name(), None)
