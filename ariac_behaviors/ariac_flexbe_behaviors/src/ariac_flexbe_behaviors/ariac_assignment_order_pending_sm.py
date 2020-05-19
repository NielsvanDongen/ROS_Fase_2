#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_behaviors.transport_piston_rod_form_bin_to_agv_state_1_sm import transport_piston_rod_form_bin_to_agv_state_1SM
from ariac_flexbe_behaviors.transport_gear_form_bin_to_agv_state_1_sm import transport_gear_form_bin_to_agv_state_1SM
from ariac_flexbe_behaviors.transport_gasket_form_bin_to_agv_state_1_sm import transport_gasket_form_bin_to_agv_state_1SM
from ariac_flexbe_behaviors.transport_part_form_sharebin_to_agv1_state_sm import transport_part_form_sharebin_to_agv1_stateSM
from ariac_flexbe_behaviors.transport_part_form_sharebin_to_agv2_state_sm import transport_part_form_sharebin_to_agv2_stateSM
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.transport_pulley_form_bin_to_agv_state_1_sm import transport_pulley_form_bin_to_agv_state_1SM
from ariac_flexbe_behaviors.transport_part_form_bin1_to_bin4_sm import transport_part_form_bin1_to_bin4SM
from ariac_flexbe_behaviors.transport_part_form_bin2_to_bin4_sm import transport_part_form_bin2_to_bin4SM
from ariac_flexbe_behaviors.transport_part_form_bin5_to_bin4_sm import transport_part_form_bin5_to_bin4SM
from ariac_flexbe_behaviors.transport_part_form_bin6_to_bin4_sm import transport_part_form_bin6_to_bin4SM
from ariac_support_flexbe_states.replace_state import ReplaceState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 16 2020
@author: Bas Jochems, Niels van Dongen
'''
class ariac_assignment_order_pendingSM(Behavior):
	'''
	verwerken van order
	'''


	def __init__(self):
		super(ariac_assignment_order_pendingSM, self).__init__()
		self.name = 'ariac_assignment_order_pending'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_piston_rod_form_bin_to_agv_state_1SM, 'transport_piston_rod_form_bin_to_agv_state_1')
		self.add_behavior(transport_gear_form_bin_to_agv_state_1SM, 'transport_gear_form_bin_to_agv_state_1')
		self.add_behavior(transport_gasket_form_bin_to_agv_state_1SM, 'transport_gasket_form_bin_to_agv_state_1')
		self.add_behavior(transport_part_form_sharebin_to_agv1_stateSM, 'transport_part_form_sharebin_to_agv1_state')
		self.add_behavior(transport_part_form_sharebin_to_agv2_stateSM, 'transport_part_form_sharebin_to_agv2_state')
		self.add_behavior(transport_pulley_form_bin_to_agv_state_1SM, 'transport_pulley_form_bin_to_agv_state_1')
		self.add_behavior(transport_part_form_bin1_to_bin4SM, 'transport_part_form_bin1_to_bin4')
		self.add_behavior(transport_part_form_bin2_to_bin4SM, 'transport_part_form_bin2_to_bin4')
		self.add_behavior(transport_part_form_bin5_to_bin4SM, 'transport_part_form_bin5_to_bin4')
		self.add_behavior(transport_part_form_bin6_to_bin4SM, 'transport_part_form_bin6_to_bin4')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1771 y:400, x:1225 y:399
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['agv_id', 'part_type', 'pose_on_agv'])
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.part = 'gasket_part'
		_state_machine.userdata.offset_part = 0.02
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix1 = '/ariac/arm1'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.config_name_bin3PreGrasp = 'bin3PreGrasp'
		_state_machine.userdata.config_name_tray1PreDrop = 'tray1PreDrop'
		_state_machine.userdata.camera_ref_frame = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_1'
		_state_machine.userdata.camera_frame = 'logical_camera_1_frame'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.agv_pose = []
		_state_machine.userdata.part_offset = 0.035
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.conveyor_belt_power = 100.0
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.gasket_part = 'gasket_part'
		_state_machine.userdata.pulley_part = 'pulley_part'
		_state_machine.userdata.piston_rod_part = 'piston_rod_part'
		_state_machine.userdata.gear_part = 'gear_part'
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.agv1 = 'agv1'
		_state_machine.userdata.agv2 = 'agv2'
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.offset_gasket = 0.036
		_state_machine.userdata.offset_pulley = 0.081
		_state_machine.userdata.offset_piston = 0.02
		_state_machine.userdata.offset_gear = 0.019
		_state_machine.userdata.offset = ''
		_state_machine.userdata.robot1 = 'arm1'
		_state_machine.userdata.robot2 = 'arm2'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.move_group_prefix2 = '/ariac/arm2'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:19 y:265
			OperatableStateMachine.add('MoveR2Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Home', 'planning_failed': 'WaitRetry10_2', 'control_failed': 'WaitRetry10_2', 'param_error': 'WaitRetry10_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1312 y:603
			OperatableStateMachine.add('transport_piston_rod_form_bin_to_agv_state_1',
										self.use_behavior(transport_piston_rod_form_bin_to_agv_state_1SM, 'transport_piston_rod_form_bin_to_agv_state_1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:1343 y:741
			OperatableStateMachine.add('transport_gear_form_bin_to_agv_state_1',
										self.use_behavior(transport_gear_form_bin_to_agv_state_1SM, 'transport_gear_form_bin_to_agv_state_1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:1318 y:27
			OperatableStateMachine.add('transport_gasket_form_bin_to_agv_state_1',
										self.use_behavior(transport_gasket_form_bin_to_agv_state_1SM, 'transport_gasket_form_bin_to_agv_state_1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:1321 y:453
			OperatableStateMachine.add('transport_part_form_sharebin_to_agv1_state',
										self.use_behavior(transport_part_form_sharebin_to_agv1_stateSM, 'transport_part_form_sharebin_to_agv1_state'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv', 'offset_part': 'offset_part'})

			# x:1320 y:302
			OperatableStateMachine.add('transport_part_form_sharebin_to_agv2_state',
										self.use_behavior(transport_part_form_sharebin_to_agv2_stateSM, 'transport_part_form_sharebin_to_agv2_state'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv', 'offset_part': 'offset_part'})

			# x:308 y:25
			OperatableStateMachine.add('gasket',
										EqualState(),
										transitions={'true': 'transport_gasket_form_bin_to_agv_state_1', 'false': 'pulley'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'gasket_part'})

			# x:322 y:111
			OperatableStateMachine.add('pulley',
										EqualState(),
										transitions={'true': 'transport_pulley_form_bin_to_agv_state_1', 'false': 'piston rod'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'pulley_part'})

			# x:324 y:199
			OperatableStateMachine.add('piston rod',
										EqualState(),
										transitions={'true': 'offset piston', 'false': 'gear'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'piston_rod_part'})

			# x:335 y:322
			OperatableStateMachine.add('gear',
										EqualState(),
										transitions={'true': 'offset gear', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'gear_part'})

			# x:333 y:538
			OperatableStateMachine.add('pulley_2',
										EqualState(),
										transitions={'true': 'offset pulley', 'false': 'piston rod_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'pulley_part'})

			# x:331 y:630
			OperatableStateMachine.add('piston rod_2',
										EqualState(),
										transitions={'true': 'transport_piston_rod_form_bin_to_agv_state_1', 'false': 'gear_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'piston_rod_part'})

			# x:332 y:724
			OperatableStateMachine.add('gear_2',
										EqualState(),
										transitions={'true': 'transport_gear_form_bin_to_agv_state_1', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'gear_part'})

			# x:335 y:430
			OperatableStateMachine.add('gasket_2',
										EqualState(),
										transitions={'true': 'offset gasket', 'false': 'pulley_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'gasket_part'})

			# x:1322 y:168
			OperatableStateMachine.add('transport_pulley_form_bin_to_agv_state_1',
										self.use_behavior(transport_pulley_form_bin_to_agv_state_1SM, 'transport_pulley_form_bin_to_agv_state_1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:899 y:426
			OperatableStateMachine.add('transport_part_form_bin1_to_bin4',
										self.use_behavior(transport_part_form_bin1_to_bin4SM, 'transport_part_form_bin1_to_bin4'),
										transitions={'finished': 'transport_part_form_sharebin_to_agv1_state', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:900 y:535
			OperatableStateMachine.add('transport_part_form_bin2_to_bin4',
										self.use_behavior(transport_part_form_bin2_to_bin4SM, 'transport_part_form_bin2_to_bin4'),
										transitions={'finished': 'transport_part_form_sharebin_to_agv1_state', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:901 y:190
			OperatableStateMachine.add('transport_part_form_bin5_to_bin4',
										self.use_behavior(transport_part_form_bin5_to_bin4SM, 'transport_part_form_bin5_to_bin4'),
										transitions={'finished': 'transport_part_form_sharebin_to_agv2_state', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:899 y:289
			OperatableStateMachine.add('transport_part_form_bin6_to_bin4',
										self.use_behavior(transport_part_form_bin6_to_bin4SM, 'transport_part_form_bin6_to_bin4'),
										transitions={'finished': 'transport_part_form_sharebin_to_agv2_state', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:606 y:191
			OperatableStateMachine.add('offset piston',
										ReplaceState(),
										transitions={'done': 'transport_part_form_bin5_to_bin4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_piston', 'result': 'offset_part'})

			# x:610 y:301
			OperatableStateMachine.add('offset gear',
										ReplaceState(),
										transitions={'done': 'transport_part_form_bin6_to_bin4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_gear', 'result': 'offset_part'})

			# x:609 y:420
			OperatableStateMachine.add('offset gasket',
										ReplaceState(),
										transitions={'done': 'transport_part_form_bin1_to_bin4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_gasket', 'result': 'offset_part'})

			# x:609 y:528
			OperatableStateMachine.add('offset pulley',
										ReplaceState(),
										transitions={'done': 'transport_part_form_bin2_to_bin4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_pulley', 'result': 'offset_part'})

			# x:10 y:384
			OperatableStateMachine.add('MoveR1Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'AGV keuze', 'planning_failed': 'WaitRetry10', 'control_failed': 'WaitRetry10', 'param_error': 'WaitRetry10'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:20 y:537
			OperatableStateMachine.add('WaitRetry10',
										WaitState(wait_time=2),
										transitions={'done': 'MoveR1Home'},
										autonomy={'done': Autonomy.Off})

			# x:45 y:115
			OperatableStateMachine.add('WaitRetry10_2',
										WaitState(wait_time=2),
										transitions={'done': 'MoveR2Home'},
										autonomy={'done': Autonomy.Off})

			# x:165 y:346
			OperatableStateMachine.add('AGV keuze',
										EqualState(),
										transitions={'true': 'gasket_2', 'false': 'gasket'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv2'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
