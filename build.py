"""Assemble the shared index from independent project records."""
import workspace
if __name__=='__main__':
    with workspace.lock():workspace.assemble()
