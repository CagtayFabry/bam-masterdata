# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Activity
# └── RobotExecution
#
# Context
# ├── WeldingProcess
# ├── CuttingProcess
# ├── WeldSegment
# ├── SimulationDomain
# └── MaterialData
#
# Processing
# ├── Welding
# │   └── LaserCTW
# └── Cutting
#
# ParameterSet
# └── CameraCalibrationParameters
#
# Sample
# ├── Component
# ├── WeldingJoint
# ├── Workpiece
# └── Weld
#
# Material
# ├── MetallicAlloy
# ├── GasMixture
# └── WeldingWireAlloy
#
# Equipment
# ├── WeldingTorchNeck
# ├── WeldingGasNozzel
# ├── WeldingContactTip
# ├── LaserWeldOptic
# ├── LaserFiber
# └── HydraulicTable
#
# Instrument
# ├── LaserSource
# ├── Pyrometer
# └── LoadCell
#
# Analysis
# └── CameraCalibration
#
# Computation
# ├── Meshing
# └── AnsisFluentRun
#
# Software
# ├── UDFModel
# └── AnsisFluent
#
# END AUTO-GENERATED CLASS HIERARCHY

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
from ..base_objects import (
    Activity,
)
from ..entities import (
    Context,
    Device,
    Entity,
    Equipment,
    Instrument,
    Material,
    PhysicalObject,
    Sample,
    Sensor,
)

# -------------------------
# MISSING TYPE STUBS
# -------------------------
from ..temp import ParameterSet, Software

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

    process_number = PropertyTypeAssignment(
        mandatory=False,
        code="PROCESS_NUMBER",
        data_type="VARCHAR",
        property_label="Process number",
        description="ISO 4063 number identifying the welding process.",
    )

    standard_edition = PropertyTypeAssignment(
        mandatory=False,
        code="STANDARD_EDITION",
        data_type="VARCHAR",
        property_label="Standard edition",
        description="Edition of ISO 4063 used to identify the welding process.",
    )


class CuttingProcess(Context):
    # GLOBAL VOCABULARY
    defs = ObjectTypeDef(
        code="CUTTING_PROCESS",
        description="""Cutting process identified by process names and numbers (ISO 4063)""",
        generated_code_prefix="",
    )

    process_number = PropertyTypeAssignment(
        mandatory=False,
        code="PROCESS_NUMBER",
        data_type="VARCHAR",
        property_label="Process number",
        description="ISO 4063 number identifying the cutting process.",
    )

    standard_edition = PropertyTypeAssignment(
        mandatory=False,
        code="STANDARD_EDITION",
        data_type="VARCHAR",
        property_label="Standard edition",
        description="Edition of ISO 4063 used to identify the cutting process.",
    )


class WeldSegment(Context):
    defs = ObjectTypeDef(
        code="WELD_SEGMENT",
        description="""abstract segmentation of a welded joint into hierarchical structure""",
        generated_code_prefix="",
    )
    layer = PropertyTypeAssignment(
        mandatory=False,
        code="LAYER",
        data_type="INTEGER",
        property_label="Layer",
        description="Number identifying the layer of the weld segment.",
    )

    bead = PropertyTypeAssignment(
        mandatory=False,
        code="BEAD",
        data_type="INTEGER",
        property_label="Bead",
        description="Number identifying the bead of the weld segment.",
    )

    weld = PropertyTypeAssignment(
        mandatory=False,
        code="WELD",
        data_type="INTEGER",
        property_label="Weld",
        description="Number identifying the weld of the weld segment.",
    )

    section = PropertyTypeAssignment(
        mandatory=False,
        code="SECTION",
        data_type="INTEGER",
        property_label="Section",
        description="Number identifying the section of the weld segment.",
    )


# ----- Processing
class Welding(Processing):
    defs = ObjectTypeDef(
        code="WELDING",
        description="""ISO/TR 25901-1:2016 2.1.1.1 welding""",
        generated_code_prefix="",
    )

    # TODO: Model the welding joint, weld segment, weld, filler material, and
    # shielding gas as parent/child relations.

    welding_process = PropertyTypeAssignment(
        mandatory=False,
        code="WELDING_PROCESS",
        data_type="OBJECT",
        object_code="WELDING_PROCESS",
        property_label="Welding process",
        description="Welding process used for the activity.",
    )

    welding_position = PropertyTypeAssignment(
        mandatory=False,
        code="WELDING_POSITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING_POSITIONS",
        property_label="Welding position",
        description="Position in which welding is performed.",
    )

    welding_procedure_specification = PropertyTypeAssignment(
        mandatory=False,
        code="WELDING_PROCEDURE_SPECIFICATION",
        data_type="VARCHAR",
        property_label="Welding procedure specification",
        description="Identifier of the welding procedure specification used.",
    )


class LaserCTW(Welding):
    defs = ObjectTypeDef(
        code="LASER_CTW",
        description="Laser welding with an externally applied strain.",
        generated_code_prefix="",
    )

    # TODO: Model the joint and workpiece as parent/child relations.
    # TODO: Add the missing preparation information; clarify whether it describes
    # groove preparation or surface preparation.

    weld_travel_speed = PropertyTypeAssignment(
        mandatory=False,
        code="WELD_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed",
        description="Travel speed along the weld.",
        units="cm/min",
    )

    shielding_gas_flow = PropertyTypeAssignment(
        mandatory=False,
        code="SHIELDING_GAS_FLOW",
        data_type="REAL",
        property_label="Shielding gas flow rate",
        description="Shielding gas flow rate.",
        units="L/min",
    )

    shielding_gas_angle = PropertyTypeAssignment(
        mandatory=False,
        code="SHIELDING_GAS_ANGLE",
        data_type="REAL",
        property_label="Shielding gas angle",
        description="Nozzle angle relative to the horizontal.",
        units="deg",
    )

    backing_gas = PropertyTypeAssignment(
        mandatory=False,
        code="BACKING_GAS",
        data_type="BOOLEAN",
        property_label="Backing gas used",
        description="Whether backing gas is used.",
    )

    laser_power = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_POWER",
        data_type="REAL",
        property_label="Laser power",
        description="Laser power used for welding.",
        units="kW",
    )

    laser_focus = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_FOCUS",
        data_type="REAL",
        property_label="Laser focus position",
        description="Laser focus position.",
        units="mm",
    )

    laser_ramp_up = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_RAMP_UP",
        data_type="BOOLEAN",
        property_label="Laser ramp-up used",
        description="Whether a power ramp is used when turning on the laser.",
    )

    laser_illumination_power = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_ILLUMINATION_POWER",
        data_type="REAL",
        property_label="Illumination laser power",
        description="Power of the illumination laser.",
        units="W",
    )

    laser_illumination_spot_size = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_ILLUMINATION_SPOT_SIZE",
        data_type="REAL",
        property_label="Illumination spot diameter",
        description="Diameter of the illuminated spot.",
        units="mm",
    )

    laser_illumination_spot_angle = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_ILLUMINATION_SPOT_ANGLE",
        data_type="REAL",
        property_label="Illumination angle",
        description="Illumination optics angle relative to the horizontal.",
        units="deg",
    )

    laser_illumination_filter = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_ILLUMINATION_FILTER",
        data_type="VARCHAR",
        property_label="Optical filters",
        description="Optical filters used in front of the camera.",
    )

    strain_rate = PropertyTypeAssignment(
        mandatory=False,
        code="STRAIN_RATE",
        data_type="REAL",
        property_label="Strain rate",
        description="Strain rate applied to the specimen.",
        units="percent/s",
    )

    strain_max = PropertyTypeAssignment(
        mandatory=False,
        code="STRAIN_MAX",
        data_type="REAL",
        property_label="Maximum strain",
        description="Maximum strain applied to the specimen.",
        units="percent",
    )

    strain_direction = PropertyTypeAssignment(
        mandatory=False,
        code="STRAIN_DIRECTION",
        data_type="REAL",
        property_label="Strain direction",
        description="Strain direction relative to the welding direction.",
        units="deg",
    )

    strain_starting_point = PropertyTypeAssignment(
        mandatory=False,
        code="STRAIN_STARTING_POINT",
        data_type="REAL",
        property_label="Strain starting point",
        description="Starting point of strain application along the weld.",
        units="mm",
    )

    strain_preload = PropertyTypeAssignment(
        mandatory=False,
        code="STRAIN_PRELOAD",
        data_type="REAL",
        property_label="Preload strain",
        description="Strain applied before the main loading.",
        units="percent",
    )

    robot_program = PropertyTypeAssignment(
        mandatory=False,
        code="ROBOT_PROGRAM",
        data_type="VARCHAR",
        property_label="Robot program",
        description="Robot control program.",
    )

    laser_program = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_PROGRAM",
        data_type="VARCHAR",
        property_label="Laser program",
        description="Laser control program.",
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

    focal_length_fx = PropertyTypeAssignment(
        code="FOCAL_LENGTH_FX",
        data_type="REAL",
        mandatory=False,
        property_label="Focal length fx",
        description="Horizontal focal length in image coordinates.",
        units="pixel",
    )

    focal_length_fy = PropertyTypeAssignment(
        code="FOCAL_LENGTH_FY",
        data_type="REAL",
        mandatory=False,
        property_label="Focal length fy",
        description="Vertical focal length in image coordinates.",
        units="pixel",
    )

    principal_point_cx = PropertyTypeAssignment(
        code="PRINCIPAL_POINT_CX",
        data_type="REAL",
        mandatory=False,
        property_label="Principal point cx",
        description="Horizontal coordinate of the principal point.",
        units="pixel",
    )

    principal_point_cy = PropertyTypeAssignment(
        code="PRINCIPAL_POINT_CY",
        data_type="REAL",
        mandatory=False,
        property_label="Principal point cy",
        description="Vertical coordinate of the principal point.",
        units="pixel",
    )

    skew = PropertyTypeAssignment(
        code="CAMERA_SKEW",
        data_type="REAL",
        mandatory=False,
        property_label="Skew",
        description="Skew term in the camera intrinsic matrix.",
        units="pixel",
    )

    radial_distortion_k1 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K1",
        data_type="REAL",
        mandatory=False,
        property_label="Radial distortion k1",
        description="First radial distortion coefficient.",
    )

    radial_distortion_k2 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K2",
        data_type="REAL",
        mandatory=False,
        property_label="Radial distortion k2",
        description="Second radial distortion coefficient.",
    )

    radial_distortion_k3 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K3",
        data_type="REAL",
        mandatory=False,
        property_label="Radial distortion k3",
        description="Third radial distortion coefficient.",
    )

    radial_distortion_k4 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K4",
        data_type="REAL",
        mandatory=False,
        property_label="Radial distortion k4",
        description="Fourth radial distortion coefficient, used by the rational model.",
    )

    radial_distortion_k5 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K5",
        data_type="REAL",
        mandatory=False,
        property_label="Radial distortion k5",
        description="Fifth radial distortion coefficient, used by the rational model.",
    )

    radial_distortion_k6 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K6",
        data_type="REAL",
        mandatory=False,
        property_label="Radial distortion k6",
        description="Sixth radial distortion coefficient, used by the rational model.",
    )

    tangential_distortion_p1 = PropertyTypeAssignment(
        code="TANGENTIAL_DISTORTION_P1",
        data_type="REAL",
        mandatory=False,
        property_label="Tangential distortion p1",
        description="First tangential distortion coefficient.",
    )

    tangential_distortion_p2 = PropertyTypeAssignment(
        code="TANGENTIAL_DISTORTION_P2",
        data_type="REAL",
        mandatory=False,
        property_label="Tangential distortion p2",
        description="Second tangential distortion coefficient.",
    )

    thin_prism_distortion_s1 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S1",
        data_type="REAL",
        mandatory=False,
        property_label="Thin-prism distortion s1",
        description="First thin-prism distortion coefficient.",
    )

    thin_prism_distortion_s2 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S2",
        data_type="REAL",
        mandatory=False,
        property_label="Thin-prism distortion s2",
        description="Second thin-prism distortion coefficient.",
    )

    thin_prism_distortion_s3 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S3",
        data_type="REAL",
        mandatory=False,
        property_label="Thin-prism distortion s3",
        description="Third thin-prism distortion coefficient.",
    )

    thin_prism_distortion_s4 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S4",
        data_type="REAL",
        mandatory=False,
        property_label="Thin-prism distortion s4",
        description="Fourth thin-prism distortion coefficient.",
    )

    sensor_tilt_tau_x = PropertyTypeAssignment(
        code="SENSOR_TILT_TAU_X",
        data_type="REAL",
        mandatory=False,
        property_label="Sensor tilt tau x",
        description="Sensor tilt parameter about the x-axis.",
        units="rad",
    )

    sensor_tilt_tau_y = PropertyTypeAssignment(
        code="SENSOR_TILT_TAU_Y",
        data_type="REAL",
        mandatory=False,
        property_label="Sensor tilt tau y",
        description="Sensor tilt parameter about the y-axis.",
        units="rad",
    )

    image_width = PropertyTypeAssignment(
        code="CALIBRATION_IMAGE_WIDTH",
        data_type="INTEGER",
        mandatory=False,
        property_label="Image width",
        description="Width of the images used for calibration.",
        units="pixel",
    )

    image_height = PropertyTypeAssignment(
        code="CALIBRATION_IMAGE_HEIGHT",
        data_type="INTEGER",
        mandatory=False,
        property_label="Image height",
        description="Height of the images used for calibration.",
        units="pixel",
    )

    rms_reprojection_error = PropertyTypeAssignment(
        code="RMS_REPROJECTION_ERROR",
        data_type="REAL",
        mandatory=False,
        property_label="RMS reprojection error",
        description="Overall root-mean-square reprojection error.",
        units="pixel",
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

    joint_status = PropertyTypeAssignment(
        mandatory=False,
        code="JOINT_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Joint status",
        description="Current state of the welding joint.",
        vocabulary_code="WELDING_JOINT_STATES",
    )

    joint_type = PropertyTypeAssignment(
        mandatory=False,
        code="JOINT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Joint type",
        description="Arrangement of the workpieces in the welding joint.",
        vocabulary_code="JOINT_TYPES",
    )

    groove_type = PropertyTypeAssignment(
        mandatory=False,
        code="GROOVE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Groove type",
        description="Groove preparation identified by its unique code number and type name.",
        vocabulary_code="GROOVE_TYPES",
    )

    workpiece_thickness = PropertyTypeAssignment(
        mandatory=False,
        code="WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Workpiece thickness",
        description="Thickness of the first workpiece.",
        units="mm",
    )

    workpiece_thickness2 = PropertyTypeAssignment(
        mandatory=False,
        code="WORKPIECE_THICKNESS_2",
        data_type="REAL",
        property_label="Workpiece thickness 2",
        description="Thickness of the second workpiece.",
        units="mm",
    )

    root_gap = PropertyTypeAssignment(
        mandatory=False,
        code="ROOT_GAP",
        data_type="REAL",
        property_label="Root gap",
        description="Gap between the workpieces at the joint root.",
        units="mm",
    )

    root_face = PropertyTypeAssignment(
        mandatory=False,
        code="ROOT_FACE",
        data_type="REAL",
        property_label="Root face",
        description="Dimension of the root face of the joint preparation.",
        units="mm",
    )

    root_face2 = PropertyTypeAssignment(
        mandatory=False,
        code="ROOT_FACE_2",
        data_type="REAL",
        property_label="Root face 2",
        description="Dimension of the second root face of the joint preparation.",
        units="mm",
    )

    root_face3 = PropertyTypeAssignment(
        mandatory=False,
        code="ROOT_FACE_3",
        data_type="REAL",
        property_label="Root face 3",
        description="Dimension of the third root face of the joint preparation.",
        units="mm",
    )

    bevel_radius = PropertyTypeAssignment(
        mandatory=False,
        code="BEVEL_RADIUS",
        data_type="REAL",
        property_label="Bevel radius",
        description="Radius of the bevel in the joint preparation.",
        units="mm",
    )

    bevel_radius2 = PropertyTypeAssignment(
        mandatory=False,
        code="BEVEL_RADIUS_2",
        data_type="REAL",
        property_label="Bevel radius 2",
        description="Radius of the second bevel in the joint preparation.",
        units="mm",
    )

    bevel_angle = PropertyTypeAssignment(
        mandatory=False,
        code="BEVEL_ANGLE",
        data_type="REAL",
        property_label="Bevel angle",
        description="Angle of the bevel in the joint preparation.",
        units="deg",
    )

    bevel_angle2 = PropertyTypeAssignment(
        mandatory=False,
        code="BEVEL_ANGLE_2",
        data_type="REAL",
        property_label="Bevel angle 2",
        description="Angle of the second bevel in the joint preparation.",
        units="deg",
    )

    groove_angle = PropertyTypeAssignment(
        mandatory=False,
        code="GROOVE_ANGLE",
        data_type="REAL",
        property_label="Groove angle",
        description="Angle of the groove in the joint preparation.",
        units="deg",
    )

    groove_angle2 = PropertyTypeAssignment(
        mandatory=False,
        code="GROOVE_ANGLE_2",
        data_type="REAL",
        property_label="Groove angle 2",
        description="Angle of the second groove in the joint preparation.",
        units="deg",
    )

    special_depth = PropertyTypeAssignment(
        mandatory=False,
        code="SPECIAL_DEPTH",
        data_type="REAL",
        property_label="Special depth",
        description="Special depth used for the 4.1.2 Frontal-Face-Groove type.",
        units="mm",
    )


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
    # Legacy MATERIAL_NUMBER is represented by the inherited MATERIAL_ID.
    # Standards used:
    # aluminium (DIN EN 573 / Teal Sheets)
    # steel (EN 10027-2)
    # nickel (EN 10269)
    # titanium (DIN 17860 ?)

    alias = PropertyTypeAssignment(
        mandatory=False,
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative name",
        description="Alternative name, abbreviation, or nickname for the alloy.",
    )

    material_group = PropertyTypeAssignment(
        mandatory=False,
        code="MATERIAL_GROUP",
        data_type="VARCHAR",
        property_label="Material group",
        description="Material group, such as a steel group.",
    )

    characteristics = PropertyTypeAssignment(
        mandatory=False,
        code="CHARACTERISTICS",
        data_type="VARCHAR",
        property_label="Characteristics",
        description="Characteristics of the alloy.",
    )

    notes = PropertyTypeAssignment(
        mandatory=False,
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="Additional notes about the alloy.",
    )


class GasMixture(Material):
    defs = ObjectTypeDef(
        code="GAS_MIXTURE",
        description="""Generic gas mixture [vol-%] e.g. shielding gas EN ISO 14175""",
        generated_code_prefix="",
    )

    argon = PropertyTypeAssignment(
        mandatory=False,
        code="ARGON",
        data_type="REAL",
        property_label="Argon",
        description="Volume fraction of argon (Ar) in the mixture.",
        units="percent",
    )

    helium = PropertyTypeAssignment(
        mandatory=False,
        code="HELIUM",
        data_type="REAL",
        property_label="Helium",
        description="Volume fraction of helium (He) in the mixture.",
        units="percent",
    )

    carbon_dioxide = PropertyTypeAssignment(
        mandatory=False,
        code="CARBON_DIOXIDE",
        data_type="REAL",
        property_label="Carbon dioxide",
        description="Volume fraction of carbon dioxide (CO2) in the mixture.",
        units="percent",
    )

    oxygen = PropertyTypeAssignment(
        mandatory=False,
        code="OXYGEN",
        data_type="REAL",
        property_label="Oxygen",
        description="Volume fraction of oxygen (O2) in the mixture.",
        units="percent",
    )

    nitrogen = PropertyTypeAssignment(
        mandatory=False,
        code="NITROGEN",
        data_type="REAL",
        property_label="Nitrogen",
        description="Volume fraction of nitrogen (N2) in the mixture.",
        units="percent",
    )

    hydrogen = PropertyTypeAssignment(
        mandatory=False,
        code="HYDROGEN",
        data_type="REAL",
        property_label="Hydrogen",
        description="Volume fraction of hydrogen (H2) in the mixture.",
        units="percent",
    )

    mixture_standard = PropertyTypeAssignment(
        mandatory=False,
        code="MIXTURE_STANDARD",
        data_type="VARCHAR",
        property_label="Mixture standard",
        description="Standard and edition used to classify the mixture.",
    )

    mixture_designation = PropertyTypeAssignment(
        mandatory=False,
        code="MIXTURE_DESIGNATION",
        data_type="VARCHAR",
        property_label="Mixture designation",
        description="Designation of the mixture according to the specified standard.",
    )


class WeldingWireAlloy(Material):
    defs = ObjectTypeDef(
        code="WELDING_WIRE_ALLOY",
        description="""Standardized welding wire alloy names (all materials)""",
        generated_code_prefix="",
    )

    alias = PropertyTypeAssignment(
        mandatory=False,
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative name",
        description="Alternative name, abbreviation, or nickname for the welding wire alloy.",
    )

    material_group = PropertyTypeAssignment(
        mandatory=False,
        code="MATERIAL_GROUP",
        data_type="VARCHAR",
        property_label="Material group",
        description="Material group of the welding wire alloy.",
    )

    characteristics = PropertyTypeAssignment(
        mandatory=False,
        code="CHARACTERISTICS",
        data_type="VARCHAR",
        property_label="Characteristics",
        description="Characteristics of the welding wire alloy.",
    )

    notes = PropertyTypeAssignment(
        mandatory=False,
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="Additional notes about the welding wire alloy.",
    )

    alloy_standard = PropertyTypeAssignment(
        mandatory=False,
        code="ALLOY_STANDARD",
        data_type="VARCHAR",
        property_label="Alloy standard",
        description="Standard and edition used to classify the welding wire alloy.",
    )

    alloy_designation = PropertyTypeAssignment(
        mandatory=False,
        code="ALLOY_DESIGNATION",
        data_type="VARCHAR",
        property_label="Alloy designation",
        description="Designation of the welding wire alloy according to the specified standard.",
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

    laser_type = PropertyTypeAssignment(
        mandatory=False,
        code="LASER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Laser type",
        description="Type of laser source.",
        vocabulary_code="LASER_TYPES",
    )

    wavelength = PropertyTypeAssignment(
        mandatory=False,
        code="WAVELENGTH",
        data_type="REAL",
        property_label="Wavelength",
        description="Emission wavelength of the laser.",
        units="nm",
    )

    output_power_max = PropertyTypeAssignment(
        mandatory=False,
        code="OUTPUT_POWER_MAX",
        data_type="REAL",
        property_label="Maximum output power",
        description="Maximum continuous-wave optical output power.",
        units="kW",
    )

    output_power_min = PropertyTypeAssignment(
        mandatory=False,
        code="OUTPUT_POWER_MIN",
        data_type="REAL",
        property_label="Minimum output power",
        description="Minimum continuous-wave optical output power.",
        units="kW",
    )

    bpp = PropertyTypeAssignment(
        mandatory=False,
        code="BPP",
        data_type="REAL",
        property_label="Beam parameter product",
        description="Measure of the quality and focusability of the laser beam.",
        units="mm*mrad",
    )


class Pyrometer(Instrument):
    defs = ObjectTypeDef(
        code="PYROMETER",
        description="""A pyrometer""",
        generated_code_prefix="",
    )

    pyrometer_type = PropertyTypeAssignment(
        mandatory=False,
        code="PYROMETER_TYPE",
        data_type="VARCHAR",
        property_label="Pyrometer type",
        description="Measuring principle, such as single-color or two-color.",
    )

    temperature_min = PropertyTypeAssignment(
        mandatory=False,
        code="TEMPERATURE_MIN",
        data_type="REAL",
        property_label="Minimum temperature",
        description="Lower limit of the measurable temperature range.",
        units="degC",
    )

    temperature_max = PropertyTypeAssignment(
        mandatory=False,
        code="TEMPERATURE_MAX",
        data_type="REAL",
        property_label="Maximum temperature",
        description="Upper limit of the measurable temperature range.",
        units="degC",
    )

    spectral_range_min = PropertyTypeAssignment(
        mandatory=False,
        code="SPECTRAL_RANGE_MIN",
        data_type="REAL",
        property_label="Minimum spectral range",
        description="Lower wavelength limit used for measurement.",
        units="µm",
    )

    spectral_range_max = PropertyTypeAssignment(
        mandatory=False,
        code="SPECTRAL_RANGE_MAX",
        data_type="REAL",
        property_label="Maximum spectral range",
        description="Upper wavelength limit used for measurement.",
        units="µm",
    )

    response_time = PropertyTypeAssignment(
        mandatory=False,
        code="RESPONSE_TIME",
        data_type="REAL",
        property_label="Response time",
        description="Time required to respond to a temperature change.",
        units="ms",
    )

    emissivity_range_min = PropertyTypeAssignment(
        mandatory=False,
        code="EMISSIVITY_RANGE_MIN",
        data_type="REAL",
        property_label="Minimum emissivity",
        description="Lower limit of the adjustable emissivity range.",
        units="percent",
    )

    emissivity_range_max = PropertyTypeAssignment(
        mandatory=False,
        code="EMISSIVITY_RANGE_MAX",
        data_type="REAL",
        property_label="Maximum emissivity",
        description="Upper limit of the adjustable emissivity range.",
        units="percent",
    )


class LoadCell(Instrument):
    defs = ObjectTypeDef(
        code="LOAD_CELL",
        description="An instrument for measuring force.",
        generated_code_prefix="",
    )

    sensor_principle = PropertyTypeAssignment(
        mandatory=False,
        code="SENSOR_PRINCIPLE",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Measurement principle",
        description="Physical principle used to measure force.",
        vocabulary_code="SENSOR_PRINCIPLES",
    )

    nominal_force = PropertyTypeAssignment(
        mandatory=False,
        code="NOMINAL_FORCE",
        data_type="REAL",
        property_label="Nominal force",
        description="Rated force the load cell is designed to measure.",
        units="kN",
    )

    force_direction = PropertyTypeAssignment(
        mandatory=False,
        code="FORCE_DIRECTION",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Force direction",
        description="Permissible force measurement direction.",
        vocabulary_code="FORCE_DIRECTIONS",
    )


class LaserWeldOptic(Equipment):
    defs = ObjectTypeDef(
        code="LASER_WELD_OPTIC",
        description="""Welding head optic used for laser welding or cutting""",
        generated_code_prefix="",
    )

    collimation_focal_length = PropertyTypeAssignment(
        mandatory=False,
        code="COLLIMATION_FOCAL_LENGTH",
        data_type="REAL",
        property_label="Collimation focal length",
        description="Focal length of the lens that collimates the beam from the fiber.",
        units="mm",
    )

    focus_focal_length = PropertyTypeAssignment(
        mandatory=False,
        code="FOCUS_FOCAL_LENGTH",
        data_type="REAL",
        property_label="Focusing focal length",
        description="Focal length of the lens that focuses the beam onto the workpiece.",
        units="mm",
    )

    magnification_ratio = PropertyTypeAssignment(
        mandatory=False,
        code="MAGNIFICATION_RATIO",
        data_type="REAL",
        property_label="Magnification ratio",
        description="Ratio of focusing to collimation focal length.",
    )

    power_max = PropertyTypeAssignment(
        mandatory=False,
        code="POWER_MAX",
        data_type="REAL",
        property_label="Maximum laser power",
        description="Maximum continuous optical power permitted for the optic.",
        units="kW",
    )

    wavelength_range_min = PropertyTypeAssignment(
        mandatory=False,
        code="WAVELENGTH_RANGE_MIN",
        data_type="REAL",
        property_label="Minimum wavelength",
        description="Lower limit of the wavelength range for which the optic is optimized.",
        units="nm",
    )

    wavelength_range_max = PropertyTypeAssignment(
        mandatory=False,
        code="WAVELENGTH_RANGE_MAX",
        data_type="REAL",
        property_label="Maximum wavelength",
        description="Upper limit of the wavelength range for which the optic is optimized.",
        units="nm",
    )

    protective_window = PropertyTypeAssignment(
        mandatory=False,
        code="PROTECTIVE_WINDOW",
        data_type="BOOLEAN",
        property_label="Protective window",
        description="Whether a protective window is installed.",
    )

    protective_window_monitoring = PropertyTypeAssignment(
        mandatory=False,
        code="PROTECTIVE_WINDOW_MONITORING",
        data_type="BOOLEAN",
        property_label="Protective window monitoring",
        description="Whether protective window monitoring is available.",
    )

    crossjet = PropertyTypeAssignment(
        mandatory=False,
        code="CROSSJET",
        data_type="BOOLEAN",
        property_label="Crossjet",
        description="Whether a pneumatic crossjet is installed.",
    )

    camera_mount = PropertyTypeAssignment(
        mandatory=False,
        code="CAMERA_MOUNT",
        data_type="VARCHAR",
        property_label="Camera mount",
        description="Type of camera connection, such as C-mount.",
    )

    fiber_connector_type = PropertyTypeAssignment(
        mandatory=False,
        code="FIBER_CONNECTOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Fiber connector type",
        description="Type of laser fiber connector.",
        vocabulary_code="FIBER_CONNECTOR_TYPES",
    )


class LaserFiber(Equipment):
    defs = ObjectTypeDef(
        code="LASER_FIBER",
        description="""fiber for transporting a laser beam""",
        generated_code_prefix="",
    )

    fiber_diameter = PropertyTypeAssignment(
        mandatory=False,
        code="FIBER_DIAMETER",
        data_type="REAL",
        property_label="Fiber diameter",
        description="Core diameter of the laser fiber.",
        units="µm",
    )

    fiber_type = PropertyTypeAssignment(
        mandatory=False,
        code="FIBER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Fiber type",
        description="Type of laser fiber.",
        vocabulary_code="FIBER_TYPES",
    )

    connector_1 = PropertyTypeAssignment(
        mandatory=False,
        code="CONNECTOR_1",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Input connector",
        description="Type of the input connector.",
        vocabulary_code="FIBER_CONNECTOR_TYPES",
    )

    connector_2 = PropertyTypeAssignment(
        mandatory=False,
        code="CONNECTOR_2",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Output connector",
        description="Type of the output connector.",
        vocabulary_code="FIBER_CONNECTOR_TYPES",
    )

    numerical_aperture = PropertyTypeAssignment(
        mandatory=False,
        code="NUMERICAL_APERTURE",
        data_type="REAL",
        property_label="Numerical aperture",
        description="Measure of the fiber's acceptance angle.",
    )

    attenuation = PropertyTypeAssignment(
        mandatory=False,
        code="ATTENUATION",
        data_type="REAL",
        property_label="Attenuation",
        description="Optical power loss per unit length, in dB/km.",
    )

    material = PropertyTypeAssignment(
        mandatory=False,
        code="MATERIAL",
        data_type="VARCHAR",
        property_label="Material",
        description="Base material of the fiber core or its doping.",
    )

    length = PropertyTypeAssignment(
        mandatory=False,
        code="LENGTH",
        data_type="REAL",
        property_label="Fiber length",
        description="Length of the laser fiber.",
        units="m",
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
