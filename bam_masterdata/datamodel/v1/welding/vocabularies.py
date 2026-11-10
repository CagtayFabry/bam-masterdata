"""Vocabulary type definitions related to welding experiments and simulation."""

from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class FiberConnectorTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="FIBER_CONNECTOR_TYPES",
        description="Types of laser fiber connectors.",
    )

    llk_d = VocabularyTerm(
        code="LLK_D", label="LLK-D", description="Trumpf LLK-D connector."
    )

    llk_x = VocabularyTerm(
        code="LLK_X", label="LLK-X", description="Trumpf LLK-X connector."
    )

    qbh = VocabularyTerm(code="QBH", label="QBH", description="QBH connector.")

    sma = VocabularyTerm(code="SMA", label="SMA", description="SMA connector.")


class FiberTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="FIBER_TYPES",
        description="Types of laser fibers.",
    )

    single_core = VocabularyTerm(
        code="SINGLE_CORE", label="Single-core", description="Single-core fiber."
    )

    brightlineweld = VocabularyTerm(
        code="BRIGHTLINEWELD",
        label="BrightLineWeld",
        description="BrightLineWeld fiber.",
    )

    structured = VocabularyTerm(
        code="STRUCTURED", label="Structured", description="Structured fiber."
    )


class LaserTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="LASER_TYPES",
        description="Types of laser active media.",
    )

    # TODO: Add vocabulary terms from LaserTypes in examples/laser.py.


class SensorPrinciples(VocabularyType):
    defs = VocabularyTypeDef(
        code="SENSOR_PRINCIPLES",
        description="Physical principles of force measurement.",
    )

    # TODO: Add vocabulary terms from SensorPrinciples in examples/laser.py.


class ForceDirections(VocabularyType):
    defs = VocabularyTypeDef(
        code="FORCE_DIRECTIONS",
        description="Permissible force measurement directions.",
    )

    # TODO: Add vocabulary terms from ForceDirections in examples/laser.py.


class JointTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="JOINT_TYPES",
        description="""Types of welding joint arrangements.""",
    )

    butt_joint = VocabularyTerm(
        code="BUTT_JOINT",
        label="Butt joint",
        description="A butt joint.",
    )

    corner_joint = VocabularyTerm(
        code="CORNER_JOINT",
        label="Corner joint",
        description="A corner joint.",
    )

    t_joint = VocabularyTerm(
        code="T_JOINT",
        label="T-joint",
        description="A T-joint.",
    )

    lap_joint = VocabularyTerm(
        code="LAP_JOINT",
        label="Lap joint",
        description="A lap joint.",
    )

    edge_joint = VocabularyTerm(
        code="EDGE_JOINT",
        label="Edge joint",
        description="An edge joint.",
    )


class BackingTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="BACKING_TYPES",
        description="""Welding support backing types""",
    )

    none = VocabularyTerm(
        code="NONE",
        label="None",
        description="No backing.",
    )

    strip = VocabularyTerm(
        code="STRIP",
        label="Strip",
        description="Strip backing.",
    )

    strap = VocabularyTerm(
        code="STRAP",
        label="Strap",
        description="Strap backing.",
    )

    ring = VocabularyTerm(
        code="RING",
        label="Ring",
        description="Ring backing.",
    )

    split_pipe = VocabularyTerm(
        code="SPLIT_PIPE",
        label="Split pipe",
        description="Split-pipe backing.",
    )


class WeldTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELD_TYPES",
        description="""Types of joining weld.""",
    )

    groove = VocabularyTerm(
        code="GROOVE",
        label="Groove",
        description="A groove weld.",
    )

    fillet = VocabularyTerm(
        code="FILLET",
        label="Fillet",
        description="A fillet weld.",
    )

    plug = VocabularyTerm(
        code="PLUG",
        label="Plug",
        description="A plug weld.",
    )

    slot = VocabularyTerm(
        code="SLOT",
        label="Slot",
        description="A slot weld.",
    )

    spot = VocabularyTerm(
        code="SPOT",
        label="Spot",
        description="A spot weld.",
    )

    seam = VocabularyTerm(
        code="SEAM",
        label="Seam",
        description="A seam weld.",
    )

    flange = VocabularyTerm(
        code="FLANGE",
        label="Flange",
        description="A flange weld.",
    )


class WeldingJointStates(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING_JOINT_STATES",
        description="""State of a welding joint.""",
    )

    prepared = VocabularyTerm(
        code="PREPARED",
        label="Prepared",
        description="The joint is prepared for welding.",
    )

    partially_welded = VocabularyTerm(
        code="PARTIALLY_WELDED",
        label="Partially welded",
        description="The joint is partially welded.",
    )

    completed = VocabularyTerm(
        code="COMPLETED",
        label="Completed",
        description="The joint is fully welded.",
    )

    other = VocabularyTerm(
        code="OTHER",
        label="Other",
        description="Another joint state.",
    )


class GrooveTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="GROOVE_TYPES",
        description="Welding groove preparations identified by code number and type according to DIN EN ISO 9692-1.",
    )

    groove_1_2_1 = VocabularyTerm(
        code="1.2.1",
        label="1.2.1 (I-Groove)",
        description="I-Groove with code number 1.2.1.",
    )

    groove_1_2_2 = VocabularyTerm(
        code="1.2.2",
        label="1.2.2 (I-Groove)",
        description="I-Groove with code number 1.2.2.",
    )

    groove_2_1 = VocabularyTerm(
        code="2.1",
        label="2.1 (I-Groove)",
        description="I-Groove with code number 2.1.",
    )

    groove_1_3 = VocabularyTerm(
        code="1.3",
        label="1.3 (V-Groove)",
        description="V-Groove with code number 1.3.",
    )

    groove_1_5 = VocabularyTerm(
        code="1.5",
        label="1.5 (V-Groove)",
        description="V-Groove with code number 1.5.",
    )

    groove_1_6 = VocabularyTerm(
        code="1.6",
        label="1.6 (UV-Groove)",
        description="UV-Groove with code number 1.6.",
    )

    groove_1_7 = VocabularyTerm(
        code="1.7",
        label="1.7 (VV-Groove)",
        description="VV-Groove with code number 1.7.",
    )

    groove_1_8 = VocabularyTerm(
        code="1.8",
        label="1.8 (U-Groove)",
        description="U-Groove with code number 1.8.",
    )

    groove_1_9_1 = VocabularyTerm(
        code="1.9.1",
        label="1.9.1 (HV-Groove)",
        description="HV-Groove with code number 1.9.1.",
    )

    groove_1_9_2 = VocabularyTerm(
        code="1.9.2",
        label="1.9.2 (HV-Groove)",
        description="HV-Groove with code number 1.9.2.",
    )

    groove_2_8 = VocabularyTerm(
        code="2.8",
        label="2.8 (HV-Groove)",
        description="HV-Groove with code number 2.8.",
    )

    groove_1_11 = VocabularyTerm(
        code="1.11",
        label="1.11 (HU-Groove)",
        description="HU-Groove with code number 1.11.",
    )

    groove_2_10 = VocabularyTerm(
        code="2.10",
        label="2.10 (HU-Groove)",
        description="HU-Groove with code number 2.10.",
    )

    groove_2_4 = VocabularyTerm(
        code="2.4",
        label="2.4 (DV-Groove)",
        description="DV-Groove with code number 2.4.",
    )

    groove_2_5_1 = VocabularyTerm(
        code="2.5.1",
        label="2.5.1 (DV-Groove)",
        description="DV-Groove with code number 2.5.1.",
    )

    groove_2_5_2 = VocabularyTerm(
        code="2.5.2",
        label="2.5.2 (DV-Groove)",
        description="DV-Groove with code number 2.5.2.",
    )

    groove_2_7 = VocabularyTerm(
        code="2.7",
        label="2.7 (DU-Groove)",
        description="DU-Groove with code number 2.7.",
    )

    groove_2_9_1 = VocabularyTerm(
        code="2.9.1",
        label="2.9.1 (DHV-Groove)",
        description="DHV-Groove with code number 2.9.1.",
    )

    groove_2_9_2 = VocabularyTerm(
        code="2.9.2",
        label="2.9.2 (DHV-Groove)",
        description="DHV-Groove with code number 2.9.2.",
    )

    groove_2_11 = VocabularyTerm(
        code="2.11",
        label="2.11 (DHU-Groove)",
        description="DHU-Groove with code number 2.11.",
    )

    groove_1_12 = VocabularyTerm(
        code="1.12",
        label="1.12 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 1.12.",
    )

    groove_1_13 = VocabularyTerm(
        code="1.13",
        label="1.13 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 1.13.",
    )

    groove_2_12 = VocabularyTerm(
        code="2.12",
        label="2.12 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 2.12.",
    )

    groove_3_1_1 = VocabularyTerm(
        code="3.1.1",
        label="3.1.1 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 3.1.1.",
    )

    groove_3_1_2 = VocabularyTerm(
        code="3.1.2",
        label="3.1.2 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 3.1.2.",
    )

    groove_3_1_3 = VocabularyTerm(
        code="3.1.3",
        label="3.1.3 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 3.1.3.",
    )

    groove_4_1_1 = VocabularyTerm(
        code="4.1.1",
        label="4.1.1 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 4.1.1.",
    )

    groove_4_1_2 = VocabularyTerm(
        code="4.1.2",
        label="4.1.2 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 4.1.2.",
    )

    groove_4_1_3 = VocabularyTerm(
        code="4.1.3",
        label="4.1.3 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 4.1.3.",
    )
