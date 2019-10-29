from ctypes import cdll, c_char_p, c_void_p
from pyenergyplus.common import RealEP


class Glycol:
    """
    This class is a Python representation of the glycol properties calculations inside EnergyPlus.
    For now, the only glycol name allowed is plain water.  This is because other fluids are only
    initialized when they are declared in the input file.  When calling this way, through the API,
    there is no input file, so no other fluids are declared.  This is ripe for a refactor to enable
    additional fluids, but water will suffice for now as an example.
    """

    def __init__(self, api: cdll, glycol_name: bytes):
        self.api = api
        self.api.glycolNew.argtypes = [c_char_p]
        self.api.glycolNew.restype = c_void_p
        self.api.glycolDelete.argtypes = [c_void_p]
        self.api.glycolDelete.restype = c_void_p
        self.api.glycolSpecificHeat.argtypes = [c_void_p, RealEP]
        self.api.glycolSpecificHeat.restype = RealEP
        self.api.glycolDensity.argtypes = [c_void_p, RealEP]
        self.api.glycolDensity.restype = RealEP
        self.api.glycolConductivity.argtypes = [c_void_p, RealEP]
        self.api.glycolConductivity.restype = RealEP
        self.api.glycolViscosity.argtypes = [c_void_p, RealEP]
        self.api.glycolViscosity.restype = RealEP
        self.instance = self.api.glycolNew(glycol_name)

    def __del__(self):
        self.api.glycolDelete(self.instance)

    def specific_heat(self, temperature: float) -> float:
        return self.api.glycolSpecificHeat(self.instance, temperature)

    def density(self, temperature: float) -> float:
        return self.api.glycolDensity(self.instance, temperature)

    def conductivity(self, temperature: float) -> float:
        return self.api.glycolConductivity(self.instance, temperature)

    def viscosity(self, temperature: float) -> float:
        return self.api.glycolViscosity(self.instance, temperature)


class Refrigerant:

    def __init__(self, api: cdll, refrigerant_name: bytes):
        self.refrigerant_name = refrigerant_name
        self.api = api
        self.api.refrigerantNew.argtypes = [c_char_p]
        self.api.refrigerantNew.restype = c_void_p
        self.api.refrigerantDelete.argtypes = [c_void_p]
        self.api.refrigerantDelete.restype = c_void_p
        self.api.refrigerantSaturationPressure.argtypes = [c_void_p, RealEP]
        self.api.refrigerantSaturationPressure.restype = RealEP
        self.api.refrigerantSaturationTemperature.argtypes = [c_void_p, RealEP]
        self.api.refrigerantSaturationTemperature.restype = RealEP
        self.api.refrigerantSaturatedEnthalpy.argtypes = [c_void_p, RealEP, RealEP]
        self.api.refrigerantSaturatedEnthalpy.restype = RealEP
        self.api.refrigerantSaturatedDensity.argtypes = [c_void_p, RealEP, RealEP]
        self.api.refrigerantSaturatedDensity.restype = RealEP
        self.api.refrigerantSaturatedSpecificHeat.argtypes = [c_void_p, RealEP, RealEP]
        self.api.refrigerantSaturatedSpecificHeat.restype = RealEP
        self.instance = self.api.refrigerantNew(refrigerant_name)

    def __del__(self):
        self.api.refrigerantDelete(self.instance)

    def saturation_pressure(self, temperature: float) -> float:
        return self.api.refrigerantSaturationPressure(temperature)

    def saturation_temperature(self, pressure: float) -> float:
        return self.api.refrigerantSaturationTemperature(pressure)

    def saturated_enthalpy(self, temperature: float, quality: float):
        return self.api.refrigerantSaturatedEnthalpy(temperature, quality)

    def saturated_density(self, temperature: float, quality: float):
        return self.api.refrigerantSaturatedDensity(temperature, quality)

    def saturated_specific_heat(self, temperature: float, quality: float):
        return self.api.refrigerantSaturatedSpecificHeat(temperature, quality)


class Psychrometrics:
    """

    """
    def __init__(self, api: cdll):
        self.api = api
        self.api.psyRhoFnPbTdbW.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyRhoFnPbTdbW.restype = RealEP
        self.api.psyHfgAirFnWTdb.argtypes = [RealEP]
        self.api.psyHfgAirFnWTdb.restype = RealEP
        self.api.psyHgAirFnWTdb.argtypes = [RealEP]
        self.api.psyHgAirFnWTdb.restype = RealEP
        self.api.psyHFnTdbW.argtypes = [RealEP, RealEP]
        self.api.psyHFnTdbW.restype = RealEP
        self.api.psyCpAirFnWTdb.argtypes = [RealEP, RealEP]
        self.api.psyCpAirFnWTdb.restype = RealEP
        self.api.psyTdbFnHW.argtypes = [RealEP, RealEP]
        self.api.psyTdbFnHW.restype = RealEP
        self.api.psyRhovFnTdbWPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyRhovFnTdbWPb.restype = RealEP
        self.api.psyTwbFnTdbWPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyTwbFnTdbWPb.restype = RealEP
        self.api.psyVFnTdbWPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyVFnTdbWPb.restype = RealEP
        self.api.psyWFnTdbH.argtypes = [RealEP, RealEP]
        self.api.psyWFnTdbH.restype = RealEP
        self.api.psyPsatFnTemp.argtypes = [RealEP]
        self.api.psyPsatFnTemp.restype = RealEP
        self.api.psyTsatFnHPb.argtypes = [RealEP, RealEP]
        self.api.psyTsatFnHPb.restype = RealEP
        self.api.psyRhovFnTdbRh.argtypes = [RealEP, RealEP]
        self.api.psyRhovFnTdbRh.restype = RealEP
        self.api.psyRhFnTdbRhov.argtypes = [RealEP, RealEP]
        self.api.psyRhFnTdbRhov.restype = RealEP
        self.api.psyRhFnTdbWPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyRhFnTdbWPb.restype = RealEP
        self.api.psyWFnTdpPb.argtypes = [RealEP, RealEP]
        self.api.psyWFnTdpPb.restype = RealEP
        self.api.psyWFnTdbRhPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyWFnTdbRhPb.restype = RealEP
        self.api.psyWFnTdbTwbPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyWFnTdbTwbPb.restype = RealEP
        self.api.psyHFnTdbRhPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyHFnTdbRhPb.restype = RealEP
        self.api.psyTdpFnWPb.argtypes = [RealEP, RealEP]
        self.api.psyTdpFnWPb.restype = RealEP
        self.api.psyTdpFnTdbTwbPb.argtypes = [RealEP, RealEP, RealEP]
        self.api.psyTdpFnTdbTwbPb.restype = RealEP

    def density(self, barometric_pressure: float, dry_bulb_temp: float, humidity_ratio: float) -> float:
        return self.api.psyRhoFnPbTdbW(barometric_pressure, dry_bulb_temp, humidity_ratio)

    def latent_energy_of_air(self, dry_bulb_temp: float) -> float:
        return self.api.psyHfgAirFnWTdb(dry_bulb_temp)

    def latent_energy_of_moisture_in_air(self, dry_bulb_temp: float) -> float:
        return self.api.psyHgAirFnWTdb(dry_bulb_temp)

    def enthalpy(self, dry_bulb_temp: float, humidity_ratio: float) -> float:
        return self.api.psyHFnTdbW(dry_bulb_temp, humidity_ratio)

    def enthalpy_b(self, dry_bulb_temp: float, relative_humidity_fraction: float, barometric_pressure: float) -> float:
        return self.api.psyHFnTdbRhPb(dry_bulb_temp, relative_humidity_fraction, barometric_pressure)

    def specific_heat(self, humidity_ratio: float, dry_bulb_temp: float) -> float:
        return self.api.psyCpAirFnWTdb(humidity_ratio, dry_bulb_temp)

    def dry_bulb(self, enthalpy: float, humidity_ratio: float) -> float:
        return self.api.psyTdbFnHW(enthalpy, humidity_ratio)

    def vapor_density(self, dry_bulb_temp: float, humidity_ratio: float, barometric_pressure: float) -> float:
        return self.api.psyRhovFnTdbWPb(dry_bulb_temp, humidity_ratio, barometric_pressure)

    def relative_humidity(self, dry_bulb_temp: float, vapor_density: float) -> float:
        return self.api.psyRhFnTdbRhov(dry_bulb_temp, vapor_density)

    def relative_humidity_b(self, dry_bulb_temp: float, humidity_ratio: float, barometric_pressure: float) -> float:
        return self.api.psyRhFnTdbWPb(dry_bulb_temp, humidity_ratio, barometric_pressure)

    def wet_bulb(self, dry_bulb_temp: float, humidity_ratio: float, barometric_pressure: float) -> float:
        return self.api.psyTwbFnTdbWPb(dry_bulb_temp, humidity_ratio, barometric_pressure)

    def specific_volume(self, dry_bulb_temp: float, humidity_ratio: float, barometric_pressure: float) -> float:
        return self.api.psyVFnTdbWPb(dry_bulb_temp, humidity_ratio, barometric_pressure)

    def saturation_pressure(self, dry_bulb_temp: float) -> float:
        return self.api.psyPsatFnTemp(dry_bulb_temp)

    def saturation_temperature(self, enthalpy: float, barometric_pressure: float) -> float:
        return self.api.psyTsatFnHPb(enthalpy, barometric_pressure)

    def vapor_density_b(self, dry_bulb_temp: float, relative_humidity_fraction: float) -> float:
        return self.api.psyRhovFnTdbRh(dry_bulb_temp, relative_humidity_fraction)

    def humidity_ratio(self, dry_bulb_temp: float, enthalpy: float) -> float:
        return self.api.psyWFnTdbH(dry_bulb_temp, enthalpy)

    def humidity_ratio_b(self, dew_point_temp: float, barometric_pressure: float) -> float:
        return self.api.psyWFnTdpPb(dew_point_temp, barometric_pressure)

    def humidity_ratio_c(self, dry_bulb_temp: float, relative_humidity_fraction: float, barometric_pressure: float) -> float:
        return self.api.psyWFnTdbRhPb(dry_bulb_temp, relative_humidity_fraction, barometric_pressure)

    def humidity_ratio_d(self, dry_bulb_temp: float, wet_bulb_temp: float, barometric_pressure: float) -> float:
        return self.api.psyWFnTdbTwbPb(dry_bulb_temp, wet_bulb_temp, barometric_pressure)

    def dew_point(self, humidity_ratio: float, barometric_pressure: float) -> float:
        return self.api.psyTdpFnWPb(humidity_ratio, barometric_pressure)

    def dew_point_b(self, dry_bulb_temp: float, wet_bulb_temp: float, barometric_pressure: float) -> float:
        return self.api.psyTdpFnTdbTwbPb(dry_bulb_temp, wet_bulb_temp, barometric_pressure)


class EnergyPlusVersion:
    """
    This is the EnergyPlus version.  Could also call into the DLL but it's the same effect.

    """
    def __init__(self):
        self.ep_version_major = int("${CMAKE_VERSION_MAJOR}")
        self.ep_version_minor = int("${CMAKE_VERSION_MINOR}")
        self.ep_version_patch = int("${CMAKE_VERSION_PATCH}")
        self.ep_version_build = str("${CMAKE_VERSION_BUILD}")

    def __str__(self) -> str:
        return "%s.%s.%s-%s" % (
            self.ep_version_major, self.ep_version_minor, self.ep_version_patch, self.ep_version_build
        )


class Functional:
    """
    This API class enables accessing structures and functionality inside EnergyPlus from an outside client.
    This functional API will be extended over time, but initial targeted functionality includes fluid and refrigerant
    property methods, and surface and geometry classes and methods.

    The Functional API class itself is really just an organizational class that provides access to nested functional
    classes through member functions.  The functional API class is instantiated by the higher level EnergyPlusAPI class,
    and clients should *never* attempt to create an instance manually.  Instead, create an EnergyPlusAPI instance, and
    call the `functional()` member function to create a Functional class instance.  For Python Plugin workflows, the
    EnergyPlusPlugin base class also provides an instance of the Functional base class through the `self.functional`
    member variable.  Clients should use that directly when needing to make functional calls into the library.
    """

    def __init__(self, api: cdll, running_as_python_plugin: bool = False):
        self.api = api
        self.api.initializeFunctionalAPI.argtypes = []
        self.api.initializeFunctionalAPI.restype = c_void_p
        if not running_as_python_plugin:
            self.api.initializeFunctionalAPI()

    def glycol(self, glycol_name: str) -> Glycol:
        """
        Returns a Glycol instance, which allows calculation of glycol properties.

        :param glycol_name: Name of the Glycol, for now only water is allowed
        :return: An instantiated Glycol structure
        """
        if isinstance(glycol_name, str):
            glycol_name = glycol_name.encode('utf-8')
        return Glycol(self.api, glycol_name)

    def refrigerant(self, refrigerant_name: str) -> Refrigerant:
        """
        Returns a Refrigerant instance, which allows calculation of refrigerant properties.

        :param refrigerant_name: Name of the Refrigerant, for now only steam is allowed
        :return: An instantiated Refrigerant structure
        """
        if isinstance(refrigerant_name, str):
            refrigerant_name = refrigerant_name.encode('utf-8')
        return Refrigerant(self.api, refrigerant_name)

    def psychrometrics(self) -> Psychrometrics:
        """
        Returns a Psychrometric instance, which allows calculation of psychrometric properties.

        :return: An instantiated Psychrometric structure
        """
        return Psychrometrics(self.api)

    @staticmethod
    def ep_version() -> EnergyPlusVersion:
        return EnergyPlusVersion()
