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
    RTX3050 = "9816_03+05+16+-+RTX+3050"
    RTX3060 = "9816_03+05+16+-+RTX+3060"
    RTX3060Ti = "9816_03+05+16+-+RTX+3060+Ti"
    RTX3070 = "9816_03+05+16+-+RTX+3070"
    RTX3070Ti = "9816_03+05+16+-+RTX+3070+Ti"
    RTX3080 = "9816_03+05+16+-+RTX+3080"
    RTX3080Ti = "9816_03+05+16+-+RTX+3080+Ti"
    RTX3090 = "9816_03+05+16+-+RTX+3090"
    RTX3090Ti = "9816_03+05+16+-+RTX+3090+Ti"
    RTX2060 = "9816_03+05+15+-+RTX+2060"
    RTX2070S = "9816_03+05+15+-+RTX+2070+SUPER"
    GTX1660S = "9816_03+04+15+-+GTX+1660+SUPER"
    RTX1660Ti = "9816_03+04+15+-+GTX+1660+Ti"
    GTX1660 = "9810_05+15+-+GTX+1660"
    GTX1650 = "9816_03+04+15+-+GTX+1650"


class SortingOptions(Enum):
    POPULARITY = "t"
    PRICE_LOWEST = "p"
    PRICE_HIGHEST = "-p"
