from inspect import signature
from typing import Any

from sphinx.domains.python import PyFunction
from sphinx.ext.autodoc import FunctionDocumenter
from sphinx.util import logging

from dagster.core.definitions.op_definition import OpDefinition

log = logging.getLogger(__name__)


class OpDocumenter(FunctionDocumenter):
    """Document op definitions."""

    objtype = 'op'
    member_order = 11

    @classmethod
    # pylint: disable-next=unused-argument
    def can_document_member(cls, member, membername, isattr, parent):
        return bool(
            isinstance(member, OpDefinition) and getattr(member, '__wrapped__')
        )

    # pylint: disable-next=unused-argument
    def format_args(self, **kwargs: Any):
        wrapped = getattr(self.object, '__wrapped__', None)
        if wrapped is not None:
            sig = signature(wrapped)
            fmt = str(sig).replace('\\', '\\\\')
            return fmt
        return ''

    def document_members(self, all_members=False):
        pass

    def check_module(self):
        # Normally checks if *self.object* is really defined in the module
        # given by *self.modname*. But since functions decorated with the @op
        # decorator are instances living in dagster, we have to check the
        # wrapped function instead.
        wrapped = getattr(self.object, '__wrapped__', None)
        if wrapped and getattr(wrapped, '__module__') == self.modname:
            return True
        return super().check_module()


# pylint: disable-next=too-few-public-methods
class OpDirective(PyFunction):
    """Sphinx op directive."""

    # pylint: disable-next=unused-argument
    def get_signature_prefix(self, sig):
        return self.env.config.dagster_op_prefix


def setup(app):
    """Setup Sphinx extension."""
    app.setup_extension('sphinx.ext.autodoc')
    app.add_autodocumenter(OpDocumenter)
    app.add_directive_to_domain('py', 'op', OpDirective)
    app.add_config_value('dagster_op_prefix', '(op)', True)

    return {
        'parallel_read_safe': True
    }
