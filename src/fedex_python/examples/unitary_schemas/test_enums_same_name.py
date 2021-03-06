# This file was generated by fedex_python.  You probably don't want to edit
# it since your modifications will be lost if fedex_plus is used to
# regenerate it.
import sys

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Builtin import *
from SCL.Rules import *

schema_name = 'test_enums_same_name'

schema_scope = sys.modules[__name__]


# ENUMERATION TYPE hair_color
hair_color = ENUMERATION(
	'bald',
	'red',
	scope = schema_scope)

# ENUMERATION TYPE favorite_color
favorite_color = ENUMERATION(
	'clear',
	'red',
	scope = schema_scope)
