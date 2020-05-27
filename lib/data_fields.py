


from mrz.checker.td1 import TD1CodeChecker, get_country
from mrz.checker.td2 import TD2CodeChecker
from mrz.checker.td3 import TD3CodeChecker
from mrz.checker.td3 import TD3CodeChecker
from mrz.checker.mrva import MRVACodeChecker
from mrz.checker.mrvb import MRVBCodeChecker


def autoChecker(text):
  text = ''.join(text.split(' '))
  data = None
  t = None
  try:
    data = TD1CodeChecker(text)
    t = 'td1'
  except :
      try:
        data = TD2CodeChecker(text)
        t = 'td2'
      except :
        try:
          data = TD3CodeChecker(text)
          t ='td3'
        except :
          try:
            data = MRVACodeChecker(text)
            t = 'mrva'
          except :
            try:
              data = MRVBCodeChecker(text)
              t = 'mrvb'
            except: 
              print(" Error : MRZ valide")
  return data, t
  

def getMRZData(text):
  data, t = autoChecker(text)
  # print(f"type : {t}")
  if data is not None:
    fields = data.fields()
    champs = str(fields).split('(')[-1][:-1]
    out = {}
    for elt in champs.split(', '):
      k, v = elt.split('=')
      v = v.strip("'").strip('"')
      out[k] = v
      # print(k,v )
    out['country_name'] = get_country(out['country'] )
    out['type'] = t
    data = out

  return data, t