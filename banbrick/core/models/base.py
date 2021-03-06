from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _

from ycyc.base.typeutils import constants


BASE_VALIDATORS = constants(
    safety_string=validators.RegexValidator(
        r"^[^\[\]\(\)\<\>=\"\',:]+$",
        _("Not allow match in: []()<>,\'\":"),
        _("Invalid string"),
    ),
)


class BaseModel(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created on"),
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        auto_now_add=True,
        verbose_name=_("Updated on"),
    )

    def __repr__(self):
        return "<{type}: id={id}>".format(
            type=self.__class__.__name__,
            id=self.id,
        )

    def __str__(self):
        return repr(self)

    class Meta:
        abstract = True


class BaseTag(BaseModel):
    name = models.CharField(
        max_length=64, null=False, blank=False,
        default=None, unique=True, db_index=True,
        verbose_name=_("Name"), validators=[
            BASE_VALIDATORS.safety_string,
        ],
    )

    class Meta:
        abstract = True

    def __repr__(self):
        return "<{type}: id={id}, name={name}>".format(
            type=self.__class__.__name__,
            name=self.name, id=self.id,
        )

    def __str__(self):
        return self.name
