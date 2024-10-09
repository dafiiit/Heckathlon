
# constants
# OPC-UA Server addresses of CPS Gates
cps01 = "opc.tcp://192.168.14.118:4840"
cps02 = "opc.tcp://192.168.14.33:4840"
cps03 = "opc.tcp://192.168.14.26:4840"
cps04 = "opc.tcp://192.168.14.80:4840"
cps05 = "opc.tcp://192.168.14.27:4840"
cps06 = "opc.tcp://192.168.14.22:4840"

# Node Ids 
##conveyor belt	
conveyorbelt_left_flag = "ns=4;s=|var|CPS-Gate.Application.CPS_GVL.cps_conveyor_belt_left_flag"
conveyorbelt_right_flag = "ns=4;s=|var|CPS-Gate.Application.CPS_GVL.cps_conveyor_belt_right_flag"
conveyorbelt_stop_flag = "ns=4;s=|var|CPS-Gate.Application.CPS_GVL.cps_conveyor_belt_stop_flag"
	
##stopper	
stopper_down_flag = "ns=4;s=|var|CPS-Gate.Application.CPS_GVL.cps_stopper_down_flag"
stopper_up_flag = "ns=4;s=|var|CPS-Gate.Application.CPS_GVL.cps_stopper_up_flag"

##conveyordetection
conveyor_detection_flag = "ns=4;s=|var|CPS-Gate.Application.CPS_GVL.cps_conveyor_detection_flag"