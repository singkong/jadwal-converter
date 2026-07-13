import re
from pathlib import Path

class SQLReader:
    def __init__(self, filename):
        self.filename = Path(filename)

    def load(self):
        text = self.filename.read_text(encoding='utf-8')
        inserts = re.findall(r'INSERT INTO.*?VALUES\s*(.*?);', text, re.S | re.I)
        rows=[]
        for block in inserts:
            rows.extend(re.findall(r'\((.*?)\)', block, re.S))
        return rows

    @staticmethod
    def split(row:str):
        cols=[];buf='';quote=False
        for ch in row:
            if ch=="'": quote=not quote
            if ch==',' and not quote:
                cols.append(buf.strip().strip("'"));buf=''
            else:
                buf+=ch
        cols.append(buf.strip().strip("'"))
        return cols
