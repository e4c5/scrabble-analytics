from tsh_to_json import tsh_to_json, json_to_tsh

from faker import Faker
fake = Faker()

records = tsh_to_json('/home/raditha/SLSL/tsh/2019/PPT3/a.t')
for record in records:
    if(record['name'] != 'bye') :
        record['name'] = fake.name()
    print (record)
    

print ("\n".join(json_to_tsh(records)))    
