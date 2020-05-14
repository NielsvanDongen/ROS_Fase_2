#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.message_state import MessageState
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_behaviors.notify_shipment_ready_sm import notify_shipment_readySM
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Bas Jochems, Niels van Dongen
'''
class transport_gasket_form_bin_to_agv_state_1SM(Behavior):
	'''
	transports part from it's bin to the selected agv
	'''


	def __init__(self):
		super(transport_gasket_form_bin_to_agv_state_1SM, self).__init__()
		self.name = 'transport_gasket_form_bin_to_agv_state_1'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(notify_shipment_readySM, 'DeliverShipment')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:71 y:147, x:609 y:234
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'agv_id', 'pose_on_agv'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.part = 'gasket_part'
		_state_machine.userdata.offset = 0.1
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = '/ariac/arm1'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.config_name_bin1PreGrasp = 'bin1PreGrasp'
		_state_machine.userdata.config_name_tray2PreDrop = 'tray2PreDrop'
		_state_machine.userdata.ref_frame = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic = '/ariac/bin1_camera'
		_state_machine.userdata.camera_frame = 'bin1_camera_frame'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.agv_pose = []
		_state_machine.userdata.part_offset_pick = 0.035
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.conveyor_belt_power = 100.0
		_state_machine.userdata.arm_id = 'arm1'
		_state_machine.userdata.part_offset_place = 0.065

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:237 y:30
			OperatableStateMachine.add('AgvIdMessage',
										MessageState(),
										transitions={'continue': 'PartTypeMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'agv_id'})

			# x:743 y:37
			OperatableStateMachine.add('MoseMessage',
										MessageState(),
										transitions={'continue': 'MoveR1PreGrasp2'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'pose_on_agv'})

			# x:531 y:36
			OperatableStateMachine.add('PartTypeMessage',
										MessageState(),
										transitions={'continue': 'MoseMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_type'})

			# x:685 y:628
			OperatableStateMachine.add('GetAgvPose',
										GetObjectPoseState(object_frame='kit_tray_1', ref_frame='arm1_linear_arm_actuator'),
										transitions={'continue': 'ComputeDrop', 'failed': 'ComputeDrop'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'agv_pose'})

			# x:1142 y:93
			OperatableStateMachine.add('WaitRetry4',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1PreGrasp2'},
										autonomy={'done': Autonomy.Off})

			# x:515 y:637
			OperatableStateMachine.add('WaitRetry7',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1ToDrop'},
										autonomy={'done': Autonomy.Off})

			# x:1090 y:652
			OperatableStateMachine.add('WaitRetry6',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1PreDrop'},
										autonomy={'done': Autonomy.Off})

			# x:16 y:320
			OperatableStateMachine.add('DeliverShipment',
										self.use_behavior(notify_shipment_readySM, 'DeliverShipment'),
										transitions={'finished': 'EndAssignment', 'failed': 'MoveR1PreDrop_2'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:925 y:91
			OperatableStateMachine.add('MoveR1PreGrasp2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'CheckPartsPoseBin', 'planning_failed': 'WaitRetry4', 'control_failed': 'WaitRetry4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin1PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:891 y:607
			OperatableStateMachine.add('MoveR1PreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GetAgvPose', 'planning_failed': 'WaitRetry6', 'control_failed': 'WaitRetry6', 'param_error': 'ComputeDrop'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_tray2PreDrop', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:473 y:516
			OperatableStateMachine.add('MoveR1ToDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperDisable', 'planning_failed': 'WaitRetry7', 'control_failed': 'WaitRetry7'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:683 y:522
			OperatableStateMachine.add('ComputeDrop',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1ToDrop', 'failed': 'MoveR1ToDrop'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'agv_pose', 'offset': 'part_offset_place', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:23 y:202
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:13 y:449
			OperatableStateMachine.add('MoveR1PreDrop_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DeliverShipment', 'planning_failed': 'DeliverShipment', 'control_failed': 'DeliverShipment', 'param_error': 'DeliverShipment'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_tray2PreDrop', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:913 y:417
			OperatableStateMachine.add('GripperEnable',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'MoveR1PreGrasp2_2', 'failed': 'WaitRetry5', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1142 y:415
			OperatableStateMachine.add('WaitRetry5',
										WaitState(wait_time=5),
										transitions={'done': 'GripperEnable'},
										autonomy={'done': Autonomy.Off})

			# x:236 y:627
			OperatableStateMachine.add('WaitRetry8',
										WaitState(wait_time=5),
										transitions={'done': 'GripperDisable'},
										autonomy={'done': Autonomy.Off})

			# x:226 y:507
			OperatableStateMachine.add('GripperDisable',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'MoveR1PreDrop_2', 'failed': 'WaitRetry8', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:914 y:177
			OperatableStateMachine.add('CheckPartsPoseBin',
										DetectPartCameraAriacState(time_out=2),
										transitions={'continue': 'ComputePick', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'part_pose'})

			# x:921 y:262
			OperatableStateMachine.add('ComputePick',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1ToPick', 'failed': 'MoveR1ToPick'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'part_offset_pick', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:910 y:341
			OperatableStateMachine.add('MoveR1ToPick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperEnable', 'planning_failed': 'WaitRetry4_2_2', 'control_failed': 'WaitRetry4_2_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1169 y:346
			OperatableStateMachine.add('WaitRetry4_2_2',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1ToPick'},
										autonomy={'done': Autonomy.Off})

			# x:1139 y:510
			OperatableStateMachine.add('WaitRetry4_2',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1PreGrasp2_2'},
										autonomy={'done': Autonomy.Off})

			# x:926 y:496
			OperatableStateMachine.add('MoveR1PreGrasp2_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1PreDrop', 'planning_failed': 'WaitRetry4_2', 'control_failed': 'WaitRetry4_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin1PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
