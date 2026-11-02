import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ContractTests(unittest.TestCase):
 def setUp(self): self.spec=json.loads((ROOT/'api/openapi.json').read_text())
 def test_contract_is_authenticated_and_honestly_pending(self):
  self.assertEqual(self.spec['security'],[{'bearerAuth':[]}])
  ids=[]
  for path, methods in self.spec['paths'].items():
   self.assertTrue(path.startswith('/v1/'))
   for operation in methods.values():
    self.assertEqual(operation['x-implementation-status'],'pending')
    self.assertNotIn('security',operation)
    ids.append(operation['operationId'])
  self.assertEqual(len(ids),len(set(ids)))
 def test_writes_bind_identity_and_allow_get_recovery(self):
  required=set(self.spec['components']['schemas']['RunRequest']['required'])
  self.assertTrue({'operationID','kind','serverID','accountID','profileID','sourceRevision','sourceHash','payloadDigest','consentReceipt'}.issubset(required))
  self.assertIn('get',self.spec['paths']['/v1/runs/{id}'])
  self.assertTrue(self.spec['paths']['/v1/sync']['put']['parameters'][0]['required'])
 def test_defaults_exist_and_do_not_claim_mastery_authority(self):
  for name in ['course-generation.md','grading.md']:
   self.assertGreater(len((ROOT/'prompts'/name).read_text().split()),40)
  self.assertIn('not independently verified mastery',(ROOT/'prompts/grading.md').read_text())
