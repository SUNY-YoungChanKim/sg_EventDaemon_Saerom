
import shotgun_api3


def registerCallbacks(reg):
    eventFilter = {
        "Shotgun_Sequence_Retirement" :None,
        "Shotgun_Episode_Retirement" :None
    }
    reg.registerCallback(
        'SequenceDelteWithShots',                                         #스크립트 이름
        'akncle&nxjqfjuJmayygugp9r',                                      #스크립트 키
        delSeqWithShots,
        eventFilter,
        None,
    )



def delSeqWithShots(sg, logger, event, args):
    
    seqId = event['meta']['entity_id']
    projectID = int(event['project']['id'])
    
    sg.revive("Sequence",seqId)
    
    sg_sequence=sg.find_one("Sequence",[['project', 'is', {'type': 'Project', 'id': projectID}],['id','is',seqId]],['shots'])
    
    if len(sg_sequence['shots']) > 0:
        for sg_shot in sg_sequence['shots']:
            sg.delete("Shot", sg_shot['id'])
    
    sg.delete('Sequence', seqId)
    return

        
