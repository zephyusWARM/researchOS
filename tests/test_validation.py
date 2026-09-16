import json, tempfile, unittest
from pathlib import Path
from researchos.validation import validate_repo

class ValidationTests(unittest.TestCase):
    def mk(self):
        td=tempfile.TemporaryDirectory(); root=Path(td.name); p=root/'projects'/'p'
        for d in ('tasks','runs','sources','evidence','claims'): (p/d).mkdir(parents=True,exist_ok=True)
        (p/'project.json').write_text(json.dumps({'id':'project-p','title':'P','status':'active','cutoff_date':'2026-09-16','created_at':'2026-09-16T00:00:00+08:00'}))
        for f in ('PROGRAM.md','SNAPSHOT.md','COVERAGE.md'): (p/f).write_text('# x')
        task={'id':'task-a','title':'A','status':'active','question':'Q','created_at':'2026-09-16T00:00:00+08:00','max_active_runs':1}
        (p/'tasks'/'task-a.json').write_text(json.dumps(task))
        return td,root,p
    def test_minimal_valid(self):
        td,root,p=self.mk(); self.addCleanup(td.cleanup)
        self.assertEqual(validate_repo(root),[])
    def test_concurrency_guard(self):
        td,root,p=self.mk(); self.addCleanup(td.cleanup)
        for i in (1,2):
            r={'id':f'run-{i}','task_id':'task-a','status':'running','started_at':'2026-09-16T00:00:00+08:00'}
            (p/'runs'/f'run-{i}.json').write_text(json.dumps(r))
        self.assertTrue(any('exceed max_active_runs' in e for e in validate_repo(root)))
    def test_supported_claim_requires_evidence(self):
        td,root,p=self.mk(); self.addCleanup(td.cleanup)
        c={'id':'claim-x-r001','claim_key':'x','revision':1,'statement':'x','status':'supported','evidence_ids':[],'created_at':'2026-09-16T00:00:00+08:00'}
        (p/'claims'/'claim-x-r001.json').write_text(json.dumps(c))
        self.assertTrue(any('requires evidence' in e for e in validate_repo(root)))
    def test_claim_fork_rejected(self):
        td,root,p=self.mk(); self.addCleanup(td.cleanup)
        base={'id':'claim-x-r001','claim_key':'x','revision':1,'statement':'x','status':'proposed','evidence_ids':[],'created_at':'2026-09-16T00:00:00+08:00'}
        (p/'claims'/'claim-x-r001.json').write_text(json.dumps(base))
        for suffix in ('a','b'):
            c={'id':f'claim-x-r002-{suffix}','claim_key':'x','revision':2,'statement':'x2','status':'proposed','evidence_ids':[],'created_at':'2026-09-16T01:00:00+08:00','supersedes':'claim-x-r001'}
            (p/'claims'/f'claim-x-r002-{suffix}.json').write_text(json.dumps(c))
        errs=validate_repo(root)
        self.assertTrue(any('fork' in e or 'multiple latest leaves' in e for e in errs))

if __name__=='__main__': unittest.main()
