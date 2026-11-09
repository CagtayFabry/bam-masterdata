"""Temporary definitions pending upstream integration."""

from bam_masterdata.metadata.definitions import ObjectTypeDef

from .entities import Context


class Software(Context):
    defs = ObjectTypeDef(
        code="SOFTWARE",
        description="""Software class stub""",
        generated_code_prefix="",
    )


class ParameterSet(Context):
    defs = ObjectTypeDef(
        code="PARAMETER_SET",
        description="""ParameterSet class stub""",
        generated_code_prefix="",
    )
