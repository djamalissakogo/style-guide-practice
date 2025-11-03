# Пример хорошего кода
is_staff = user.role in ("admin", "manager")
if user.is_active and is_staff and not user.is_banned:
    grant_access()
