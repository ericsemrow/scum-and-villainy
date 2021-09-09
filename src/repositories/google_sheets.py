from __future__ import print_function
import os.path, re, json
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials


class GoogleSheets(object):
  SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
  sheet = None
  range = {"B5":"name","M2":"crew","M5":"alias","B8":"look","E13":"heritage","B11":"heritage_override","O13":"background","K11":"background_override","K16":"vice","B14":"vice_override","B18":"stress_1","C18":"stress_2","D18":"stress_3","E18":"stress_4","F18":"stress_5","G18":"stress_6","H18":"stress_7","I18":"stress_8","J18":"stress_9","K18":"trauma_1","O18":"trauma_2","K19":"trauma_3","O19":"trauma_4","C25":"harm1_1","H25":"harm1_2","C23":"harm2_1","H23":"harm2_2","C21":"harm3","R24":"armor","R25":"heavy","R26":"special","U9":"ability1_check","V9":"ability1","U12":"ability2_check","V12":"ability2","U14":"ability3_check","V14":"ability3","U16":"ability4_check","V16":"ability4","U18":"ability5_check","V18":"ability5","U20":"ability6_check","V20":"ability6","U22":"ability7_check","V22":"ability7","U24":"ability8_check","V24":"ability8","U26":"ability9_check","V26":"ability9","U29":"ability10_check","V29":"ability10","U30":"ability11_check","V30":"ability11","U31":"ability12_check","V31":"ability12","AU7":"playbook_xp1","AV7":"playbook_xp2","AW7":"playbook_xp3","AX7":"playbook_xp4","AY7":"playbook_xp5","AZ7":"playbook_xp6","BA7":"playbook_xp7","BB7":"playbook_xp8","AW9":"insight_xp1","AX9":"insight_xp2","AY9":"insight_xp3","AZ9":"insight_xp4","BB9":"insight_xp5","BA9":"insight_xp6","AW14":"prowess_xp1","AX14":"prowess_xp2","AY14":"prowess_xp3","AZ14":"prowess_xp4","BB14":"prowess_xp5","BA14":"prowess_xp6","AW19":"resolve_xp1","AX19":"resolve_xp2","AY19":"resolve_xp3","AZ19":"resolve_xp4","BB19":"resolve_xp5","BA19":"resolve_xp6","AP10":"doctor1","AQ10":"doctor2","AR10":"doctor3","AS10":"doctor4","AP11":"hack1","AQ11":"hack2","AR11":"hack3","AS11":"hack4","AP12":"rig1","AQ12":"rig2","AR12":"rig3","AS12":"rig4","AP13":"study1","AQ13":"study2","AR13":"study3","AS13":"study4","AP15":"helm1","AQ15":"helm2","AR15":"helm3","AS15":"helm4","AP16":"scramble1","AQ16":"scramble2","AR16":"scramble3","AS16":"scramble4","AP17":"scrap1","AQ17":"scrap2","AR17":"scrap3","AS17":"scrap4","AP18":"skulk1","AQ18":"skulk2","AR18":"skulk3","AS18":"skulk4","AP20":"attune1","AQ20":"attune2","AR20":"attune3","AS20":"attune4","AP21":"command1","AQ21":"command2","AR21":"command3","AS21":"command4","AP22":"consort1","AQ22":"consort2","AR22":"consort3","AS22":"consort4","AP23":"sway1","AQ23":"sway2","AR23":"sway3","AS23":"sway4"}

  def __init__(self):
    service_account = os.environ.get("GOOGLE_SERVICE_ACCOUNT")
    if service_account is not None:
      creds = Credentials.from_service_account_info( json.loads(service_account), scopes=self.SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    self.sheet = service.spreadsheets()

  def get_sheet_id(self, url):
    regex = re.compile(r'/spreadsheets/d/([a-zA-Z0-9-_]+)')
    parts = regex.search(url)
    assert parts, "This isn't a valid sheet"

    return parts.group(1)
  
  def get_sheet_by_id(self, id):
    result = self.sheet.values().batchGet(spreadsheetId=id, ranges=list(self.range.keys())).execute()
    values = result.get('valueRanges', [])
    #values = result.get('values', [])

    char_dict = {}
    for value in values:
      new_key = value["range"].split("!",1)[1]
      potential_value = None
      try:
        potential_value = value["values"][0][0]
      except KeyError:
        pass
      
      char_dict[self.range[new_key]] = potential_value
    
    char_dict["id"] = id
    char_dict["playbook"] = value["range"].split("!",1)[0]
    return char_dict