from enum import Enum


class BaseURL(Enum):
    DE_DOMAIN = "https://geizhals.de/"
    AT_DOMAIN = "https://geizhals.at/"
    EU_DOMAIN = "https://geizhals.eu/"
    PL_DOMAIN = "https://cenowarka.pl/"
    UK_DOMAIN = "https://skinflint.co.uk/"


class CathegoryKeywords(Enum):
    GPU_PCIE = "gra16_512"
    CPU_AMD = "cpuamdam4"
    CPU_INTEL = "cpu1151"
    SSD = "hdssd"
    EXTERN_HDD = "hdx"
    HDD = "hde7s"
    MONITOR = "monlcd19wide"
    HEADPHONE = "sphd"
    MB_AMD_AM4 = "mbam4"
    MB_INTEL_1700 = "mbp4_1700"
    MB_INTEL_1200 = "mbp4_1200"
    PC_CASE = "gehatx"
    MOUSE = "mouse"
    MOUSE_PAD = "egpads"
    KEYBOARD = "kb"
    CONTROLLER = "eggamepad"
    RAM = "ramddr3"
    TABLET_PC = "nbtabl"
    NOTEBOOK = "nb"
    CPU_COOLER = "cpucooler"
    COOLING_FAN = "coolfan"
    THERMAL_COMPOUND = "cooltc"
    POWER_SUPPLY = "gehps"
    WATER_COOLING_SET = "coolwsets"
    NAS = "hdxnas"
    USB_STICK = "sm_usb"
    PRINTER_3D = "dr3d"


class Currencies(Enum):
    EURO = "euro"
    DOLLAR = "dollar"
    PLN = "PLN"
    POUND = "pound"
    UNKNOWN = "unknown"


class NvidiaGPUs(Enum):
    RTX3050 = "RTX 3050"
    RTX3060 = "RTX 3060"
    RTX3060Ti = "RTX 3060 Ti"
    RTX3070 = "RTX 3070"
    RTX3070Ti = "RTX 3070 Ti"
    RTX3080 = "RTX 3080"
    RTX3080Ti = "RTX 3080 Ti"
    RTX3090 = "RTX 3090"
    RTX3090Ti = "RTX 3090 Ti"
    RTX2060 = "RTX 2060"
    GTX1660S = "GTX 1660 Super"
    RTX1660Ti = "GTX 1660 Ti"
    GTX1660 = "GTX 1660"
    GTX1650 = "GTX 1650"
