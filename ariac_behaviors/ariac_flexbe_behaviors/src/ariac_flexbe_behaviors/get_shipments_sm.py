#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.get_products_sm import get_productsSM
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_behaviors.notify_shipment_ready_sm import notify_shipment_readySM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Apr 19 2020
@author: Gerard Harkema
'''
class get_shipmentsSM(Behavior):
	'''
	Tests the starting and stopping of the assignment

This example is a part of the order example.
	'''


	def __init__(self):
		super(get_shipmentsSM, self).__init__()
		self.name = 'get_shipments'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(get_productsSM, 'get_products')
		self.add_behavior(notify_shipment_readySM, 'DeliverShipment')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1381 y:133, x:931 y:389
		_state_machine = OperatableStateMachine(outcomes=['finished', 'fail'], input_keys=['Shipments', 'NumberOfShipments'])
		_state_machine.userdata.Shipments = []
		_state_machine.userdata.NumberOfShipments = 0
		_state_machine.userdata.Products = []
		_state_machine.userdata.NumberOfProducts = 0
		_state_machine.userdata.AgvID = ''
		_state_machine.userdata.ShipmentIndex = 1
		_state_machine.userdata.ShipmentType = ''
		_state_machine.userdata.ShipmentIterator = 0
		_state_machine.userdata.OneValue = 1
		_state_machine.userdata.agv_id = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:43 y:24
			OperatableStateMachine.add('GetProducts',
										GetProductsFromShipmentState(),
										transitions={'continue': 'agv id', 'invalid_index': 'fail'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'Shipments', 'index': 'ShipmentIterator', 'shipment_type': 'ShipmentType', 'agv_id': 'AgvID', 'products': 'Products', 'number_of_products': 'NumberOfProducts'})

			# x:914 y:32
			OperatableStateMachine.add('IncrementShipmentsIterator',
										AddNumericState(),
										transitions={'done': 'CompareShepmentsIterator'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'ShipmentIterator', 'value_b': 'OneValue', 'result': 'ShipmentIterator'})

			# x:910 y:138
			OperatableStateMachine.add('CompareShepmentsIterator',
										EqualState(),
										transitions={'true': 'DeliverShipment', 'false': 'GetProducts'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'ShipmentIterator', 'value_b': 'NumberOfShipments'})

			# x:730 y:26
			OperatableStateMachine.add('get_products',
										self.use_behavior(get_productsSM, 'get_products'),
										transitions={'finished': 'IncrementShipmentsIterator', 'fail': 'fail'},
										autonomy={'finished': Autonomy.Inherit, 'fail': Autonomy.Inherit},
										remapping={'Products': 'Products', 'NumberOfProducts': 'NumberOfProducts', 'agv_id': 'agv_id'})

			# x:549 y:20
			OperatableStateMachine.add('agv id',
										ReplaceState(),
										transitions={'done': 'get_products'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'AgvID', 'result': 'agv_id'})

			# x:1138 y:100
			OperatableStateMachine.add('DeliverShipment',
										self.use_behavior(notify_shipment_readySM, 'DeliverShipment'),
										transitions={'finished': 'finished', 'failed': 'fail'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
