# -*- coding: utf-8 -*-

"""FSInfo structure handling for FAT32 filesystems."""


class FSInfo:
    #: Magic value at the start of an FSInfo struct
    LEAD_SIG_MAGIC = 0x41615252
    #: Magic value at the end of an FSInfo struct
    TRAIL_SIG_MAGIC = 0xAA550000

    #: BPB header layout in struct formatted string
    fsinfo_header_layout = "<L480x"
    #: BPB header fields when extracted with bpb_header_layout
    fsinfo_header_vars = ["BS_jmpBoot", "BS_OEMName", "BPB_BytsPerSec",
                       "BPB_SecPerClus", "BPB_RsvdSecCnt", "BPB_NumFATS",
                       "BPB_RootEntCnt", "BPB_TotSec16", "BPB_Media",
                       "BPB_FATSz16", "BPB_SecPerTrk", "BPB_NumHeads",
                       "BPB_HiddSec", "BPB_TotSec32"]

    @staticmethod
    def from_bytes(data: bytes) -> "FSInfo":
        """Deserialize FSInfo binary data into FSInfo class instance.

        :param data: `bytes`: 512 bytes of binary data to be deserialized
        """

