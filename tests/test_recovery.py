import unittest
from pathlib import Path
from researchos.recovery import build_context

class RecoveryTests(unittest.TestCase):
    def test_dogfood_context_builds(self):
        root=Path(__file__).resolve().parents[1]
        text=build_context(root/'projects'/'ntu-gice-phase2')
        self.assertIn('Recovery Context',text)
        self.assertIn('task-phase2-full-corpus-scan',text)

if __name__=='__main__': unittest.main()
