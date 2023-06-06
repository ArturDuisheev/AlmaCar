from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone_number, username, inn, password, promotion, is_staff, is_superuser, **extra_fields):
        if not phone_number:
            raise ValueError("Вы не ввели phone_number!")
        if not username:
            raise ValueError("Вы не ввели ФИО!")
        if not inn:
            raise ValueError("Вы не ввели ваш номер!")
        if not password:
            raise ValueError("Вы не ввели пароль!")
        user = self.model(
            phone_number=phone_number,
            username=username,
            inn=inn,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            promotion=promotion,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_superuser(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("Вы не ввели ваше phone_number !")
        if not password:
            raise ValueError("Вы не ввели пароль!")
        superuser = self.model(
            phone_number=phone_number,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
        if password:
            superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser

    def create_user(
            self,
            phone_number,
            username,
            inn,
            promotion,
            password=None,
            **extra_fields
    ):

        return self._create_user(phone_number, username, inn, password, promotion, is_staff=False, is_superuser=False,
                                 **extra_fields)

    def create_superuser(
            self,
            phone_number,
            password=None,
    ):

        superuser = self._create_superuser(phone_number, password)
        superuser.save(using=self._db)
        return superuser