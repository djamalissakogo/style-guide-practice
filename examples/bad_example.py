# Пример плохого кода
if user.is_active and (user.role == "admin" or user.role == "manager") and not user.is_banned:
    grant_access()
