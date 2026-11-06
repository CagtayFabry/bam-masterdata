"""Vocabulary type definitions related to welding experiments and simulation."""

from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class JointTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="JOINT_TYPES",
        description="""Types of welding joint arrangements.""",
    )


# butt_joint
# corner_joint
# t_joint
# lap_joint
# edge_joint


class BackingTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="BACKING_TYPES",
        description="""Welding support backing types""",
    )


# none
# strip
# strap
# ring
# split-pipe


class WeldTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELD_TYPES",
        description="""Type of joining weld.""",
    )


# groove
# fillet
# plug
# slot
# spot
# seam
# flange


class WeldingJointStates(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING_JOINT_STATES",
        description="""State of a welding joint.""",
    )


# prepared
# partially welded
# completed
# other
