#!/usr/bin/python2.4
#
# Copyright 2010 Google Inc. All Rights Reserved.

"""
"""

__author__ = 'hwasoolee@google.com.com (Hwasoo Lee)'

#Ebml Levels
LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVEL_4 = 4
LEVEL_5 = 5
LEVEL_6 = 6

#Ebml types
EBML_SUB_ELEMENT = 0
EBML_BINARY = 1
EBML_UINTEGER = 2
EBML_UTF8 = 3
EBML_FLOAT = 4
EBML_DATE = 5
EBML_STRING = 6
EBML_UINTEGER_1BIT = 7

#Ebml header
EBML = 0x1A45DFA3
EBML_VERSION = 0x4286
EBML_READ_VERSION = 0x42F7
EBML_MAX_ID_LENGTH = 0x42F2
EBML_MAX_SIZE_LENGTH = 0x42F3
EBML_DOC_TYPE = 0x4282
EBML_DOC_TYPE_VERSION = 0x4287
EBML_DOC_TYPE_READ_VERSION = 0x4285

#Global elements
CRC_32 = 0xBF
VOID = 0xEC

#Segment code
SEGMENT = 0x18538067

#Meta seek information codes
SEEKHEAD = 0x114D9B74
SEEK = 0x4DBB
SEEKID = 0x53AB
SEEKPOSITION = 0x53AC

#Segment info codes
SEGMENT_INFO = 0x1549A966
SEGMENTUID = 0x73A4
SEGMENTFILENAME = 0x7384
PREVUID = 0x3CB923
PREVFILENAME = 0x3C83AB
NEXTUID = 0x3EB923
NEXTFILENAME = 0x3E83BB
SEGMENTFAMILY = 0x4444
CHAPTERTRANSLATE = 0x6924
CHAPTERTRANSLATEEDITIONUID = 0x69FC
CHAPTERTRANSLATECODEC = 0x69BF
CHAPTERTRANSLATEID = 0x69A5
TIMECODESCALE = 0x2AD7B1
DURATION = 0x4489
DATEUTC = 0x4461
TITLE = 0x7BA9
MUXINGAPP = 0x4D80
WRITINGAPP = 0x5741

#Cluster codes
CLUSTER = 0x1F43B675
TIMECODE = 0xE7
SILENT_TRACKS = 0x5854
SILENT_TRACK_NUMBER = 0x58D7
POSITION = 0xA7
PREVSIZE = 0xAB
BLOCK_GROUP = 0xA0
BLOCK = 0xA1
BLOCK_ADDITIONS = 0x75A1
BLOCK_MORE = 0xA6
BLOCK_ADD_ID = 0xEE
BLOCK_ADDITIONAL = 0xA5
BLOCK_DURATION = 0x9B
REFERENCE_PRIORITY = 0xFA
REFERENCE_BLOCK = 0xFB
CODEC_STATE = 0xA4
SLICES = 0x8E
TIME_SLICE = 0xE8
LACE_NUMBER = 0xCC
SIMPLE_BLOCK = 0xA3

#Track codes
TRACKS = 0x1654AE6B
TRACK_ENTRY = 0xAE
TRACK_NUMBER = 0xD7
TRACK_UID = 0x73C5
TRACK_TYPE = 0x83
FLAG_ENABLED = 0xB9
FLAG_DEFAULT = 0x88
FLAG_FORCED = 0x55AA
FLAG_LACING = 0x9C
MIN_CACHE = 0x6DE7
MAX_CACHE = 0x6DF8
DEFAULT_DURATION = 0x23E383
TRACK_TIMECODE_SCALE = 0x23314F
MAX_BLOCK_ADDITION_ID = 0x55EE
NAME = 0x536E
LANGUAGE = 0x22B59C
CODEC_ID = 0x86
CODEC_PRIVATE = 0x63A2
CODEC_NAME = 0x258688
ATTACHMENT_LINK = 0x7446
CODEC_DECODE_ALL = 0xAA
TRACK_OVERLAY = 0x6FAB
TRACK_TRANSLATE = 0x6624
TRACK_TRANSLATE_EDITION_UID = 0x66FC
TRACK_TRANSLATE_CODEC = 0x66BF
TRACK_TRANSLATE_TRACK_ID = 0x66A5
VIDEO = 0xE0
FLAG_INTERLACED = 0x9A
STEREO_MODE = 0x53B8
PIXEL_WIDTH = 0xB0
PIXEL_HEIGHT = 0xBA
PIXEL_CROP_BOTTOM = 0x54AA
PIXEL_CROP_TOP = 0x54BB
PIXEL_CROP_LEFT = 0x54CC
PIXEL_CROP_RIGHT = 0x54DD
DISPLAY_WIDTH = 0x54B0
DISPLAY_HEIGHT = 0x54BA
COLOR_SPACE = 0x2EB524
FRAME_RATE = 0x2383E3
AUDIO = 0xE1
SAMPLING_FREQUENCY = 0xB5
OUTPUT_SAMPLING_FREQUENCY = 0x78B5
CHANNELS = 0x9F
BIT_DEPTH = 0x6264
CONTENT_ENCODINGS = 0x6D80
CONTENT_ENCODING = 0x6240
CONTENT_ENCODING_ORDER = 0x5031
CONTENT_ENCODING_SCOPE = 0x5032
CONTENT_ENCODING_TYPE = 0x5033
CONTENT_COMPRESSION = 0x5034
CONTENT_COMP_ALGO = 0x4254
CONTENT_COMP_SETTINGS = 0x4255
CONTENT_ENCRYPTION = 0x5035
CONTENT_ENC_ALGO = 0x47E1
CONTENT_ENC_KEY_ID = 0x47E2
CONTENT_SIGNATURE = 0x47E3
CONTENT_SIG_KEY_ID = 0x47E4
CONTENT_SIG_ALOG = 0x47E5
CONTENT_SIG_HASH_ALGO = 0x47E6

#Cueing data codes
CUES = 0x1C53BB6B
CUE_POINT = 0xBB
CUE_TIME = 0xB3
CUE_TRACK_POSITIONS = 0xB7
CUE_TRACK = 0xF7
CUE_CLUSTER_POSITION = 0xF1
CUE_BLOCK_NUMBER = 0x5378


ATTACHMENTS = 0x1941A469
ATTACHED_FILE = 0x61A7
FILE_DESCRIPTION = 0x467E
FILE_NAME = 0x466E
FILE_MIME_TYPE = 0x4660
FILE_DATA = 0x465C
FILE_UID = 0x46AE

CHAPTERS = 0x1043A770
EDITION_ENTRY = 0x45B9
EDITION_UID = 0x45BC
EDITION_FLAG_HIDDEN = 0x45BD
EDITION_FLAG_DEFAULT = 0x45DB
EDITION_FLAG_ORDERED = 0x45DD
CHAPTER_ATOM = 0xB6
CHAPTER_UID = 0x73C4
CHAPTER_TIME_START = 0x91
CHAPTER_TIME_END = 0x91
CHAPTER_FLAG_HIDDEN = 0x98
CHAPTER_FLAG_ENABLED = 0x4598
CHAPTER_SEGMENT_UID = 0x6E67
CHAPTER_SEGMENT_EDITION_UID = 0x6EBC
CHAPTER_PHYSICAL_EQUIV = 0x63C3
CHAPTER_TRACK = 0x8F
CHAPTER_TRACK_NUMBER = 0x89
CHAPTER_DISPLAY = 0x80
CHAP_STRING = 0x85
CHAP_LANGUAGE = 0x437C
CHAP_COUNTRY = 0x437E
CHAP_PROCESS = 0x6944
CHAP_PROCESS_CODEC_ID = 0x6955
CHAP_PROCESS_PRIVATE = 0x450D
CHAP_PROCESS_COMMAND = 0x6911
CHAP_PROCESS_TIME = 0x6922
CHAP_PROCESS_DATA = 0x6933

TAGS = 0x1254C367
TAG = 0x7373
TARGETS = 0x63C0
TARGET_TYPE_VALUE = 0x68CA
TARGET_TYPE = 0x63CA
#TRACK_UID = 0x63C5
EDITION_UID = 0x63C9
CHAPTER_UID = 0x63C4
ATTACHMENT_UID = 0x63C6
SIMPLE_TAG = 0x67C8
TAG_NAME = 0x45A3
TAG_LANGUAGE = 0x447A
TAG_DEFAULT = 0x4484
TAG_STRING = 0x4487
TAG_BINARY = 0x4485

seek_head_dic = {
      SEEKHEAD : ('SeekHead', LEVEL_1, EBML_SUB_ELEMENT),
      SEEK : ('Seek', LEVEL_1, EBML_SUB_ELEMENT),
      SEEKID : ('SeekId', LEVEL_2, EBML_BINARY),
      SEEKPOSITION : ('SeekPosition', LEVEL_3, EBML_UINTEGER),
      VOID : ('Void', LEVEL_1, EBML_BINARY)
    }

segment_info_dic = {
     SEGMENT_INFO : ('SegmentInfo', LEVEL_1, EBML_SUB_ELEMENT),
     SEGMENTUID : ('SegmentUID', LEVEL_2, EBML_BINARY),
     SEGMENTFILENAME : ('SegmentFilename', LEVEL_2, EBML_UTF8),
     PREVUID : ('PrevUID', LEVEL_2, EBML_BINARY),
     PREVFILENAME : ('PrevFilename', LEVEL_2, EBML_UTF8),
     NEXTUID : ('NextUID', LEVEL_2, EBML_BINARY),
     NEXTFILENAME : ('NextFilename', LEVEL_2, EBML_UTF8),
     SEGMENTFAMILY : ('SegmentFamily', LEVEL_2, EBML_BINARY),
     CHAPTERTRANSLATE : ('ChapterTranslate', LEVEL_2, EBML_SUB_ELEMENT),
     CHAPTERTRANSLATEEDITIONUID : ('ChapterTranslateEditionUID', LEVEL_3, EBML_UINTEGER),
     CHAPTERTRANSLATECODEC : ('ChapterTranslateCodec', LEVEL_3, EBML_UINTEGER),
     CHAPTERTRANSLATEID : ('ChapterTranslateID', LEVEL_3, EBML_BINARY),
     TIMECODESCALE : ('TimecodeScale', LEVEL_2, EBML_UINTEGER),
     DURATION : ('Duration', LEVEL_2, EBML_FLOAT),
     DATEUTC : ('DateUTC', LEVEL_2, EBML_DATE),
     TITLE : ('Title', LEVEL_2, EBML_UTF8),
     MUXINGAPP : ('MuxingApp', LEVEL_2, EBML_UTF8),
     WRITINGAPP : ('WritingApp', LEVEL_2, EBML_UTF8)
    }

track_dic = {
     TRACKS : ('Track', LEVEL_1, EBML_SUB_ELEMENT),
     TRACK_ENTRY : ('Track Entry', LEVEL_2, EBML_SUB_ELEMENT),
     TRACK_NUMBER : ('Track Number', LEVEL_3, EBML_UINTEGER),
     TRACK_UID : ('Track Uid', LEVEL_3, EBML_UINTEGER),
     TRACK_TYPE : ('Track Type', LEVEL_3, EBML_UINTEGER),
     FLAG_ENABLED : ('Flag Enabled', LEVEL_3, EBML_UINTEGER),
     FLAG_DEFAULT : ('Flag Default', LEVEL_3, EBML_UINTEGER),
     FLAG_FORCED :  ('Flag Forced', LEVEL_3, EBML_UINTEGER),
     FLAG_LACING :  ('Flag Lacing', LEVEL_3, EBML_UINTEGER),
     DEFAULT_DURATION : ('Default Duration', LEVEL_3, EBML_UINTEGER),
     NAME: ('Name', LEVEL_3, EBML_UTF8),
     LANGUAGE : ('Language', LEVEL_3, EBML_STRING),
     CODEC_ID : ('Codec Id', LEVEL_3, EBML_STRING),
     CODEC_PRIVATE : ('Codec Private', LEVEL_3, EBML_BINARY),
     CODEC_NAME : ('Codec Name', LEVEL_3, EBML_UTF8),
     VIDEO : ('Video', LEVEL_3, EBML_SUB_ELEMENT),
     FLAG_INTERLACED : ('Flag Interlaced', LEVEL_4, EBML_UINTEGER),
     PIXEL_WIDTH : ('Pixel Width', LEVEL_4, EBML_UINTEGER),
     PIXEL_HEIGHT : ('Pixel Height', LEVEL_4, EBML_UINTEGER),
     PIXEL_CROP_BOTTOM : ('Pixel Crop Bottom', LEVEL_4, EBML_UINTEGER),
     PIXEL_CROP_TOP : ('Pixel Crop Top', LEVEL_4, EBML_UINTEGER),
     PIXEL_CROP_LEFT : ('Pixel Crop Left', LEVEL_4, EBML_UINTEGER),
     PIXEL_CROP_RIGHT : ('Pixel Crop Right', LEVEL_4, EBML_UINTEGER),
     DISPLAY_WIDTH : ('Display Width', LEVEL_4, EBML_UINTEGER),
     DISPLAY_HEIGHT : ('Display Height', LEVEL_4, EBML_UINTEGER),
     FRAME_RATE : ('Frame Rate', LEVEL_4, EBML_FLOAT),
     AUDIO : ('Audio', LEVEL_3, EBML_SUB_ELEMENT),
     SAMPLING_FREQUENCY : ('Sampling Frequency', LEVEL_4, EBML_FLOAT),
     OUTPUT_SAMPLING_FREQUENCY : ('Output sampling Frequency', LEVEL_4,
                                  EBML_FLOAT),
     CHANNELS : ('Channels', LEVEL_4, EBML_UINTEGER),
     BIT_DEPTH : ('Bit Depth', LEVEL_4, EBML_UINTEGER),
     VOID : ('Void', LEVEL_1, EBML_BINARY),
     #not valid webm from here
     TRACK_TIMECODE_SCALE : ('Track Timecode Scale', LEVEL_3, EBML_FLOAT)
  }

cue_dic = {
      CUES : ('Cues', LEVEL_1, EBML_SUB_ELEMENT),
      CUE_POINT : ('Cue Point', LEVEL_2, EBML_SUB_ELEMENT),
      CUE_TIME : ('Cue Time', LEVEL_3, EBML_UINTEGER),
      CUE_TRACK_POSITIONS : ('Cue Track Positions', LEVEL_3, EBML_SUB_ELEMENT),
      CUE_TRACK : ('Cue Track', LEVEL_4, EBML_UINTEGER),
      CUE_CLUSTER_POSITION : ('Cue Cluster Position', LEVEL_4, EBML_UINTEGER),
      CUE_BLOCK_NUMBER : ('Cue Block Number', LEVEL_4, EBML_UINTEGER)
   }

cluster_dic = {
      CLUSTER : ('Cluster', LEVEL_1, EBML_SUB_ELEMENT),
      TIMECODE : ('TimeCode', LEVEL_2, EBML_UINTEGER),
      SILENT_TRACKS : ('SilentTracks', LEVEL_2, EBML_SUB_ELEMENT),
      SILENT_TRACK_NUMBER : ('SilentTrackNumber', LEVEL_3, EBML_UINTEGER),
      POSITION : ('Position', LEVEL_2, EBML_UINTEGER),
      PREVSIZE : ('PrevSize', LEVEL_2, EBML_UINTEGER),
      BLOCK_GROUP : ('BlockGroup', LEVEL_2, EBML_SUB_ELEMENT),
      BLOCK : ('Block', LEVEL_3, EBML_BINARY),
      BLOCK_ADDITIONS : ('BlockAdditions', LEVEL_3, EBML_SUB_ELEMENT),
      BLOCK_MORE : ('BlockMore', LEVEL_4, EBML_SUB_ELEMENT),
      BLOCK_ADD_ID : ('BlockAddId', LEVEL_5, EBML_UINTEGER),
      BLOCK_ADDITIONAL : ('BlockAdditional', LEVEL_5, EBML_BINARY),
      BLOCK_DURATION : ('BlockDuration', LEVEL_3, EBML_UINTEGER),
      REFERENCE_PRIORITY : ('ReferencePriority', LEVEL_3, EBML_UINTEGER),
      REFERENCE_BLOCK : ('ReferenceBlock', LEVEL_3, EBML_UINTEGER),
      CODEC_STATE : ('CodecState', LEVEL_3, EBML_BINARY),
      SLICES : ('Slices', LEVEL_3, EBML_SUB_ELEMENT),
      TIME_SLICE : ('TimeSlice', LEVEL_4, EBML_SUB_ELEMENT),
      LACE_NUMBER : ('LaceNumber', LEVEL_5, EBML_UINTEGER),
      SIMPLE_BLOCK : ('SimpleBlock', LEVEL_2, EBML_BINARY)
    }

dic_element = { SEEKHEAD : seek_head_dic, SEGMENT_INFO : segment_info_dic, TRACKS : track_dic,
               CUES : cue_dic, CLUSTER : cluster_dic }
