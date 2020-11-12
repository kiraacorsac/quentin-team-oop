import unittest
from TDD_organized_lesson.AlertCreators.camera import Camera
from TDD_organized_lesson.security_system import SecuritySystem


class CameraTest(unittest.TestCase):

    def setUp(self):
        self.camera = Camera("Camera1", ["backyard", "outside"])

    def test_isConnected_securitySystemNotNone_true(self):
        # setUp
        # set up everything you need to run the test

        system = SecuritySystem()  
        self.camera.security_system = system

        self.assertTrue(self.camera.isConnected())


    def test_detectMovement_nightTimeNightMode_createsAlert(self):
        pass