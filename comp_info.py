import os
import sys

def cpuInfo():
    print("CPU Info: Inforamation about the cpu and processing units. \n")
    os.system("lscpu")

def hwlist():
    print("\n\n\nHardware List: Details and brief information about multiple different hardware units such as cpu, memory, disk, usb controllers, network adapters etc.\n")
    os.system("lshw -short")

def hwInfo():
    print("\n\n\nHardware Info: Detailed and brief information about hardware\n")
    os.system("hwinfo --short")

def pciInfo():
    print("\n\n\nPCI Info: List of all the pci buses and details about the devices connected to them.\n")
    os.system("lspci")

def usbInfo():
    print("\n\n\nUSB Info: USB controllers and details about devices connected to them\n")
    os.system("lsusb")

def loginInfo():
    print("\n\n\nLogin Info: \n")
    os.system("lslogins")

def scsiDevices():
    print("\n\n\nList of the scsi/sata devices like hard drives and optical drives\n")
    os.system("lsscsi")

cpuInfo()
hwlist()
hwInfo()
pciInfo()
usbInfo()
loginInfo()
scsiDevices()
