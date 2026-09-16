import unittest
from researchos.immutability import check_record_change

class ImmutabilityTests(unittest.TestCase):
    def test_claim_edit_rejected(self):
        self.assertTrue(check_record_change('claims',{'id':'claim-a'},{'id':'claim-a','x':1}))
    def test_terminal_run_edit_rejected(self):
        old={'id':'run-a','task_id':'task-a','status':'succeeded','started_at':'x','ended_at':'y'}
        new={**old,'summary':'changed'}
        self.assertTrue(check_record_change('runs',old,new))
    def test_running_run_can_terminalize(self):
        old={'id':'run-a','task_id':'task-a','status':'running','started_at':'x','base_commit':'abc'}
        new={**old,'status':'interrupted','ended_at':'y'}
        self.assertEqual(check_record_change('runs',old,new),[])
    def test_run_identity_cannot_change(self):
        old={'id':'run-a','task_id':'task-a','status':'running','started_at':'x','base_commit':'abc'}
        new={**old,'task_id':'task-b','status':'failed','ended_at':'y'}
        self.assertTrue(check_record_change('runs',old,new))

if __name__=='__main__': unittest.main()
