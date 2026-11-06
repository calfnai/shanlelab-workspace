"""Verify stale writes fail and project updates preserve unrelated records."""
import contextlib, io, json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import workspace

class SharedUpdates(unittest.TestCase):
    def test_stale_write_and_project_isolation(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            records = root / 'projects';records.mkdir()
            (root / 'site').mkdir()
            (root / 'site/image.png').touch()
            def project(key):
                return dict(id=key, title=key, en=key, description='', note='',
                            conversation='12345678', conversationName=key,
                            items=[dict(file='image.png', thumb='image.png')], links=[])
            for key in ('alpha', 'beta'):
                (records / (key+'.json')).write_text(json.dumps(project(key)))
            beta_before = (records / 'beta.json').read_bytes()
            alpha = records / 'alpha.json'
            stale = dict(revision=workspace.revision(alpha), project=project('alpha'))
            changed = dict(revision=stale['revision'], project={**project('alpha'), 'title':'Confirmed version'})
            with patch.object(workspace, 'ROOT', root), patch.object(workspace, 'RECORDS', records), contextlib.redirect_stdout(io.StringIO()):
                with workspace.lock():workspace.put(changed)
                with self.assertRaisesRegex(ValueError, 'Revision conflict'):
                    with workspace.lock():workspace.put(stale)
                self.assertEqual(beta_before, (records / 'beta.json').read_bytes())
                data = json.loads((root/'site/data.js').read_text()[17:-1])
                self.assertEqual(data['projects'][0]['title'], 'Confirmed version')
                self.assertEqual(len(data['projects']), 2)

if __name__ == '__main__':unittest.main()
