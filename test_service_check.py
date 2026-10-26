import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, socket, threading
from service_check import check
class T(unittest.TestCase):
    def test_local_service(self):
        srv = socket.socket(); srv.bind(("127.0.0.1", 0)); srv.listen(1)
        port = srv.getsockname()[1]
        import service_check
        service_check.SERVICES["testsvc"] = port
        try: self.assertTrue(check("127.0.0.1", "testsvc"))
        finally: srv.close()
    def test_unknown_service(self):
        with self.assertRaises(KeyError): check("127.0.0.1", "nosuchservice")
if __name__ == "__main__": unittest.main()
