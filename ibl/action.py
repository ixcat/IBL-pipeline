import datajoint as dj
from . import reference

schema = dj.schema(dj.config.get('database.prefix', '') + 'ibl_reference')

@schema
class ProcedureType(dj.Manual):
    definition = """
    procedure_type_name:                varchar(255)
    ---
    procedure_type_uuid:                varchar(64)
    procedure_type_description=null:    varchar(1024)
    """

@schema
class Weighing(dj.Manual):
    # <class 'actions.models.Weighing'>
    definition = """
    -> Subject
    weighing_time:		datetime		# date time
    ---
    weigh_uuid:        varchar(36)
    weight:			    float			# weight
    -> [nullable] reference.LabMember
    """

@schema
class WaterAdministration(dj.Manual):
    # <class 'actions.models.WaterAdministration'>
    definition = """
    -> Subject
    administration_time:	datetime		# date time
    ---
    wateradmin_uuid:        varchar(36)     
    water_administered:		float			# water administered
    hydrogel=null:		    boolean         # hydrogel
    -> [nullable] reference.LabMember
    """

@schema
class WaterRestriction(dj.Manual):
    # <class 'actions.models.WaterRestriction'>
    definition = """
    -> Subject
    restriction_start_time:     datetime	# start time
    ---
    restriction_uuid:           varchar(36) 
    restriction_end_time:       datetime	# end time
    -> reference.LabLocation     
    """
    
@schema
class Surgery(dj.Manual):
    # <class 'actions.models.Surgery'>
    definition = """
    -> Subject
    surgery_start_time:		datetime        # surgery start time
    ---
    surgery_end_time:		datetime        # surgery end time
    -> reference.LabMember
    outcome_type:		    enum('None', 'a', 'n', 'r')	    # outcome type
    surgery_narrative:      varchar(255)	# narrative
    """

@schema
class SurgeryLabMember(dj.Manual):
    definition = """
    -> Surgery
    -> reference.LabMember
    """

class SurgeryProcedure(dj.Manual):
    definition = """
    -> Surgery
    -> ProcedureType
    """

@schema
class VirusInjection(dj.Manual):
    # <class 'actions.models.VirusInjection'>
    # XXX: user was m2m field in django
    definition = """
    -> Subject
    injection_time:		    datetime        # injection time
    ---
    injection_uuid:         varchar(36)     
    injection_volume:		float   		# injection volume
    rate_of_injection:		float           # rate of injection
    injection_type:		    varchar(255)    # injection type
    """

@schema
class OtherAction(dj.Manual):
    # <class 'actions.models.OtherAction'>
    definition = """
    -> Subject
    other_action_start_time:    datetime	# start time
    ---
    other_action_uuid:          varchar(36)
    other_action_end_time:      datetime	# end time
    description:                varchar(255)    # description
    -> reference.Location
    """