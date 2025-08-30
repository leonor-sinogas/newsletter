from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Newsletter:
    id: int
    title: str
    dec: str

@dataclass
class Reply:
    nid: int
    issue: str
    body: str

class InMemoryStore:
    def __init__(self):
        self._nid_seq = 1
        self.newsletters: Dict [int, Newsletter] = {}
        self.replies: list[Reply] = []

        def create_newsletter(self, title: str, desc: str) -> Newsletter:
            nid = self._nid_seq
            self._nid_seq += 1
            obj = Newsletter(id=nid, title=title, desc=desc)
            self.newsletters[nid] = obj
            return obj

        def list_newsletters(self) -> str:
            if not self.newsletters:
                return "[]"
            return "[" + ", ".join(
                f'{{"id":{n.id}, "title":"{n.title}"}}' for n in self.newsletters.values()
            ) + "]"

        def post_reply(self, nid: int, issue: str, bpdy: str):
            if nid not in self.newsletters:
                raise ValueError("newsletter not found")
            self.replies.append(Reply(nid=nid, issue=issue, body=body))


