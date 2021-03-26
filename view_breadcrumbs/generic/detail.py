from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from ..utils import action_view_name
from .list import ListBreadcrumbMixin


def _model_repr(instance):
    return force_str(instance)


class DetailBreadcrumbMixin(ListBreadcrumbMixin):
    # Home / object List / object
    @property
    def crumbs(self):
        return super(DetailBreadcrumbMixin, self).crumbs + [
            (_model_repr, self._detail_view_url),
        ]

    def _detail_view_url(self, instance):
        return reverse(
            action_view_name(instance, self.detail_view_suffix),
            kwargs={"pk": instance.pk},
        )
