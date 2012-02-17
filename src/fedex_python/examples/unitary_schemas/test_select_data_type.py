# This file was generated by fedex_python.  You probably don't want to edit
# it since your modifications will be lost if fedex_plus is used to
# regenerate it.
from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Expr import *

####################
 # ENTITY weld #
####################
class weld(BaseEntityClass):
	'''Entity weld definition.

	:param composition
	:type composition:STRING
	'''
	def __init__( self , composition, ):
		self.composition = composition

	@apply
	def composition():
		def fget( self ):
			return self._composition
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument composition is mantatory and can not be set to None')
			check_type(value,STRING)
			self._composition = value
		return property(**locals())

####################
 # ENTITY glue #
####################
class glue(BaseEntityClass):
	'''Entity glue definition.

	:param composition
	:type composition:STRING

	:param solvent
	:type solvent:STRING
	'''
	def __init__( self , composition,solvent, ):
		self.composition = composition
		self.solvent = solvent

	@apply
	def composition():
		def fget( self ):
			return self._composition
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument composition is mantatory and can not be set to None')
			check_type(value,STRING)
			self._composition = value
		return property(**locals())

	@apply
	def solvent():
		def fget( self ):
			return self._solvent
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument solvent is mantatory and can not be set to None')
			check_type(value,STRING)
			self._solvent = value
		return property(**locals())

####################
 # ENTITY wall_mounting #
####################
class wall_mounting(BaseEntityClass):
	'''Entity wall_mounting definition.

	:param mounting
	:type mounting:STRING

	:param on
	:type on:STRING

	:param using
	:type using:attachment_method
	'''
	def __init__( self , mounting,on,using, ):
		self.mounting = mounting
		self.on = on
		self.using = using

	@apply
	def mounting():
		def fget( self ):
			return self._mounting
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument mounting is mantatory and can not be set to None')
			check_type(value,STRING)
			self._mounting = value
		return property(**locals())

	@apply
	def on():
		def fget( self ):
			return self._on
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument on is mantatory and can not be set to None')
			check_type(value,STRING)
			self._on = value
		return property(**locals())

	@apply
	def using():
		def fget( self ):
			return self._using
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument using is mantatory and can not be set to None')
			check_type(value,attachment_method)
			self._using = value
		return property(**locals())

####################
 # ENTITY screw #
####################
class screw(BaseEntityClass):
	'''Entity screw definition.

	:param body_length
	:type body_length:REAL

	:param pitch
	:type pitch:REAL
	'''
	def __init__( self , body_length,pitch, ):
		self.body_length = body_length
		self.pitch = pitch

	@apply
	def body_length():
		def fget( self ):
			return self._body_length
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument body_length is mantatory and can not be set to None')
			check_type(value,REAL)
			self._body_length = value
		return property(**locals())

	@apply
	def pitch():
		def fget( self ):
			return self._pitch
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument pitch is mantatory and can not be set to None')
			check_type(value,REAL)
			self._pitch = value
		return property(**locals())

####################
 # ENTITY nail #
####################
class nail(BaseEntityClass):
	'''Entity nail definition.

	:param body_length
	:type body_length:REAL

	:param head_area
	:type head_area:REAL
	'''
	def __init__( self , body_length,head_area, ):
		self.body_length = body_length
		self.head_area = head_area

	@apply
	def body_length():
		def fget( self ):
			return self._body_length
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument body_length is mantatory and can not be set to None')
			check_type(value,REAL)
			self._body_length = value
		return property(**locals())

	@apply
	def head_area():
		def fget( self ):
			return self._head_area
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument head_area is mantatory and can not be set to None')
			check_type(value,REAL)
			self._head_area = value
		return property(**locals())
# SELECT TYPE permanent_attachment
permanent_attachment=SELECT([glue,weld])
# SELECT TYPE temporary_attachment
temporary_attachment=SELECT([nail,screw])
# SELECT TYPE attachment_method
attachment_method=SELECT([permanent_attachment,temporary_attachment])
