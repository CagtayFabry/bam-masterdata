"""Object type definitions related to welding experiments and simulation."""

from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType

from ..activities import (
    Analysis,
    Calibration,
    Computation,
    Experiment,
    Measurement,
    Processing,
)
from ..base_objects import Activity, Entity

# -------------------------
# MISSING TYPE STUBS
# -------------------------

Context = Entity
MaterialEntity = Entity

Software = Context
ParameterSet = Context

Sample = MaterialEntity
Material = MaterialEntity
Device = MaterialEntity

Instrument = Device
Equipment = Device
Sensor = Device

# -------------------------
# GENERAL
# -------------------------


# ----- Activity
class RobotExecution(Activity):
    defs = ObjectTypeDef(
        code="ROBOT_EXECUTION",
        description="""Execution of a robot program""",
        generated_code_prefix="",
    )


class WeldingProcess(Context):
    # GLOBAL VOCABULARY
    defs = ObjectTypeDef(
        code="WELDING_PROCESS",
        description="""Welding process identified by process names and numbers (ISO 4063)""",
        generated_code_prefix="",
    )


class CuttingProcess(Context):
    # GLOBAL VOCABULARY
    defs = ObjectTypeDef(
        code="CUTTING_PROCESS",
        description="""Cutting process identified by process names and numbers (ISO 4063)""",
        generated_code_prefix="",
    )


class WeldSegment(Context):
    defs = ObjectTypeDef(
        code="WELD_SEGMENT",
        description="""abstract segmentation of a welded joint into hierarchical structure""",
        generated_code_prefix="",
    )
    # Layer
    # bead
    # weld
    # section


# ----- Processing
class Welding(Processing):
    defs = ObjectTypeDef(
        code="WELDING",
        description="""ISO/TR 25901-1:2016 2.1.1.1 welding""",
        generated_code_prefix="",
    )


class Cutting(Processing):
    defs = ObjectTypeDef(
        code="CUTTING",
        description="""A cutting step""",
        generated_code_prefix="",
    )


# ----- ParameterSet
class CameraCalibrationParameters(ParameterSet):
    defs = ObjectTypeDef(
        code="CAMERA_CALIBRATION_PARAMETERS",
        description="""intrinsic (and extrinsic?) camera calibration parameters derived from a calibration run""",
        generated_code_prefix="",
    )


# ----- Sample
class Component(Sample):
    defs = ObjectTypeDef(
        code="COMPONENT",
        description="""assembly incorporating one or more welded joint(s) (2.1.4.2), ISO/TR 25901-1:2016 weldment (2.1.1.4) """,
        generated_code_prefix="",
    )


class WeldingJoint(Sample):
    defs = ObjectTypeDef(
        code="WELDING_JOINT",
        description="""physical layout of the workpieces AND resulting groove preparation (e.g. Butt joint + V-Groove), ISO/TR 25901-1:2016  joint (2.1.4.1)""",
        generated_code_prefix="",
    )
    # joint_type (vocab, e.g. butt joint, T-joint etc.)
    # groove preparation parameters
    # (describing the groove preparation angles etc.)
    # status (vocab, WeldingJointState)


class Workpiece(Sample):
    defs = ObjectTypeDef(
        code="WORKPIECE",
        description="""a single metallic plate, sheet, tube or similarly shaped sample""",
        generated_code_prefix="",
    )
    # shape (EN 10079, DIN EN 12258-1)
    # material (object, MetallicAlloy)
    # treatments (vocab) (multivalue)(RAW_MAT_TREATMENT_STEEL,RAW_MAT_TREATMENT_ALU)


class Weld(Sample):
    defs = ObjectTypeDef(
        code="WELD",
        description="""result of welding (2.1.1.1) Note 1 to entry: The weld includes the weld metal (2.1.2.1) and the heat-affected zone (2.1.2.2).""",
        generated_code_prefix="",
    )


# ----- Material
class MetallicAlloy(Material):
    defs = ObjectTypeDef(
        code="METALLIC_ALLOY",
        description="""Material Number and name according to VDEh""",
        generated_code_prefix="",
        prev_versions=["RAW_MATERIAL_CODE:v0"],
    )
    # Standards used:
    # aluminium (DIN EN 573 / Teal Sheets)
    # steel (EN 10027-2)
    # nickel (EN 10269)
    # titanium (DIN 17860 ?)


class GasMixture(Material):
    defs = ObjectTypeDef(
        code="GAS_MIXTURE",
        description="""Generic gas mixture [vol-%] e.g. shielding gas EN ISO 14175""",
        generated_code_prefix="",
    )


class WeldingWireAlloy(Material):
    defs = ObjectTypeDef(
        code="WELDING_WIRE_ALLOY",
        description="""Standardized welding wire alloy names (all materials)""",
        generated_code_prefix="",
    )


# Equipment
class WeldingTorchNeck(Equipment):
    defs = ObjectTypeDef(
        code="WELDING_TORCH_NECK",
        description="""arc welding torch neck component (can be generic type or specific)""",
        generated_code_prefix="",
    )


class WeldingGasNozzel(Equipment):
    defs = ObjectTypeDef(
        code="WELDING_GAS_NOZZEL",
        description="""arc welding torch gas nozzel (can be generic type or specific)""",
        generated_code_prefix="",
    )


class WeldingContactTip(Equipment):
    defs = ObjectTypeDef(
        code="WELDING_CONTACT_TIP",
        description="""arc welding or wire contact tip (can be generic type or specific)""",
        generated_code_prefix="",
    )


# -------------------------
# LASER
# -------------------------


class LaserSource(Instrument):
    defs = ObjectTypeDef(
        code="LASER_SOURCE",
        description="""Laser beam generator""",
        generated_code_prefix="",
    )


class Pyrometer(Instrument):
    defs = ObjectTypeDef(
        code="PYROMETER",
        description="""A pyrometer""",
        generated_code_prefix="",
    )


class LaserWeldOptic(Equipment):
    defs = ObjectTypeDef(
        code="LASER_WELD_OPTIC",
        description="""Welding head optic used for laser welding or cutting""",
        generated_code_prefix="",
    )


class LaserFiber(Equipment):
    defs = ObjectTypeDef(
        code="LASER_FIBER",
        description="""fiber for transporting a laser beam""",
        generated_code_prefix="",
    )


class HydraulicTable(Equipment):
    defs = ObjectTypeDef(
        code="HYDRAULIC_TABLE",
        description="""sample holder with hydraulic setup for strain application""",
        generated_code_prefix="",
    )


# -------------------------
# SIMULATION
# -------------------------


class CameraCalibration(Analysis):
    defs = ObjectTypeDef(
        code="CAMERA_CALIBRATION",
        description="""calibrating a camera setup for intrinsic (and extrinsic) parameters using checkerboards, charuco or similar.""",
        generated_code_prefix="",
    )


class Meshing(Computation):
    defs = ObjectTypeDef(
        code="MESHING",
        description="""Calculating a mesh for simulations""",
        generated_code_prefix="",
    )


class AnsisFluentRun(Computation):
    defs = ObjectTypeDef(
        code="ANSIS_FLUENT_RUN",
        description="""A simulation performed with Ansis Fluent""",
        generated_code_prefix="",
    )


class UDFModel(Software):
    defs = ObjectTypeDef(
        code="UDF_MODEL",
        description="""A UDF Model""",
        generated_code_prefix="",
    )


class AnsisFluent(Software):
    defs = ObjectTypeDef(
        code="ANSIS_FLUENT",
        description="""Ansis Fluent Software""",
        generated_code_prefix="",
    )


class SimulationDomain(Context):
    defs = ObjectTypeDef(
        code="SIMULATION_DOMAIN",
        description="""Describes the domain over which the simulation is defined (e.g. subdomain of a workpiece)""",
        generated_code_prefix="",
    )


class MaterialData(Context):
    defs = ObjectTypeDef(
        code="MATERIAL_DATA",
        description="""Describes material properties as used for simulations""",
        generated_code_prefix="",
    )
    # material (object, MetallicAlloy)
    # source (string)
    # temperature dependent properties (json)
