from bam_masterdata.datamodel.object_types import WeldingEquipment
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class GasNozzel(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.GAS_NOZZEL",
        description="""A gas nozzel used to supply shielding gas to the welding zone or other welding related sections//Gasdüse zur Zuführung von Schutzgas zum Prozessbereich oder anderen Sektionen beim Schweißen""",
        generated_code_prefix="INS.WLD_EQP.GAS_NZL",
    )

    gas_nozzel_outflow_diameter = PropertyTypeAssignment(
        code="GAS_NOZZEL.OUTFLOW_DIAMETER",
        data_type="REAL",
        property_label="Outflow Diameter",
        units="mm",
        description="""Diameter of the outflow opening of the gas nozzel in [mm]//Durchmesser der Austrittsöffnung der Gasdüse in [mm]""",
        mandatory=False,
        show_in_edit_views=True,
        section="Dimensions",
    )

    gas_nozzel_length = PropertyTypeAssignment(
        code="GAS_NOZZEL.LENGTH",
        data_type="REAL",
        property_label="Length",
        units="mm",
        description="""Total length of the gas nozzel in [mm]//Gesamtlänge der Gasdüse in [mm]""",
        mandatory=False,
        show_in_edit_views=True,
        section="Dimensions",
    )

    gas_nozzel_thread = PropertyTypeAssignment(
        code="GAS_NOZZEL.THREAD",
        data_type="STRING",
        property_label="Thread",
        description="""THread description of the gas nozzel connector section//Gewindebeschreibung des Gasdüsenanschlusses""",
        mandatory=False,
        show_in_edit_views=True,
        section="Dimensions",
    )


class ContactTip(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.CONTACT_TIP",
        description=""" """,
        generated_code_prefix="INS.WLD_EQP.CNTCT_TIP",
    )

    contact_tip_wire_bore_diameter = PropertyTypeAssignment(
        code="CONTACT_TIP.WIRE_BORE_DIAMETER",
        data_type="REAL",
        property_label="Wire Diameter",
        units="mm",
        description="""Bore diameter of the wire in [mm]//Lochdurchmesser für die Drahtführung in [mm]""",
    )

    contact_tip_material_alloy = PropertyTypeAssignment(
        code="CONTACT_TIP.MATERIAL_ALLOY",
        data_type="STRING",
        property_label="Material Alloy",
        units="",
        description="""Base material or alloy of the tip (e.g., E-Cu, CuCrZr, DSC, DHP); affects conductivity, hardness and thermal performance//Grundmaterial oder Legierung der Stromdüse (z. B. E-Cu, CuCrZr, DSC, DHP); beeinflusst Leitfähigkeit, Härte und thermische Belastbarkeit""",
    )

    contact_tip_plating_coating = PropertyTypeAssignment(
        code="CONTACT_TIP.PLATING_COATING",
        data_type="STRING",
        property_label="Plating or Coating",
        units="",
        description="""Surface finish or coating applied to improve spatter resistance and electrical contact (e.g., nickel, silver)//Oberflächenbeschichtung zur Verbesserung der Spritzerbeständigkeit und elektrischen Kontaktqualität (z. B. Nickel, Silber)""",
    )

    contact_tip_thread_type = PropertyTypeAssignment(
        code="CONTACT_TIP.THREAD_TYPE",
        data_type="STRING",
        property_label="Thread Type",
        units="",
        description="""Thread specification for mounting (e.g., M6, M8, M10)//Gewindespezifikation für die Montage (z. B. M6, M8, M10)""",
    )

    contact_tip_overall_length = PropertyTypeAssignment(
        code="CONTACT_TIP.OVERALL_LENGTH",
        data_type="REAL",
        property_label="Overall Length",
        units="mm",
        description="""Total length of the contact tip in [mm]//Gesamtlänge der Stromdüse in mm""",
    )

    # contact_tip_outer_diameter = PropertyTypeAssignment(
    #     code="CONTACT_TIP.OUTER_DIAMETER",
    #     data_type="REAL",
    #     property_label="Tip Outer Diameter",
    #     units="mm",
    #     description="""Outer diameter of the tip body; determines mechanical fit in nozzle and holder//Außendurchmesser der Stromdüse; bestimmt die mechanische Passung in Gasdüse und Halter""",
    # )

    # contact_tip_inner_geometry = PropertyTypeAssignment(
    #     code="CONTACT_TIP.INNER_GEOMETRY",
    #     data_type="ENUM",
    #     property_label="Inner Geometry",
    #     units="",
    #     description="""Internal bore geometry (round, star, fluted) influencing wire contact and wear behaviour//Innere Bohrungsgeometrie (rund, sternförmig, gerillt), beeinflusst Drahtkontakt und Verschleißverhalten""",
    # )

    contact_tip_rated_current = PropertyTypeAssignment(
        code="CONTACT_TIP.RATED_CURRENT",
        data_type="REAL",
        property_label="Rated Current",
        units="A",
        description="""Continuous current rating in amperes; indicates thermal and electrical limits//Dauerstrombelastbarkeit in Ampere; zeigt thermische und elektrische Grenzen an""",
    )

    # contact_tip_hardness = PropertyTypeAssignment(
    #     code="CONTACT_TIP.HARDNESS",
    #     data_type="REAL",
    #     property_label="Hardness",
    #     units="HV",
    #     description="""Material hardness in Vickers (HV); correlates with wear resistance//Materialhärte nach Vickers (HV); korreliert mit Verschleißbeständigkeit""",
    # )

    # contact_tip_thermal_softening_temp = PropertyTypeAssignment(
    #     code="CONTACT_TIP.THERMAL_SOFTENING_TEMPERATURE",
    #     data_type="REAL",
    #     property_label="Thermal Softening Temperature",
    #     units="°C",
    #     description="""Temperature at which material begins to soften; critical for high‑duty welding//Temperatur, bei der das Material zu erweichen beginnt; entscheidend für Hochleistungs-Schweißprozesse""",
    # )

    # contact_tip_spatter_resistance = PropertyTypeAssignment(
    #     code="CONTACT_TIP.SPATTER_RESISTANCE",
    #     data_type="ENUM",
    #     property_label="Spatter Resistance",
    #     units="",
    #     description="""Qualitative measure of resistance to weld spatter accumulation//Qualitative Bewertung der Beständigkeit gegenüber Schweißspritzern""",
    # )

    # contact_tip_service_life_estimate = PropertyTypeAssignment(
    #     code="CONTACT_TIP.SERVICE_LIFE_ESTIMATE",
    #     data_type="REAL",
    #     property_label="Service Life Estimate",
    #     units="hours",
    #     description="""Estimated operational life under defined conditions (hours or wire‑meters)//Geschätzte Einsatzdauer unter definierten Bedingungen (Stunden oder Drahtmeter)""",
    # )

    # contact_tip_compatible_wire_types = PropertyTypeAssignment(
    #     code="CONTACT_TIP.COMPATIBLE_WIRE_TYPES",
    #     data_type="STRING",
    #     property_label="Compatible Wire Types",
    #     units="",
    #     description="""List of compatible wire types (solid, flux‑cored, stainless, aluminium)//Liste kompatibler Drahttypen (Massivdraht, Fülldraht, Edelstahl, Aluminium)""",
    # )
