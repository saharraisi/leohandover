# System level config
SATELLITE_R = 25 * 1000
NUMBER_UE = 7
SATELLITE_V = 7.56 * 1000
SATELLITE_GROUND_DELAY = 3
SATELLITE_SATELLITE_DELAY = 1
CORE_DELAY = 10
DURATION = 10000
RETRANSMIT = True
RETRANSMIT_THRESHOLD = SATELLITE_GROUND_DELAY * 2 + SATELLITE_SATELLITE_DELAY * 2 + 20
MAX_RETRANSMIT = 15
CPU_SCALE = 4
QUEUED_SIZE = 500
GROUP_AREA_L = 1 * 1000
# Parameters
# TODO
# 1. The UEs will perform random access only the first time, which means the satellites will first goes to the massive UEs.
# 1.1 If restricting only one random access is weird, we can assign UEs during configuration.
# 2. Handover Decision should be set too.

# This labels the initial position of satellites
POS_SATELLITES = {
    1: (-25 * 1000, 0),
    2: (-37.5 * 1000, 0),
    3: (-50 * 1000, 0),
}

MEASUREMENT_REPORT = "MEASUREMENT_REPORT"
HANDOVER_REQUEST = "HANDOVER_REQUEST"
HANDOVER_ACKNOWLEDGE = "HANDOVER_ACKNOWLEDGE"
RRC_RECONFIGURATION = "RRC_RECONFIGURATION"
RRC_RECONFIGURATION_COMPLETE = "RRC_RECONFIGURATION_COMPLETE"
RRC_RECONFIGURATION_COMPLETE_RESPONSE = "RRC_RECONFIGURATION_COMPLETE_RESPONSE"
PATH_SHIFT_REQUEST = "PATH_SHIFT_REQUEST"
RETRANSMISSION = "RETRANSMISSION"
SWITCH_TO_GROUP_HANDOVER = "SWITCH_TO_GROUP_HANDOVER"

GROUP_HANDOVER_NOTIFY = "GROUP_HANDOVER_NOTIFY"
PROCESS_ONE_UE = "PROCESS_ONE_UE"
SWITCH_TO_GROUP_HANDOVER = "SWITCH_TO_GROUP_HANDOVER"

PROCESSING_TIME = {
    MEASUREMENT_REPORT: 0.5 * CPU_SCALE,
    HANDOVER_REQUEST: 0.5 * CPU_SCALE,
    HANDOVER_ACKNOWLEDGE: 0.1 * CPU_SCALE,
    RRC_RECONFIGURATION_COMPLETE: 0.1 * CPU_SCALE,
    PATH_SHIFT_REQUEST: 0.1 * CPU_SCALE,
    RETRANSMISSION: 0.5 * CPU_SCALE,
    PROCESS_ONE_UE: 0.1 * CPU_SCALE,
}

# TODO Under change, the message and Queue size.
'''
The satellite will handle inter-satellite tasks and Random access request at first priority
Random Access and inter-satellite messages will not be restricted to Queue Size.
because that's not the beginning of a handover.
'''

SATELLITE_CPU = 4
UE_CPU = 4

'''
The below constants defined the state machine of UE
'''
# The UE is actively communicating with source base station
# and the UE has not made any action
ACTIVE = "ACTIVE"
# The UE sent the measurement report and waiting for configuration
WAITING_RRC_CONFIGURATION = "WAITING_RRC_CONFIGURATION"
# The UE lost the connection without being RRC configured
# MEANING that the UE failed to be handoff.
INACTIVE = "INACTIVE"
# The UE has received the RRC configuration message
RRC_CONFIGURED = "RRC_CONFIGURED"
# The UE has sent the random access request with RRC_RECONFIGURATION_COMPLETE
WAITING_RRC_RECONFIGURATION_COMPLETE_RESPONSE = "WAITING_RRC_RECONFIGURATION_COMPLETE_RESPONSE"

'''
The below defines group handover state
'''
